import sqlite3


class Bdd:

    def __init__(self):
        nom = 'spratacus'
        dmg = '45'
        hp = '400'
        nbm = '5'
        ide = 0

        self.conn = sqlite3.connect('bddjeu.db')

        # céer d'un curseur
        self.cur = self.conn.cursor()

        # check si table jeu existe

        if (not self.checkTablesExists(self.cur)):
            # Création de requete
            self.creationTable()

        # envoye
        self.newPlayer(nom, dmg, hp, nbm)
        self.deletePlayer(ide)
        self.recup()

        # Fermer la connexion
        self.conn.close

    def checkTablesExists(self, cur):
        self.cur.execute(
            """
            SELECT name FROM sqlite_master WHERE name='jeu';
            """
        )
        return self.cur.fetchone()

    def newPlayer(self, nom, dmg, hp, nbm):
        # creation de variable

        self.cur.execute("INSERT INTO jeu (nom, dmg, hp, nbm) VALUES ('" + nom + "', '" + dmg + "', '" + hp +"', '" + nbm + "')")

        # Envoyer de requete
        self.conn.commit()

    def creationTable(self):
        req = "CREATE TABLE jeu(id INTEGER PRIMARY KEY AUTOINCREMENT, nom VARCHAR(255), dmg VARCHAR(255), hp VARCHAR(255), nbm VARCHAR(255))"
        self.cur.execute(req)

    def deletePlayer(self, ide):
        sup = "DELETE FROM jeu WHERE nom = 'io'"
        self.cur.execute(sup)
        self.conn.commit()
    def recup(self):
        rec = "SELECT nom, dmg, hp, nbm FROM jeu WHERE nom = 'io'"
        self.cur.execute(rec)
        user1 = self.cur.fetchone()
        print(user1)

    def sauv(self,nom,dmg,hp, nbm):
        save = self.cur.execute("INSERT INTO jeu (nom, dmg, hp, nbm) VALUES ('" + nom + "', '" + dmg + "','" + hp + "','" + nbm + "')")
        self.cur.execute(save)

bdd = Bdd()
