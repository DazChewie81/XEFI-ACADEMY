import random


class Monstre:
    
    def stat(self):
      print(f" Un {self.nom} à {self.pv} pv, {self.dmg} de d'attaque et {self.ats} de vitesse d'attaque, vous attaque.")
    
class Orque(Monstre):
    def __init__(self):
      monstre_list = ['Goblin', 'Orque', 'Voleur', 'Dragon', 'Vampire']  
      self.nom = random.choice(monstre_list) 
      self.pv = random.randrange(10, 100)    
      self.dmg = random.randrange(10, 20)
      self.ats = random.randrange(1, 10)
      
         
          
testorque = Orque()
testorque.stat()
