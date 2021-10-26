import cgi
import index
import sqlite3

# récupération des données du formulaire
index_vin = cgi.FieldStorage()
nom_vin = index_vin.getvalue("nom_vin")
appellation = index_vin.getvalue("appellation")
couleur = index_vin.getvalue("couleur")
nb_bouteilles = index_vin.getvalue("nb_bouteilles")
millesime = index_vin.getvalue("millesime")

# insertion des données du formulaire dans la base
connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()

donnees_vin = [nom_vin, appellation, couleur, nb_bouteilles, millesime]
bouteilles = []
bouteilles.append(nb_bouteilles)


def ajout_vin(donnees_vin):
    """Ajoute du vin possedant les caracteristiques donnees"""
    curseur.execute(
        """INSERT INTO Vins(nom_vin, appellation, couleur, nb_bouteilles, millesime) VALUES(?, ?, ?, ?, ?)""", donnees_vin)
    connexion.commit()
    curseur.close()
    connexion.close()


ajout_vin(donnees_vin)


index.landing_page()
