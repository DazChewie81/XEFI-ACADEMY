# On importe les bibliothèques
from controller.classe import *
from controller.monstre import *
from time import*
#from view.UI import FenetrePrincipale

# On initie le classe jeu
class Jeu():
    
    def __init__(self):
        self.pseudo = None
        self.choix = None
        self.classe = None
        self.envaincus = 0
        self.jeux_en_cour = True
        #self.__lancement()
        
    # On créer la fonction qui permet au joueur d'infliger des dégats à l'ennemi
    def attaque_contre_monstre(self, adversaire):
        adversaire.pv -= self.classe.dmg
        print(f"{self.pseudo} attaque {adversaire.name}\nIl lui fait {self.classe.dmg} point(s) de dégat\n{adversaire.name} a maintenant {adversaire.pv} pv\n")

    # On créer la fonction qui permet à l'ennemi d'infliger des dégats au joueur
    def attaque_contre_hero(self, adversaire):
        self.classe.pv -= adversaire.dmg
        print(f"{adversaire.name} s'en prend {self.classe.pseudo}\nIl lui fait {adversaire.dmg} point(s) de dégat\n{self.pseudo} a maintenant {self.classe.pv} pv\n")

    # On créer la fonction qui lance le début du jeu
    def lancement(self):
        # Le message d'introduction
        print("Bienvenue sur 'Le Jeu de Fou', ici, vous devrez vaincre le maximum d'Ogre sans vous faire tuer....... \n")
        print("Avant de commencez, qu'elle est votre pseudo ?\n")
        #self.pseudo = '' #input("Avant de commencez, qu'elle est votre pseudo ?\n")
        print("Vous aurez le choix entre 4 classes : 1.Paladin, 2.Assassin, 3.Archer, 4.Mage")
        print("Quelle classe choisissez-vous ? \nVeuillez sélectionner le boutton correspondant !")

        #self.choix = '' #int(input("Quelle classe choisissez-vous ? \nVeuillez sélectionner le numéro correspondant !"))
        #self.__choixclasse()
        
    #On initie la fonction qui permet de choisir la classe voulue
    def choixclasse(self, num):
        choix_valide = False
        self.choix=num
        while choix_valide != True:           
            if self.choix == 1:
                self.classe = Paladin(self.pseudo)
                choix_valide = True
                                
            elif self.choix == 2:
                self.classe = Assassin(self.pseudo)
                choix_valide = True

            elif self.choix == 3:
                self.classe = Archer(self.pseudo)
                choix_valide = True
                
            elif self.choix == 4:
                self.classe = Mage(self.pseudo)
                choix_valide = True

            else:
                print("Je n'ai pas compris votre réponse, veuillez recommencer votre choix")
                print("Vous aurez le choix entre 4 classes : \n1.Paladin\n 2.Assassin\n 3.Archer\n 4.Mage")
                #self.choix = int(input("Quelle classe choisissez-vous ?"))

        #On affiche les statistiques, on lance ensuite le COMBAT    
        self.__stat()
        self.__combat()
        
    #Cette fonction permet d'afficher les attribues de la classe    
    def __stat(self):
        print(f"classe : {self.classe.name}\npseudo : {self.classe.pseudo}\npv : {self.classe.pv}\ndmg : {self.classe.dmg}\nats : {self.classe.ats}")

    # Cette fonction permet de compter le nombre d'ennemis vaincus
    def __ennemis_vaincus(self):
        self.classe.pv > 0
        self.envaincus += 1
        if self.jeux_en_cour == False:
            print("Bravo ! Vous avez vaincus",self.envaincus,"ennemis\n")
            
    #On initie la fonction qui permet aux personnages de se battrent
    def __combat(self):
        # Tant que le joueur est encore en vie on continue à créer des monstres
        while self.jeux_en_cour:
                
            joueurs_en_vie = True
                
            adversaire = Adversaire()
            adversaire.stat()
                
            while joueurs_en_vie:
                
                # Si les deux combattants ont encore de la vie, le joueur inflige des dégats à l'ennemi    
                if adversaire.pv > 0 and self.classe.pv > 0:
                    self.attaque_contre_monstre(adversaire)
                    sleep(2)
                
                # Si les deux combattants ont encore de la vie, l'ennemi inflige des dégats au joueur         
                if self.classe.pv > 0 and adversaire.pv > 0:
                    self.attaque_contre_hero(adversaire)
                    sleep(2)

                # Si après les attaques l'adversaire n'a plus de vie, on rajoute 1 au compteur d'ennemis vaincus    
                if adversaire.pv <= 0 :
                    joueurs_en_vie = False
                    print("Vous avez tué l'ennemi BRAVO !\n")
                    sleep(2)
                    self.__ennemis_vaincus()

                # Si apres les attaques le joueur n'a plus de vie, on affiche combien de monstres il a tuer        
                if self.classe.pv <= 0:
                    self.jeux_en_cour = False
                    joueurs_en_vie = False
                    print("Vous avez perdu contre l'ennemi ! GAME OVER\n")
                    sleep(2)
                    self.__ennemis_vaincus()





