from classe import *

print("Bienvenue sur 'Le Jeu de Fou', ici, vous devrez vaincre le maximum d'Ogre sans vous faire tuer....... ")
pseudo = input("Avant de commencez, qu'elle est votre pseudo ?")

print("Vous aurez le choix entre 4 classes : 1.Paladin, 2.Assassin, 3.Archer, 4.Mage")
choix = int(input("Quelle classe choisissez-vous ? \nVeuillez sélectionner le numéro correspondant !"))


choix_valide = False
while choix_valide != True:
    
    if choix == 1:
        classe = Paladin(pseudo)
        choix_valide = True
        
        
    elif choix == 2:
        classe = Assassin(pseudo)
        choix_valide = True

    elif choix == 3:
        classe = Archer(pseudo)
        choix_valide = True
        
    elif choix == 4:
        classe = Mage(pseudo)
        choix_valide = True
        
    else:
        print("Je n'ai pas compris votre réponse, veuillez recommencer votre choix")
        print("Vous aurez le choix entre 4 classes : 1.Paladin, 2.Assassin, 3.Archer, 4.Mage")
        choix = int(input("Quelle classe choisissez-vous ?"))

classe.stat()

