import cv2
import numpy as np

blur_degree = 3
gray_treshold = 230

def read_image():
    pixel_data = np.genfromtxt('figs/input1.txt', skip_header=1, dtype=str)
    array = pixel_data[:, 1::3]
    array = np.char.strip(array, ',')
    array = array.astype(np.uint8)
    cv2.imwrite('figs/image.jpg', array)
    
def grayscaler():
    img = cv2.imread('figs/image.jpg')
    img[img <= gray_treshold] = 0
    img[img > gray_treshold] = 255
    cv2.imwrite('figs/image-grayed.jpg', img)
    
def remove_noise():
    img = cv2.imread('figs/image-grayed.jpg', cv2.IMREAD_GRAYSCALE)
    img = cv2.medianBlur(img, blur_degree)
    cv2.imwrite('figs/image-noise-removed.jpg', img)
    
def star_finder():
    img = cv2.imread('figs/image-noise-removed.jpg', cv2.IMREAD_GRAYSCALE)
    
    edged = cv2.Canny(img, 30, 200)
    cv2.imwrite('figs/image-stars-edged.jpg', edged)
    
    contours, hierarchy = cv2.findContours(edged,  
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
    
    cv2.putText(img, f"count: {len(contours)}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
    
    cv2.rectangle(img, (10, 10), (50, 50), (255, 0, 0), 1)
    rect_scale = (4, 4)
    for i in range(len(contours)):
        print('coordinate:', contours[i][0])
        center = (contours[i][0][0,0],contours[i][0][0,1])
        pt1 = (center[0] - rect_scale[0], center[1] - rect_scale[1])
        pt2 = (center[0] + rect_scale[0], center[1] + rect_scale[1])
        cv2.rectangle(img, pt1, pt2, (255, 0, 0), 1)
        
    cv2.imwrite('figs/image-stars-found.jpg', img)

    
def show_image(img):
    cv2.imshow('stars', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

read_image()
grayscaler()
remove_noise()
star_finder()
