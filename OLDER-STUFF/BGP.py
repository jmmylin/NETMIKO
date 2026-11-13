from netmiko import ConnectHandler
from inv_SSH_file import inv

for device in inv:
    if "WAN" in device['hostname']:
        with ConnectHandler(**device["conn"]) as conn:
            conn.enable()
            config = [
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
            print(conn.send_config_set(config))
            print("***************************************************************************")
#########################################################################################################################################

    if "FW" in device['hostname']:
        with ConnectHandler(**device["conn"]) as conn:
            conn.enable()
            config = [
            "no router bgp 65140",
            "router bgp 65140",
                f"bgp router-id {device['v950_ip']}",
                "bgp log-neighbor-changes",
                "!",
                "neighbor 10.254.0.98 remote-as 65140", 
                "neighbor 10.254.0.99 remote-as 65140", 
                "!",
                "address-family ipv4",
                    "bgp redistribute-internal",
                    "network 0.0.0.0",
                    #redistribute eigrp 100 route-map EIGRP_into_BGP
                    "neighbor 10.254.0.98 activate", "neighbor 10.254.0.98 next-hop-self", "neighbor 10.254.0.98 soft-reconfiguration inbound",
                    "neighbor 10.254.0.99 activate", "neighbor 10.254.0.99 next-hop-self", "neighbor 10.254.0.99 soft-reconfiguration inbound",
                "exit-address-family",
            ]
            print(conn.send_config_set(config))
            print("***************************************************************************")