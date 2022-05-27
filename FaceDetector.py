#Random range numbers.
from random import randrange

#OpenCV library.
import cv2

#Load pre-trained frontalface data.
trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

'''

#This one is for random or many images.

#Choose any image.
random_image=cv2.imread('iAm.jpg')

#Covert to greyscale.
greyscale_image=cv2.cvtColor(random_image,cv2.COLOR_BGR2GRAY)

#Detect faces.
face_directions=trained_face_data.detectMultiScale(greyscale_image)

#Wrap faces with rectangles.
for(x,y,w,h) in face_directions:
    cv2.rectangle(random_image,(x,y),(x+w,y+h),(0,randrange(129,256),0),2)

#Shows the image with faces.
cv2.imshow('face detector app',random_image)

#Apply this so that everything work.
cv2.waitKey()

'''

# '''

#Live video capture.
live_webcam_video=cv2.VideoCapture(0)

#loop forever over frames.
while True:

    #read the current frame.
    successful_frame_read,frame=live_webcam_video.read()

    #Convert to greyscale.
    greyscale_webcam=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Detect faces.
    face_directions=trained_face_data.detectMultiScale(greyscale_webcam)

    #Wrap faces with rectangles.
    for(x,y,w,h) in face_directions:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,randrange(129,256),0),2)

    #Shows the image with faces.
    cv2.imshow('Face Detector App (Press Q to quit!)',frame)

    #Apply this so that everything work.
    key=cv2.waitKey(1)

    #Press Q or q to quit.
    if key==81 or key==113:
        break

#Release the VideoCapture object.
live_webcam_video.release()

#Everything worked perfectly.
print('Code Completed!')

# '''