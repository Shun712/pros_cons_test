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

# ④抽出した領域を用いて、ミルククラウン領域とそれ以外を分けたmask画像を作成
out = np.zeros_like(img_thresh)
mask = cv2.drawContours(out, [contour], -1, color=255, thickness=-1)
result = np.where(mask==255, img_thresh, out)
# img_contour = cv2.drawContours(img_thresh, contours, -1, (255, 0, 0), 3)
cv2.imshow("img_edge", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
