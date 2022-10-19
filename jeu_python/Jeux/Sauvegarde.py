import subprocess
class Sauvegarde:
  def __init__(self, nom):
    self.nom = nom
        
  def save(self):
    fichier = open("/home/simon/Documents/XEFI-ACADEMY/jeu_python/bdd/save.txt", "a")
    fichier.write("Bonjour tout seul")
    fichier.close()
    