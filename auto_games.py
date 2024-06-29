from random import randint
import cv2
import mss
import numpy as np

import os
from pywinauto.application import Application
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click, press
import time
from auto_laile import PressKey,ReleaseKey

# KEYS = 0x2C, 0x2C
# for key in KEYS:
#     PressKey(key)
#
#
# click(button='left', coords=(960, 530)), (click(button='left', coords=(860, 470)))
#
# while True:
#     list_button =[0xCD,0xCB,0xC8,0xC8, 0x2C,0x2D,0x2E,0x1C,0x2F]
#     rand_int = randint(0,len(list_button)-1)
#     KEYS = list_button[rand_int]
#     PressKey(KEYS)
#     time.sleep(1)
#     ReleaseKey(KEYS)
#     PressKey(0xCD)
#     time.sleep(1)
#     ReleaseKey(0xCD)
#     PressKey(0x2C)
#     time.sleep(1)
#     ReleaseKey(0x2C)


import torch
import torch.nn as nn

# Определение архитектуры нейронной сети
class PopulationNN(nn.Module):
    def __init__(self):
        super(PopulationNN, self).__init__()
        self.hidden_layer = nn.Linear(6, 10)  # Скрытый слой с 10 нейронами
        self.output_layer = nn.Linear(10, 1)  # Выходной слой с 1 нейроном

    def forward(self, x):
        x = torch.relu(self.hidden_layer(x))  # Применение функции активации ReLU к скрытому слою
        x = self.output_layer(x)
        return x

# Создание экземпляра нейронной сети
model = PopulationNN()

# Определение функции потерь и оптимизатора
criterion = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# Пример обучения на некоторых искусственно созданных данных
X_train = torch.randn(100, 6)  # Входные данные
Y_train = torch.randn(100, 1)  # Метки

# Обучение нейронной сети
for epoch in range(1000):
    optimizer.zero_grad()
    outputs = model(X_train)
    loss = criterion(outputs, Y_train)
    loss.backward()
    optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f'Epoch {epoch+1}, Loss: {loss.item()}')


from PIL import Image

img = Image.open('Screen_new_1.PNG')
tensor_data = torch.tensor(np.array(img))

input_data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]  # пример входных данных
input_tensor = torch.tensor(input_data).float()  # преобразование в тензор PyTorch

# Передача входных данных через нейросеть
output = model(input_tensor)

print('Результат нейронной сети для входных данных:', output.item())



# Получение предсказаний на новых данных
X_new = torch.randn(1, 6)
predictions = model(X_new)
print('Predictions:', predictions)
test_input = torch.rand(1,6)
print(model(test_input))
