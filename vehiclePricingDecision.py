from datetime import datetime
from vehicleDatabaseParser import VehicleDatabaseParser
from vehicle import Vehicle
from resultCodes import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class VehiclePricingDecision:

    def __init__(self):
        pass
    def decisionMaker(self, vehicle, currentWeight):
        ''' The method that makes the decision whether or not to open the toll for a given vehicle. '''
        # Check vehicle details first
        if not self.__checkRcStatus(vehicle):
            # TODO : Add logging debug statements and change return type based on action to be taken
            return VEHICLE_RC_NOT_ACTIVE

        # True if Registration has not expired
        if not self.__checkRegistrationExpiry(vehicle):
            # TODO : Add logging debug statements and change return type based on action to be taken
            return VEHICLE_REGISTRATION_EXPIRED

        # True if not expired
        if not self.__checkInsuranceExpiry(vehicle):
            # TODO : Add logging debug statements and change return type based on action to be taken
            return VEHICLE_INSURANCE_EXPIRED
        
        # Check weight if vehicle is within the allowed maximum weight
        if not self.__checkOverload(vehicle, currentWeight):
            # TODO : Add logging debug statements and change return type based on action to be taken
            return VEHICLE_OVERLOADED
        
        # If vehicle is legal and allowed, proceed for calculation of toll price
        tollPrice = self.__calculateTollPrice(currentWeight)
        
        return tollPrice

    def __calculateTollPrice(self, currentWeight):
        ''' Pricing of the allowed vehicles '''
        print("Calculating your toll price...")
        return currentWeight//12

    def __checkRcStatus(self, vehicle):
        print("Checking your Vehicle RC Status...")
        if vehicle.rcStatus == 'ACTIVE':
            print('DONE.')
            return True
        else:
            return False
    
    def __checkRegistrationExpiry(self, vehicle):
        print("Checking your Vehicle Registration validity...")
        expiryDate = datetime.strptime(vehicle.registrationExpiryDate, '%d-%b-%Y').date()
        if expiryDate > datetime.today().date():
            print("DONE.")
            return True
        else:
            return False

    def __checkInsuranceExpiry(self, vehicle):
        print("Checking your Vehicle Insurance Validity...")
        expiryDate = datetime.strptime(vehicle.insuranceExpiryDate, '%d-%b-%Y').date()
        if expiryDate > datetime.today().date():
            print("DONE.")
            return True
        else:
            print("Vehicle Insurance Validity Date:", vehicle.insuranceExpiryDate)
            print("Todays date:", datetime.today().date())
            return False
    
    def __checkOverload(self, vehicle, currentWeight):
        print("Checking the weight of vehicle for overload...")
        if currentWeight >= vehicle.vehicleGvwr:
            print("Current Weight of the vehicle =", currentWeight)
            print("Maximum allowed weight for your vehicle =", vehicle.vehicleGvwr)
            return False
        else:
            print("DONE.")
            return True

if __name__ == "__main__":
    # Following used for debugging
    vehicleDatabaseParser = VehicleDatabaseParser('VehicleDatabase.db')
    vehicle = Vehicle(vehicleDatabaseParser.getAsListVehicleDetails('KA02JK2930'))
    vehiclePricingDecision = VehiclePricingDecision()
    vehiclePricingDecision.decisionMaker(vehicle, currentWeight=150)

