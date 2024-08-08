from ultralytics import YOLO

model = YOLO("yolov8m.pt")  # выбор модели для тренировки yolov8m.pt

model.train(data='D:/Project_University/Noita_Neuro/Image_Enemy_Lilies/data.yaml',
            epochs=100)  # надо создать файл data.yaml в котором:
###path: ../datasets/roboflow

###  train: train/images  #путь к train      для этого лучше использовать https://roboflow.com/?ref=ultralytics
###  val: valid/images   #путь к valid
###  test: test/images   #путь к папке test

###  names:
###  0: noita_state  #классы которые надо найти и которые размечены
###
###
