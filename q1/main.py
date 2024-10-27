from PIL import Image, ImageEnhance, ImageOps
from pytesseract import pytesseract 
import cv2
import numpy as np

def grayscaler():
    img = Image.open("figs/car.jpg")
    img = img.resize((img.width * 15, img.height * 15))
    img = img.convert('L')
    img = img.point(lambda x: 0 if x < 50 else 255, '1')
    img.save("figs/enhanced-car.jpg")
    
def extract_text():
    img = Image.open("figs/enhanced-car.jpg") 

    text = pytesseract.image_to_string(img) 

    print("text found: ", text[:-1])

grayscaler()
extract_text()
