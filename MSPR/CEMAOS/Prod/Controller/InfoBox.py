import socket

# Récupérez le nom de la machine
hostname = socket.gethostname()

# Récupérez l'adresse IP de la machine
ip_address = socket.gethostbyname(hostname)

loopback=("127.0.0.1","127.0.0.2")

if ip_address in loopback:
    ip_address="Non connecté"
