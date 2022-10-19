from classe import *
from monstre import *
from time import*

class LJDF():
    
    def __init__(self):
        self.pseudo = None
        self.choix = None
        self.classe = None
        self.envaincus = 0
        self.jeux_en_cour = True
        #self.__lancement()
        
    def attaque_contre_monstre(self, adversaire):
        adversaire.pv -= self.classe.dmg
        print(f"{self.pseudo} attaque {adversaire.name}\nIl lui fait {self.classe.dmg} point(s) de dégat\n{adversaire.name} a maintenant {adversaire.pv} pv\n")
        
    def attaque_contre_hero(self, adversaire):
        self.classe.pv -= adversaire.dmg
        print(f"{adversaire.name} s'en prend {self.classe.pseudo}\nIl lui fait {adversaire.dmg} point(s) de dégat\n{self.pseudo} a maintenant {self.classe.pv} pv\n")

            
    def lancement(self):
        
        print("Bienvenue sur 'Le Jeu de Fou', ici, vous devrez vaincre le maximum d'Ogre sans vous faire tuer....... \n")
        self.pseudo = input("Avant de commencez, qu'elle est votre pseudo ?\n")

        print("Vous aurez le choix entre 4 classes : 1.Paladin, 2.Assassin, 3.Archer, 4.Mage")
        self.choix = int(input("Quelle classe choisissez-vous ? \nVeuillez sélectionner le numéro correspondant !"))
        
        self.__choixclasse()
        
    def __choixclasse(self):
        choix_valide = False
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
                self.choix = int(input("Quelle classe choisissez-vous ?"))
            
        self.__stat()
        self.__combat()
        
        
    def __stat(self):
        print(f"classe : {self.classe.name}\npseudo : {self.classe.pseudo}\npv : {self.classe.pv}\ndmg : {self.classe.dmg}\nats : {self.classe.ats}")


    def __ennemis_vaincus(self):
        self.classe.pv > 0
        self.envaincus += 1
        if self.jeux_en_cour == False:
            print("Bravo ! Vous avez vaincus",self.envaincus,"ennemis\n")
            

    def __combat(self):

        while self.jeux_en_cour:
                
            joueurs_en_vie = True
                
            adversaire = Adversaire()
            adversaire.stat()
                
            while joueurs_en_vie:
                    
                if adversaire.pv > 0 and self.classe.pv > 0:
                    self.attaque_contre_monstre(adversaire)
                    sleep(2)
                        

                if self.classe.pv > 0 and adversaire.pv > 0:
                    self.attaque_contre_hero(adversaire)
                    sleep(2)
                    
                if adversaire.pv <= 0 :
                    joueurs_en_vie = False
                    print("Vous avez tué l'ennemi BRAVO !\n")
                    sleep(2)
                    self.__ennemis_vaincus()
                        
                if self.classe.pv <= 0:
                    self.jeux_en_cour = False
                    joueurs_en_vie = False
                    print("Vous avez perdu contre l'ennemi ! GAME OVER\n")
                    sleep(2)
                    self.__ennemis_vaincus()
 
        print("FINITO")





