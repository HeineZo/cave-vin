import cgi
import sqlite3
import script
import functools


def landing_page():
    print("""
        <!DOCTYPE html>
        <html lang ="fr">
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
            <title> Cave à vin </title>
            <link rel="shortcut icon" href="src/img/grapes-color.png" />
            <script defer src="https://use.fontawesome.com/releases/v5.15.3/js/all.js"></script>
            <script type=""text/javascript" src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        </head>

        <body>
            <!-- On met l'entierté du body dans une div afin de le rendre flou quand on cliquera sur un popup -->
            <div class="container" id="blur">
                <!-- Afin de se balader sur le site tout simplement -->
                <scroll-page id="page-0">
                </scroll-page>
                <!-- Haut de page -->
                <section class="top-page">
                    <!-- Menu de navigation -->
                    <header class="header">
                        <a href='#page-0'>
                            <img src="src/img/grapes.png"alt="Icone de vin">
                        </a>
                        <nav class="nav">
                            <li>
                                <a href='#page-1' class="middle">Ajouter</a>
                            </li>
                            <li>
                                <a href='#page-2' class="middle">Afficher</a>
                            </li>
                        </nav>
                    </header>

                    <div class="landing_page">
                        <!-- Grand titre animé -->
                        <svg class="title" viewBox="0 0 960 300">
                            <symbol id="s-text">
                                <text text-anchor="middle" x="50%" y="80%" class="big-title">Bienvenue dans votre</text>
                                <text text-anchor="middle" x="50%" y="100%" class="big-title">cave à vin</text>
                            </symbol>
                            <g class = "g-ants">
                                <use xlink:href="#s-text" class="text-copy"></use>
                                <use xlink:href="#s-text" class="text-copy"></use>
                                <use xlink:href="#s-text" class="text-copy"></use>
                                <use xlink:href="#s-text" class="text-copy"></use>
                                <use xlink:href="#s-text" class="text-copy"></use>
                            </g>
                        </svg>
                    </div>
                </section>

                <scroll-page id="page-1">
                </scroll-page>

                <!-- Milieu de page -->
                <section class="first">
                    <div class="Ajouter">
                        <h2 class="mid-title"> Ajouter </h2>
                    </div>
                    <!-- Ajouter de nouveaux vin -->
                    <form action = "/compl_base_vins.py" method = "post">
                        <fieldset class="vin">
                            <legend> Nouveau vin </legend>
                            <p>
                                <label for = "nom_vin"> Nom du vin </label>
                                <input type = "text" id = "nom_vin" name = "nom_vin" placeholder="Poggerino" required>
                                <label for = "appellation"> L'appellation du vin </label>
                                <input type = "text" id = "appellation" name = "appellation" placeholder="Chianti Classico" required>
                                <label for = "couleur"> Couleur du vin </label>
                                <input type = "text" id = "couleur" name = "couleur" placeholder="Rouge" required>
                                <label for="nb_bouteilles">Nombre de bouteilles :</label>
                                <input class= "numero" type="number" id="nb_bouteilles" name="nb_bouteilles" min="1" max="99" placeholder="0" required>
                                <label for="millesime">Millésime (année) :</label>
                                <input class= "millesime" id="millesime" name="millesime" placeholder="1992" required>
                                <div>
                                    <button type="submit" class="submit">Envoyer
                                        <i class="fas fa-arrow-up"></i>
                                    </button>
                                </div>
                            </p>
                        </fieldset>
                    </form>

                    <!-- Ajouter une nouvelle appellation -->
                    <form action = "/compl_base_appel.py" method = "post">
                        <fieldset class="appellation">
                            <legend> Nouvelle appellation </legend>
                            <p>
                                <label for = "nom"> Nom de l'appellation </label>
                                <input type = "text" id = "nom" name = "nom" placeholder="Chianti classico" required>""")
    liste_region()
    print("""                   <label for="pays"> Pays </label>
                                <select name="pays" id="pays" required>
                                    <option value="" selected="selected">Selectionnez un pays</option>
                                </select>
                                <label for="region"> Région </label>
                                <select name="region" id="region" required>
                                    <option value="" selected="selected" required>Selectionnez une région</option>
                                </select>
                                <label for = "mets"> Mets associés </label>
                                <input type = "text" id = "mets" name = "mets" placeholder="Charcuterie, Fromages" required>
                                <div>
                                    <button type="submit" class="submit">Envoyer
                                        <i class="fas fa-arrow-up"></i>
                                    </button>
                                </div>
                            </p>
                        </fieldset>
                    </form>
                </section>

                <scroll-page id="page-2">
                </scroll-page>

                <!-- Bas de page -->
                <section class="second">
                    <div class="Afficher">
                        <h2 class="mid-title"> Afficher </h2>
                    </div>
                    <div class="affich_vin">
                        <!-- Bouton popup pour ajouter ou supprimer des vins existants -->
                        <a class="edit-icon" onclick="toggle()" title="Ajouter/Supprimer"><i class="far fa-edit"></i></a>
                            """)
    affich_vins()
    print("""       </div>
                    <form action = "/reset-vin.py" method = "post">
                        <div class="details">
                            <!-- Bouton pour réinitialiser le tableau -->
                            <button class="reset-vin">
                                <span class="short-text">
                                    <i class="fas fa-sync-alt"></i>
                                </span>
                                <span class="long-text">RESET</span>
                            </button>
                            <!-- Animation -->
                            <script type = "text/javascript">
                                $(".reset-vin").hover(function() {
                                    $(".long-text").addClass("show-long-text");
                                    $(".short-text").addClass("show-short-text");
                                }, function () {
                                    $(".long-text").removeClass("show-long-text");
                                    $(".short-text").removeClass("show-short-text");
                                });
                            </script>
                            <!-- Bouton permettant de savoir le total des vins et des bouteilles par couleur -->
                            <a onclick="enable()" id="arrow" title="Détails"><i class="fas fa-angle-double-down"></i></a>
                            <div id="more">
                                <a class="all-wine"><i class="fas fa-wine-glass-alt"></i>
                                &nbsp;""", total())
    print("""                   bouteilles au total
                                </a>
                                <a class="unique">""", nb_bouteilles_couleur())

    print("""                   </a>
                            </div>
                        </div>
                    </form>
                    <!-- Ouvrir le popup -->
                    <script>
                        function enable(){
                            var more = document.getElementById('more');
                            more.classList.toggle('active');
                            var arrow = document.getElementById('arrow');
                            arrow.classList.toggle('down');
                        }
                    </script>
                    <div class = "affich_appel">
                        <!-- Bouton popup permettant de connaître les vins et les appellations en fonction des régions -->
                        <a class="question-icon" onclick="activate()" title="En savoir plus sur les régions"><i class="fas fa-question"></i></a> """)
    affich_appel()
    print("""           <!-- Bouton de réinitialisation pour la table appellation -->
                        <form action = "/reset-appel.py" method = "post">
                            <div class="appel">
                                <button class="reset-vin">
                                    <span class="short-text">
                                        <i class="fas fa-sync-alt"></i>
                                    </span>
                                    <span class="long-text">RESET</span>
                                </button>
                                <script type = "text/javascript">
                                    $(".reset-vin").hover(function() {
                                        $(".long-text").addClass("show-long-text");
                                        $(".short-text").addClass("show-short-text");
                                    }, function () {
                                        $(".long-text").removeClass("show-long-text");
                                        $(".short-text").removeClass("show-short-text");
                                    });
                                </script>
                            </div>
                        </form>
                    </div >                
                </section>
            </div>
            <!-- Popup pour ajouter ou supprimer des vins existants -->
            <div id="pop">
                <form action = "/supp_base_vins.py" method = "post">
                    <h2 class="add-title"> Ajouter / Supprimer un vin </h2>
                    <div class="form-container">
                        <label for = "id_vin" class="vin_id">ID du vin</label>
                        <input type = "text" id = "id_vin" name = "id_vin" placeholder = "1" required>
                        <label for = "nb_bouteilles" class="btl_id">Nombre de bouteilles</label>
                        <input class = "numero" type = "number" id = "nb_bouteilles_ask" name = "nb_bouteilles_ask" min = "1" max = "99" placeholder = "0" required>
                    </div>
                    <div class="logo">
                        <button type = "submit" class = "supprim">Supprimer
                        <i class = "fas fa-trash-alt"></i>
                        </button>
                        <button type = "submit" class = "ajout" formaction = "/ajout_base_vins.py">Ajouter
                        <i class = "fas fa-plus"></i>
                        </button>
                    </div>
                    <a class="close" onclick="toggle()">Fermer</a>
                </form>
            </div>
            <!-- Popup des vins et des appellations en fonction des régions -->
            <div id="question">
                <h2 class="more-region">Provenance des vins et des appellations</h2>""")
    affich_region()
    print("""
                <a class="close" onclick="activate()">Fermer</a>
            </div>
            <!-- Animation d'affichage pour les popup et effet de flou -->
            <script type="text/javascript">
                function toggle(){
                    var blur = document.getElementById('blur');
                    blur.classList.toggle('active');
                    var pop = document.getElementById('pop');
                    pop.classList.toggle('active');
                    window.scrollTo(2000, 2000);
                }
                function activate(){
                    var blur = document.getElementById('blur');
                    blur.classList.toggle('active');
                    var question = document.getElementById('question');
                    question.classList.toggle('active');
                    window.scrollTo(1900, 1900);
                }
            </script>
            <!-- Rechercher quel met est associé à quel vin -->
            <div class="container-mets">
                <div class="mets">
                    <form action = "/mets.py" method = "post">
                        <h2 class="mets-title"> Mets associés aux vins </h2>
                        <input type = "text" id = "search_mets" name = "search_mets" placeholder="Charcuterie" required>
                        <button class="meal"><i class="fas fa-concierge-bell"></i></button>
                    </form>
                </div>
            </div>
        </body>
        <!-- Pied de page -->
        <footer>
            <div class="footer-content">
                <h3> Lycée Marcellin Berthelot </h3>
                <ul class='contact'>
                    <li class="reseaux"><a class="reseaux" href='https://www.lycee-marcellinberthelot-questembert.ac-rennes.fr/'><i class="fas fa-home"></i></a></li>
                    <li class="reseaux"><a class="reseaux" href='https://www.instagram.com/cvl.marcellin_berthelot/'><i class="fab fa-instagram"></i></a></li>
                </ul>
                <p>Copyright &copy;2021 designed by <span>Enzo & Elouann</span></p>
            </div>
        </footer>
    </html>""")


