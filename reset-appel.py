import index
import sqlite3

# connexion à la base 'base_vins.db'
connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()


def reset_table():
    """Réinitialisation de la table Appellations"""
    # on supprime tous les éléments
    curseur.execute("""DELETE FROM Appellations""")
    # on remet l'incrémentation à 0
    curseur.execute(
        """DELETE FROM sqlite_sequence WHERE name = 'Appellations'""")
    connexion.commit()
    curseur.close()
    connexion.close()


reset_table()
index.landing_page()
