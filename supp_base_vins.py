import cgi
import index
import sqlite3
import functools

# on récupère l'id du vin et le nombre de bouteilles à supprimer
form = cgi.FieldStorage()
nb_bouteilles = int(form.getvalue("nb_bouteilles_ask"))
id_vin = form.getvalue("id_vin")

# on les range dans des listes
donnees_vin = [nb_bouteilles, id_vin]
id = [id_vin]

# connexion à la base 'base_vins.db'
connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()


def del_vin():
    """Supprime le vin s'il n'y a plus de bouteilles"""
    curseur.execute(
        """SELECT nb_bouteilles FROM Vins WHERE id = (?)""", id)
    i = curseur.fetchone()
    # On transforme le résultat obtenue en INTEGER
    rest = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    # S'il n'y a plus de bouteilles alors on supprime totalement l'élément
    if rest <= 0:
        curseur.execute(
            """DELETE FROM Vins WHERE id = (?)""", id)


def supp_vin(donnees):
    """Supprime une quantité désirée de vin en fonction de son id"""
    curseur.execute(
        """UPDATE Vins SET nb_bouteilles = nb_bouteilles - (?) WHERE id = (?)""", donnees)
    del_vin()
    connexion.commit()
    curseur.close()
    connexion.close()


supp_vin(donnees_vin)

index.landing_page()
