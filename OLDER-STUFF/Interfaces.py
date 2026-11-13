from netmiko import ConnectHandler
from inv_SSH_file import inv



for device in inv:
    if 'WAN' in device['hostname']: 
        with ConnectHandler(**device["conn"]) as conn:
            conn.enable()
            config = [
                "vlan 950",
                  "name WAN-VLAN",
                "exit",
                "!",
                "int vlan 950", f"ip address {device['v950_ip']} 255.255.255.240", "no shutdown",
                "!",
                "int Gi0/1",
                  "desc WAN-to-WAN",
                  "switchport trunk encap dot1q",
                  "switchport mode trunk",
                  "no shutdown",
                "exit",
                "!",
                "int range Gi1/0 - 3",
                  "switchport trunk encap dot1q",
                  "switchport trunk allowed vlan 950",
                  "switchport mode trunk",
                  "no shutdown",
                "exit",
                "!",
                "int Gi1/0", "desc MAIN_FW", "exit",
                "int Gi1/1", "desc WB_FW", "exit",
                "int Gi1/2", "desc ASC_FW", "exit",
                "int Gi1/3", "desc HH_FW", "exit",
            ]

            print("***************************************************************************")
            print(conn.send_config_set(config))
            # print(conn.send_command("show run | inc hostname"))
            # print(conn.send_command("show run | inc console"))
            # print(conn.send_command("show run | inc domain-name"))
            # print(conn.send_command("show run | sec line con 0"))

    elif 'FW' in device['hostname']: 
        with ConnectHandler(**device["conn"]) as conn:
            conn.enable()
            config = [
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

          
                "int Gi0/1",
                  "desc FW-to-WAN1",
                  "switchport trunk encap dot1q",
                  "switchport trunk allowed vlan 950",
                  "switchport mode trunk",
                  "no shutdown",
                "exit",
            "!",
                "int Gi0/2",
                  "desc FW-to-WAN2",
                  "switchport trunk encap dot1q",
                  "switchport trunk allowed vlan 950",
                  "switchport mode trunk",
                  "no shutdown",
                "exit",
            "!",
                "int Gi0/3",
                  "desc FW-to-CORE",
                  "switchport trunk encap dot1q",
                  "switchport trunk allowed vlan 951",
                  "switchport mode trunk",
                  "no shutdown",
                "exit",
            "!",
            ]

            print("***************************************************************************")
            print(conn.send_config_set(config))
            # print(conn.send_command("show run | inc hostname"))
            # print(conn.send_command("show run | inc console"))
            # print(conn.send_command("show run | inc domain-name"))
            # print(conn.send_command("show run | sec line con 0"))

    else:
        pass







############################################