def affich_vins():
    """Tableau des vins"""
    # connexion à la base 'base_vins.db'
    connexion = sqlite3.connect('base_vins.db')
    curseur = connexion.cursor()
    # Zone de recherche faisant office de filtre dans le tableau afin de trouver un élément plus rapidement
    print("""<input type="text" id="SearchVin" onkeyup="SearchFunction()" placeholder="Rechercher" title='Exemple: "Poggerino"'>""")
    print("<table class=""centre"" id=""myTable"">")  # tableau des vins
    print("<thead>")
    # nom de la table avec 6 colonnes
    print("<tr><th colspan = '6'> Vins </th></tr>")
    print("</thead>")
    print("<tbody>")
    # en-tête
    print("<tr><th>ID</th><th>Nom</th><th>Appellation</th><th>Couleur</th><th>Nombre</th><th>Millésime</th></tr>")
    # Récupérer tous les éléments du tableau vin
    curseur.execute("""SELECT * FROM Vins""")
    for tuple in curseur:  # affichage des éléments
        print("<tr>")
        liste = list(tuple)
        for champ in liste:
            print("<td>" + str(champ) + "</td>")
    print("</tr>")
    print("</tbody>")
    print("</table>")
    # Javascript permettant le filtrage des données dans la zone de recherche
    print("""<script>
                function SearchFunction(event) {
                    //On met toutes les valeurs en majuscule afin d'avoir un maximum de résultats
                    var filter = event.target.value.toUpperCase();
                    //On choisit la table des vins
                    var rows = document.querySelector("#myTable tbody").rows;

                    for (var i = 0; i < rows.length; i++) {
                        // Déclaration des variables qui correspondent à chaque colonne du tableau
                        var id = rows[i].cells[0].textContent.toUpperCase();
                        var nom = rows[i].cells[1].textContent.toUpperCase();
                        var appellation = rows[i].cells[2].textContent.toUpperCase();
                        var couleur = rows[i].cells[3].textContent.toUpperCase();
                        var nombre = rows[i].cells[4].textContent.toUpperCase();
                        var millesime = rows[i].cells[5].textContent.toUpperCase();
                        // Si l'élément correspond, alors l'afficher
                        if (id.indexOf(filter) > -1 || nom.indexOf(filter) > -1 || appellation.indexOf(filter) > -1 || couleur.indexOf(filter) > -1 || nombre.indexOf(filter) > -1 || millesime.indexOf(filter) > -1) {
                            rows[i].style.display = "";
                        } else {
                            rows[i].style.display = "none";
                        }
                    }
                }

                document.querySelector('#SearchVin').addEventListener(
                    'keyup', SearchFunction, false);
            </script>""")


