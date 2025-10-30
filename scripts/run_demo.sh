#!/bin/bash
# Run live camera demo
cd "$(dirname "$0")/.." || exit
yolo detect predict model=weights/yolo11n.pt source=0 device=mps show=True

