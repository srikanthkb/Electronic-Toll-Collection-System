import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

VEHICLE_RC_NOT_ACTIVE = 1
VEHICLE_REGISTRATION_EXPIRED = 2
VEHICLE_INSURANCE_EXPIRED = 3
VEHICLE_OVERLOADED = 4
VEHICLE_ALLOWED = 5

def vehicleNotAllowed(reason):
    print("There seems to be a problem...")
    print(reason)
    print('Please wait until the officials arrive and resolve this manually...')
    print('Thank you...')

def vehicleAllowed(price):
    print('Your vehicle Toll price:', price)
    print('The amount deducted from your FASTag-Wallet:', price)
    print('Remaining Balance: Rs.', 200-price)       # Check how to get current E-Toll-Balance
    print('Wear seat belt and Drive Safe...')

def decideTollAction(tollDecision):
    if tollDecision == VEHICLE_RC_NOT_ACTIVE:
        return vehicleNotAllowed('Vehicle RC Status is not ACTIVE')
    elif tollDecision == VEHICLE_RC_NOT_ACTIVE:
        return vehicleNotAllowed('Vehicle Registration has expired')
    elif tollDecision == VEHICLE_INSURANCE_EXPIRED:
        return vehicleNotAllowed('Vehicle Insurance has expired')
    elif tollDecision == VEHICLE_OVERLOADED:
        return vehicleNotAllowed('Vehicle is loaded above maximum capacity')
    else:
        return vehicleAllowed(tollDecision)