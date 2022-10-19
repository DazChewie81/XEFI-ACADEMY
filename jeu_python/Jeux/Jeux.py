from .Arme import Arme
from .Personnage import Personnage
from .Monstre import Monstre
from .Guerrier import Guerrier
from .Mage import Mage
from .Sauvegarde import Sauvegarde

class Jeux:
  def __init__(self):
    pass

  def newgame(self, event=None):
    orc = Monstre("Orc", 15 ,3)
    baton = Arme("baton phénix", 5)
    mage = Mage(baton)
    simon = Personnage("Pendaroue", 30, mage)
    print(simon.pseudo)
    print(f"Il reste {orc.pv} à l'orc")
    simon.classe.attaque(baton, orc)
    print(f"Il reste {orc.pv} à l'orc")