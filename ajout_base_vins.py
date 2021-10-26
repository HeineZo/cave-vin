import cgi
import index
import sqlite3

# connexion à la base 'base_vins.db'
connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()

# on récupère les informations rentrée dans le popup
index_vin = cgi.FieldStorage()
id_vin = index_vin.getvalue("id_vin")
nb_bouteilles = index_vin.getvalue("nb_bouteilles_ask")

# on les range dans un tuple
donnees_vin = (nb_bouteilles, id_vin)


def ajout_vin(donnees):
    """Supprime une quantité désirée de vin en fonction de son id"""
    curseur.execute(
        """UPDATE Vins SET nb_bouteilles = nb_bouteilles + (?) WHERE id = (?)""", donnees)
    connexion.commit()
    curseur.close()
    connexion.close()


ajout_vin(donnees_vin)

index.landing_page()
