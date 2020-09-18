#BY Asad Qadri
#To read text from images using pytesseract library

import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

import cv2

img =cv2.imread('1.png')	#can read different formats such as png, jpg, jpeg

cv2.imshow("Sample Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(img)

print(text)