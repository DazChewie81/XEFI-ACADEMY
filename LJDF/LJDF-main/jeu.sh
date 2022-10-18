#!/bin/bash

choix(){
	cowsay "Bonjour et bienvenu sur Le Jeu De Fou!!!   O M G " 

	echo  "|| FAIS TON CHOIX : ||"
	option=("Nouvelle partie" "Charger" "Quit")
	select opt in "${option[@]}"
	do
		case $opt in
			"Nouvelle partie")
				echo "Creation de la partie"
				python3 LJDF.py 
				break
				;;
			"Charger")
				echo "Chargement"
				break
				;;
			"Quit")
				break
				;;
			*)echo "invalid option $reply";;
		esac
	done
}
choix
