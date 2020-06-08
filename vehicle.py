from vehicleDatabaseParser import VehicleDatabaseParser

class Vehicle:
    ''' Vehicle class to handle data from the Vehicle Database '''
    def __init__(self, vehicleDetails):
        self.id = vehicleDetails[0]
        self.registrationNumber = vehicleDetails[1]
        self.registrationDate = vehicleDetails[2]
        self.ownerName = vehicleDetails[3]
        self.vehicleModel = vehicleDetails[4]
        self.insuranceExpiryDate = vehicleDetails[5]
        self.registrationExpiryDate = vehicleDetails[6]
        self.rcStatus = vehicleDetails[7]
        self.vehicleGvwr = vehicleDetails[8]
    
    def __printDetails(self):
        print("ID: ", self.id)
        print("Registration Number: ", self.registrationNumber)
        print("Registration Date: ", self.registrationDate)
        print("Owner Name: ", self.ownerName)
        print("Vehicle Model: ", self.vehicleModel)
        print("Insurance Expiry Date: ", self.insuranceExpiryDate)
        print("Registration Expiry Date: ", self.registrationExpiryDate)
        print("RC Status: ", self.rcStatus)
        print("Vehicle GVWR(kg): ", self.vehicleGvwr)

if __name__ == "__main__":
    # Use for Debugging
    vehicleDatabaseParser = VehicleDatabaseParser('VehicleDatabase.db')
    vehicle = Vehicle(vehicleDatabaseParser.getAsListVehicleDetails('KA02JK2930'))
    vehicle._Vehicle__printDetails()
