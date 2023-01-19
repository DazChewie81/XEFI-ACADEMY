#!/bin/bash

# Stocker l'URL dans une variable
url="http://example.com/download-test"

# Utiliser curl pour récupérer la valeur de téléchargement
download_value=$(curl -w %{speed_download} -o /dev/null -s $url)

# Afficher la valeur de téléchargement
echo "La valeur de téléchargement est: $download_value octets/s"
