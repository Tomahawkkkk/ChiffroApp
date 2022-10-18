# CryptoApp

Fonctionne sous Python 3.X
	
Objectif : Obtenir une App permettant de chiffrer/déchiffrer des messages.

Intéret : Montée en compétence Python, chiffrement, interface graphique, machine learning, graphs, Weak IA.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

### TO DO :

Task : [DONE] Factoriser en classe la gestion des traductions des messages (ex: message => message sans accent).

Task : [DONE] Etudier Learning/Securite_Chiffrement et établir la liste de méthode à implémenter dans /CryptoMethods.

Task : [DONE] Concevoir l'architecture du code avec les commentaires au bon endroit.

Task : [DONE] Compartimenter mieux que ca le code sourde de CryptoApp

Task : [DONE] Relire le code pour vérifier les coquilles (1er coup)

Task : [95%] Passer tous le code source + commentaires en anglais, man for real ...

Task : [DONE] Faire en sorte que le terminal se clean/réinitialise dès que je rentre une commande, sinon il y a trop de texte dans le terminal, ce n'est pas lisible ==> os.system("clear")

Task : [DONE] Ajouter à chaque fin de chemin une variable exemple chemin = "Crypter/Cesar/Terminal".

Task : [DONE] Ajouter un Section Parameter au debut de CryptoApp, insérer un booléen pour print le path choisi par l'utilisateur ou non.

Task : [DONE] Aerer le code.

Task : [DONE] Tester CryptoApp manuellement pour étudier les chemins et les displayPathUser.

Task : [DONE] L'App doit permettre à l'utilisateur de choisir sa méthode de chiffrement parmi la liste présente dans /CryptoMethods.

Task : [DONE] Pour les méthodes "Non implémentés", afficher simplement un print("En cours d'implémentation")

Task : [DONE] L'utilisateur doit pouvoir choisir s'il veut déchiffrer en connaissant la méthode ou non.

Task : [DONE] Vérifier que Errors Manager fonctionne correctement selon tous les cas de figures.

Task : [DONE] Mettre en commentaires les demandes [Informations] qui ne servent à rien.

Task : [DONE] Supprimer les demandes d'informations définitivement.

Task : [DONE] Mettre en commentaires les demandes [UnknownCommand] qui ne servent à rien.

Task : [DONE] Supprimer les demandes "UnknownCommand" définitivement.

Task : [DONE] Mettre en commentaires les demandes [Quitter] qui ne servent à rien.

Task : [DONE] Supprimer les demandes "Quitter" définitivement.

Task : [DONE] CryptoApp vérifie que cryptoApp_in.txt et cryptoApp_out.txt existe, sinon les génère automatiquement.

Task : [DONE] Exporter dans un fichier .py la méthode de chiffrement Cesar, et gérer son importation dans CryptoApp.py

Task : [DONE] Faire tourner le chiffrement Cesar.

Task : [DONE] Faire tourner le déchiffremment Cesar.

Task : [DONE] L'utilisateur peut choisir d'avoir sa clé Cesar générée aléatoirement ou alors la choisir lui même via Terminal ou FIlseSystem.

Task : [DONE] Mettre Cesar.py en anglais

Task : [DONE] Faire fonctionner encrypt/decrypt Cesar avec le FileSystem

Task : [DONE] Implémenter la fonction SetupCesarKey()/Terminal dans Cesar.py

Task : [DONE] Implémenter la fonction GetCesarKey() dans Cesar.py

Task : [DONE] Implémenter la subfonction SetupCesarKey()/cesarKeyGenerator() dans Cesar.y

Task : [DONE] Tester l'intervalle de clé possibles pour la "classe" César.

Task : [DONE] Ecrire le message adéquat dans la variable [SetupCesarKey_InputsAccepted] pour bien conseiller l'utilisateur.

Task : [DONE] Intégrer "Parameters" && "ErrorsManager" directement dans la classe Cesar

Task : [DONE] Gérer les erreurs du à l'importations de ClassCesar.py en lançant "python3 CryptoApp.py"

Task : [DONE] Optimiser ClassCesar.py

Task : [DONE] Exporter dans un fichier .py le "Error Manager", qui permet de centraliser toutes la gestion des erreurs du projet CryptoApp.

Task : [DONE] Exporter tous les Inputs/Outputs files dans un même fichier .py, que chaque classes pourra charger dès le début (si besoin).

