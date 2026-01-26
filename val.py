import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO


if __name__ == '__main__':
    model = YOLO('runs/detect/train/weights/best.pt')
    model.val(data='dataset.yaml',
              split='test',
              imgsz=640,
              batch=1,
              )