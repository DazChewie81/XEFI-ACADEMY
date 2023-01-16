import socket
import psutil
import requests
import socket

# On vérifie si on joints internet
def connexion():
    try:
        # on tente de se connecter à google pour voir si on est connecté
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        pass
    return False

if connexion():
    co="Connecté"
else:
    co="Non connecté"

# Connexion en Wifi / Ethernet
def is_connected():
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                if "wifi" in interface.lower():
                    print("Connecté en wifi")
                elif "eth" in interface.lower():
                    print("Connecté en ethernet")
                else:
                    if interface != 'lo':
                        print(f"Connecté en {interface}")

is_connected()

# Récupère l'ip publique
def get_public_ip():
    try:
        response = requests.get("https://httpbin.org/ip")
        if response.status_code == 200:
            data = response.json()
            return data["origin"]
    except:
        pass
    return "Impossible de récupérer l'adresse IP publique"

print(get_public_ip())


#! A vérifier
# Récupère le nom de domaine
def get_domain_name():
    hostname = socket.gethostname()
    try:
        return socket.gethostbyname(hostname)
    except socket.gaierror:
        return "Impossible de récupérer le nom de domaine"

print(get_domain_name())
