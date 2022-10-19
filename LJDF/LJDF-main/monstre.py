import random


class Monstre:
    
    def stat(self):
        print(f"nom : {self.name}\npv : {self.pv}\ndmg : {self.dmg}\nats : {self.ats}")
    
class Adversaire(Monstre):
    def __init__(self):
      monstre_list = ['Goblin', 'Orque', 'Voleur', 'Dragon', 'Vampire']  
      self.name = random.choice(monstre_list) 
      self.pv = random.randrange(10, 100)    
      self.dmg = random.randrange(10, 20)
      self.ats = random.randrange(1, 10)
      
         
          