import constants as c
import numpy as np
import pybullet_data
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.rounds)
        #print(self.values)

    def Get_Value(self, x):
         self.values[x] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
         #if (x == 999):
             #print(self.values)

    def Save_Values(self):
         numpy.save('data/SensorValue.npy', self.values)
         
