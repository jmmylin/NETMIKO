inv = [
    {
        "conn": {
            "device_type": "cisco_ios", 
            "host": "192.168.1.201",
            "username": "admin",
            "password": "XXXXXXX",
            }, 
        "hostname": "WAN1",
        "v950_ip": "10.254.0.98",
        "bgp_wan_peer": "10.254.0.99",
        "DC_int": "Gi0/2",
        "DC_ip": "20.20.20.2",
        "DC_eigrp_network": "20.20.20.0 0.0.0.3",
    },
    {
        "conn": {
            "device_type": "cisco_ios",
            "host": "192.168.1.202",
            "username": "admin",
            "password": "Cisco123",
            },
        "hostname": "WAN2",
        "v950_ip": "10.254.0.99",
        "bgp_wan_peer": "10.254.0.98",
        "DC_int": "Gi0/3",
        "DC_ip": "30.30.30.2",
        "DC_eigrp_network": "30.30.30.0 0.0.0.3",
    },
    {
        "conn": {
            "device_type": "cisco_ios",
            "host": "192.168.1.203",
            "username": "admin",
            "password": "Cisco123",
            },
        "hostname": "MAIN_FW",
        "v950_ip": "10.254.0.100",
        "v951_ip": "10.140.254.68",
        "bgp_core_peer": "10.140.254.66",
        "bgp_core_asn": "65141",
    },     
    {
        "conn": {
            "device_type": "cisco_ios",
            "host": "192.168.1.204",
            "username": "admin",
            "password": "Cisco123",
            },
        "hostname": "WB_FW",
        "v950_ip": "10.254.0.101",
        "v951_ip": "10.142.254.68",
        "bgp_core_peer": "10.142.254.66",
        "bgp_core_asn": "65142",
    },
    {
        "conn": {
            "device_type": "cisco_ios",
            "host": "192.168.1.205",
            "username": "admin",
            "password": "Cisco123",
            },
        "hostname": "ASC_FW",
        "v950_ip": "10.254.0.102",
        "v951_ip": "10.143.254.68",
        "bgp_core_peer": "10.143.254.66",
        "bgp_core_asn": "65143",

    }, 
    {
        "conn": {
            "device_type": "cisco_ios",
            "host": "192.168.1.206",
            "username": "admin",
            "password": "Cisco123",
            },
        "hostname": "HH_FW",
        "v950_ip": "10.254.0.103",
        "v951_ip": "10.144.254.68",
        "bgp_core_peer": "10.144.254.66",
        "bgp_core_asn": "65144",
    }, 
    {
        "conn": {
            "device_type": "cisco_ios",
            "host": "192.168.1.207",
            "username": "admin",
            "password": "Cisco123",
            },
        "hostname": "CORE",
        "v950_ip": "10.254.0.104",
    }
]
