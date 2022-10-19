import sqlite3


class Bdd:


    def __init__(self):
        
        nom = 'eihfuhu'
        mail = 'dpokcvdhi@gmail.com'
        
        self.conn = sqlite3.connect('bddjeu.db')

        #céer d'un curseur
        self.cur = self.conn.cursor()
        
        #check si table jeu existe
        
        if (not self.checkTablesExists(self.cur)):
            
            # Création de requete 
            self.creationTable()
            
        #envoye
        self.newPlayer(nom, mail)   
        #self.deletePlayer()

        # Fermer la connexion 
        self.conn.close

    def checkTablesExists (self, cur):
        self.cur.execute(
        """
        SELECT name FROM sqlite_master WHERE name='jeu';
        """
        )
        return self.cur.fetchone()




    def newPlayer (self, nom, mail):
        
        # creation de variable
        #o = "oj"
        #p = "pkgmail.com"

        #self.sql_insert = "INSERT INTO jeu (nom, email) VALUES ('" + nom +"', '"+ mail +"')"
        
        self.cur.execute("INSERT INTO jeu (nom, email) VALUES ('" + nom +"', '"+ mail +"')")
         
         # Envoyer de requete 
        self.conn.commit()

    def creationTable(self):
        req = "CREATE TABLE jeu(id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, email TEXT)"
        self.cur.execute(req)
        
        
    #def deletePlayer(self):
    #    sup = "DELETE FROM jeu WHERE nom = 'eihfuhu'"
    #    self.cur.execute(sup)
    #    print('alo')
        
        
        
        
bdd= Bdd()