import cv2
import numpy as np
print("package installed")

# #read the image
# img = cv2.imread("resources/img.jpg")
# #show the image
# cv2.imshow("read image",img)
# cv2.waitKey(0)


# reading the video
# cap = cv2.VideoCapture("resources/girl.MOV")
# #display the video
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video",img)
#     if cv2.waitkey(1) & 0xFF == ord("q"):
#         break

# #reading and displaying the webcam
# webcam = cv2.VideoCapture(0)
# #define the width and height
# webcam.set(3,640)
# webcam.set(4,480)
# #display the webcamwhile True:
#     success, img = webcam.read()
#     cv2.imshow("webcam",img)
#     if cv2.waitkey(1) & 0xFF == ord("q"):
#         break

#converting image to grayscale
img = cv2.imread("resources/img.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", imgGray)
cv2.waitKey(0)
#edge detection 1
# Using the Canny filter to get contours
edges = cv2.Canny(imgGray, 20, 30)
# Using the Canny filter with different parameters
edges_high_thresh = cv2.Canny(imgGray, 60, 120)
# Stacking the images to print them together
# For comparison
images = np.hstack((imgGray, edges, edges_high_thresh))

# Display the resulting frame
cv2.imshow('img', canny_images)

#eroding an image
img = cv2.imread("resources/img.jpg")
cv2.imshow("image", img)
cv2.waitKey(0)
kernel = 
imgErode = cv2.erode(img, kernel, iterations=3)
cv2.imshow("eroded", imgErode)
cv2.waitKey(0)

img = cv2.imread("Resources/img.jpg")

cv2.imshow("Image",img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (3,9), 0)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)


cv2.waitKey(0)

#edge detection 2
img = cv2.imread("Resources/img.jpg")
mycanny = cv2.canny(img,100,100)



