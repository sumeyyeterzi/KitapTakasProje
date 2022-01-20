import cv2
import numpy as np 
import os 
path ='ImagesQuery'
orb= cv2.ORB_create(nfeatures=1000)

#### Import  Images
images = []
classNames= []
myList = os.listdir(path)
print('Total Classes Detected',len(myList))
for cl in myList:
  imgCur = cv2.imread(f'{path}/{cl}',0)
  images.append(imgCur)
  classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findDes(images):
  desList= []
  for img in images:
    kp,des = orb.detectAndCompute(img, None)
    desList.append(des)
    return desList

desList = findDes(images)
print(len(desList))

cap = cv2.PictureCapture(0)
while True:
  success, img2 =cap.read()
  imgOriginal =img2.copy()
  img2= cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
  
  cv2.imshow('img2',imgOriginal)
  cv2.waitKey(1)
  #cv2.destroyAllWindows()


#bf = cv2.BFMatcher()
#matches = bf.knnMatch(des1, des2,k=2)
#good =[]
#for  m,n in matches: 
  #  if m.distance <0.75*n.distance:
     #   good.append([m])
      #  print(len(good))    
      #  img3=cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
      
#cv2.imshow('Kp1',imgKp1)
#cv2.imshow('Kp2',imgKp2)

#cv2.imshow('img1',img1)
#cv2.imshow('img2',img2)
#cv2.imshow('img3',img3)

#cv2.waitKey()
#cv2.destroyAllWindows()