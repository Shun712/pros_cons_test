import imp
import cv2
import numpy as np

# ①「milkdrop.bmp」を読み込み、cv2.imread()を用いて表示
img = cv2.imread('milkdrop.bmp')
cv2.imshow('OpenCV', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ②白色領域(ミルククラウン)とそれ以外の2値画像を作成
img_mono = cv2.imread('milkdrop.bmp', 0)
threshold = 165
ret, img_thresh = cv2.threshold(img_mono, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow("img_th", img_thresh)
cv2.waitKey()
cv2.destroyAllWindows()