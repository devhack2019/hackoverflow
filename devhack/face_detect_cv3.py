import cv2
import sys
import numpy as np
import PIL
from PIL import Image
import os

# Get user supplied values
imagePath = sys.argv[1]
path = imagePath.split('.')
path = path[0]
cascPath = "haarcascade_frontalface_default.xml"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.imread(imagePath)
image2 = image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.21,
    minNeighbors=8,
    minSize=(100,100)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

print("Found {0} faces!".format(len(faces)))

i=1

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    a = np.zeros((h,w,3))
    a = image[y-15:y+h+15, x-15:x+w+15, :]
    a = PIL.Image.fromarray(np.uint8(a))
    a = a.convert('LA') #convert to GrayScale
    a.save(path+"_"+str(i)+".png", "PNG", subsampling=0, quality=100)
    b=cv2.imread(path+"_"+str(i)+".png",1)
    cv2.imwrite(path+"_"+str(i)+".png",b)
    i+=1

    #to draw bounding boxes around found images
    cv2.rectangle(image2, (x, y), (x+w, y+h), (0, 255, 0), 2)


#cv2.imshow("Faces found", image)
cv2.imwrite(path+"_result.jpg", image2)
cv2.waitKey(0)
