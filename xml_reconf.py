import lxml
from lxml import etree
from xml import etree



parsers = lxml.etree.ElementTree()

parsers

path = ''

image_height= 0
image_width = 0
box_x_width = 0
box_x_left = 0
box_y_top = 0
box_width = 0
box_height = 0

x_center = (box_x_left+box_x_width/2)/image_width
y_center = (box_y_top+box_height/2)/image_height
width = box_width/image_width
height = box_height/image_height


