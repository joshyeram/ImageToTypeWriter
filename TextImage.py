import numpy as np
import time
from PIL import Image, ImageDraw, ImageFont
import cv2
import os


String = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h I j k l m n o p q r s t u v w x y z 1 2 3 4 5 6 7 8 9 0 ! ? , . \' \" @ # $ % ^ & * ( ) _ + - ="

def createCharacterImage(s, fs):
    width = fs * 100
    height = int(fs + fs/10)
    img = Image.new(mode="RGB", size=(width,height), color='white')
    font = ImageFont.truetype('Courier', fs)
    draw = ImageDraw.Draw(img)
    draw.text((1, 2), s, font=font, fill="black")
    img.save("characters.png")

def parseImageCharacters(s, fs, path):
    image = Image.open(path)
    x = 0
    for c in s:
        if c == " ":
            x += int(fs * .6)
            continue
        cr = (x, 0, x + int(fs * (2/3)), int(fs * (1.1)))
        cC = image.crop(cr)
        #. \' \" @ # $ % ^ & * ( ) _ + - =
        if c == ".":
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/period.png"
        elif c == '\'':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/sq.png"
        elif c == '\"':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/dq.png"
        elif c == '@':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/at.png"
        elif c == '#':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/ht.png"
        elif c == '$':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/dollar.png"
        elif c == '%':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/percent.png"
        elif c == '^':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/crt.png"
        elif c == '&':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/amp.png"
        elif c == '*':
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/ast.png"
        elif c.isupper():
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/upper" + c + '.png' 
        else:
            fileName = "/Users/joshchung/Projects/ImageToTypeWriter/characters/" + c + '.png'
        with open(fileName, 'wb') as f:
            cC.save(f)
        x += int(fs * .6)

def imageToNumpyArrays():
    arrs = []
    for filename in os.listdir("characters/"):
        if filename.endswith(".png"):
            filename = "characters/"+filename
            image = cv2.imread(filename)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            name = filename[11:len(filename)-4]
            arrs.append((gray, name))
    return arrs

createCharacterImage(String, 30)
parseImageCharacters(String, 30, 'characters.png')
print(imageToNumpyArrays())