import subprocess
class Sauvegarde:
  def __init__(self, nom):
    self.nom = nom
        
  def save(self):
    fichier = open("saves/save.txt", "a")
    fichier.write("Bonjour tout seul")
    fichier.close()