import cv2

import pytesseract


pytesseract.pytesseract.tesseract_cmd = 'D:\Tesseract-OCR\\tesseract.exe'
#pytesseract.pytesseract.tesseract_cmd = 'D:\python\lib\site-packages\pytesseract\pytesseract.py'

# read the image
image = cv2.imread('image.png')

# pre-processing the image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 3)

# perform OCR
text = pytesseract.image_to_string(gray, lang = 'eng',config='--psm 11')


print(text)

f= open("amazonproduct.txt","w+")
f.write(text)