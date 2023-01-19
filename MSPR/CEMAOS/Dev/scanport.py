import socket

#se connect aux differents ports sur les ip "x.x.x.x-x.x.x.x"
def scan_ports(ip_range):
    #variables pour les ports ouverts
    ports_open = []
    #variable pour les addresses
    start_ip, end_ip = ip_range.split("-")
    #lis la liste des adresse et les "decoupe" au niveau du -
    for host in range(int(start_ip.split(".")[-1]), int(end_ip.split(".")[-1])+1):
        ip = ".".join(start_ip.split(".")[:-1]) + "." + str(host)
        #parcours les ports 1 à 65535
        for port in range(1, 65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)
            try:
                #essaye de se connecter au port
                s.connect((ip, port))
                print(f"Port {port} ouvert sur {ip}")
                ports_open.append((ip, port))
                s.close()
            except:
                #si il n'arrive pas a se connecter, capture l'erreur pour assurer le bon deroulement de la suite
                s.close()
    return ports_open

print(scan_ports("172.16.71.1-172.16.71.1"))
