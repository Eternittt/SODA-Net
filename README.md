### 1. install

Install all dependencies for this project: `pip install -r requirements.txt`


```
pip install ultralytics
```

### 2.Usage

#### 2.1 train

```
python train.py 
```

#### 2.2val

```
python val.py 
```

### 3.Key Directory Structure  

#### 3.1 Configuration Files (ultralytics/cfg)

Model Architecture: Located in the models/SODA-YOLO subdirectory, containing detailed configuration files for network structures.

Dataset Settings: Defined in the dataset.yaml file, where paths, classes, and related parameters can be configured.

Training/Testing Setup: Managed via default.yaml, including hyperparameters, optimizer settings, and other training configurations.

#### 3.2 Module Implementations (ultralytics/nn/modules/block)