def affich_appel():
    """Tableau des appellations"""
    # connexion à la base 'base_vins.db'
    connexion = sqlite3.connect('base_vins.db')
    curseur = connexion.cursor()
    # Zone de recherche faisant office de filtre dans le tableau afin de trouver un élément plus rapidement
    print("""<input type="text" id="SearchAppellation" onkeyup="SearchFunction1()" placeholder="Rechercher" title='Exemple: "Toscane"'>""")
    print("<table class=""centre"" id=""myTable1"">")  # tableau des appellations
    print("<thead>")
    # nom de la table avec 6 colonnes
    print("<tr><th colspan = '5'> Appellations </th></tr>")
    print("</thead>")
    print("<tbody>")
    # en-tête
    print("<tr><th>ID</th><th>Nom</th><th>Pays</th><th>Région</th><th>Mets</th></tr>")
    # Récupérer tous les élements du tableau appellation
    curseur.execute("""SELECT * FROM Appellations""")
    for tuple in curseur:  # affichage des éléments
        print("<tr>")
        liste = list(tuple)
        for champ in liste:
            print("<td>" + str(champ) + "</td>")
    print("</tr>")
    print("</tbody>")
    print("</table>")
    curseur.close()
    connexion.close()
    # Javascript permettant le filtrage des données dans la zone de recherche
    print("""<script type="text/javascript">
                function SearchFunction1(event) {
                    //On met toutes les valeurs en majuscule afin d'avoir un maximum de résultats
                    var filter = event.target.value.toUpperCase();
                    //On choisit la table des appellations
                    var rows = document.querySelector("#myTable1 tbody").rows;

                    for (var i = 0; i < rows.length; i++) {
                        // Déclaration des variables qui correspondent à chaque colonne du tableau
                        var id = rows[i].cells[0].textContent.toUpperCase();
                        var nom = rows[i].cells[1].textContent.toUpperCase();
                        var pays = rows[i].cells[2].textContent.toUpperCase();
                        var region = rows[i].cells[3].textContent.toUpperCase();
                        var mets = rows[i].cells[4].textContent.toUpperCase();
                        // Si l'élément correspond, alors l'afficher
                        if (id.indexOf(filter) > -1 || nom.indexOf(filter) > -1 || pays.indexOf(filter) > -1 || region.indexOf(filter) > -1 || mets.indexOf(filter) > -1) {
                            rows[i].style.display = "";
                        } else {
                            rows[i].style.display = "none";
                        }
                    }
                }

                document.querySelector('#SearchAppellation').addEventListener(
                    'keyup', SearchFunction1, false);
            </script>""")


