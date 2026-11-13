from netmiko import ConnectHandler
from inv_SSH_file import inv


for sw in inv:
    with ConnectHandler(**sw["conn"]) as conn:
        conn.enable()
        config = [
            "no logging console",
            "no ip domain-lookup",
        "!",
            f"hostname {sw['hostname']}",
        "!",
            "line con 0",
            "logging synchronous",
            "exec-timeout 0 0",
            "privi level 15",
            "exit",
        ]
        print(conn.send_config_set(config))
        print("***************************************************************************")
        # print(conn.send_command("show run | inc hostname"))
        # print(conn.send_command("show run | inc console"))
        # print(conn.send_command("show run | inc domain-name"))
        # print(conn.send_command("show run | sec line con 0"))







############################################



