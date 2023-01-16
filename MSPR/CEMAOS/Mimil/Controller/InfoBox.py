import socket

# Récupérez le nom de la machine
hostname = socket.gethostname()

# Récupérez l'adresse IP de la machine
ip_address = socket.gethostbyname(hostname)
