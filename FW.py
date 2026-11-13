from netmiko import ConnectHandler
from inv_SSH_file import inv



for device in inv:
    if 'FW' in device['hostname']: 
        with ConnectHandler(**device["conn"]) as conn:
            conn.enable()
            config = [
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
                "vlan 951",
                  "name FW-VLAN",
                "exit",
            "!",
                "int vlan 950", f"ip address {device['v950_ip']} 255.255.255.240", "no shutdown",
                "int vlan 951", f"ip address {device['v951_ip']} 255.255.255.248", "no shutdown",
                "int Gi0/1", "desc FW-to-WAN1", "switchport trunk encap dot1q", "switchport trunk allowed vlan 950", "switchport mode trunk", "no shutdown", "exit",
                "int Gi0/2", "desc FW-to-WAN2", "switchport trunk encap dot1q", "switchport trunk allowed vlan 950", "switchport mode trunk", "no shutdown", "exit",
                "default int Gi0/3",
                "int Gi0/3", "desc FW-to-CORE", "switchport mode access", "switchport access vlan 951", "no shutdown", "exit",
            "!",
                "no router bgp 65140",
                "router bgp 65140",
                f"bgp router-id {device['v950_ip']}",
                "bgp log-neighbor-changes",
                "!",
                "neighbor 10.254.0.98 remote-as 65140", 
                "neighbor 10.254.0.99 remote-as 65140",
                f"neighbor {device['bgp_core_peer']} remote-as {device['bgp_core_asn']}" 
                "!",
                "address-family ipv4",
                  "bgp redistribute-internal",
                  "network 0.0.0.0",
                  #redistribute eigrp 100 route-map EIGRP_into_BGP
                  "neighbor 10.254.0.98 activate", "neighbor 10.254.0.98 next-hop-self", "neighbor 10.254.0.98 soft-reconfiguration inbound",
                  "neighbor 10.254.0.99 activate", "neighbor 10.254.0.99 next-hop-self", "neighbor 10.254.0.99 soft-reconfiguration inbound",
                  f"neighbor {device['bgp_core_peer']} activate", f"neighbor {device['bgp_core_peer']} soft-reconfiguration inbound",  
                "exit-address-family",
            ]
            print("***************************************************************************")
            print(conn.send_config_set(config))

    else:
        pass