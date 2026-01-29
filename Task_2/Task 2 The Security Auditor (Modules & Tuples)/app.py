import scanner


def main():


    active_ports=[22, 80, 21, 443, 23, 8080]

    print(f"list of active ports: {active_ports}")

    scanner.check_ports(active_ports)


main()
