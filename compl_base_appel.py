import cgi
import index
import sqlite3

index_appel = cgi.FieldStorage()
nom = index_appel.getvalue("nom")
pays = index_appel.getvalue("pays")
region = index_appel.getvalue("region")
met1 = index_appel.getvalue("met1")
met2 = index_appel.getvalue("met2")
met3 = index_appel.getvalue("met3")

connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()

donnees_appel = (nom, pays, region)
donnees_mets = (met1, met2, met3)

def ajout_appel(donnees_appel):
    """Ajoute les valeurs dans la table appellation"""
    curseur.execute(
        """INSERT INTO Appellations(nom, pays, region) VALUES(?, ?, ?)""", donnees_appel)

def ajout_met(donnees_mets):
    """Ajoute les valeurs dans la table mets"""
    curseur.executemany(
        """INSERT INTO Mets(nom_met) VALUES(?)
            INSERT INTO Mets(nom_met) VALUES(?)
            INSERT INTO Mets(nom_met) VALUES(?)""", donnees_mets)

ajout_appel(donnees_appel)
ajout_met(donnees_mets)

connexion.commit()
curseur.close()
connexion.close()
index.landing_page()
