import numpy as np
from cv2 import cv2
import imutils
import sys
import pytesseract
import pandas as pd
import time

# Path for Tesseract-OCR executable file
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# Arguments for tesseract commands
configr = ('-l eng --oem 1 --psm 3')

class NumberPlateRecognition:

    def __init__(self):
        pass

    def getNumberPlate(self, image):

        numberPlateImage = self.__findNumberPlate__(image)
        numberPlate = pytesseract.image_to_string(numberPlateImage, config=configr)

        return numberPlate

    def __findNumberPlate__(self, image):
        ''' Handles all the pre-processing of image before passing it to Tesseract OCR '''

        resizedImage = imutils.resize(image, width=500)
        grayImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
        filteredImage = cv2.bilateralFilter(grayImage, 11, 17, 17)

        cannyEdges = cv2.Canny(filteredImage, 170, 200)

        contours, _ = cv2.findContours(cannyEdges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        sortedContours = sorted(contours, key=cv2.contourArea, reverse=True)[:30]
        
        NumberPlateCount = 0
        for contour in sortedContours:
            perimeter = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02*perimeter, True)
            if len(approx) == 4:
                NumberPlateCount = approx
                break
        
        imageMask = np.zeros(grayImage.shape, np.uint8)
        newImage = cv2.drawContours(imageMask, [NumberPlateCount], 0, 255, -1)
        finalImage = cv2.bitwise_and(image, image, mask=imageMask)

        return finalImage

if __name__ == '__main__':
    numberPlateRecognition = NumberPlateRecognition()
    img = cv2.imread('test.jpeg')
    licenseNumber = numberPlateRecognition.getNumberPlate(img)
    print("Number Plate of Vehicle: ", licenseNumber)

