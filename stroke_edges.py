'''
边缘检测

'''
import cv2
import numpy as np

from scipy import ndimage

def stroke_edges(src, dst, blurKsize, edgeKsize):
    if blurKsize >= 3:
        bluredSrc = cv2.medianBlur(src, blurKsize)
        graySrc = cv2.cvtColor(bluredSrc, cv2.COLOR_RGB2GRAY)
    else:
        graySrc = cv2.cvtColor(src, cv2.COLOR_RGB2GRAY)
    cv2.Laplacian(graySrc, cv2.CV_8U, graySrc, ksize=edgeKsize)

    normalizedInverseAlpha = (1.0/255) * (255 - graySrc)
    channels = cv2.split(src)
    for channel in channels:
        channel[:] = channel * normalizedInverseAlpha
    cv2.merge(channels, dst)
    return graySrc

img = cv2.imread('./OIP.jpeg')
cv2.imshow('src', img)
image_edge = stroke_edges(img, img, 5, 3)
cv2.imshow('edge', image_edge)
cv2.imshow('dst', img)
cv2.waitKey(0)
cv2.destroyAllWindows

