# -*- coding:utf-8 -*-
# 展示一张图片
import cv2

img = cv2.imread("images/snail.jpeg")
cv2.imshow("蜗牛🐌", img)

cv2.waitKey(0)
cv2.destroyAllWindows()