import cv2
import imutils

# img = cv2.imread('example2.jpg')
# cv2.imshow('Display Name', img)
# cv2.waitKey(0)

img = cv2.imread('example.jpg')

(w,h,d) = img.shape
print("width{}, height{}, depth{}".format(w,h,d))

img = imutils.resize(img, width=500)
cv2.imshow('picture', img)
(w, h, d) = img.shape
print("width{}, height{}, depth{}".format(w,h,d))
cv2.waitKey(0)
