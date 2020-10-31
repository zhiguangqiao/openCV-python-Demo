#!/usr/bin/env python3

'''
高通滤波器
两个自定义卷积 实现高通滤波，分别为 3x3核 和 5x5核
结果证明 原图 减去 高斯模糊后的图 高通滤波效果更好

原图 - GaussianBlur 就是高通滤波器
GaussianBlur 就是典型的 低通滤波器
'''
import cv2
import numpy as np

from scipy import ndimage

kernel_3x3 = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
kernel_5x5 = np.array([[-1, -1, -1, -1, -1], [-1, 1, 2, 1, -1], [-1, 2, 4, 2, -1], [-1, 1, 2, 1, -1], [-1, -1, -1, -1, -1]])


img = cv2.imread('./OIP.jpeg', 0)

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

blurred = cv2.GaussianBlur(img, (11, 11), 0)

g_hpf = img - blurred

cv2.imshow('3x3', k3)
cv2.imshow('5x5', k5)

cv2.imshow('img', img)
cv2.imshow('blurred', blurred)
cv2.imshow('g_hpf', g_hpf)
cv2.waitKey(0)
cv2.destroyAllWindows
