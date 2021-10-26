import index
import sqlite3

# connexion à la base 'base_vins.db'
connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()


def reset_vin():
    """Réinitialisation de la table Vins"""
    # on supprime tous les éléments
    curseur.execute("""DELETE FROM Vins""")
    # on remet l'incrémentation à 0
    curseur.execute("""DELETE FROM sqlite_sequence WHERE name = 'Vins'""")
    connexion.commit()
    curseur.close()
    connexion.close()


reset_vin()
index.landing_page()
