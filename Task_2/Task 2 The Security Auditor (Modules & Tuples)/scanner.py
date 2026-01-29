DANGEROUS_PORTS = (21, 23, 445)

def check_ports(active_ports):


    found_dangerous = False

    for port in active_ports:
        if port in DANGEROUS_PORTS:
            print(f"Warning! dangerous port {port} found")
            found_dangerous = True
        else:
            print(f"port: {port} safe")
    if not found_dangerous:
        print("no dangerous port found in active ports")

