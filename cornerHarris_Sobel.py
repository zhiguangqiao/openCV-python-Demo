import cv2
import numpy as np

img = cv2.imread('./meituan.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
print(dst.max())
print(dst)
img[dst > 0.01 * dst.max()] = [0, 0, 255]
cv2.imshow('corners', dst)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows