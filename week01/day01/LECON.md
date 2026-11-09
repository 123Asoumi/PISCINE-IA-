# Leçon — Day 01 (Python Environment)

Mémo personnel des notions et commandes vues pendant le Day 01.

---

## 📦 Les imports Python (task03/sysinfo.py)

Un `import` = ouvrir une boîte à outils fournie avec Python.

| Import | Boîte | Outil utilisé | Rôle |
| `import sys` | `sys` | — | infos sur l'interpréteur Python |
| `import platform` | `platform` | `platform.python_version()` | version de Python (ex. `3.10.12`) |
| | | `platform.system()` | nom de l'OS (ex. `Linux`) |
| `import os` | `os` | `os.getcwd()` | dossier courant (*get current working directory*) |

---

## 🔑 SSH — le badge d'accès GitHub

| Commande | Rôle |
|---|---|
| `ssh-keygen -t ed25519 -C "email"` | générer une paire de clés SSH (privée + publique) |
| `cat ~/.ssh/id_ed25519.pub` | afficher la clé **publique** (celle qu'on donne à GitHub) |
| `ssh -T git@github.com` | tester la connexion à GitHub |

- Clé **privée** (`id_ed25519`) = secrète, ne jamais partager.
- Clé **publique** (`.pub`) = se colle dans GitHub (Settings → SSH keys).

---

## 🗂️ Git — la sauvegarde (add → commit → push)

| Commande | Rôle |
|---|---|
| `git status` | voir ce qui a changé |
| `git add .` / `git add -A` | mettre les fichiers dans le carton (`-A` inclut les suppressions) |
| `git commit -m "message"` | fermer le carton avec une étiquette |
| `git push` | envoyer vers GitHub |
| `git rm -r --cached dossier` | arrêter de suivre un dossier **sans l'effacer** du disque |
| `git ls-files` | lister les fichiers suivis par Git |

Image : `add` = ranger dans le carton · `commit` = coller l'étiquette · `push` = donner au livreur.

---

## 🐍 Environnement Python (venv + pip)

| Commande | Rôle |
|---|---|
| `python3 -m venv .venv` | créer l'environnement virtuel |
| `source .venv/bin/activate` | entrer dans l'environnement (affiche `(.venv)`) |
| `python -m pip install --upgrade pip numpy` | installer des librairies dans le venv |
| `python -m pip freeze > requirements.txt` | écrire la liste des librairies dans un fichier |
| `python3 fichier.py` | exécuter un script |
| `python3 -m py_compile fichier.py` | vérifier la syntaxe sans exécuter |

- Un **venv** isole les librairies du projet (un atelier à part).
- Règle d'or : à l'intérieur d'un venv, utiliser `python -m pip` (jamais `pip` tout seul).
- `.venv/` ne se pousse **jamais** sur Git → on l'ajoute au `.gitignore`.

---

## 📁 Fichiers & système (commandes Linux de base)

| Commande | Rôle |
|---|---|
| `cd dossier` | changer de dossier |
| `ls` / `ls -l` | lister le contenu |
| `cat fichier` | afficher le contenu d'un fichier |
| `cp source dest` | copier |
| `mv source dest` | déplacer / renommer |
| `rm -rf dossier` | supprimer (⚠️ puissant, irréversible) |
| `chmod 600 fichier` | permissions : lecture/écriture pour le propriétaire seul (clé privée) |
| `chmod +x fichier` | rendre un fichier exécutable (scripts) |
| `echo "texte"` | afficher du texte |
| `echo "..." \| sudo tee fichier` | écrire dans un fichier protégé (en admin) |

---

## 🛠️ Réseau & système (dépannage rencontré)

| Commande | Rôle |
|---|---|
| `ping -c 3 github.com` | tester si une adresse répond |
| `sudo apt install python3.10-venv` | installer un paquet système |
| `sudo apt update` | rafraîchir la liste des paquets |
| `wsl -u root` | entrer dans WSL en administrateur |
| `passwd tino` | changer le mot de passe d'un utilisateur |

---

## 💡 Notions transversales

- **`sudo`** = exécuter en administrateur (demande le mot de passe).
- **`-m`** (comme `python -m pip`) = « lance ce module Python » → garantit le bon outil.
- **`>`** = rediriger la sortie d'une commande vers un fichier (au lieu de l'écran).
- **Codes de sortie** : `0` = succès, autre = erreur (`exit 1` dans un script).
- **WSL vs Windows** = deux maisons séparées (trousseaux de clés, mots de passe distincts).

---

## 📜 Script push.sh (task06)

```bash
#!/usr/bin/env bash          # shebang : exécuter avec bash

if [ $# -eq 0 ]; then        # si aucun argument n'est donné
    echo 'Usage: ./push.sh "commit message"'
    exit 1                   # arrêter avec un code d'erreur
fi

git add -A                   # tout ajouter
git commit -m "$1"           # commit avec le message fourni ($1)
git push                     # envoyer sur GitHub
```

- `$#` = nombre d'arguments · `$1` = 1er argument.
- `if ... ; then ... fi` = structure d'un test en bash.
