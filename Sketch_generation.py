import cv2
img= cv2.imread("E:\pic\clz\WhatsApp Image 2021-10-26 at 6.43.24 PM.jpeg")
gr= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(gr)
blur = cv2.GaussianBlur(invert,(21,21),0)
invertblur = cv2.bitwise_not(blur)
sketch= cv2.divide(gr,invertblur,scale=250.1000)


cv2.imshow("original",img)
cv2.imshow("Sketch",sketch)
cv2.waitKey(0)