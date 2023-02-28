from motor import MOTOR
from sensor import SENSOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
    def __init__(self):
        self.robotId=p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain.nndf")

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
       for neuronName in self.nn.Get_Neuron_Names():
           if self.nn.Is_Motor_Neuron(neuronName):
               self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
               self.desiredAngle = self.nn.Get_Value_Of(neuronName)
               self.motors[self.jointName].Set_Value(robot, self.desiredAngle)
               print(neuronName+" : "+self.jointName)
               print(self.desiredAngle)
       #for motor in self.motors.values() :
            #print(motor)
            #motor.Set_Value(robot, x)

    def Think(self):
        self.nn.Update()
        self.nn.Print()

