#!/usr/bin/env python3

'''
边缘检测
canny 函数
'''
import cv2
import numpy as np

img = cv2.imread('./meituan.jpg', 0)
cv2.imwrite('canny.jpg', cv2.Canny(img, 200, 300))
cv2.imshow('canny.jpg', cv2.imread('canny.jpg'))
cv2.waitKey(0)
cv2.destroyAllWindows