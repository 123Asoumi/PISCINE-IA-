# special01 — Cat or Dog?

Classifieur d'images chat/chien construit from scratch (SmallCNN) puis par transfer learning (ResNet18).
Special piscine IA — Project 01.

## Setup

```bash
pip install -r requirements.txt
```

Sur Colab : Runtime > Change runtime type > T4 GPU.

## Reproductibilité

- Seed fixe : **42** partout.
- Le test set est ouvert **exactement deux fois** (Jour 5 et Jour 6).

## Structure

```
special01-cat-or-dog/
  notebooks/   01_explore.ipynb  02_train_cnn.ipynb  03_transfer.ipynb
  src/         data.py  model.py  train.py  predict.py
  models/      poids sauvegardés (hors Git)
  experiments.csv   une ligne par run d'entraînement
  MODEL_CARD.md
  DESIGN.md
```

## Chiffres du dataset

<!-- TODO (Task 02) : coller ici les nombres imprimés par le téléchargement : len(trainval), len(test), img.size, label -->

## Baseline majoritaire

<!-- TODO (Task 03) : cats=..., dogs=..., majority baseline accuracy=...% -->

## Meilleur run

<!-- TODO (Task 12) : courbes du meilleur run + 1 paragraphe sur l'effet du learning rate -->

## Utilisation de predict.py

```bash
python3 src/predict.py photos/rex.jpg --weights models/best.pt
```
