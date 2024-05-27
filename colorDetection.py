import imutils
import cv2

####for Phone in blue
##redLower = (101,101,90)         
##redUpper = (121,203,191)

####for a flower box
##redLower = (124,49,79)       
##redUpper = (179,255,255)

###for (green balm)
##redLower = (68,41,75)
##redUpper = (84,188,139)

###for face
##redLower = (0,23,38)
##redUpper = (61,214,146)

###for Hit
##redLower = (124,49,79)       
##redUpper = (179,255,255)

###for Green T-shirt
##redLower = (58,206,0)       
##redUpper = (100,255,255)

#for Light source
redLower = (0,0,255)       
redUpper = (0,0,255)

camera = cv2.VideoCapture(0)

while True:
    
    (grabbed, frame) = camera.read()

    frame = imutils.resize(frame, width = 1000)

    blurred = cv2.GaussianBlur(frame, (11, 11), 0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)


    mask = cv2.inRange(hsv, redLower, redUpper)
    mask = cv2.erode(mask,None, iterations = 2)
    mask = cv2.dilate(mask,None, iterations = 2)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    center = None

    if len(cnts) > 0:
        c = max(cnts, key = cv2.contourArea)
        ((x,y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m10"] / M["m00"]))
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius),(0, 255, 255), -1)
            print(center, radius)
            if radius > 250:
                 print("stop")
            else:
                if(center[0]<150):
                    print("Right")
                elif(center[0]>450):
                    print("Left")
                elif(radius<250):
                    print("Front")
                else:
                    print("Stop")
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()        
