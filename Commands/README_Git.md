Autotest visuel: é è ê ë à â ä ï î œ ç ù  « » ` ’ ' " ~ ° { } [ ] | & 
Si la ligne ci-dessus ne s'affiche pas correctement, ne pas sauver le fichier.
Depuis l'editeur, designer l'encodage "Unicode UTF-8", puis relancer l'editeur.

Description
===========

Contient les commandes les plus frequemment utilisees concernant l'outil Git


Commandes usuelles
==================

- Liste des commandes courantes
```sh
git help
```
- Aide sur une commande particulière
```sh
git help myGitCommand
```
- Pour consulter l'état du dépot local (fichiers modifiés, prêts pour le commit, ...)
```sh
git status
```
- Liste les fichiers géres par Git
```sh
git ls-files
```
- Consulter l'historique
```sh
git log
git log --graph --oneline
git log myFile
git log myCommit
git log --graph myFile
git log --oneline myFile
```

- avec la liste des fichiers modifiés
```sh
git log -1 --numstat
```
- Recherche d'une chaine dans tous les fichiers du dépot
```sh
git grep TODO
```
- Diff graphique
```sh
git difftool
git difftool -y 
git difftool dc9a26a de1a8c1
```
- Pour un fichier donné
```sh
git difftool myFile
```
- Comparaison de deux tags
```sh
git difftool V005 V011 myFile
```
- Affichage graphique du contenu du dépot
```sh
gitk --all
```

- Ménage des fichiers temporaires (cf .gitignore) et ceux non gérés par git, à partir du dossier courant
```sh
# Pour vérification avant suppression: Affiche seulement les fichiers et dossiers
git clean -dxn
# Après controle affichage précédent, pour lancer la suppression effective
git clean -dxf
```


Recommandations
===============

- Faire des commit le plus souvent possible

Par exemple une fois par jour.
De préférence, un commit pour un ensemble cohérent d'impacts sur plusieurs fichiers

- A chaque étape, lire les éventuels messages d'erreurs de git

Ils donnent souvent la solution

- Renommage ou suppression de fichiers déjà gérés sous Git

**IMPORTANT**: Ne pas renommer/supprimer depuis l'explorateur de fichiers ni par commandes unix (mv, rm)
mais utiliser la commande Git, afin que Git comprendre au plus tôt les changements attendus
```sh
git mv myOldFile myNewFile
git rm myFile
```

Administration
==============

- Creation du dépot central bare (sans working dir)
A faire une unique fois par l'integrateur
```sh
cd /nfs/ptfloti/git_repos
git init --bare IVQ_ENV.git
```

- Creation de la branche initiale, basé sur un tag particulier
A faire une unique fois dans un dépot local
```sh
git branch maint myTag ou myCommit
```
Première remontée dans le dépot central, pour mise à disposition
```sh
git push origin maint
```
Puis utilisation de la branche dans un autre clone
```sh
git checkout maint
```

- Pose d'un nouveau tag

ie: Figer une version officielle (a faire par le coordinateur)
```sh
git tag -a IVQ_ENV_4.x.0 -m "Validation 4.x.x.x-0"
git push --tags
```

- Pour poser un tag sur un ancien commit
```sh
git tag -a 4.x.0 fc26976e4e7c15c47dbaef09f1d18e6b36ddb976 -m "4.x.x.x-0"
```

- Lister les tags, avec les commentaires
```sh
git tag -n
```
- Dans un dépot local, se positionner sur un tag précis
```sh
git checkout IVQ_ENV_1.3.020
```
- Lister les tags remote
```sh
git ls-remote --tags origin  
```

** Création/modification des tags **

- Dupliquer un tag
```sh
git tag newTag oldTag
```
- Supprimer un tag local
```sh
git tag -d oldTag
```
- Supprimer un tag remote
```sh
git push origin :refs/tags/oldTag
```
- Push de tous les tags
```sh
git push --tags
```
- Push d'un tag
```sh
git push monTag
```

- Suppression définitive d'une partie de historique (**Ne jamais utiliser !**)
```sh
git filter-branch --tree-filter 'rm -rf monRepertoireASupprimer' HEAD
Rewrite e06eee1a202f96494043a6a2e88df7b9d4b9c54d (58/92)Warning: commit message does not conform to UTF-8.
You may want to amend it after fixing the message, or set the config
variable i18n.commitencoding to the encoding your project uses.
Rewrite 027365b1daa45262b42fdb9a0442fa4ba0c8a679 (92/92)
Ref 'refs/heads/master' was rewritten
```

- Complétion des commandes et infos dans le prompt (branche courante, ...)
```sh
Légende:
% : Présence de fichiers pas connus de git
* : Présence de fichiers déjà sous git, et modifiés
+ : Présence de fichiers prets à être commités
Cf en PTF:  /nfs/ptfloti/admin/etc/bashrc_common
DARKGREEN="\[\033[01;32m\]"
DARKBLUE="\[\033[01;34m\]"
DARKPINK="\[\033[01;35m\]"
NO_COLOR="\[\033[00m\]"
GIT_PS1=''
GIT_CONFIG_FILE=/etc/bash_completion.d/git
if [ -f ${GIT_CONFIG_FILE} ]; then
  . ${GIT_CONFIG_FILE}
  export GIT_PS1_SHOWDIRTYSTATE=1
  export GIT_PS1_SHOWSTASHSTATE=1
  export GIT_PS1_SHOWUNTRACKEDFILES=1
  export GIT_PS1_SHOWUPSTREAM=verbose
  export GIT_PS1_DESCRIBE_STYLE=branch
  export GIT_PS1_SHOWCOLORHINTS=1
  GIT_PS1='$(__git_ps1 " (%s)")'
