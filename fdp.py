import cv2
# loading camera
cap = cv2.VideoCapture(0)
# loading face data
face_detect = cv2.CascadeClassifier('face1.xml')
eye_detect = cv2.CascadeClassifier('eye1.xml')
print(dir(face_detect))
while cap.isOpened():
    # taking pictures
    status,frame = cap.read() 
    #converting into gray
    grayimg = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    print(grayimg)
    # now we can detect face
    face = face_detect.detectMultiScale(grayimg)
    print(face)
    # rectangle
    for (x,y,w,h) in face:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),4)
            onlyface = frame[y:y+h,x:x+w]
            eye=eye_detect.detectMultiScale(onlyface)
            for (ex,ey,ew,eh) in eye:
                cv2.rectangle(onlyface,(ex,ey),(ex+ew,ey+eh),(255,0,0),2)
    cv2.imshow('face',frame)        
    cv2.imshow('face1',onlyface)
    if cv2.waitKey(10) & 0xff == ord('r'):
        break

# to destroy all windows by imshow
cv2.destroyAllWindows()
# stop camera
cap.release()    