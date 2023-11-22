from ImageParse import *

temp = imageToGrayScale('Zebra.jpg')
temp = pixelateImage(temp, 7,10)

cv2.imshow('Zebra',temp)
cv2.waitKey(0)