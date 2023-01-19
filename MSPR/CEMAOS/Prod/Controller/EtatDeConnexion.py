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
                    return "Wifi"
                    
                elif "eth" in interface.lower():
                    return "Ethernet"
                else:
                    if interface != 'lo':
                        return f"Interface {interface}"
                        



# Récupère l'ip publique
def IpPublique():
    try:
        response = requests.get("https://httpbin.org/ip")
        if response.status_code == 200:
            data = response.json()
            return data["origin"]
    except:
        pass
    return "Impossible de récupérer l'adresse IP publique"