import cv2
import numpy as np




  

yol = r'ornek2.jpg'

kitapresmi = cv2.imread(yol)

grikitapresmi = cv2.cvtColor(kitapresmi, cv2.COLOR_BGR2GRAY)

karsilastir = cv2.imread('kitap1.jpg',0)

w, h = karsilastir.shape[::-1]

# Perform match operations.
res = cv2.matchTemplate(grikitapresmi,karsilastir,cv2.TM_CCOEFF_NORMED)

threshold = 0.8

# Store the coordinates of matched area in a numpy array
loc = np.where( res >= threshold)

# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
    cv2.rectangle(grikitapresmi, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)


print(loc)
# Show the final image with the matched area.
cv2.imshow('Sonuc',karsilastir)
cv2.waitKey()
cv2.destroyAllWindows()