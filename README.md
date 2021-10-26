# cave-vin
Site de gestion de cave à vin utilisant une bdd manipulée avec MySQL

-------------------------------------------------------------------

ACCEDER AU SITE :
Pour accéder à votre cave vous aurez besoin de lancer le fichier 
serveur.py depuis un IDE muni du langage Python en version 3.7 ou 
supérieur. Suivez le lien qui s'affiche dans la console pour aller
sur le site.

-------------------------MODIFIER LA CAVE--------------------------

- AJOUTER UNE BOUTEILLE DE VIN :
Remplissez le formulaire "Nouveau vin" avec toutes les informations 
nécessaires à l'identification d'un vin, ce qui comprend : son nom, 
son appellation, sa couleur, le nombre de bouteilles, et le millésime
(année), puis appuyez sur le bouton d'envoi.

- AJOUTER UNE APPELLATION :
Remplissez le formulaire "Nouvelle appellation" avec toutes les
caractéristiques d'une appellation : nom, pays, région et 5 mets
maximum associés à l'appellation, puis appuyez sur le bouton d'envoi.

- RETIRER UNE BOUTEILLE :
Appuyez sur le bouton avec le symbole de carré avec un crayon situé
à côté du titre du tableau des vins puis saissez l'ID du vin que vous 
souhaitez retirer.

- REINITIALISER LA CAVE :
Si vous souhaitez supprimer toutes les données des vins ou des appellations, 
appuyez sur un des boutons "reset" symbolisés par des flèches en rotation 
sous le tableau correspondant.

-----------------------------NAVIGATION----------------------------

- NAVIGATION SUR LE SITE :
Le menu de navigation vous permet de faire défiler la page jusqu'à
l'endroit désiré. Le logo de tonneau ramène en haut de la page,
le bouton "Ajouter" ramène sur les deux formulaire et le bouton
"Afficher" se centre sur le tableau des vins.

---------------------REQUÊTES SUPPLEMENTAIRES----------------------

- BOUTON DETAILS :
Le bouton symbolisé par deux flèches orientées vers le bas
se situant en bas du tableau des vins vous permet de dérouler un popup 
contenant des informations supplémentaires sur la cave à vin, tel que : 
le nombre total de bouteilles et le nombre de bouteilles par couleur 
de vin.

- RECHERCHE :
Deux barres de recherche se situent chacunes au dessus des tableaux
des vins et des appellations. Elles permettent de filtrer les
éléments affichés dans le tableau pour n'afficher que les éléments
correspondant à votre recherche.

- INFORMATIONS PAR REGION :
Le bouton "?" se situant au dessus du tableau des appellations
permet d'afficher un tableau contenant les appellations et les
vins pour chaque région.

- METS ASSOCIES AUX VINS :
Le formulaire situé sous le tableau des appellations permet d'afficher
le(s) vin(s) associés au met saisi.
