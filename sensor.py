import constants as c
import numpy as np
import pybullet_data
import pyrosim.pyrosim as pyrosim

class SENSOR:

    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.rounds)
        #print(self.values)

    def Get_Value(self, t):
        factor = 20
        w = 3
        x = 6
        y= 9
        z = 12
        if (self.linkName == "FrontLowerLeg"):
            self.values[t] = np.sin(factor*w*t)

        if (self.linkName == "BackLowerLeg"):
            self.values[t] = np.sin(factor*y*t)

        if (self.linkName == "RightLowerLeg"):
            self.values[t] = np.sin(factor*z*t)

        if (self.linkName == "LeftLowerLeg"):
           self.values[t] = np.sin(factor*x*t)

        else:
            self.values[t] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)

        if (t == 299):
            print(self.values)

    def Save_Values(self):
         np.save('data/SensorValue.npy', self.values)
         