def affich_region():
    """Tableau des régions"""
    # connexion à la base 'base_vins.db'
    connexion = sqlite3.connect('base_vins.db')
    curseur = connexion.cursor()
    print("<table class=""table_region"">")  # nouveau tableau région
    print("<thead>")
    # nom de la table avec 3 colonnes
    print("<tr><th colspan = '3'> Régions </th></tr>")
    print("</thead>")
    print("<tbody>")
    print("<tr><th>Région</th><th>Vin</th><th>Appellation</th></tr>")  # en-tête
    # Faire le lien entre le tableau appellation et le tableau vin
    curseur.execute("""SELECT region, GROUP_CONCAT(nom_vin) AS Nom_vin, GROUP_CONCAT(appellation) AS appellation 
                        FROM Vins AS V 
                        JOIN Appellations AS A 
                        ON V.appellation = A.nom 
                        GROUP BY region;
                    """)
    for tuple in curseur:  # affichage des éléments
        print("<tr>")
        liste = list(tuple)
        for champ in liste:
            print("<td>" + str(champ) + "</td>")
    print("</tr>")
    print("</tbody>")
    print("</table>")
    curseur.close()
    connexion.close()


def total():
    """Total des bouteilles"""
    # connexion à la base 'base_vins.db'
    connexion = sqlite3.connect('base_vins.db')
    curseur = connexion.cursor()
    # Récolter toutes les bouteilles
    curseur.execute("""SELECT SUM(nb_bouteilles) FROM Vins""")
    i = curseur.fetchone()
    # Les transformer en int pour les afficher
    rest = functools.reduce(lambda sub, ele: sub * 10 + ele, i)
    curseur.close()
    connexion.close()
    return rest


