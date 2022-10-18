class Classe:
  def __init__(self, classes):
    self.classes = classes
    
#fait perdre des pv à ceQuiPerdDesPv en fonction de ceQuiFaitPerdreDesPv
  def attaque(self, ceQuiFaitPerdreDesPv, ceQuiPerdDesPv):
      self.ceQuiPerdDesPv = ceQuiPerdDesPv
      self.ceQuiFaitPerdreDesPv = ceQuiFaitPerdreDesPv
      ceQuiPerdDesPv.pv = ceQuiPerdDesPv.pv - ceQuiFaitPerdreDesPv.degat