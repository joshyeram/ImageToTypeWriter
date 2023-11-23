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
    _, t = cv2.threshold(image,t1,t2,cv2.THRESH_BINARY)
    return t

def resizeImageScale(image, scale):
    height, width = image.shape[:2]
    dw = width * scale
    dh = height * scale
    resize = cv2.resize(image, (dw, dh), interpolation=cv2.INTER_LINEAR)
    return resize

def resizeImage(image, w, h):
    height, width = image.shape[:2]
    dw = width - (width % w)
    dh = height - (height % h)
    resize = cv2.resize(image, (dw, dh), interpolation=cv2.INTER_LINEAR)
    return resize

