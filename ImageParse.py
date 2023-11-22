import numpy as np
import cv2

def imageToGrayScale(path):
    image = cv2.imread(path)
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    return gray

def pixelateImage(image, dw, dh):
    height, width = image.shape[:2]
    ph = int(height / dh)
    pw = int(width / dw)
    pixelate = cv2.resize(image, (pw, ph), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(pixelate, (width, height), interpolation=cv2.INTER_NEAREST)
    return output

def thresholdImage(image,t1,t2):
    _, t = cv2.threshold(image,t1,t2,cv2.THRESH_BINARY_INV)
    return t

temp = imageToGrayScale('Zebra.jpg')
temp = pixelateImage(temp, 7,10)


cv2.imshow('Zebra',temp)
cv2.waitKey(0)

