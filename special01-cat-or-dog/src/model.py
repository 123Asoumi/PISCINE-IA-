"""SmallCNN (Jour 3) + ResNet18 transfer (Jour 6)."""
import torch.nn as nn


# --- Task 08 : ton CNN from scratch ----------------------------------------
class SmallCNN(nn.Module):
    def __init__(self, n_classes=2):
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(3, 16, kernel_size=3, padding=1), nn.ReLU(), nn.MaxPool2d(2),
            ...,  # TODO: block 2, 16 -> 32 channels
            ...,  # TODO: block 3, 32 -> 64 channels
        )
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(..., 64),  # TODO: combien de features après Flatten ?
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, n_classes),
        )

    def forward(self, x):
        return self.classifier(self.features(x))


# --- Task 17 : ResNet18 pré-entraîné (à écrire Jour 6) ----------------------
# def build_resnet18(device):
#     from torchvision import models
#     ...  # freeze body, remplace fc par Linear(..., 2)
