from motor import MOTOR
from sensor import SENSOR
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import constants as c
import os

class ROBOT:
    def __init__(self, solutionID):
        self.robotId=p.loadURDF("body.urdf")
        self.solutionID = solutionID
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
            

    #goal is to overwrite sensor neuron with sin signal
    #t is time step
    def Sense(self, t):        
        #TorsoSensorValues[t] = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")
        #print(self.sensors)
        #overwrite ONE touch sensor with sin(xt) where x is set my user
        for sensor in self.sensors.values() :
            sensor.Get_Value(t)
            #print(sensor.Get_Value(t))


    def Prepare_To_Act(self):
        self.motors={}
        for jointName in pyrosim.jointNamesToIndices:
            #print(jointName)
            self.motors[jointName] = MOTOR(jointName)
    

    def Act(self,robot, x):
       for neuronName in self.nn.Get_Neuron_Names():
           if self.nn.Is_Motor_Neuron(neuronName):
               self.jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
               self.desiredAngle = self.nn.Get_Value_Of(neuronName)*c.motorJointRange
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
        #stateOfLinkZero = p.getLinkState(self.robotId,0)
        #positionOfLinkZero = stateOfLinkZero[0]
        #xCoordinateOfLinkZero = positionOfLinkZero[0]

        #replaced above with below
        #the horizontal position og the backleg of qudraped
        basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
        #the horizontal position of torso
        basePosition = basePositionAndOrientation[0]
        xPosition = basePosition[0]

        #file = open("fitness"+str(self.solutionID)+".txt","w")
        file = open("tmp"+str(self.solutionID)+".txt","w")
        file.write(str(xPosition))
        file.close()
        os.system("mv tmp"+str(self.solutionID)+".txt fitness"+str(self.solutionID)+".txt")
        exit()

