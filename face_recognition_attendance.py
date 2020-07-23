# import Libraries
import  face_recognition as fe
import cv2
import numpy as np

#Add images

imgelon=fe.load_image_file(r"C:\Users\Lenovo\Desktop\FACE RECOGNITION + ATTENDANCE PROJECT\Images\Elon_Musk.jpg")
imgtest=fe.load_image_file(r"C:\Users\Lenovo\Desktop\FACE RECOGNITION + ATTENDANCE PROJECT\Images\elon.jfif")

imgelon=cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

#Show images untill press enter 

cv2.imshow("IMAGE_ELON",imgelon)
cv2.imshow("IMAGE_TEST",imgtest)
while True:
    k=cv2.waitKey(1)
    if k==13:
        break
cv2.destroyAllWindows()