fi
COMMON_PROMPT="[\u@\h \W${GIT_PS1}]\$ "
PS1="${DARKGREEN}${COMMON_PROMPT}${NO_COLOR}"
```


Dépots PROD
===========

- Pré-requis: Le compte SeaNaps de l'utilisateur (loti-*) doit être autorisé:

Le groupe loti-integrator doit être en groupe secondaire,
(cf commande id), sinon faire demande CSERV.

- Les espaces Integration

/nfs/LOTI/GIT/Int_Repositories/IVQ (Utilisé pour sauvegardes par l'intégrateur, et recup sur PROD)
```sh
drwxrwxr-x 7 loti-gitmgr loti-integrator 4096 24 juin  17:52 IVQ_ENV.git
drwxrwxr-x 7 loti-gitmgr loti-integrator 4096 24 juin  17:51 ptfloti_admin.git
```

- Les espaces Developpement Central (non utilisé)

/nfs/LOTI/GIT/Repositories/IVQ
```sh
drwxrwsr-x 7 loti-gitmgr loti 4096 24 juin  17:50 IVQ_ENV.git
drwxrwsr-x 7 loti-gitmgr loti 4096 24 juin  17:50 ptfloti_admin.git
```

- L'espace Developpement Individuel
```sh
/nfs/LOTI/GIT/Working_Directories/EXT/${LOGNAME}
```

Remontée PTF->PROD
==================

- Le principe  

Le dépot PTF est automatiquement archivé tous les soirs (jobs Jenkins) dans un fichier ptf.bundle.

Le dépot officiel GCL est cloné dans un dépot de travail.

Le bundle est y déclaré en dépot secondaire, depuis lequel on pull les derniers commits/tags.

On push les commits/tags vers le dépot GCL.

- [Transfert](./README_Admin/index.html#passerelle) de ptf.bundle de PTF vers PROD  
(-k -r /nfs/ptfloti/ivq/tmp/ptf.bundle)

- Création du clone PROD, à faire une fois (en PROD)
```sh
cd /nfs/LOTI/GIT/Working_Directories/EXT/${LOGNAME}
git clone /nfs/LOTI/GIT/Int_Repositories/IVQ/IVQ_ENV.git IVQ_ENV_GCL
cd IVQ_ENV_GCL
```
puis effectuer les git config comme pour un dépot habituel (cf plus bas)

et ajouter le dépot PTF bundle (en PROD)
```sh
git remote -v
git remote add ptf /nfs/LOTI/sas/${LOGNAME}/in/ptf.bundle
git remote -v
```

- Resynchronisation du dépot local à partir du bundle (en PROD)
```sh
newgrp loti-integrator
umask 0002
cd /nfs/LOTI/GIT/Working_Directories/EXT/${LOGNAME}/IVQ_ENV_GCL
git pull ptf master
git pull --tags ptf master
```

- Remontée dans le dépot GCL (en PROD)
```sh
git push
git push --tags
```

- Vérification du dépot d'intégration PROD (en PROD)
```sh
git ls-remote --tags origin
```
- Rectification les droits trop restreints (-r--r--r-- pour un utilisateur)
```sh
chmod -R ug+rw /nfs/LOTI/GIT/Int_Repositories/IVQ/IVQ_ENV.git
```
- Vérification des droits d'accès dans le dépot d'intégration PROD (droits minimum: -rw-rw-r--)
```sh
ls -lR /nfs/LOTI/GIT/Int_Repositories/IVQ/IVQ_ENV.git | egrep -v -e "rw.rw.r.." | sort | uniq | more
```
Aucun fichier ne doit y apparaitre avec votre nom d'utilisateur.


Dépot utilisateur
=================

- Clone du depot central vers un depot utilisateur - En plateforme
```sh
cd /nfs/ptfloti/ivq/users/XXXXX
git clone /nfs/ptfloti/git_repos/IVQ_ENV.git
```

- Clone du depot central vers un depot utilisateur - En PROD
```sh
cd /nfs/LOTI/GIT/Working_Directories/EXT/${LOGNAME}
git clone userloti@admin:/nfs/ptfloti/git_repos/IVQ_ENV.git
```

- Params locaux au projet cf .git/config
```sh
cd IVQ_ENV
identifiant="loti-MonIdentifiant" # Cf indentifiant PROD, ex: loti-planese
# Positionner le user (automatique en PROD)
git config user.name "$identifiant"
git config user.email "${identifiant}@seanaps.dcns"
# Colorisation de l'affichage sous git 
git config color.ui true
# pull: en mode rebase par defaut (plutot que merge)
git config branch.master.rebase true
# Branche partagée secondaire
git config branch.maint.remote origin
git config branch.maint.merge refs/heads/maint
git config branch.maint.rebase true
```

- Les vérifier
```sh
git config -l
```

- Si besoin (pas utile pour démarrer), création de la branche dev
```sh
git branch dev
```
- Positionnement sur la branche dev
```sh
git checkout dev
```


Utilisation dépot
=================

- Travaux dans la branche dev

Vérifier l'ensemble des changements en cours
```sh
git difftool
```

- Marquer seulement les changements a prendre en compte

pour les nouveaux fichiers ainsi que les changements dans les fichiers deja geres
```sh
git add myFile
```

- Commit des changements marques (cf add)

Ne pas utiliser l'option -a, afin de mieux controler les changements
```sh
git commit -m "commentaire"
```

- Pour retoucher le commentaire du dernier commit (si faute de frappes, ...)
```sh
git commit --amend
```

- Pour modifications suite à revue de code
```sh
git commit -m "Revue 00x: Commentaire spécifique à prise en compte des remarques"
```

- Si besoin, annuler les modifications en working dir (retour au stagge)
```sh
git checkout -- myFile
```

- Retour sur une ancienne version
```sh
git checkout myCommit Myfile
```

- Retour sur la version la plus à jour
```sh
git checkout HEAD Myfile
```

- Détails d'un commit
```sh
git show [commit]
```

- Stash: Pour push le dépot local sans effacer les fichiers que l'on ne veut pas remonter

Commit les changements -> save des fichiers locaux -> récupère le dépot -> remonte les modifications au dépot -> récupère les fichiers locaux
```
git commit [FILES]
git stash
git pull
git push
git stash list
git stash pop
```

Branches dev
============

Cette méthode n'est utilisée qu'en cas de développement particulier sur du long terme
ne nécessitant pas d'être remontée en dépot central.

Resynchronisation du dépot local sur le dépot central (méthode avec branche dev temporaire locale)

- Le principe de synchronisation entre depots
La branche master du dépot local toujours en miroir du dépot central (origin)
La branche dev du depot local impérativement pour les modifications.
Cette branche dev supporte le rebase afin de garder un historique lineaire (et donc restant lisible)

- Pre-requis: Tous les fichiers déjà gérés sous git doivent être commités dans la branche dev

- Synchronisation du master local
```sh
git checkout master
git fetch origin
git merge origin/master
```
et sortir de l'éventuelle session d'edition (vi) par ":wq"

- Fusion dans la branche de dev
```sh
git checkout dev
git rebase -i master
```
Vérifier la présence de conflits dans la partie "unmerged" du
```sh
git status
```
- Si conflits, editer ces fichiers en repérant les marques
```sh
  <<<<<<< HEAD
  =======
  >>>>>>> xxxx
