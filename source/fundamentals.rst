#################
Principes de base
#################

Généralités
===========

Une application dite de «bureau» ou desktop application est un programme exécuté directement par l'ordinateur de l'utilisateur du logiciel. Une telle application utilise généralement les ressources du système d'exploitation de la machine sur laquelle il est installé (fenêtres, menus, boîtes de dialogue,...) pour permettre une interaction avec l'utilisateur (entrée et sortie de données, pilotage de l'application,...).



Des logiciels tels que Word, Photoshop ou Audacity ainsi que la plupart des programmes conçus avec un environnement de développement tels que IDLE sont typiquement des applications desktop: elles sont exécutées par le processeur de l'ordinateur sur lequel elles sont installées et font usage des ressources de son système d'exploitation.	

Une **application web** est quant à elle une application installée sur un serveur web et exécutée par le processeur de ce dernier. L'utilisateur interagit à distance avec une application web principalement par le biais d'un navigateur web tel que Firefox, Chrome ou Internet Explorer. Le navigateur affiche des pages web jouant le rôle d'interface utilisateur graphique. Facebook est un exemple d'une telle application. Les utilisateurs d'une application web n'ont pas besoin de l'installer sur leur ordinateur comme c'est le cas d'une application desktop. Le programme fonctionne sur un serveur web envoyant au navigateur web de l'utilisateur des pages HTML faisant office d'interface. Le navigateur ne fait que réceptionner, afficher et retourner des informations à l'application web qui s'occupe de traiter les informations par le biais du processeur du serveur web sur lequel elle est installée.

Une application web est donc un programme (pouvant être écrit dans différents langages de scripts tels que PHP, Python ou Perl) exécuté sur un serveur web. Le fonctionnement de la plupart des applications web repose sur l'utilisation de formulaires HTML qui permettent à l'utilisateur de choisir ou saisir des données à transmettre à l'application web en paramètres. Une fois les données traitées par l'application web, celle-ci construit le code HTML de la page web réceptionnant la réponse à transmettre à l'internaute via le réseau. Les pages web transmises par l'application web à l'internaute sont personnalisées selon les choix ou les saisies de ce dernier. Nous les appelons dès lors pages web dynamiques.

Le but de ce chapitre sera de comprendre le fonctionnement d'une application web et d'en implémenter une à l'aide du microframework *Flask* développé en  Python.
Pages statiques et dynamiques
Les pages web sont des documents au format HTML que l'on peut consulter via un réseau à l'aide de logiciel appelé navigateur. Les pages HTML sont installés dans les répertoires publics d'un autre ordinateur où fonctionne en permanence un logiciel appelé serveur web. 
Lorsqu'une connexion est établie entre cet ordinateur et celui de l'internaute, le logiciel navigateur de l'utilisateur peut dialoguer avec le logiciel serveur en lui envoyant des requêtes par l'intermédiaire de toute une série de dispositifs matériels et logiciels qui constituent le réseau connectant la machine client à celle du serveur. Les pages web sont alors retournées au navigateur par le serveur en guise de réponse à la requête précédemment envoyée.

Le protocole de communication développé pour le web est le HTTP (HyperText Transfer Protocol. Il s'agit d'un ensemble de règles de communication que doivent respecter deux ordinateurs installés sur un même réseau pour s'échanger des informations. Le protocole HTTP gère la transmission des pages web et autorise l'échange des données dans les deux sens.


Dans le cas de la simple consultation de sites, le transfert d'informations a surtout lieu dans un sens, à savoir du serveur vers le navigateur: les pages consultées lui sont transmises sous forme de fichiers HTML. Nous parlons alors de pages statiques, dans la mesure où le contenu de ces pages ne peut être mis à jour automatiquement mais nécessite l'intervention du webmaster du site pour modifier le code source et y ajouter des nouveautés. De telles pages web sont réalisées uniquement à l'aide des langages HTML et CSS.

Dans le cadre de la consultation de pages statiques, le navigateur n'envoie guère au serveur que de petites quantités d'informations, essentiellement sous forme d'adresses URL des pages que l'internaute désire consulter. Néanmoins, il existe des sites web permettant à l'utilisateur de fournir des quantités d'informations plus importantes au serveur web par le biais de formulaires HTML: des références personnelles pour l'inscription à un club ou la réservation d'une chambre d'hôtel, un numéro de carte de crédit pour la commande d'un article sur un site de commerce électronique, un avis, une suggestion, etc. Dans ce cas, l'information transmise est prise en charge, du côté du serveur, par une application web qui se chargera de son traitement et renverra une réponse adéquate à l'internaute sous la forme d'une nouvelle page web. Le contenu de cette page web n'est pas figé mais change en fonction des informations transmises par l'utilisateur via le formulaire. Nous parlons alors de page dynamique dans la mesure où elle a été construite sans l'intervention du webmaster.


L'objectif de ce cours est de vous rendre capable de réaliser des sites web dynamiques à l'aide du module Flask offert par le langage Python. Les pages dynamiques seront donc générées par Python puis envoyées au navigateur de la même manière qu'un site statique. Un tel bagage vous donnera ainsi les outils nécessaires à la réalisations de sites contenant les éléments suivants:	 	 		 	
un espace membre: vos visiteurs pourront s'inscrire sur votre site et avoir accès à des sections qui leur sont réservées;
un forum:il est courant aujourd'hui de voir les sites web proposer un forum de discussion pour s'entraider ou simplement passer le temps;
un compteur de visiteurs: vous pourrez facilement compter le nombre de visiteurs qui se sont connectés à votre site durant une journée ou même connaître le nombre d'internautes en train d'y naviguer;
des actualités: vous pourrez automatiser l'écriture d'actualités, en offrant à vos visiteurs la possibilité d'en rédiger, de les commenter, etc.;
une newsletter: vous pourrez envoyer un email à tous vos membres régulièrement pour leur présenter les nouveautés de votre site et les inciter à revenir le visiter;	 	 		 	
Bien entendu, ce ne sont là que des exemples. Il est possible d'aller encore plus loin, tout dépendant de vos besoins. Sachez par exemple que la quasi-totalité des sites de jeux en ligne sont dynamiques.