# Tas 05 - What is a model, really?

> A remplir avec TES propres mots (3 a 5 phrases chacune), SANS assistant IA.
> Tu pourras demander une correction apres, et noter tes erreurs dans la section Corrections.

## 1. Difference entre une IA et un modele d'IA ?
      une ia es un promgrame mathématique qui es conçu dans le but d'imiter l'intelligence humaines dans certaines taches,
      un modele lui es un systeme matématique basé sur de nombreuse donné afin de pouvoir fournir des résultat

## 2. Qu'est-ce qu'un reseau de neurones ?
      un réseau de neurones es une sytemes mathématiques conçu pour imiter simplement les neurones humaines

## 3. Comment une IA apprend-elle a partir de donnees ?
      une ia apprend a distinger le vrai du faux a partir d'exemples du types un chat un chien
      et a travers un longue boucle d'erreur et de correction sera capable identifier des chats

## 4. Qu'est-ce qu'un dataset ?
       un dataset es une basse de donnée organiser avec une cibles a trouvé et des caractériques a identifier pour cette cibles 
       (une dataset peux  contenir n'importe quelle donné)

## 5. Difference entre entrainer un modele et utiliser un modele deja entraine ?
       entrainer un modele c'est partir de zero pour créer son propre modele alors que utiliser un modele existant c'est utiliser un modle déja entrainer et qui n fait quasiment pas d'erreur


Cat detector :

Voici les étapes :

Étape 1 : On fournit des données

On donne 1 000 images à notre modèle :
- 500 images de chats.
- 500 images de chiens.
Étape 2 : Le modèle fait des prédictions

Il analyse une image et prédit :

« Je pense que c'est un chien. »

Étape 3 : On mesure son erreur

On compare sa prédiction avec la bonne réponse.

Par exemple :
- Réponse attendue : Chat.
- Prédiction : Chien.
- Résultat : Erreur.
Étape 4 : On corrige le modèle

Grâce à des méthodes mathématiques comme la rétropropagation (Backpropagation), le modèle ajuste ses paramètres pour réduire son erreur.

Étape 5 : On recommence

Le modèle répète ce processus sur de nombreux exemples.

Petit à petit, il devient meilleur pour reconnaître les chats.
Le cycle d'apprentissage
1. Recevoir des données
2. Faire une prédiction
3. Calculer l'erreur (Loss)
4. Ajuster les paramètres (Backpropagation + Optimizer)
5. Recommencer

À retenir : une IA ne devient pas intelligente par magie. Elle ajuste ses paramètres grâce aux exemples et aux erreurs.      

Voici les étapes :

Étape 1 : On fournit des données

On donne 1 000 images à notre modèle :
- 500 images de chats.
- 500 images de chiens.
Étape 2 : Le modèle fait des prédictions

Il analyse une image et prédit :

« Je pense que c'est un chien. »

Étape 3 : On mesure son erreur

On compare sa prédiction avec la bonne réponse.

Par exemple :
- Réponse attendue : Chat.
- Prédiction : Chien.
- Résultat : Erreur.
Étape 4 : On corrige le modèle

Grâce à des méthodes mathématiques comme la rétropropagation (Backpropagation), le modèle ajuste ses paramètres pour réduire son erreur.

Étape 5 : On recommence

Le modèle répète ce processus sur de nombreux exemples.

Petit à petit, il devient meilleur pour reconnaître les chats.
Le cycle d'apprentissage
1. Recevoir des données
2. Faire une prédiction
3. Calculer l'erreur (Loss)
4. Ajuster les paramètres (Backpropagation + Optimizer)
5. Recommencer

À retenir : une IA ne devient pas intelligente par magie. Elle ajuste ses paramètres grâce aux exemples et aux erreurs.