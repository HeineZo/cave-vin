import cgi
import index
import sqlite3

# récupération des données du formulaire
index_appel = cgi.FieldStorage()
nom = index_appel.getvalue("nom")
pays = index_appel.getvalue("pays")
region = index_appel.getvalue("region")
mets = index_appel.getvalue("mets")

# connexion à la base 'base_vins.db'
connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()

# on les range dans un tuple
donnees_appel = (nom, pays, region, mets)


def ajout_appel(donnees_appel):
    """Ajoute les valeurs dans le tableau appellation"""
    curseur.execute(
        """INSERT INTO Appellations(nom, pays, region, mets) VALUES(?, ?, ?, ?)""", donnees_appel)


ajout_appel(donnees_appel)

connexion.commit()
curseur.close()
connexion.close()

index.landing_page()  # lancement de la page formulaire
