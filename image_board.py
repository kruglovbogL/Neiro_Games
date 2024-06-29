
import cv2
import os

# path
path = r'D:\Project_University\Noita_Neuro\Screen_lilies_3.PNG'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Start coordinate, here (5, 5)
# represents the top left corner of rectangle
start_point = (5, 5)

# Ending coordinate, here (220, 220)
# represents the bottom right corner of rectangle
end_point = (220, 220)

# Blue color in BGR
color = (0,255,0)

# Line thickness of 2 px
thickness = 2

# Using cv2.rectangle() method
# Draw a rectangle with blue line borders of thickness of 2 px
image = cv2.rectangle(image, start_point, end_point, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)

cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()