```
et supprimer ces marques et les parties inutiles,
puis reprise apres resolution des conflits
```sh
git add myFile
git rebase --continue
# et sortir de la session d'edition (vi) par ":wq"
```

- Ménage des fichiers temporaires *$py.class et non gérés par git, à partir du dossier courant
```sh
cdi
git clean -dxn
git clean -dxf
```

- Vérification de la non-regression dans le dépot local


Contrôles avant push
====================

- Revue de code par un pair

Identifier si besoin des portions de code à déplacer en bibliothèque commune

- Si impact dans les bibliothèques communes

Faire une relecture avec un autre scripteur, et tests de non-régression à passer au miminum sur
```sh
00_LIB/Templates/F02_PistesOperateur_PointsSpeciaux/PT_LOTI_NG_FSST_F02_10010
03_ARM/F04_Torpille_MU90/PT_LOTI_NG_ARM_F04_10030
02_FSST/F31_EnrichirSupprimer_PistesTactiques/PT_LOTI_NG_FSST_F31_10010
```

- Vérifier la forme des scripts, depuis le répertoire le plus haut de vos modifications, via
```sh
ivqAudit.sh
```
et effectuer les modifications, puis add/commit si necesssaire

- Si impact général (lib, ...) enrichir CHANGELOG.txt (cf V0xx_encours), puis commit


Push
====

Remontée du dépot local vers le dépot central (méthode avec branche dev temporaire locale)

Effectuer IMPERATIVEMENT au préalable la resynchronisation depuis le dépot central
Cf toutes les étapes du bloc plus haut "Resynchronisation du dépot local sur le dépot central"

- Remontee du master local vers le depot distant
```sh
git checkout master
git merge dev
git push origin master
```

- Retour dans la branche dev pour les futures modifications
```sh
git checkout dev
```


Branches
========

Méthode simplifiée (sans branche dev locale temporaire) pour branches centralisées

- Principe

Une branche master pour les nouveaux développements
Une branche maint restant compatible avec la branche de maintenance
Des transferts ponctuels peuvent être effectués d'une branche à une autre
en désignant un commit particulier.

- Changement de branches
```sh
git checkout master
ou alias
gitmaster

