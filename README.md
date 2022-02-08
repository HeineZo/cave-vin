# Cave à vin <img alt="Title" src="/src/img/grapes-color.png" width="3%">

![GitHub release (latest by date)](https://img.shields.io:/github/v/release/PandAmiral/cave-vin)

Application web de gestion de cave à vin

- [Lancer le serveur](#lancer-le-serveur-local)

- [Modifier le contenu de la cave](#modifier-la-cave-à-vin)

   - [Ajouter une bouteille de vin](#ajouter-une-bouteille-de-vin)
   
   - [Ajouter une appellation](#ajouter-une-appellation)

   - [Retirer une bouteille](#retirer-une-bouteille)
   
   - [Réinitialiser la cave](#réinitialiser-la-cave)

- [Naviguer dans l'application](#navigation)

- [Requêtes supplémentaires](#requêtes-supplémentaires)
  
    - [Bouton détails](#bouton-détails)
    
    - [Recherche](#recherche)
    
    - [Informations par région](#informations-par-région)
    
    - [Mets associés à un vin](#mets-associés-à-un-vin)

## Lancer le serveur local

1. Saisir la commande depuis le dossier principal :
```
python serveur.py
```
2. Se rendre sur l'url
http://localhost:80/compl_base_vins.py


## Modifier la cave à vin

### Ajouter une bouteille de vin

Remplissez le formulaire "Nouveau vin" avec toutes les informations 
nécessaires à l'identification d'un vin, ce qui comprend : son nom, 
son appellation, sa couleur, le nombre de bouteilles, et le millésime
(année), puis appuyez sur le bouton d'envoi.

<img alt="Ajouter un vin" src="https://media.discordapp.net/attachments/563777849451085824/939869000043737098/unknown.png" width="25%">

### Ajouter une appellation
Remplissez le formulaire "Nouvelle appellation" avec toutes les
caractéristiques d'une appellation : nom, pays, région et 5 mets
maximum associés à l'appellation, puis appuyez sur le bouton d'envoi.

<img alt="Ajouter un vin" src="https://cdn.discordapp.com/attachments/563777849451085824/939869049045794836/unknown.png" width="25%">


### Retirer une bouteille
Appuyez sur le bouton avec le symbole de carré avec un crayon situé
à côté du titre du tableau des vins puis saissez l'ID du vin que vous 
souhaitez retirer.

<img alt="Ajouter un vin" src="https://media.discordapp.net/attachments/563777849451085824/939870280149532702/unknown.png" width="25%">

### Réinitialiser la cave
Si vous souhaitez supprimer toutes les données des vins ou des appellations, 
appuyez sur un des boutons "reset" symbolisés par des flèches en rotation 
sous le tableau correspondant.

## Navigation

### Navigation sur le site
La bar de navigation vous permet de faire défiler la page jusqu'à
l'endroit désiré. Le logo de tonneau ramène en haut de la page,
le bouton "Ajouter" ramène sur les deux formulaire et le bouton
"Afficher" centre sur le tableau des vins.

## Requêtes supplémentaires

### Bouton détails
Le bouton symbolisé par deux flèches orientées vers le bas
se situant en bas du tableau des vins vous permet de dérouler un popup 
contenant des informations supplémentaires sur la cave à vin, tel que : 
le nombre total de bouteilles et le nombre de bouteilles par couleur 
de vin.

### Recherche
Deux barres de recherche se situent chacunes au dessus des tableaux
des vins et des appellations. Elles permettent de filtrer les
éléments affichés dans le tableau pour n'afficher que les éléments
correspondant à votre recherche.

### Informations par région
Le bouton "?" se situant au dessus du tableau des appellations
permet d'afficher un tableau contenant les appellations et les
vins pour chaque région.

### Mets associés à un vin
Le formulaire situé sous le tableau des appellations permet d'afficher
le(s) vin(s) associé(s) au met saisi.
