from wimSensorSystem import WimSensorSystem
from numberPlateRecognition import NumberPlateRecognition
from vehicleDatabaseParser import VehicleDatabaseParser
from vehicle import Vehicle
from vehiclePricingDecision import VehiclePricingDecision
from cv2 import cv2
from resultCodes import *
import logging
import imutils

# Use for debug ONLY
database = 'VehicleDatabase.db'
image = cv2.imread('test1.jpg')

def log_setup():
    log_format = ('%(asctime)s %(levelname)-8s [%(filename)-25s:%(lineno)-4d] %(message)s')
    logging.Formatter(fmt=log_format, datefmt='%H:%M:%S')
    logging.getLogger().setLevel(logging.DEBUG)

def main(image):

    ''' Main function of Electronic Toll Collection System '''

    # Assuming vehicle has passed over the sensor
    wimSensorSystem = WimSensorSystem()
    print("Welcome to WIM Sensor based toll...")
    currentVehicleWeight = wimSensorSystem.getWeight()

    # Simultaneously Number Plate is recognized from the image
    numberPlateRecognition = NumberPlateRecognition()
    print("Processing your number plate...")
    vehicleRegistrationNumber = numberPlateRecognition.getNumberPlate(image)

    # Connect to Vehicle Database to fetch details
    vehicleDatabaseParser = VehicleDatabaseParser(database)

    # Fetch the details from the database/API
    print("Fetching your vehicle details...")
    currentVehicle = Vehicle(vehicleDatabaseParser.getAsListVehicleDetails(vehicleRegistrationNumber))

    # Vehicle Pricing and Toll Decision
    vehiclePricingDecision = VehiclePricingDecision()
    print("Verifying your vehicle details...")
    tollDecision = vehiclePricingDecision.decisionMaker(currentVehicle, currentVehicleWeight)
    
    decideTollAction(tollDecision)
    cv2.imshow("Car image ", imutils.resize(image,width=250))
    cv2.imshow("Number Plate", imutils.resize(cv2.imread('numberPlateImage.jpg'), width=250))
    cv2.waitKey(0)

if __name__ == "__main__":
    image = cv2.imread('manju.jpg')
    main(image)