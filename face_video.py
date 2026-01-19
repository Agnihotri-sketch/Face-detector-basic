import cv2
import cv2.data

modelPath = cv2.data.haarcascades +"haarcascade_frontalface_default.xml"
model =cv2.CascadeClassifier(modelPath)

camera = cv2.VideoCapture(0)
while True:
    status, image = camera.read()
    faces = model.detectMultiScale(image, 1.3, 3)

    for face in faces:
        x,y,w,h = face
        image = cv2.rectangle(image,(x,y),(x+w, y+h),(252,236),3)
        image = cv2.putText(image,"Face Detected",(x,y-30),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,10),3)

    cv2.imshow("Faces", image)
    if cv2.waitKey(1) ==97:
        break
