#!/bin/bash
# Quick training test
cd "$(dirname "$0")/.." || exit
yolo detect train \
  data=./vplab_indoor.yaml \
  model=weights/yolo11n.pt \
  epochs=3 \
  imgsz=320 \
  batch=4 \
  device=mps \
  name=finetune_smoke

