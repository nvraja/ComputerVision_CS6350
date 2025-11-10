# YOLO11 V1.1 – Object Detection

This project fine-tunes the YOLO11 model for object detection using custom data and other pics captured.

---
Folder structure:
~/CV/yolo/
├─ data/                         
├─ dataset/             
│  ├─ train/
│  │   ├─ images/
│  │   └─ annotations.json  (optional if Roboflow uses one global file)
│  ├─ val/
│  │   ├─ images/
│  │   └─ annotations.json
│  └─ test/
│      ├─ images/
│      └─ annotations.json
├─ test_images/
├─ data.yaml                  
├─ outputs/
├─ weights/
├─ scripts/
│   ├─ readme.txt
│   └─ enviornment.yml
├─ readme.txt
└─ enviornment.yml

## 🧩 Setup

```bash
# Create and activate environment
conda env create -f environment.yml
conda activate yolo11

# Launch JupyterLab
jupyter lab
