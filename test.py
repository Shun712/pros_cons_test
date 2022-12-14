import cv2
import numpy as np

# ①「milkdrop.bmp」を読み込み、cv2.imshow()を用いて表示
img_origin = cv2.imread('milkdrop.bmp')
cv2.imshow('ImageOrigin', img_origin)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ②白色領域(ミルククラウン)とそれ以外の2値画像を作成
img_binary = cv2.imread('milkdrop.bmp', 0)
threshold = 134
img_thresh = cv2.threshold(img_binary, threshold, 255, cv2.THRESH_BINARY)[1]

# ③作成した2値画像をもとに、白色領域（ミルククラウン）の輪郭を抽出
contours = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
contour = max(contours, key=lambda x: cv2.contourArea(x))

# ④抽出した領域を用いて、ミルククラウン領域とそれ以外を分けたmask画像を作成
mask = np.zeros_like(img_thresh)
result = cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
cv2.imwrite("mask.bmp", result)

# ⑤ミルククラウン領域のみを、cv2.imshow()を用いて表示
img_mask = cv2.imread("mask.bmp")
milkcrown = cv2.bitwise_and(img_origin, img_mask)
cv2.imshow("ImageMilkcrown", milkcrown)
cv2.waitKey(0)
cv2.destroyAllWindows()
