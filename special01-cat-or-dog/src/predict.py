"""Outil ligne de commande (Jour 7). Doit tourner sans le code d'entraînement ni le dataset."""
import argparse
import torch
from PIL import Image

CLASSES = ["cat", "dog"]


def load_model(weights_path, device):
    ...  # TODO: reconstruire l'architecture, load_state_dict, eval()


def predict(model, image_path, device):
    ...  # TODO: open, convert("RGB"), eval_tf, softmax -> (label, prob)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("images", nargs="+")
    ap.add_argument("--weights", default="models/best.pt")
    ap.add_argument("--threshold", type=float, default=0.8)
    args = ap.parse_args()
    ...  # TODO: une ligne par image ; fichier manquant -> message clair + exit code 1 ;
         #       proba < threshold -> "unsure"
