import Arme
class Guerrier:
  def __init__(self, arme):
    self.arme = arme

#fait perdre des pv à ceQuiPerdDesPv en fonction de ceQuiFaitPerdreDesPv
  def attaque(self, ceQuiFaitPerdreDesPv, ceQuiPerdDesPv):
      self.ceQuiPerdDesPv = ceQuiPerdDesPv
      self.ceQuiFaitPerdreDesPv = ceQuiFaitPerdreDesPv
      ceQuiPerdDesPv.pv = ceQuiPerdDesPv.pv - ceQuiFaitPerdreDesPv.degat