class Personnage():     
       
    # Constructeur         
    
    def stat(self):
        print(f"classe : {self.name}\npseudo : {self.pseudo}\npv : {self.pv}\ndmg : {self.dmg}\nats : {self.ats}")
        
    def testbagare(self, Assassin):
        Assassin.pv -= self.dmg
        print(f"{self.pseudo} attaque {Assassin.pseudo}\nIl lui fait {self.dmg} point(s) de dégat\n{Assassin.pseudo} a maintenant {Assassin.pv} pv")
    def testrendlescoups(self, Assassin):
        self.pv -= Assassin.dmg
        print(f"{Assassin.pseudo} s'en prend {self.pseudo}\nIl lui fait {Assassin.dmg} point(s) de dégat\n{self.pseudo} a maintenant {self.pv} pv")
   
class Paladin(Personnage):
    def __init__(self,pseudo):
        self.name = "Paladin"
        self.pseudo = pseudo
        self.pv = 200
        self.dmg = 10
        self.ats = 10
        
class Assassin(Personnage):
    def __init__(self,pseudo):
        self.name = "Assassin"
        self.pseudo = pseudo
        self.pv = 100
        self.dmg = 35
        self.ats = 30
        
class Archer(Personnage):
    def __init__(self,pseudo):
        self.name = "Archer"
        self.pseudo = pseudo
        self.pv = 75
        self.dmg = 20
        self.ats = 30
        
class Mage(Personnage):
    def __init__(self,pseudo):
        self.name = "Mage"
        self.pseudo = pseudo
        self.pv = 75
        self.dmg = 50
        self.ats = 10
    

