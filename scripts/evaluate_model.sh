#!/bin/bash
# Evaluate pretrained model on validation set
cd "$(dirname "$0")/.." || exit

yolo detect val \
  data=./vplab_indoor.yaml \
  model=weights/yolo11n.pt \
  device=mps \
  imgsz=640 \
  save_json=True \
  name=pretrained_eval

