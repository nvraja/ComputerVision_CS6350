from ultralytics import YOLO

loc = '/home/da24c025/CV/test_images'

model = YOLO("yolov11n.pt") 

# Batch prediction - all images in a folder
model.predict(source=loc, save=True, conf=0.25)
