import logging

class WimSensorSystem:
    ''' This measures the weight based on weigh-in-motion sensors.
        Input: WIM sensor reading.
        Output: Weight in kgs
    '''
    def __init__(self):
        pass
    
    def getWeight(self):
        ''' Return sample weight for now'''
        weight = 1000
        print('Current Weight of your vehicle: {}kgs'.format(weight))
        return weight
