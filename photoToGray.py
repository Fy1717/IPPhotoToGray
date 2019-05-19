import cv2



img= cv2.imread("fyy.jpg",0)

cv2.imshow("fyy",img)

k=cv2.waitKey(0) & 0XFF

if k == 27:
    cv2.destroyAllWindows()
elif k==ord("s"):
    cv2.imwrite("C:\\Users\\frkny\\Desktop\\grifyy.jpg",img)
