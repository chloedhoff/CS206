from motor import MOTOR
from sensor import SENSOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim

class ROBOT:
    def __init__(self):
        self.robotId=p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors={}
        for linkName in pyrosim.linkNamesToIndices:
            #print(linkName)
            self.sensors[linkName] = SENSOR(linkName)
            
    def Sense(self, x):        
        #TorsoSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")
        for sensor in self.sensors.values() :
            sensor.Get_Value(x)


    def Prepare_To_Act(self):
        self.motors={}
        for jointName in pyrosim.jointNamesToIndices:
            print(jointName)
            self.motors[jointName] = MOTOR(jointName)
    

    def Act(self,robot, x):
       pass
       for motor in self.motors.values() :
            motor.Set_Value(robot, x) 


