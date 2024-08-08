import cv2
import numpy as np

my_photo = cv2.imread('Screen_lilies_2.PNG')
filterd_image  = cv2.medianBlur(my_photo,7)
img_grey = cv2.cvtColor(filterd_image,cv2.COLOR_BGR2GRAY)

#set a thresh
thresh = 100

#get threshold image
ret,thresh_img = cv2.threshold(img_grey, thresh, 255, cv2.THRESH_BINARY)

#find contours
contours, hierarchy = cv2.findContours(thresh_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(type(contours),type(hierarchy))
#create an empty image for contours
img_contours = np.uint8(np.zeros((my_photo.shape[0],my_photo.shape[1])))

cv2.drawContours(img_contours, contours, -1, (255,255,255), 1)

cv2.imshow('origin', my_photo) # выводим итоговое изображение в окно
cv2.imshow('res', img_contours) # выводим итоговое изображение в окно

img_contou = np.uint8(np.zeros((my_photo.shape[2],my_photo.shape[1])))
cv2.imshow('countour',img_contou)

cv2.waitKey()
cv2.destroyAllWindows()