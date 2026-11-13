from netmiko import ConnectHandler
from inv_SSH_file import inv

for device in inv:
    with ConnectHandler(**device["conn"]) as conn:
        conn.enable()
        output = conn.send_command("show ip eigrp neighbor")
        print('')
        print('')
        print(f"-----{device['hostname']}--------------------------------------------------------------------------------")
        print(output)        