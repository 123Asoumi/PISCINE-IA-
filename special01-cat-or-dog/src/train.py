"""Boucle d'entraînement + évaluation (Jour 4)."""
import torch
import torch.nn as nn


# --- Task 11 : fonction d'évaluation (à écrire toi-même) -------------------
# def evaluate(model, loader, loss_fn, device):
#     """Retourne (loss moyenne, accuracy). Dedans : model.eval() + torch.no_grad()."""
#     ...


@torch.no_grad()
def predict_all(model, loader, device):
    """Retourne labels et probabilités de classe pour tout un loader."""
    model.eval()
    ys, probs = [], []
    for x, y in loader:
        p = torch.softmax(model(x.to(device)), dim=1)
        ys.append(y)
        probs.append(p.cpu())
    return torch.cat(ys), torch.cat(probs)


# --- Task 10 : la boucle d'entraînement ------------------------------------
def train(model, train_loader, val_loader, device, epochs=15, lr=1e-3):
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        for x, y in train_loader:
            x, y = x.to(device), y.to(device)
            logits = ...   # TODO 1: forward pass
            loss = ...     # TODO 2: comparer logits et labels
            ...            # TODO 3: remettre les gradients à zéro
            ...            # TODO 4: backpropagation
            ...            # TODO 5: mettre à jour les poids
        # val_loss, val_acc = evaluate(model, val_loader, loss_fn, device)
        # print(f"epoch {epoch:2d}  val_loss {val_loss:.3f}  val_acc {val_acc:.3f}")
