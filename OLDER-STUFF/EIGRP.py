from netmiko import ConnectHandler
from inv_SSH_file import inv

for device in inv:
    if 'WAN' in device['hostname']:
        with ConnectHandler(**device["conn"]) as conn:
            conn.enable()
            config = [
                "no router eigrp 100",
                "router eigrp 100",
                "network 10.0.0.0",
                "passive-interface default",
                "no passive-interface Vlan950",
            ]

            print("***************************************************************************")
            print(conn.send_config_set(config))
            print(conn.send_command("show run | sec router eigrp"))


############################################



