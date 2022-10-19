
class Monstre:
  def __init__(self, nom, pv, degat):
    self.nom = nom
    self.pv = pv
    self.degat = degat
  
  def attaque(self, ceQuiPerdDesPv):
    self.ceQuiPerdDesPv = ceQuiPerdDesPv
    self.ceQuiPerdDesPv.pv = ceQuiPerdDesPv.pv - self.degat