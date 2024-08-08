# import tensorflow as tf
# # from keras.src.utils import to_categorical
# from sklearn.preprocessing import LabelEncoder
# from tensorflow import keras
# from tensorflow.keras import layers
# import pandas as pd
# import numpy as np
# import cv2
# import os
# import tensorflow as tf
# from PIL import Image
# import numpy as np
# from tensorflow.keras import datasets, layers, models
# import matplotlib.pyplot as plt
import cv2
import numpy as np
import torch.jit
import torch
from PIL import Image
import time
from imageai.Classification.Custom import ClassificationModelTrainer
from imageai.Detection.Custom import DetectionModelTrainer
import os
from imageai.Classification.Custom import CustomImageClassification
import cv2
from ultralytics import YOLO
from imageai.Classification.Custom import ClassificationModelTrainer
from imageai.Detection.Custom import DetectionModelTrainer
import os
from imageai.Classification.Custom import CustomImageClassification
import timm
from keras_applications import imagenet_utils
from ultralytics.utils.plotting import Annotator
from ultralytics.utils.plotting import Annotator, colors
#Train_models_Netv2                    !!!!!!!!!!!!!!!!!!!!!
# model.train(data='data.yaml',epochs=100)




# #ЗАГРУЗКА МОЕЙ модели И РАСПОЗНАВАНИЕ ПРЕДМЕНА С ПОМОЩЬЮ ОБУЧЕННОЙ!!!! СЕТИ
model = YOLO("best.pt")

cap = cv2.VideoCapture("ENDER LILIES Speedrun Any.mp4")
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
writer = cv2.VideoWriter("Ultralytics circle annotation.avi", cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

while True:
    ret, im0 = cap.read()
    if not ret:
        break

    annotator = Annotator(im0, line_width=2)

    results = model.predict(im0)
    boxes = results[0].boxes.xyxy.cpu()
    clss = results[0].boxes.cls.cpu().tolist()

    for box, cls in zip(boxes, clss):
        x1, y1 = int((box[0] + box[2]) // 2), int((box[1] + box[3]) // 2)
        annotator.box_label(box, label=model.names[int(cls)], color=colors(int(cls), True))

    writer.write(im0)
    cv2.imshow("Ultralytics circle annotation", im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

writer.release()
cap.release()
cv2.destroyAllWindows()




