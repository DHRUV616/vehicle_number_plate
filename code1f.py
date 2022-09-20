import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
import cv2
import matplotlib.pyplot as plt
import matplotlib.lines as lines
import pytesseract

image = cv2.imread('C:/Users/dhruv/Downloads/car12.png') 
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)   

def plot_images(img1, img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)     
    ax1.imshow(img1)
    ax1.set(title="Normal Image")   

    ax2 = fig.add_subplot(122)    
    ax2.imshow(img2, cmap='gray')
    ax2.set(title="Grayscale Image")
    #plt.show()


plot_images(image,gray)

blur = cv2.bilateralFilter(gray, 10, 15, 15)

def plot_images(img1, img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)     # one row two columns and targeting the first column
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Grayscale Image")   # adding title

    ax2 = fig.add_subplot(122)    # one row two columns and targeting the second column
    ax2.imshow(img2, cmap='gray')
    ax2.set(title="Grayscale Blurred Image")
    #plt.show()


plot_images(gray, blur)

edges = cv2.Canny(blur, 15, 100)

def plot_images(img1, img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)     # one row two columns and targeting the first column
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Grayscale Blurred Image")   # adding title

    ax2 = fig.add_subplot(122)     # one row two columns and targeting the second column
    ax2.imshow(img2, cmap='gray')
    ax2.set(title="Image with Edges")
    #plt.show()

plot_images(blur, edges)

counters,new = cv2.findContours(edges.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

image_copy = image.copy() 

cv2.drawContours(image_copy,counters,-1,(255,0,0),2)

def plot_image(img1,img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Image with edges")

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2,cmap='gray')
    ax2.set(title="Image with contour")
    #plt.show()
      
plot_image(edges,image_copy)

print(len(counters))

counters_new = sorted(counters,key=cv2.contourArea,reverse=True)[:20]

image_copy = image.copy()

cv2.drawContours(image_copy,counters_new,-1,(255,0,255),2)

def plot_image(img1,img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Normal Image")

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2,cmap='gray')
    ax2.set(title="Sorted Contour Image")
    #plt.show()

plot_image(image,image_copy)

plate = None

for counter in counters_new:
    perimeter = cv2.arcLength(counter,True)
    edges_count = cv2.approxPolyDP(counter,0.01*perimeter,True)

    if len(edges_count)==4:                  
       print("in")
       x,y,w,z = cv2.boundingRect(counter) 
       plate = image[y:y+z,x:x+w]
       break

type(plate)

cv2.imwrite("plate.png", plate)

def plot_images(img1):
    fig = plt.figure(figsize=[10,10])
    ax1 = fig.add_subplot(111)    
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Plate Image")
    #plt.show()

plot_images(plate)

import pytesseract
from PIL import Image
value =Image.open('C:/Users/dhruv/OneDrive/Desktop/plate.png')
text=pytesseract.image_to_string(value,config='')
print("the number on the plate is\n\n")
print(text)


def find_contours(dimensions, img) :
    cntrs, _ = cv2.findContours(img.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    lower_width = dimensions[0]
    upper_width = dimensions[1]
    lower_height = dimensions[2]
    upper_height = dimensions[3]
    cntrs = sorted(cntrs, key=cv2.contourArea, reverse=True)[:15]
    
    ci = cv2.imread('contour.jpg')
    
    x_cntr_list = []
    target_contours = []
    img_res = []
    for cntr in cntrs :
        intX, intY, intWidth, intHeight = cv2.boundingRect(cntr)
        
        if intWidth > lower_width and intWidth < upper_width and intHeight > lower_height and intHeight < upper_height :
            x_cntr_list.append(intX) 
            char_copy = np.zeros((44,24))
            char = img[intY:intY+intHeight, intX:intX+intWidth]
            char = cv2.resize(char, (20, 40))
            cv2.rectangle(ci, (intX,intY), (intWidth+intX, intY+intHeight), (50,21,200), 2)
            plt.imshow(ci, cmap='gray')
            char = cv2.subtract(255, char)
            char_copy[2:42, 2:22] = char
            char_copy[0:2, :] = 0
            char_copy[:, 0:2] = 0
            char_copy[42:44, :] = 0
            char_copy[:, 22:24] = 0
            img_res.append(char_copy)
    plt.show()
    indices = sorted(range(len(x_cntr_list)), key=lambda k: x_cntr_list[k])
    img_res_copy = []
    for idx in indices:
        img_res_copy.append(img_res[idx])
    img_res = np.array(img_res_copy)

    return img_res

def segment_characters(image) :
    img_lp = cv2.resize(image, (333, 75))
    img_gray_lp = cv2.cvtColor(img_lp, cv2.COLOR_BGR2GRAY)
    _, img_binary_lp = cv2.threshold(img_gray_lp, 200, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    img_binary_lp = cv2.erode(img_binary_lp, (3,3))
    img_binary_lp = cv2.dilate(img_binary_lp, (3,3))

    LP_WIDTH = img_binary_lp.shape[0]
    LP_HEIGHT = img_binary_lp.shape[1]
    img_binary_lp[0:3,:] = 255
    img_binary_lp[:,0:3] = 255
    img_binary_lp[72:75,:] = 255
    img_binary_lp[:,330:333] = 255

   
    dimensions = [LP_WIDTH/6,
                       LP_WIDTH/2,
                       LP_HEIGHT/10,
                       2*LP_HEIGHT/3]
    plt.imshow(img_binary_lp, cmap='gray')
    #plt.show()
    cv2.imwrite('contour.jpg',img_binary_lp)

    #getting contours
    char_list = find_contours(dimensions, img_binary_lp)

    return char_list
    
char = segment_characters(plate)
    
for i in range(10):
  plt.subplot(1, 10, i+1)
  plt.imshow(char[i], cmap='gray')
  plt.axis('off')
  plt.show()
