import cgi
import index
import sqlite3
import functools

# récupération des données du formulaire
index_vin = cgi.FieldStorage()
mets = index_vin.getvalue("search_mets")

# connexion à la base 'base_vins.db'
connexion = sqlite3.connect('base_vins.db')
curseur = connexion.cursor()

donnees_mets = (mets)


def recherche_mets(donnees):
    """ Recherche quel met correspond à quel vin"""
    curseur.execute("""SELECT nom_vin
                        FROM Vins AS V 
                        JOIN Appellations AS A 
                        ON V.appellation = A.nom                        
                        WHERE A.mets LIKE ?
                        ORDER BY A.mets""", ('%' + donnees + '%',))
    i = curseur.fetchall()
    # on enlève les caractères parasites
    final = "/".join(map(str, i))
    final = final.replace(',', '').replace(
        "'", "").replace("(", "").replace(")", "")
    # on le retourne en html
    print("""<a class="recherche">Vin(s) associé(s) :""", final)
    print("""</a>""")


recherche_mets(donnees_mets)
index.landing_page()