def nb_bouteilles_couleur():
    """Nombre de bouteilles par couleur"""
    # connexion à la base 'base_vins.db'
    connexion = sqlite3.connect('base_vins.db')
    curseur = connexion.cursor()
    # Récolter toutes les bouteilles par couleur
    curseur.execute(
        """SELECT couleur, SUM (nb_bouteilles)
	        FROM Vins
	        GROUP BY couleur;""")
    i = curseur.fetchall()
    curseur.close()
    connexion.close()
    final = []
    # Les afficher sans charactères parasites
    for tup in i:
        tup = ' {1} bouteilles de {0} <br>'.format(*tup)
        final.append(tup)

    return " ".join(map(str, final))


def liste_region():
    """Choix des régions"""
    print("""<script>
                // On déclare tous les pays et toutes les régions de ces pays
                var subjectObject = {
                "Allemagne": {
                    "Ahr": ["Ahr"],
                    "Pays de Bade": ["Pays de Bade"],
                    "Franconie": ["Franconie"],
                    "Hessische Bergstrasse": ["Hessische Bergstrasse"],
                    "Mittelrhein": ["Mittelrhein"],
                    "Mosel": ["Mosel"],
                    "Nahe": ["Nahe"],
                    "Pfalz": ["Pfalz"],
                    "Rheingau": ["Rheingau"],
                    "Rheinhessen": ["Rheinhessen"],
                    "Saale-Unstrut": ["Saale-Unstrut"],
                    "Saxe": ["Saxe"],
                    "Wurtemberg": ["Wurtemberg"],
                },
                "Argentine": {
                    "Mendoza": ["Mendoza"],
                    "San Juan": ["San Juan"],
                    "Salta": ["Salta"],
                    "La Rioja": ["La Rioja"],
                    "Catamarca": ["Catamarca"],
                    "Rio Negro": ["Rio Negro"],
                    "Jujuy": ["Jujuy"],
                    "Neuquen": ["Neuquen"],
                    "Medanos": ["Medanos"],
                },
                "Espagne": {
                    "Alicante": ["Alicante"],
                    "Almansa": ["Almansa"],
                    "Catalogne": ["Catalogne"],
                    "Jumilla": ["Jumilla"],
                    "Penedes": ["Penedes"],
                    "Priorat Montsant": ["Priorat Montsant"],
                    "Ribera del Duero": ["Ribera del Duero"],
                    "Rioja": ["Rioja"],
                    "Toro": ["Toro"],
                    "Yecla": ["Yecla"],
                },
                "Etats-Unis": {
                    "Central Valley":["Central Valley"],
                    "Napa Valley":["Napa Valley"],
                    "Sonoma Valley":["Sonoma Valley"],
                    "Oregon":["Oregon"],
                    "Etat de Washington":["Etat de Washington"],
                },
                "France": {
                    "Alsace":["Alsace"],
                    "Beaujolais et Lyonnais":["Beaujolais et Lyonnais"],
                    "Bordelais":["Bordelais"],
                    "Bourgogne":["Bourgogne"],
                    "Champagne":["Champagne"],
                    "Corse":["Corse"],
                    "Jura":["Jura"],
                    "Languedoc":["Languedoc"],
                    "Lorraine":["Lorraine"],
                    "Poitou-Charentes":["Poitou-Charentes"],
                    "Provence":["Provence"],
                    "Roussillon":["Roussillon"],
                    "Savoie et Bugey":["Savoie et Bugey"],
                    "Sud-Ouest":["Sud-Ouest"],
                    "Vallée de la Loire et Centre":["Vallée de la Loire et Centre"],
                    "Vallée du Rhone":["Vallée du Rhone"],
                    "Vins de Pays":["Vins de Pays"],
                    "Luxembourg":["Luxembourg"],
                },
                "Italie": {
                    "Abruzzes":["Abruzzes"],
                    "Basilicate":["Basilicate"],
                    "Calabre":["Calabre"],
                    "Campanie":["Campanie"],
                    "Emilie - Romagne":["Emilie - Romagne"],
                    "Frioul-Venetie-Julienne":["Frioul-Venetie-Julienne"],
                    "Latium":["Latium"],
                    "Ligurie":["Ligurie"],
                    "Lombardie":["Lombardie"],
                    "Les Marches":["Les Marches"],
                    "Molise":["Molise"],
                    "Ombrie":["Ombrie"],
                    "Piemont":["Piemont"],
                    "Pouilles":["Pouilles"],
                    "Sardaigne":["Sardaigne"],
                    "Sicile":["Sicile"],
                    "Toscane":["Toscane"],
                    "Trentin-Haut-Adige":["Trentin-Haut-Adige"],
                    "Val d'Aoste":["Val d'Aoste"],
                    "Venetie":["Venetie"],
                },
                "Russie": {
                    "Kaliningrad":["Kaliningrad"],
                    "Nord-Ouest":["Nord-Ouest"],
                    "Nord":["Nord"],
                    "Centre":["Centre"],
                    "Centre-Tchernozem":["Centre-Tchernozem"],
                    "Volga-Viatka":["Volga-Viatka"],
                    "Volga":["Volga"],
                    "Caucase du Nord":["Caucase du Nord"],
                    "Oural":["Oural"],
                    "Extreme-Orient":["Extreme-Orient"],
                },
                }
                window.onload = function() {
                // On récupère l'id de la sélection des pays et des régions dans l'html
                var Pays = document.getElementById("pays");
                var Region = document.getElementById("region");
                for (var x in subjectObject) {
                    Pays.options[Pays.options.length] = new Option(x, x);
                }
                Pays.onchange = function() {
                    // Si la sélection pays est changée, alors on peut changer la sélection région
                    Region.length = 1;
                    // Proposer les régions en fonction du pays sélectionné
                    for (var y in subjectObject[this.value]) {
                    Region.options[Region.options.length] = new Option(y, y);
                    }
                }
                }
            </script>""")


script.css()
