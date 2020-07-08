import cv2

color = (255, 255, 0)
#add our cascade
facecascade = cv2.CascadeClassifier("resources/cascade.xml")
#read the imaage with face
img = cv2.imread("resources/faces.png")
#resize the image
imResize = cv2.resize(img, (600,400))
#convert to grayscale
imgGray = cv2.cvtColor(imResize, cv2.COLOR_BGR2GRAY)
#find the faces in the image
#define the scale factor 
#define the miminum neighbor
face = facecascade.detectMultiScale(imgGray,1.1, 4)
#create a ounding box of across the detected images
#looping over every single image
#startimg point(x ,y)
#corner points(w , h)
for (x, y, w ,h) in face:
    #draw  bounding box
    cv2.rectangle(imResize, (x, y), (x+w, y+h), color, 2)
    #input text "face"
    cv2.putText(imResize, "face", (x, y-5), cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,color,1 )
cv2.imshow("Resized", imResize)
cv2.waitKey(0)




