import numpy as np
from constants import *
# Every single compare emthod must take two np array of the same size.
# It will return a value from 0 to 1 to depict its similarity
# We will use this value to sort later
def compareSimple(img1, img2):
    sim = 0
    if(img1.shape is not img2.shape):
        print("The images must have the same shape to compare")
        exit()
    height, width = image.shape[:2]
    for h in height:
        for w in width:
            sim += abs(img1[h][w]-img2[h][w])
    total = fw * fh * 255
    return sim/total