from datetime import datetime
from vehicleDatabaseParser import VehicleDatabaseParser
from vehicle import Vehicle
from resultCodes import *

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
        print("Calculating your toll price...")
        tollPrice = self.__calculateTollPrice(currentWeight)
        
        return tollPrice

    def __calculateTollPrice(self, currentWeight):
        ''' Pricing of the allowed vehicles '''
        return currentWeight//25

    def __checkRcStatus(self, vehicle):
        if vehicle.rcStatus == 'ACTIVE':
            return True
        else:
            return False
    
    def __checkRegistrationExpiry(self, vehicle):
        expiryDate = datetime.strptime(vehicle.registrationExpiryDate, '%d-%b-%Y').date()
        if expiryDate > datetime.today().date():
            return True
        else:
            return False

    def __checkInsuranceExpiry(self, vehicle):
        expiryDate = datetime.strptime(vehicle.insuranceExpiryDate, '%d-%b-%Y').date()
        if expiryDate > datetime.today().date():
            return True
        else:
            return False
    
    def __checkOverload(self, vehicle, currentWeight):
        if currentWeight >= vehicle.vehicleGvwr:
            return False
        else:
            return True

if __name__ == "__main__":
    # Following used for debugging
    vehicleDatabaseParser = VehicleDatabaseParser('VehicleDatabase.db')
    vehicle = Vehicle(vehicleDatabaseParser.getAsListVehicleDetails('KA02JK2930'))
    vehiclePricingDecision = VehiclePricingDecision()
    vehiclePricingDecision.decisionMaker(vehicle, currentWeight=150)

