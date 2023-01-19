import subprocess

# Stocker le nom du script bash dans une variable
bash_script = "download.sh"

# Exécuter le script bash en utilisant subprocess.run
result = subprocess.run(["bash", bash_script])
