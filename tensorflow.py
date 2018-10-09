import cv2
import tensorflow as tf

image = cv2.imread('jas.png',0)

cv2.imshow('image',image)
cv2.imwrite('jaswhite.png',image)

cv2.waitKey(0)
cv2.destroyAllWindows()