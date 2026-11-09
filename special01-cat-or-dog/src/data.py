"""Transforms, split train/val, DataLoaders (Jour 2)."""
import torch
from torch.utils.data import Subset, DataLoader
from torchvision import datasets, transforms

IMG = 128
MEAN, STD = [0.485, 0.456, 0.406], [0.229, 0.224, 0.225]  # ImageNet


# --- Task 04 : split train / val -------------------------------------------
def split_indices(n, val_fraction=0.15, seed=42):
    g = torch.Generator().manual_seed(seed)
    idx = torch.randperm(n, generator=g).tolist()
    n_val = int(val_fraction * n)
    return idx[n_val:], idx[:n_val]  # train_idx, val_idx


# --- Task 05 : transforms ---------------------------------------------------
train_tf = transforms.Compose([
    transforms.Resize((IMG, IMG)),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    transforms.ToTensor(),
    transforms.Normalize(MEAN, STD),
])

eval_tf = transforms.Compose([
    transforms.Resize((IMG, IMG)),
    transforms.ToTensor(),
    transforms.Normalize(MEAN, STD),
])


# --- Task 06 : datasets & loaders ------------------------------------------
def make_loaders(root, batch_size=32, num_workers=2):
    def ds(split, tf):
        return datasets.OxfordIIITPet(root=root, split=split,
                                      target_types="binary-category", transform=tf)

    trainval_len = len(ds("trainval", eval_tf))
    train_idx, val_idx = split_indices(trainval_len)

    train_ds = Subset(ds("trainval", train_tf), train_idx)
    val_ds = Subset(ds("trainval", eval_tf), val_idx)
    test_ds = ds("test", eval_tf)

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=...,  # TODO
                              num_workers=num_workers)
    val_loader = DataLoader(val_ds, batch_size=batch_size, shuffle=False,
                            num_workers=num_workers)
    test_loader = ...  # TODO: same as val
    return train_loader, val_loader, test_loader


# TODO (Task 06) : écris toi-même la fonction qui ANNULE la normalisation
# pour pouvoir afficher une image (denormalize).
