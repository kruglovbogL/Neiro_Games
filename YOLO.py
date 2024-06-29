import cv2
from ultralytics import YOLO
from imageai.Classification.Custom import ClassificationModelTrainer
from imageai.Detection.Custom import DetectionModelTrainer
import os
from imageai.Classification.Custom import CustomImageClassification

model = YOLO("best.pt")

# model.train(data='data.yaml',epochs=100)

img_path = 'Снимок.PNG'
results = model.predict(img_path)
result = results[0]
output = []
# for box in result.boxes:
#     x1, y1, x2, y2 = [
#         round(x) for x in box.xyxy[0].tolist()
#     ]
#     class_id = box.cls[0].item()
#     prob = round(box.conf[0].item(), 2)
#     output.append([
#         x1, y1, x2, y2, result.names[class_id], prob
#     ])
for box in result.boxes:
    x,y,width,height = box
    x2,y2 = x + width, y + height
    cv2.rectangle(img_path,(x,y),(x2,y2),(0,255,0),1)

cv2.imshow('Windows_show_img',img_path)
cv2.waitKey(0)
cv2.destroyAllWindows()