Task : [DONE] Réfléchir comment implémenter une classe "Parameters" pour partager les paramètres de CryptoApp.py dans Cesar.py au début de ce fichier (permet d'avoir la même variable DisplayFilePreview par exemple)
		-> Utiliser les PARAMETERS de ClassErrorsManager.py...
		-> Il faudra forcement importer ClassParameters.py dans le ClassErrorsManager.py

Task : [DONE] Utiliser le template de ClassCesar pour implémenter ClassSymetric.py && ClassAsymetric
		-> Maj ClassParameters.py
		-> Maj ClassErrorsManager.py
		-> Grosse Maj CryptoApp.py
			-> Remplacer Vigenere/Masque Jetable ... par Symetric et Asymetric 

Task : [???DONE???] Réussir à faire tourner "pip install -r requirements.txt"
	-> Error message :
	-> Requirements file provided! Importing into Pipfile...
Pipfile.lock (a79791) out of date, updating to (5fa6e6)...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
on error: Py_Initialize: Unable to get the locale encoding
ImportError: No module named 'encodings'

Current thread 0x00007fb23a958740 (most recent call first):
Aborted (core dumped)
<!-- /home/thomas/.local/lib/python2.7/site-packages/pipenv/_compat.py:113: ResourceWarning: Implicitly cleaning up <TemporaryDirectory '/tmp/pipenv-zXpLEt-requirements'> -->
  <!-- warnings.warn(warn_message, ResourceWarning) -->

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task : Comprendre comment fonctionne la lib "Cryptography" :
		-> https://cryptography.io/en/latest/
		-> Lire la doc sur le chiffrement symétrique

from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")
token
b'...'
f.decrypt(token)
b'my deep dark secret'

Task : Implémentation Chiffrement/Dechiffrement symétrique
		-> ClassSymetric.py

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task : Implémentation Chiffrement/Dechiffrement asymétrique
		-> ClassAsymetric.py


Task : Lire le cours Crypto101.pdf


Task : Prendre les bonnes décicions sur le Dev de CryptoApp suite à la lecture du cours Crypto101.pdf

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Task : 	Complexifier mon chiffrement Cesar en créant une combinaison de plusieurs Cesar.
		Ce qui me permettrait de ne pas implémenter Vigenere et Masque Jetable pour me concentrer sur ce qui m'interesse vraiment.
			->ClassCombinaison.py
			-> Inputs 1 : "01120120102010201121"
				-> 0 == CesarKey à 1 chiffre
				-> 1 == CesarKey à 2 chiffres 
				-> 2 == Représente le "-" du nombre négatif qui suit.
			-> Inputs 2 : "46383920375648294875"
				-> La concaténation des Cesarkeys de la combinaion
				-> Il faut "ranger" Inputs 2 avec l'aide de Inputs 1
				-> Dès que c'est rangé, on peut déchiffrer couche par couche

Task : Implémentation du Dechiffrement KO, va me permettre de manipuler les dictionnaires de plusieurs langues (ça sera une très bonne introduction pour la suite (cassage...))
			-> ClassBreak_method1.py
			-> A terme il faudra un ClassBreakManager.py

Task : Implémentation Chiffrement/Dechiffrement PGP
		-> A creuser

# A développer au moment opportun :

Task : Comprendre les abréviations/vocabulaire :
	* Beast Attack
	* Stream Cipher
	* AES (A Encryption Standard)
	* ECB Mode
	* CBC
	* CTR
	* More advanced stuff
		* Authentic encryption mode
			* GCM, EAX, OCB, IAPM, CCM, CWC

	* Diffie-Hellman Key Exchange
	* Extention Attacks
	* SHA-3 era
	* KDF (Key description function)

Task : Implémenter une méthode permettant à CryptoApp la "compréhension" de la "combinaison" de chiffrement

Task : Implémenter une méthode permettant de déchiffrer la "combinaison" suite à l'output de la méthode "compréhension"

Task : Concevoir un dataset de message cryptés (un jeu d'entrée pour implémenter mes méthodes de cassage en somme)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Taches hypothétiques futures :

Task : Réfléchir comment intégrer docker dans CryptoApp, Follow-up Docker/Get Started Part 3 : Services

Task : Revoir l'interface console de CryptoApp pour l'optimiser.

Task : Etudier en détail les framework MachineLearning Python, https://github.com/josephmisiti/awesome-machine-learning#python

Task : Déterminer les frameworks dont j'ai besoin.

Task : Trouver le moyen de s'interfacer avec des vrais sites avec mot de passe

Task : Parralléliser le cassage : Implémenter des Bots chargés de faire tourner chacun une méthode de déchiffrage (Parralléliser avec Docker ?)

Task : CryptoApp doit pouvoir me permettre de sécuriser mes communications personnelles (cf cours OpenClassroom)

Task : Utiliser Pylint pour scanner mon code et vérifier que mon code suis les bonnes pratiques pep 8

Task : Réaliser une interface graphique optimale du projet.

Task : A la fin du chiffrage, l'app doit retourner à l'utilisateur la clé de cryptage (par sms, par mail?) 

Task : [NOT A PRIORITY] Proposer à l'utilisateur de vider les fichiers d'entrée automatiquement grâce à un "Parameter" (gràce à la preview, l'utilisateur peut avoir envie de tout réinitialiser)

########################################################################################

# Idea(s) : 

1) Source code encrypting ?

2) Text files encrypting ? (cesarKey, In, Out...)

2) Convert text in binary, convert binary in text

3) Demander à L'ANSSI de m'envoyer des messages cryptés de niveaux différents
