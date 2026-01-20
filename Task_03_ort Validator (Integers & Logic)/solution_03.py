port_string ="8080"

port_string = int(port_string)


if(0 < port_string < 65536):
    print("Valid")

else:
    print("invalid")

