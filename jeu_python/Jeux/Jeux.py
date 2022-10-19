from Jeux.Arme import Arme
from Jeux.Personnage import Personnage
from Jeux.Monstre import Monstre
from Jeux.Guerrier import Guerrier
from Jeux.Mage import Mage
from Jeux.Sauvegarde import Sauvegarde

class Jeux:
  def __init__(self):
    pass

  def newgame(self, event=None):
    orc = Monstre.Monstre("Orc", 15 ,3)
    baton = Arme.Arme("baton phénix", 5)
    mage = Mage.Mage(baton)
    simon = Personnage.Personnage("Pendaroue", 30, mage)
    print(simon.pseudo)
    print(f"Il reste {orc.pv} à l'orc")
    simon.classe.attaque(baton, orc)
    print(f"Il reste {orc.pv} à l'orc")