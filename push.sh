#!/usr/bin/env bash

# TODO(human): ecris la logique du script.
#
# 1) Si AUCUN message n'est donne (nombre d'arguments == 0) :
#       afficher :  Usage: ./push.sh "commit message"
#       puis arreter le script.
#    Structure d'un test en bash :
#       if [ CONDITION ]; then
#           echo "..."
#           exit 1
#       fi
#    Indice condition : [ $# -eq 0 ]   ( -eq veut dire "egal a" )
#
# 2) Sinon, enchainer :
#       git add -A
#       git commit -m "$1"      (les guillemets autour de $1 sont importants)
#       git push
#
# Astuce : pour afficher du texte en bash on utilise  echo "..."

if [ $# -eq 0 ]; then
   echo "Usage: ./push.sh "commit message""
   exit 1
fi
   git add -A
   git commit -m "$1"
   git push
