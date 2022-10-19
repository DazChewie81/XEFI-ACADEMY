from classe import*
class JeuPrincipal():
    def jeu(self):
        print("Bienvenue sur 'Le Jeu de Fou', ici, vous devrez vaincre le maximum d'Ogre sans vous faire tuer....... ")
        self.pseudo = input("Avant de commencez, qu'elle est votre pseudo ?")

        print("Vous aurez le choix entre 4 classes :\n 1.Paladin,\n 2.Assassin,\n 3.Archer,\n 4.Mage")
        self.choix = int(input("Quelle classe choisissez-vous ? \nVeuillez sélectionner le numéro correspondant !"))


        self.choix_valide = False
        while self.choix_valide != True:
            
            if self.choix == 1:
                self.classe = Paladin(pseudo)
                self.choix_valide = True
                
                
            elif self.choix == 2:
                self.classe = Assassin(pseudo)
                self.choix_valide = True

            elif self.choix == 3:
                self.classe = Archer(pseudo)
                self.choix_valide = True
                
            elif self.choix == 4:
                self.classe = Mage(pseudo)
                self.choix_valide = True
                
            else:
                print("Je n'ai pas compris votre réponse, veuillez recommencer votre choix")
                print("Vous aurez le choix entre 4 classes : 1.Paladin, 2.Assassin, 3.Archer, 4.Mage")
                self.choix = int(input("Quelle classe choisissez-vous ?"))

        self.classe.stat()

app = JeuPrincipal()
app