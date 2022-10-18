
#########################################################

## Commandes git :

git status

git init // répertoire courant doit etre considéré comme un repository git.

git status // git nous dit qu'il y a des fichiers non trackés dans le répertoire.

git add * // Tracke tous les fichiers du répertoire.

git status

git commit -m "Add CryptoApp prj" // Commit initial

git log // Permet de visualiser l'historique des commits.

git commit -a -m "Update 1 file" // Si on modifie un fichier qui est déjà tracké apr git, on peut l'add et le commit directement avec cette commande.

git checkout 81c06f8233fe132cc86c33eb5d927774d60c6d4f // Permet de se positionner sur une version du code antérieur.

git checkout master // Permet de revenir sur la version actuelle du code (last committed)

git remote // Un remote == Github, on prends nos commits et on les envoit sur un remote

git clone lienGithub// Permet de récupérer un repository provenant d'un remote.

git remote add origin https://github.com/Thomas156984/CryptoApp.git // Connecte le répertoire du terminal avec le répertoire Github

git push origin master // Dès que la connection est établie entre le répertoire local et le répertoire Github : on peut push le commit sur le remote répertoire Github.

git pull origin master // Récupérer du code en provenance de Github.

# Gérer les branches :

git branch // Permet de voir les branches existantes dans le répertoire, et la branche actuellement sélectionnée.

git branch maNewBranche // Permet de créer une nouvelle branche

git checkout maNewBranche // Permet de changer de branche

git merge maNewBranche // (en se situant dans la branche master) : Permet de fusionner maNewBranche dans master.

git merge master // (en se situant dans la branche maNewBranche) : Permet de fusionner master dans maNewBranche.

git branch -d maNewBranche // Permet de supprimer la branche.

// Gérer un conflit merge :

Il faut commit la gestion du conflit, et apparement ca merge automatiquement.

// Savoir qui a fait une modification :

git blame main.py // Qui a modifié quelle ligne de ce fichier.

git show 81c06f8233fe132cc86c33eb5d927774d60c6d4f // Permet de voir le contenu d'un commit avec comparaison avant/après.

git stash // Permet d'enregistrer temporairement les modifications, pour y revenir après.

git stash pop // Permet de récupérer ses modifications pour continuer à bosser dessus, ATTENTION, ca vide l'espace mémoire donc il faudra committer les modifs après , sinon modifs perdue.

git stash apply // Si vous voulez garder les modifications dans votre stash, vous pouvez utiliser apply à la place de pop.

# Contribuer à un projet open-source :

// Demande de pull request == proposer une amélioration de code ou un ajout de fonctionalité

fork le repository du projet == fais moi une copie du projet sur mon compte
Create your feature branch (git checkout -b my-new-feature)
Commit your changes (git commit -am 'Add some feature')
Push to the branch (git push origin my-new-feature)
Create new Pull Request

#########################################################

## Procédure de réinitialisation du répertoire Git :

git rm -r --cached . (don't forget the little ".")
git init
// check .gitignore
git add .
git commit -m "first commit"
git remote add origin https://github.com/Thomas156984/CryptoApp.git
git push -u origin master

#########################################################