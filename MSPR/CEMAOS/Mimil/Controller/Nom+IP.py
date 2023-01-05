import socket

# Récupérez le nom de la machine
hostname = socket.gethostname()

# Récupérez l'adresse IP de la machine
ip_address = socket.gethostbyname(hostname)

# Affichez le résultat
print(f"Nom de la machine: {hostname}")
print(f"Adresse IP: {ip_address}")
