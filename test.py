import cv2
import numpy as np

# ①「milkdrop.bmp」を読み込み、cv2.imshow()を用いて表示
img_origin = cv2.imread('milkdrop.bmp')
cv2.imshow('OpenCV', img_origin)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ②白色領域(ミルククラウン)とそれ以外の2値画像を作成
img_binary = cv2.imread('milkdrop.bmp', 0)
threshold = 135
ret, img_thresh = cv2.threshold(img_binary, threshold, 255, cv2.THRESH_BINARY)
cv2.imshow("img_th", img_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ③作成した2値画像をもとに、白色領域（ミルククラウン）の輪郭を抽出
contours = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
contour = max(contours, key=lambda x: cv2.contourArea(x))
