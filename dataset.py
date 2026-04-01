import os
import numpy as np
np.seterr(divide='raise', invalid='raise')
from torch.utils.data import Dataset

class WaveformDataset(Dataset):
    """Dataset for loading waveform data from text files."""
    
    def __init__(self, data_dir="data", filelist=None):
        self.data_dir = data_dir
        
        if filelist and os.path.exists(filelist):
            with open(filelist, 'r') as f:
                self.files = [line.strip() for line in f if line.strip()]
        else:
            self.files = sorted([
                f for f in os.listdir(data_dir) 
                if f.endswith('.txt') and not f.startswith('.')
            ])
    
    def __len__(self):
        return len(self.files)
    
    def __getitem__(self, idx):
        filename = self.files[idx]
        filepath = os.path.join(self.data_dir, filename)
        
        waveform = np.loadtxt(filepath).astype(np.float32)
        max_amplitude = np.max(np.abs(waveform))
        waveform_normalized = waveform / max_amplitude
        
        return {
            'filename': filename,
            'waveform': waveform_normalized,
            'max_amplitude': max_amplitude
        }