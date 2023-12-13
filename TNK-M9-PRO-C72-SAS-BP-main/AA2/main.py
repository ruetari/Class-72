import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import math
import cvzone

from cvzone.FaceMeshModule import FaceMeshDetector


cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

menuImages = [] 
path = "filters"
pathList = os.listdir(path)
pathList.sort()

for pathImg in pathList:
    img = (cv2.imread(path + "/" + pathImg, cv2.IMREAD_UNCHANGED))
    menuImages.append(img)

menuCount = len(menuImages)

detector = HandDetector(detectionCon=0.8)
faceDetector = FaceMeshDetector(maxFaces=2)

# Create an array of menuChoices

menuChoice = -1

isImageSelected = False


while True:
    success, cameraFeedImg = cap.read()
    cameraFeedImg = cv2.flip(cameraFeedImg, 1)

    wHeight, wWidth, wChannel = cameraFeedImg.shape
    x = 0
    xIncrement = math.floor(wWidth / menuCount)


    handsDetector = detector.findHands(cameraFeedImg, flipType=False)
    hands = handsDetector[0]
    cameraFeedImg = handsDetector[1]

    try:
        if hands:
            hand1 = hands[0]
            lmList1 = hand1["lmList"]  
            indexFingerTop = lmList1[8]
            indexFingerBottom = lmList1[6]
            handType = hand1["type"]

           

            if (indexFingerTop[1] < xIncrement):
                i = 0
                while (xIncrement*i <= wWidth):
                    if (indexFingerTop[0] < xIncrement*i):
                        menuChoice = i-1
                        isImageSelected = True
                        break
                    i = i+1

            if (indexFingerTop[1] > indexFingerBottom[1]):
                isImageSelected = False
                # Set menuChoice at index menuChoice to 1
                

            # Check the hand type is Left and set the menuChoices array to six 0's.
            
            

    except Exception as e:
        print(e)

    cameraFeedImg, faces = faceDetector.findFaceMesh(cameraFeedImg, draw= False)

    try:
        for face in faces: 
            xLoc= face[21][0]
            yLoc= face[21][1]

            if(menuChoice > -1):
                if(isImageSelected): 
                    image = cv2.resize(menuImages[menuChoice],(100, 100))
                    cameraFeedImg= cvzone.overlayPNG(cameraFeedImg, image, [int(indexFingerTop[0]), int(indexFingerTop[1])])
            # Loop throught choice in menuChoices and run following code only if menuChoice at that index has value 1
            
                # Check if menuChoice at index choice is 1 then only show the image
                
            dist = math.dist(face[21], face[251])
            scale = 90
            dx = 0
            dy = 0
            
            # Replace menuChoice with choice
            if(menuChoice == 0):
                scale = 90
                dx = 5
                dy = 40
            if(menuChoice == 1):
                scale = 85
                dx = 5
                dy = 80
            if(menuChoice == 2):
                scale = 55
                dx = 20
                dy = 60
            if(menuChoice == 3):
                scale = 70
                dx = 15
                dy = 30
            if(menuChoice == 4):
                scale = 80
                dx = 10
                dy = 30  
            if(menuChoice == 5):
                scale = 55
                dx = 20
                dy = 40
                
            resizefactor = dist/scale

            XLoc = int(xLoc - (resizefactor*dx))
            YLoc = int(yLoc - (resizefactor * dy))
            
            # Replace menuChoice with choice
            filterImg = cv2.resize(menuImages[menuChoice], (100, 100))
            filterImg = cv2.resize(filterImg, (0, 0), fx = resizefactor, fy = resizefactor)
            
            
            cameraFeedImg= cvzone.overlayPNG(cameraFeedImg, filterImg, [XLoc, YLoc])

    except Exception as e:
            print("Exception", e) 

    try:
        for image in menuImages:
            margin = 20
            image = cv2.resize(image, (xIncrement - margin, xIncrement - margin))
            cameraFeedImg = cvzone.overlayPNG(cameraFeedImg, image, [x, 0])
            x = x + xIncrement
    except:
        print("out of bounds")
   
    cv2.imshow("Face Filter App", cameraFeedImg)
    cv2.waitKey(1)
