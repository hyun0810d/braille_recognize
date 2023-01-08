import cv2
img=cv2.imread("a.jpg",cv2.IMREAD_GRAYSCALE)
dst=cv2.resize(img,(400,500))
ret,binary=cv2.threshold(dst,200,255,cv2.THRESH_BINARY)
cv2.imshow('img',dst)
cv2.imshow('binary',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
