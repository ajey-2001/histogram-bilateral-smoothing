import cv2
import numpy as np

def import_img():
    img = cv2.imread('smooth_test.png')
    return img

def bilateral_blur(img):
    bilateral = cv2.bilateralFilter(img, 25, 100, 100)
    comp = np.hstack((img,bilateral))
    cv2.imshow("Smoothing comparison",comp)
    cv2.waitKey()

IMG=import_img()
bilateral_blur(IMG)