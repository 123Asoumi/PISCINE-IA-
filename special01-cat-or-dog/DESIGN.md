# DESIGN — notes de conception

> Règle du projet : tu écris chaque réponse toi-même d'abord. Pas d'assistant pour le premier jet.

## Task 01 — Think before you code (Jour 1)

1. Input / output du modèle (formes exactes) :
2. Que veut dire « le modèle a appris », concrètement, en termes de nombres ?
3. Quelle métrique dit que le modèle marche ? Pourquoi l'accuracy seule est dangereuse si 2× plus de chiens que de chats ?
4. Trois façons d'avoir raison pour une mauvaise raison :
5. Deux types de photos où tu t'attends à ce qu'il échoue :

## Task 05 — Transforms
- Que fait chaque ligne (ToTensor : forme + plage de valeurs ? Normalize : pourquoi soustraire une moyenne ?)
- Pourquoi resize en carré malgré les ratios différents ? Qu'est-ce qu'on perd ?
- Augmentation ajoutée + justification. Laquelle serait fausse pour cette tâche ?

## Task 07 — Shapes by hand
- Conv2d(3,16,k=3,p=1) sur 128×128 : forme de sortie ? nb de paramètres ?
- Après MaxPool2d(2) :
- Idem pour 32 puis 64 canaux : forme avant le classifieur ?
- Linear brut pixels -> 64 neurones : nb de paramètres ? Comparaison :

## Task 11 — eval()
- Pourquoi model.eval() ET torch.no_grad() ?
