import torch
import numpy as np
import random
from torch.utils.data import DataLoader
from dataset import WaveformDataset
from tqdm import tqdm

def train():
    dataset = WaveformDataset("data", filelist="filelist.txt")
    print(f"Dataset size: {len(dataset)} samples")
    
    dataloader = DataLoader(
        dataset,
        batch_size=16,
        shuffle=True,
        num_workers=4,
    )
    
    print("Starting training...")
    for epoch in range(3):
        print(f"\nEpoch {epoch + 1}")
        for batch_idx, batch in enumerate(tqdm(dataloader)):
            # Simulate training step
            waveforms = batch['waveform']
        print(f"Epoch {epoch + 1} complete")
    
    print("\nTraining finished successfully!")

if __name__ == "__main__":
    train()