from netmiko import ConnectHandler
from inv_SSH_file import inv

for device in inv:
    if 'WAN' in device['hostname']: 
        with ConnectHandler(**device["conn"]) as conn:
            conn.enable()
            config = [
            "!",
                "no logging console",
                "no ip domain-lookup",
            "!",
                f"hostname {device['hostname']}",
            "!",
                "line con 0",
                  "logging synchronous",
                  "exec-timeout 0 0",
                  "privi level 15",
                "exit",
            "!",
                "vlan 950",
                  "name WAN-VLAN",
                "exit",
            "!",
                "int vlan 950", f"ip address {device['v950_ip']} 255.255.255.240", "no shutdown", "exit",
            "!",
                "int Gi0/1", "desc WAN-to-WAN", "switchport trunk encap dot1q", "switchport mode trunk", "no shutdown", "exit",
                f"int {device['DC_int']}", "no switchport", f"ip address {device['DC_ip']} 255.255.255.252", "no shut", "exit",
            "!",
                "int range Gi1/0 - 3", "switchport trunk encap dot1q", "switchport trunk allowed vlan 950", "switchport mode trunk", "no shutdown", "exit",
                "int Gi1/0", "desc MAIN_FW", "exit",
                "int Gi1/1", "desc WB_FW", "exit",
                "int Gi1/2", "desc ASC_FW", "exit",
                "int Gi1/3", "desc HH_FW", "exit",
            "!",
                "no router eigrp 100",
                "router eigrp 100",
                "network 10.0.0.0",
                f"network {device['DC_eigrp_network']}",
                "passive-interface default",
                "no passive-interface Vlan950",
                f"no passive-interface {device['DC_int']}"
            "!",
                "no router bgp 65140",
                "router bgp 65140",
                f"bgp router-id {device['v950_ip']}",
                "bgp cluster-id 10.254.0.98",
                "bgp log-neighbor-changes",
            "!",
                f"neighbor {device['bgp_wan_peer']} remote-as 65140", f"neighbor {device['bgp_wan_peer']} update-source Vlan 950",
                "neighbor 10.254.0.100 remote-as 65140", "neighbor 10.254.0.100 update-source vlan 950",
                "neighbor 10.254.0.101 remote-as 65140", "neighbor 10.254.0.101 update-source vlan 950",
                "neighbor 10.254.0.102 remote-as 65140", "neighbor 10.254.0.102 update-source vlan 950",
                "neighbor 10.254.0.103 remote-as 65140", "neighbor 10.254.0.103 update-source vlan 950",
            "!",
                "address-family ipv4",
                    "bgp redistribute-internal",
                    "network 0.0.0.0",
                    #redistribute eigrp 100 route-map EIGRP_into_BGP
                    f"neighbor {device['bgp_wan_peer']} activate", f"neighbor {device['bgp_wan_peer']} next-hop-self", f"neighbor {device['bgp_wan_peer']} soft-reconfiguration inbound",
                    "neighbor 10.254.0.100 activate", "neighbor 10.254.0.100 route-reflector-client", "neighbor 10.254.0.100 next-hop-self", "neighbor 10.254.0.100 soft-reconfiguration inbound",
                    "neighbor 10.254.0.101 activate", "neighbor 10.254.0.101 route-reflector-client", "neighbor 10.254.0.101 next-hop-self", "neighbor 10.254.0.101 soft-reconfiguration inbound",
                    "neighbor 10.254.0.102 activate", "neighbor 10.254.0.102 route-reflector-client", "neighbor 10.254.0.102 next-hop-self", "neighbor 10.254.0.102 soft-reconfiguration inbound",
                    "neighbor 10.254.0.103 activate", "neighbor 10.254.0.103 route-reflector-client", "neighbor 10.254.0.103 next-hop-self", "neighbor 10.254.0.103 soft-reconfiguration inbound",
                "exit-address-family",
            ]
            print("***************************************************************************")
            print(conn.send_config_set(config))