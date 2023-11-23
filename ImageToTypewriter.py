from ImageParse import *
from constants import *
from comparators import *



temp = imageToGrayScale('Zebra.jpg')
temp = thresholdImage(temp,80,255)
temp = resizeImageScale(temp, 3)
temp = resizeImage(temp, fw, fh)
temp = pixelateImage(temp, fw, fh)
cv2.imshow('Zebra',temp)
cv2.waitKey(0)