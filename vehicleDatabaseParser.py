import sqlite3


class VehicleDatabaseParser():
    def __init__(self, database):
        self.conn = sqlite3.connect(database)
        self.c = self.conn.cursor()
        
    def getAsListVehicleDetails(self, number):
        return self.c.execute("SELECT * FROM VEHICLE_INFO WHERE REGISTRATION_NUMBER=?", (number,)).fetchall()[0]
        
if __name__ == "__main__":
    # Use for debugging
    vehicleDatabaseParser = VehicleDatabaseParser('VehicleDatabase.db')
    print(vehicleDatabaseParser.getAsListVehicleDetails('KA02JK2930'))