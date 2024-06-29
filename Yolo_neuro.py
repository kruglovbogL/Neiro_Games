from ultralytics import YOLO

model = YOLO("yolov8m.pt")


results = model.predict('Screen_lilies_1')