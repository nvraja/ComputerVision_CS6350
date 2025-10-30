#!/bin/bash
# Run batch prediction on test images
cd "$(dirname "$0")/.." || exit

yolo detect predict \
  model=weights/yolo11n.pt \
  source=test_images \
  device=mps \
  imgsz=640 \
  conf=0.25 \
  save=True \
  save_crop=True \
  show=False

echo "Latest prediction results:"
ls -lt runs/detect | head -n 5