git checkout maint
ou alias
gitmaint
```

- Resynchronisation de la branche courant du dépot local sur le dépot central
```sh
git pull
```
NB: Enchaine un fetch de toutes les branches et un rebase de la branche courante seulement
Pour resynchroniser une autre branche, s'y positionner et refaire git pull

- Ménage des fichiers temporaires *$py.class et non gérés par git, à partir du dossier courant
```sh
cdi
git clean -dxn
git clean -dxf
```

- Vérifications des modifications locales avant remontée en dépot central (cf plus haut)

Non-regression (pas d'exception levées à l'execution, ...)
```sh
ivqAudit.sh
```
Si impact général (lib, ...) enrichir CHANGELOG.txt (cf V0xx_encours)

- Remontée de toutes les branches du dépot local vers le dépot central
```sh
git push
Pour ne remonter qu'une branche, la désigner
git push origin master
git push origin maint
```

- Transfert d'un commit d'une branche vers une autre

Repérer dans la branche d'origine le numéro de commit à transférer
```sh
git log --graph --oneline
Depuis la branche destination, désigner ce numéro de commit
git cherry-pick myCommitNum
ex:
git cherry-pick 2fff805
ou le SHA-1 complet 2fff8053cdc4094d29cf2fd086e9f140f249d82c
```

Notes
=====

Voici des traces pour des cas particuliers lors du pull/push

- pull: Conflits de lignes détectés

Si conflits (cf git status), vois plus bas
  Editer les fichiers en repérant les marques ```<<< === >>>``` et garder les blocs utiles
  Puis pour reprendre, apres résolution des conflits
```sh
  git add myFile
  git rebase --continue
