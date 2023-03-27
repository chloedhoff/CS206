from motor import MOTOR
from sensor import SENSOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os

class ROBOT:
    def __init__(self, solutionID):
        self.solutionID = solutionID
        self.robotId=p.loadURDF("body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()
        self.nn = NEURAL_NETWORK("brain"+str(solutionID)+".nndf")
        os.system("rm brain"+str(solutionID)+".nndf")

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
            #print(jointName)
            self.motors[jointName] = MOTOR(jointName)
    

    def Act(self,robot, x):
       for neuronName in self.nn.Get_Neuron_Names():
           if self.nn.Is_Motor_Neuron(neuronName):
               self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
               self.desiredAngle = self.nn.Get_Value_Of(neuronName)
               self.motors[self.jointName].Set_Value(robot, self.desiredAngle)
               #print(neuronName+" : "+self.jointName)
               #print(self.desiredAngle)
       #for motor in self.motors.values() :
            #print(motor)
            #motor.Set_Value(robot, x)

    def Think(self):
        self.nn.Update()
#####Printing neural network#####
        #self.nn.Print()

    def Get_Fitness(self):
        stateOfLinkZero = p.getLinkState(self.robotId,0)
        #print(stateOfLinkZero)
        #print(self.stateOfLinkZero)
        positionOfLinkZero = stateOfLinkZero[0]
        #print(positionOfLinkZero)
        xCoordinateOfLinkZero = positionOfLinkZero[0]
        #print(xCoordinateOfLinkZero)

        #file = open("fitness"+str(self.solutionID)+".txt","w")
        file = open("tmp"+str(self.solutionID)+".txt","w")
        file.write(str(xCoordinateOfLinkZero))
        file.close()
        os.system("mv tmp"+str(self.solutionID)+".txt fitness"+str(self.solutionID)+".txt")
        exit()

