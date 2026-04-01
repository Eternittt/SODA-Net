import warnings, os
warnings.filterwarnings('ignore')
from ultralytics import YOLO
import torch


if __name__ == '__main__':
    model = YOLO(r'ultralytics/cfg/models/SODA-Net/SODA-Net.yaml')
    torch.cuda.empty_cache()
    model.train(data='dataset.yaml',
                imgsz=640,
                epochs=500,
                batch=16,
                workers=8,
                device=0,
                patience=100,
                )