```
et sortir de la session d'edition (vi) par ":wq"

Ou bien pour revenir dans l'état original
```sh
  git rebase --abort
```

- pull: Si le dépot local est déjà synchronisé

Current branch master is up to date.

- push: Si le dépot central est déjà à jour

Everything up-to-date

- pull: Si un conflit de ligne est détecté

```sh
remote: Counting objects: 5, done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 0 (delta 0)
Unpacking objects: 100% (3/3), done.
From /nfs/ptfloti/ivq/users/PSE/work/gitSandBox/SANDBOX
   9a10dfc..5736738  master     -> origin/master
First, rewinding head to replay your work on top of it...
Applying: XXX
Using index info to reconstruct a base tree...
Falling back to patching base and 3-way merge...
Auto-merging CHANGELOG.txt
CONFLICT (content): Merge conflict in CHANGELOG.txt
Failed to merge in the changes.
Patch failed at 0001 XXX
When you have resolved this problem run "git rebase --continue".
If you would prefer to skip this patch, instead run "git rebase --skip".
To restore the original branch and stop rebasing run "git rebase --abort".
puis faire un git status et repérer les lignes du type
#       both modified:      CHANGELOG.txt
```

- push: Si le pull n'a pas été fait avant, et que d'autres modifications
existent dans le dépot central, Git bloque la remontée
```sh
To /nfs/ptfloti/ivq/users/PSE/work/gitSandBox/SANDBOX.git
 ! [rejected]        master -> master (non-fast-forward)
error: failed to push some refs to '/nfs/ptfloti/ivq/users/PSE/work/gitSandBox/SANDBOX.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes before pushing again.  See the 'Note about
fast-forwards' section of 'git push --help' for details.
```

- push: OK depuis branch master, mais autre branche v1 non synchronisée
```sh
Counting objects: 7, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (5/5), done.
Writing objects: 100% (5/5), 508 bytes, done.
Total 5 (delta 3), reused 0 (delta 0)
Unpacking objects: 100% (5/5), done.
To /nfs/ptfloti/ivq/users/PSE/work/gitSandBox/SANDBOX.git
   bd98457..5733591  master -> master
 ! [rejected]        v1 -> v1 (non-fast-forward)
error: failed to push some refs to '/nfs/ptfloti/ivq/users/PSE/work/gitSandBox/SANDBOX.git'
To prevent you from losing history, non-fast-forward updates were rejected
Merge the remote changes before pushing again.  See the 'Note about
fast-forwards' section of 'git push --help' for details.
```

- cherry-pick avec conflit
```sh
git cherry-pick ea035806756d6a8e252a778ae59bcd5f6db22b63
Automatic cherry-pick failed.  After resolving the conflicts,
mark the corrected paths with 'git add <paths>' or 'git rm <paths>'
and commit the result with:
        git commit -c ea035806756d6a8e252a778ae59bcd5f6db22b63
```
