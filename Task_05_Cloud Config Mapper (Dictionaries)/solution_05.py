virtual_machine = {
    "id": "vm01",
    "ip": "192.168.1.101",
    "status": "running",
    "region": "bd-div-01"
}

virtual_machine ["status"] = "stopped"

virtual_machine ["instance_type"] = "t3.large"

print(virtual_machine)