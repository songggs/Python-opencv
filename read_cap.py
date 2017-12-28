import cv2
import numpy
import matplotlib.pyplot as plt

#打开摄像头
cap = cv2.VideoCapture(0)

while(1):
    ret, frame = cap.read()
    cv2.imshow("capture", frame)
    #等待1s，q键退出
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

#释放摄像头，关闭所有窗口
cap.release()
cv2.destroyAllWindows()
