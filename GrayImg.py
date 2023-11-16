import cv2
import matplotlib

img=cv2.imread("E://openCV_images/girl5.jpg")
r=cv2.resize(img,(700,500))
cv2.imshow("img",r)
cv2.waitKey(0)

grayImg=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
r2=cv2.resize(grayImg,(700,500))
#cv2.imwrite("E://openCV_images/GrayImg.jpg",grayImg)
cv2.imshow("img",r2)

cv2.waitKey(0)
cv2.destroyAllWindows()