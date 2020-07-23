# import Libraries
import  face_recognition as fe
import cv2
import numpy as np

#Add images

imgelon=fe.load_image_file(r"C:\Users\Lenovo\Desktop\FACE RECOGNITION + ATTENDANCE PROJECT\Images\Elon_Musk.jpg")
imgtest=fe.load_image_file(r"C:\Users\Lenovo\Desktop\FACE RECOGNITION + ATTENDANCE PROJECT\Images\elon.jfif")

imgelon=cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
imgtest=cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

#Locate and encode Images patterns

loc_imgelon=fe.face_locations(imgelon)[0]
loc_imgtest=fe.face_locations(imgtest)[0]

encode_imgelon=fe.face_encodings(imgelon)[0]
encode_imgtest=fe.face_encodings(imgtest)[0]

#Draw Rectange on Detected face
cv2.rectangle(imgelon,(loc_imgelon[3],loc_imgelon[0]),(loc_imgelon[1],loc_imgelon[2]),(255,125,134),2)
cv2.rectangle(imgtest,(loc_imgtest[3],loc_imgtest[0]),(loc_imgtest[1],loc_imgtest[2]),(255,125,134),2)

#Show images untill press enter 

cv2.imshow("IMAGE_ELON",imgelon)
cv2.imshow("IMAGE_TEST",imgtest)
while True:
    k=cv2.waitKey(1)
    if k==13:
        break
cv2.destroyAllWindows()