# ajout d'un style
def css():
    print("""
        <style>
            /* Import des polices */
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100;200;300;400;500;600;700;800;900&display=swap');
            @import url('https://fonts.googleapis.com/css?family=Saira+Extra+Condensed');
            
            /* Tous les éléments */
            * {
                font-family: 'Montserrat';
                font-size: 20px;
            }
            
            /* Simuler un effet de scroll lorsqu'on veut naviguer plus rapidement avec les boutons du men ude navigation */
            html {
                scroll-behavior: smooth;
            }
            
            /* Image de fond */
            section.top-page {
                background: url('src/img/background.png');
                background-size: cover;
                height: 150vh;
                padding: 25px;
            }
            
            /* En-tête */
            header.header {
                display: flex;
                align-items: center;
                position : fixed;
                top: 0;
                padding: 25px;
            }
            
            header.header img {
                width: 100px;
            }
            
            /* Menu de navigation */
            nav.nav {
                display: inline-flex;
                justify-content: space-evenly;
                list-style: none;
                width: 400px;
                margin-left: 10px;
                text-align: center;
            }

            nav.nav li {
                color: white;
                display: inline-flex;

            }
            
            /* Animation bouton menu de navigation */
            a.middle{
                color: white;
                position: relative;
                text-decoration: none;
            }
            
            a.middle:before {
              content: "";
              position: absolute;
              width: 0;
              height: 1px;
              bottom: 0;
              left: 0;
              background-color: #FFF;
              visibility: hidden;
              transition: all 0.3s ease-in-out;
            }
            
            a.middle:hover:before {
              visibility: visible;
              width: 100%;
            }
            
            /* Grand titre animé */
            .big-title{
                font-size:85px;
                user-select: none;
            }

            svg.title {
                display: block;
                width: 1000px;
                height: 700px;
                margin: 0 auto;
            }

            .text-copy {
                fill: none;
                stroke: white;
                stroke-dasharray: 6% 29%;
                stroke-width: 5px;
                stroke-dashoffset: 0%;
                animation: stroke-offset 7s infinite linear;
            }

            .text-copy:nth-child(1){
                stroke: #4D163D;
                animation-delay: -1;
            }

            .text-copy:nth-child(2){
                stroke: #840037;
                animation-delay: -2s;
            }

            .text-copy:nth-child(3){
                stroke: #BD0034;
                animation-delay: -3s;
            }

            .text-copy:nth-child(4){
                stroke: #CD4E60;
                animation-delay: -4s;
            }

            .text-copy:nth-child(5){
                stroke: #A5072E;
                animation-delay: -5s;
            }

            @keyframes stroke-offset{
                100% {stroke-dashoffset: -35%;}
            }
            
            /* Corps du site */
            body {
                background-color: black;
                margin: 0 auto;
                position: relative;
            }
            
            /* Titres secondaires */
            .mid-title {
                font-size: 50px;
                font-family: 'Saira Extra Condensed', cursive;
                position: relative;
                color: white;
                text-align: center;
                letter-spacing: 5px;
                margin-top: 200px;
                user-select: none;
            }
            
            .mid-title::before {
                content: "";
                position: absolute;
                background-color: white;
                width: 50px;
                height: 7px;
            }
            
            /* Ajouter vin & appellation */
            legend {
                color: white;
            }
            
            section.first {
                height: 550px;
            }

            fieldset.vin {
                position: relative;
                padding: 10px;
                margin-left: 400px;
                width: 300px;
                float: left;
            }
            
            fieldset.ajout_supp {
                position: relative;
                padding: 10px;
                margin-left: 400px;
                width: 300px;
            }

            fieldset.appellation {
                position: relative;
                padding: 10px;
                margin-right: 400px;
                width: 300px;
                float: right;
            }
            
            input {
              height: 40px;
            }
            
            input:focus {
              border: 2px solid #8E041E;
              outline: none;
            }

            label {
                display: flex;
                margin-bottom: 10px;
                margin-top: 10px;
                color: white;
            }

            /* Recherche vin */
            #SearchVin, #SearchAppellation {
                background-image: url('/src/img/searchicon.png');
                background-position: 7px 7px;
                background-size: 25px 25px;
                background-repeat: no-repeat;
                margin-left:auto; 
                margin-right:auto;
                display: flex;
                font-size: 16px;
                padding: 12px 20px 12px 40px;
                border: 1px solid #ddd;
                margin-bottom: 12px;
                margin-top: 20px;
            }

            /* Tableaux */
             table.centre {
                margin-left:auto; 
                margin-right:auto;
                margin-bottom: 100px;
                margin-top: 10px;
            }
            
            table {     
                table-layout: fixed;
                width: 50%;
                border-collapse: collapse;
                border: 3px solid #4C4C4C;   
                border-top: none; 
                border-right: none;
                border-left: none;    
            }

            table.table_region {
                width: 100%;
            }

            thead {
                background-color: #8E041E;
                color: white;
            }

            tr {
                color: white;
            }
            
            td {
                color: white;
                padding: 15px;
                border: 3px solid #4C4C4C;
            }

            .suppr {
                background-color: black;
                color: white;
            }
           
            /* Reset vin */
            .reset-vin {
                position: absolute;
                margin-top: 10px;
                margin-right: 40%;
                width: 31px;
	            height: 30px;
                transition: all 300ms;
                cursor: pointer;
                border: none;
                border-radius: 10px;
                color: white;
                background: #434343;
                font-size: 30px;
                font-family: roboto, sans-serif;
            }

            .reset-vin:hover {
                transition: all 400ms cubic-bezier(.62, .1, .5, 1);
                background-color: #8E041E;
                width: 150px;
            }

            .short-text {
                transition: all 1s ease 0s;
                display: flex;
            }

            .long-text {
                position: absolute;
                transition: all 300ms ease 0s;
                opacity: 0;
                color: white;
                width: auto;
                margin-left: 40px;
                left: 5px;
                top: 5px;
            }

            .long-text.show-long-text {
                transition: all 300ms ease 0s;
                opacity: 1;
                text-transform: uppercase;
                font-size: 20px;
                width: auto;
                letter-spacing: 3px;
            }

            /* Reset appellation */
            .appel {
                position: relative;
                top: -100px;
                display: flex;
                justify-content: center;
            }

            /* Bouton d'envoi */
            .submit {
                color: #494949;
                text-transform: uppercase;
                background: white;
                padding: 10px;
                border: 4px solid #494949;
                border-radius: 6px;
                display: inline-block;
                transition: all 0.3s ease 0s;
                text-decoration: none;
                margin-left: 75px;
                margin-top: 10px;
                cursor:pointer;
            }

            .submit:hover {
                color: #20bf6b;
                border-radius: 50px;
                border-color: #20bf6b;
                transition: all 0.3s ease 0s;
                cursor:pointer;
            }


            /* Total des vins */
            .details {
                position: relative;
                top: -100px;
                display: flex;
                justify-content: center;
            }

            #arrow
            {
                cursor: pointer;
                transition: all 0.3s ease 0s;
                color: white;
                margin-top: 5px;
            }

            #arrow.down{transform: rotate(180deg);}

            #more
            {
                position: absolute;
                margin-top: -50px;
                top: 40%;
                left: 50%;
                transform: translate(-50%, 50%);
                border-radius:10px;
                visibility: hidden;
                opacity: 0;
                transition: 0.5s;
                width: 300px;
                height: auto;
                min-height: 100px;
                cursor: auto;
                color: white;
            }

            #more.active
            {   
                top: 50%;
                background-color: #8E041E;
                border-radius:20px;
                visibility: visible;
                opacity: 1;
                transition: 0.5s;
                margin-top: -30px;
            }

            .all-wine {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 5px;
                font-size: 15px;
            }

            .unique {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-top: 5px;
                font-size: 15px;
                margin-bottom: 5px;
            }
            /* Add & Delete */
            /* Bouton */
            .edit-icon {
                position: absolute;
                margin-left: 1100px;
                margin-top: 10px;
                cursor:pointer;
                color: white;
                transition: transform 450ms;
            }

            .edit-icon:hover {
                transition: transform 125ms;
                transform: translateY(-5px);
            }

            /* Effet de flou */
            #blur.active
            {
                filter: blur(5px);
                pointer-events: none;
                user-select: none;
                overflow: hidden;
            }

            .add-title {
                color: #434343;
                margin-top: -10px;
            }

            .vin_id, .btl_id {
                color: #434343;
            }

            .form-container {
                padding-top: 10px;
            }

            .numero {
                width: 265px;
            }

            .logo {
                position: absolute;
                left: 0;
                width: 400px;
                margin-top: 50px;      
            }

            /* Bouton d'ajout et de retirement */
            .supprim, .ajout {
                color: #494949;
                text-transform: uppercase;
                background: white;
                border: 4px solid #494949;
                border-radius: 6px;
                display: inline-block;
                padding: 10px;
                transition: all 0.3s ease 0s;
                text-decoration: none;
                margin-left: 20px;
                cursor:pointer;
            }

            .supprim:hover {
                color: #b53131;
                border-radius: 50px;
                border-color: #b53131;
                transition: all 0.3s ease 0s;
            }

            .ajout:hover {
                color: #20bf6b;
                border-radius: 50px;
                border-color: #20bf6b;
                transition: all 0.3s ease 0s;
            }

            /* Fermer le popup */
            .close {
                display: flex;
                flex-direction: column;
                justify-content: flex-end;
                align-items: center;
                text-decoration: none;
                color: white;
                background-color: #ed3330;
                padding: 10px;
                cursor: pointer;
                margin-top: 150px;
                border-radius:10px;
                transition: all 0.4s ease 0s;
            }

            .close:hover {
                background: #434343;
                letter-spacing: 1px;
                transition: all 0.4s ease 0s;
            }

            /* Popup */
            #pop 
            {
                position: absolute;
                top: 40%;
                left: 50%;
                transform: translate(-50%, 50%);
                border-radius:10px;
                visibility: hidden;
                opacity: 0;
                transition: 0.5s;
                width: 300px;
                height: 400px;
                padding: 50px;
                background: #fff;
            }

            /* Popup activé */
            #pop.active
            {   
                top: 50%;
                visibility: visible;
                opacity: 1;
                transition: 0.5s;
            }
            
            /* Region pour vin et appellation */
            .question-icon {
                position: absolute;
                margin-left: 1100px;
                margin-top: 10px;
                cursor:pointer;
                color: white;
                transition: transform 450ms;
            }

            .question-icon:hover {
                transform: translateY(-5px);
                transition: transform 125ms;
            }

            /* Popup */
            #question
            {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, 50%);
                visibility: hidden;
                opacity: 0;
                transition: 0.5s;
                padding: 50px;
                color: white;
            }

            /* Popup activé */
            #question.active
            {   
                top: 50%;
                visibility: visible;
                opacity: 1;
                transition: 0.5s;
            }

            /* Mets */
            .container-mets {
                display: flex;
                justify-content: center;
                align-items: center;
                margin-bottom: 100px;
                color: white;
                height: 50px;
            }

            .mets-title {
                text-align: left;
                margin-left: 13px;
            }

            .meal {
                margin-left: 10px;
                color: white;
                cursor: pointer;
                border: none;
                outline: none;
                background: none;
                transition: all 0.3s ease-in 0s;
            }

            .meal:hover {
                color: #20bf6b;
                transition: all 0.3s ease 0s;
            }

            /* Barre de recherche */
            #search_mets {
                text-align: center;
                border: none;
                border-radius: 10px;
                transition: all 0.4s ease 0s;
            }

            #search_mets:focus {
                border-radius: 30px;
                transition: all 0.4s ease 0s;
                outline: none;
            }

            .recherche {
                position: absolute;
                color: white;
                bottom: 1;
                left: 0;
                right: 0;
                text-align: center;
                margin-bottom: 310px;
            }
            
            /* Footer */
            footer {
                bottom: 0;
                left: 0;
                background: #080808;
                font-family: "Open Sans";
                height: auto;
                width: 100%;
                color: white;
            }

            .footer-content {
                display: flex;
                align-items: center;
                justify-content: center;
                flex-direction: column;
                text-align: center;
            }

            .footer-content h3 {
                color: white;
                font-size: 1.8rem;
                font-weight: 400;
                text-transofrm: capitalize;
                line-height: 3rem;
            }

            .footer-content p {
                max-width: 500px;
                margin: 10px auto;
                line-height: 28px;
                font-size: 14px;
            }

            .contact {
                list-style: none;
                display: flex;
                align-items: center;
                justify-content: center;
                margin: 1rem 0 3rem 0;
            }

            .contact li.reseaux, a.reseaux {
                margin: 0 10px;
                text-decoration: none;
                color: white;
                transition: all 2s ease-out 0s;
            }

            .contact li.reseaux:hover, a.reseaux:hover {
                transition: all 2s ease-out 0s;
                transform: rotate(1080deg);
            }

            .footer-content p {
                text-align: center;
                font-size: 14px;
                word-spacing: 2px;
                text-transform: capitalize; 
                user-select: none;
            }

            .footer-content span {
                text-transform: uppercase;
                opacity: .4;
                font-weight: 200;
            }

        </style>
    """)
