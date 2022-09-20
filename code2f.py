import cv2
# Implementation of matplotlib function
import matplotlib.pyplot as plt
import matplotlib.lines as lines

img = cv2.imread('C:/Users/dhruv/Downloads/car10.png') #imread is used to read the image
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          #cvtColor is used to cnage the color
                                                #COLOR_BGR2GRAY is used to convert into gray image
           # RED = BLUE #BROWN = BROWN #BLUE = BROWN #SKY BLUE = YELLOW  #WHITE = WHITE #LIGHT BLACK = LIGHT BROWN  #GRAY = GARY

def plot_images(img1,img2):
    fig = plt.figure(figsize=[20,20]) #20,20 is the axis number represent
    ax1 = fig.add_subplot(121)        #subplot is used to large or small the image larger the subplot value smalller the size
    ax1.imshow(img1)                   #imshow is used to insert the image into ax1 and disply data ino image
    ax1.set(title="Normal image")              
    ax2 = fig.add_subplot(122)
    ax2.imshow(img2,cmap='gray') #cmap is the colormap instance or registered colormap name .IT show the image as it is before but
                                  # turns into gray if we donot use the cmap we get the yellish part at the boundry of image 
    ax2.set(title="GrayScale image")
    #plt.show() #when imshow function does not display the image try adding plt.show at the end of the image it will display image
    
plot_images(img,gray)

blur = cv2.bilateralFilter(gray,10,100,100)
                           #(gray = is the image
                           # 10 jo h wo boundary k pixel ko blur karti h jitna gayda 10 value utna gyada blur
                           # 100 is used to blur the centre part of image or you can say that main image
                           # 100 is used to get pixel mixed higher the 100 value higher the pixel mixed
                           # note that filter is not used to blur the image but it is used to filter the image

def plot_images(img1,img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img,cmap='gray')
    ax1.set(title="GrayScale Image")

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2,cmap='gray')
    ax2.set(title="GrayScale Blurred Image")
    #plt.show()
    
plot_images(gray,blur)

edges = cv2.Canny(blur,15,100) #cv2.Canny is used to to detec the edges of python
                               #it first take image,then its aperature size (min value and max value)
                              #jitni kam min value hogi utni gyada hi edge detect hogi
                              #jitni gyada max value hogi utni kam edge detect hogi

def plot_images(img1,img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Blurred images")

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2,cmap='gray')
    ax2.set(title="Image with Edges")
    #plt.show()
            
plot_images(blur,edges)

#counters mean the line joining across all the points along the boundry of image that have same intensity
# matlab counter line ko points ko jjoin karke line bana deta h us image k charo taraf  us image k kuch points honge unko join karta h
#findCounters extract the counter of image


                                 #MAIN MOTIVE OF THIS PROGRAM


counters,new = cv2.findContours(edges.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
                        #isme counter,new likha h us sajah gyada tar 2 hi vaiable aate h gyada tar time
                        # ex like jo book se dekha h countours,heirarchy #findContours ki speeling dhang se yad rakhna
                        # First one is source image i.e jo edge image hoti h
                        # second is contour retrieval mode matlab counter matlab line us object ya kan sakte h us object ki boundary
                          #to ye jo outer object hoga uski boundry ko hi detect karegi 
                        # third one is countour approximation mode matlab jaise ek image h uski boundary or ek edge p bahout point
                           #honge jinko join karke jo boundry line bani manlo ek square object h uski counter banane k liye bas 4
                            #boundary p jo point h unki se hi image ban gygi ye bhi ho sakta h us line p boundry k alawa or bhi point
                              #ho jp ye chiz points ko jitne kam ho sake utne kam karta h taki image counter ya image bhi ban gaye or
                                #points bhi kam se kam store karne pade

image_copy = img.copy() # image ko copy karta h

                           #DRAW COUNTERS

cv2.drawContours(image_copy,counters,-1,(255,0,0),2)

                           # first input is image
                           # second input is counter variable that takes the definston which detect the image
                           # -1 represent that to draw the all counter

                           #(x1,x2,x3) ye wo coordinted h color k har coordinates ek color represnt karti h ki kisi bhi conter ki
                              # boundry detect ho rahi h uska color kase ho

                              # (0,0,0) represent black color of boundry
                              # (0,255,0) represent light green color of boundry
                              # (0,0,255) represent blue color of boundry
                              # (255,0,0) represent red color of boundry
                              # (0,255,255) represent light blue color of boundry
                              # (255,0,255) represent purple color of boundry
                              # (255,255,0) represent yellow color of boundry
                              # (255,255,255) represent white color of boundry


                           
                           # 2 represent ki jo boundry kisi bhi object ki ban rahi h uski thckness kitni hot matlab boundry line kitni
                                  # moti ya patli honi chiaye jitni kam value utni kam thickness


def plot_image(img1,img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Normal Image")

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2,cmap='gray')
    ax2.set(title="Image with contour")
    #plt.show()
      
plot_image(img,image_copy)

print(len(counters))


                                    # SORTING THE COUNTER
                                    
counters_new = sorted(counters,key=cv2.contourArea,reverse=True)[:20]

image_copy = img.copy()

cv2.drawContours(image_copy,counters_new,-1,(255,0,255),2)

def plot_image(img1,img2):
    fig = plt.figure(figsize=[20,20])
    ax1 = fig.add_subplot(121)
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Normal Image")

    ax2 = fig.add_subplot(122)
    ax2.imshow(img2,cmap='gray')
    ax2.set(title="Sorted Counter Image")
    #plt.show()

plot_image(img,image_copy)


                                      # PLATE

                            

plate = None

for counter in counters_new:
    perimeter = cv2.arcLength(counter,True)
                                                 #It specifies whether a image is closed figure or not
    edges_count = cv2.approxPolyDP(counter,0.01*perimeter,True)
                                                 # ye ek tarah se precision deta h ji ek image jisme pahle se counter bane hue h
                                                 # usme shape aache se banane k liye
                                                 #len(edge_count)==4 ka matlab h ki jo hamne contour use karke jo image li h uske agr
                                                 # agr 4 hi cooordinate honge jabhi wo use h aaygi jaise ki plate

    if len(edges_count)==4:                  
       print("in")
       x,y,w,z = cv2.boundingRect(counter) #Iska matlab jo bhi image detect karte h wo mostly rectenguar hoti h ya phr ye
                                            #ye function char coordinates return karti h jo bhi best fit rectengular shape hogi
       plate = img[y:y+z,x:x+w]
       break

type(plate)

cv2.imwrite("plate.png", plate)

def plot_images(img1):
    fig = plt.figure(figsize=[10,10])
    ax1 = fig.add_subplot(111)     # one row two columns and targeting the first column
    ax1.imshow(img1,cmap='gray')
    ax1.set(title="Plate Image")
    plt.show()

plot_images(plate)

char = segment_characters(plate)

for i in range(10):
    plt.subplot(1,10,i+1)
    plt.imshow(char[i],cmap="gray")
    plt.axis('off')
#import pytesseract
#pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#print(pytesseract.image_to_string("plate.png"))


       


