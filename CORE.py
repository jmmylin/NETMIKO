from netmiko import ConnectHandler
from inv_SSH_file import inv

for device in inv:
    if 'CORE' in device['hostname']: 
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
                "vrf definition ASC",  "rd 65150:143", "address-family ipv4", "exit-address-family",
                "vrf definition HH",   "rd 65150:144", "address-family ipv4", "exit-address-family",
                "vrf definition MAIN", "rd 65150:140", "address-family ipv4", "exit-address-family",
                "vrf definition WB",   "rd 65150:142", "address-family ipv4", "exit-address-family",
            "!",
                "interface GigabitEthernet1/0", "no switchport", "vrf forwarding MAIN", "ip address 10.140.254.66 255.255.255.248", "no shutdown", "exit",
                "interface GigabitEthernet1/1", "no switchport", "vrf forwarding WB",   "ip address 10.142.254.66 255.255.255.248", "no shutdown", "exit",
                "interface GigabitEthernet1/2", "no switchport", "vrf forwarding ASC",  "ip address 10.143.254.66 255.255.255.248", "no shutdown", "exit",
                "interface GigabitEthernet1/3", "no switchport", "vrf forwarding HH",   "ip address 10.144.254.66 255.255.255.248", "no shutdown", "exit",
            "!",
                "interface Loopback 141", "vrf forw MAIN", "ip addr 10.141.32.1 255.255.255.0", "no shut", "exit",
                "interface Loopback 142", "vrf forw WB",   "ip addr 10.142.32.1 255.255.255.0", "no shut", "exit",
                "interface Loopback 143", "vrf forw ASC",  "ip addr 10.143.32.1 255.255.255.0", "no shut", "exit",
                "interface Loopback 144", "vrf forw HH",   "ip addr 10.144.32.1 255.255.255.0", "no shut", "exit",
            "!",
                "no router bgp 65150",
                "router bgp 65150",
                  "bgp router-id 7.7.7.7",
                  "bgp log-neighbor-changes",
            "!",
                  "address-family ipv4 vrf MAIN",
                    "neighbor 10.140.254.68 remote-as 65140",
                    "neighbor 10.140.254.68 local-as 65141 no-prepend replace-as",
                    "neighbor 10.140.254.68 activate",
                    "redistribute connected",
                  "exit-address-family",
            "!",
                  "address-family ipv4 vrf WB",
                    "neighbor 10.142.254.68 remote-as 65140",
                    "neighbor 10.142.254.68 local-as 65142 no-prepend replace-as",
                    "neighbor 10.142.254.68 activate",
                    "redistribute connected",
                  "exit-address-family",
            "!",
                  "address-family ipv4 vrf ASC",
                    "neighbor 10.143.254.68 remote-as 65140",
                    "neighbor 10.143.254.68 local-as 65143 no-prepend replace-as",
                    "neighbor 10.143.254.68 activate",
                    "redistribute connected",
                  "exit-address-family",
            "!",                 
                 "address-family ipv4 vrf HH",
                    "neighbor 10.144.254.68 remote-as 65140",
                    "neighbor 10.144.254.68 local-as 65144 no-prepend replace-as",
                    "neighbor 10.144.254.68 activate",
                    "redistribute connected",
                  "exit-address-family",
            ]
            print("***************************************************************************")
            print(conn.send_config_set(config))

    else:
        pass








