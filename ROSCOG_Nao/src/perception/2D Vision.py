''' 
ROSCOG MODULE: PERCEPTION  | SUBMODULE: VISION | MICROMODULE: 2D VISION
                                                                        
              ,----..                  A7         ,----..                
,-.----.     /   /   \   .--.--.     ,----..     /   /   \    ,----..    
\    /  \   /   .     : /  /    '.  /   /   \   /   .     :  /   /   \   
;   :    \ .   /   ;.  \  :  /`. / |   :     : .   /   ;.  \|   :     :  
|   | .\ :.   ;   /  ` ;  |  |--`  .   |  ;. /.   ;   /  ` ;.   |  ;. /  
.   : |: |;   |  ; \ ; |  :  ;_    .   ; /--` ;   |  ; \ ; |.   ; /--`   
|   |  \ :|   :  | ; | '\  \    `. ;   | ;    |   :  | ; | ';   | ;  __  
|   : .  /.   |  ' ' ' : `----.   \|   : |    .   |  ' ' ' :|   : |.' .' 
;   | |  \'   ;  \; /  | __ \  \  |.   | '___ '   ;  \; /  |.   | '_.' : 
|   | ;\  \\   \  ',  / /  /`--'  /'   ; : .'| \   \  ',  / '   ; : \  | 
:   ' | \.' ;   :    / '--'.     / '   | '/  :  ;   :    /  '   | '/  .' 
:   : :-'    \   \ .'    `--'---'  |   :    /    \   \ .'   |   :    /   
|   |.'       `---`                 \   \ .'      `---`      \   \ .'    
`---'                                `---`                    `---`      
   2017                                          A7MD1337                    

:;~... .   .  ROS Cognitive Architecture for AGI .     .     .  .  ~,;:; 
------------------------------------------------------------------------

Vision Processes:

== 2D Vision ==

- Image Segmentation:

1. Background Subtraction Model:
~BackgroundSubtractorMOG2: 
https://docs.opencv.org/3.3.0/d1/dc5/tutorial_background_subtraction.html
~Foreground Extraction

2. Object Detection:
~Thresholding
~Edge Detection
~Texture Analysis
~Tracking and Region Growing
~Geometric Analysis (size, shape)

'''
########################################################################
#		Perception: Vision Module - using OpenCV
# Done: 
# (currently only recognizes faces in images. 
# BG/FG segmentation

# To be Done:
# have to set metacognition module to know vision input dimensions)

#######################################################################
#
#---------------Importing libraries and dependencies-------------------

import cv2 # import OpenCV
import sys # 
import numpy as np # for BGFB

video_capture = cv2.VideoCapture(0) # asgn variable to cv stream AND set camera device

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Display the resulting frame
    cv2.imshow('Vision Module', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): # press q to quit /make message
        break

video_capture.release()
cv2.destroyAllWindows()

#---------------Background Segmentation--------------------------------

'''
BackgroundSubtractorMOG2

It is also a Gaussian Mixture-based Background/Foreground Segmentation Algorithm. It is based on two papers by Z.Zivkovic, "Improved adaptive Gausian mixture model for background subtraction" in 2004 and "Efficient Adaptive Density Estimation per Image Pixel for the Task of Background Subtraction" in 2006. 
'''

cap = cv2.VideoCapture('vtest.avi')
fgbg = cv2.createBackgroundSubtractorMOG2()
while(1):
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()

#--------------- facial recognition --------------------------------

cascPath = sys.argv[1] # /traverse directory to memory>haarcascades
faceCascade = cv2.CascadeClassifier(cascPath)

facerec = '0'

if facrec = '1':

# convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# /categories: currently only faces supported
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )
#   objects = 

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)



# When everything is done, release the capture



'''
load camera and display in gray

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
'''
##
