import cv2 
import numpy as np

from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd="C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"

kaynak=""

def metinOku(resim_yolu):
    image=cv2.imread(resim_yolu)

    image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


    kernel=np.ones((1,1),np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    image=cv2.dilate(image,kernel,iterations=1)

  
    image=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,31,2)
    cv2.imwrite(kaynak+'temizlenmisResim.png',image)

    sonuc=pytesseract.image_to_string(Image.open(kaynak+'temizlenmisResim.png'),lang='tur')

    return sonuc









temizMetin = metinOku('resim3.png').replace("&","₺")



print(temizMetin)




