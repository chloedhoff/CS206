import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import os
import random
import time

class SOLUTION:
    def __init__(self, ID):
        self.myID = ID
        #print(self.myID)
        self.weights = np.random.rand(c.numSensorNeurons, c.numMotorNeurons)
        self.weights= self.weights*2 -1
        #print(self.weights)

    #def Evaluate(self, directOrGUI):
    
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI +" "+str(self.myID)+" &")
        #os.system("python3 simulate.py GUI 0 2&>1 &")


    def Wait_For_Simulation_To_End(self):
        while not os.path.exists("fitness"+str(self.myID)+".txt"):
            time.sleep(0.01)

        f = open("fitness"+str(self.myID)+".txt","r")
        self.fitness = float(f.read())
        #print(self.fitness)
        f.close()
        os.system("rm fitness"+str(self.myID)+".txt")
        

    def Create_World(self):
        pyrosim.Start_SDF("world.sdf")
        pyrosim.Send_Cube(name="Box", pos=[x2,y2,z] , size=[length,width,height])
        pyrosim.End()

    
    def Create_Body(self):
        pyrosim.Start_URDF("body.urdf")
        pyrosim.Send_Cube(name="BackLeg", pos=[0,-1,1] , size=[.2,1,.2])
        
        pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" ,type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Torso", pos=[0,.5,0] , size=[length,width,height])
        
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg"  , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLeg", pos=[0,.5,0] , size=[.2,1,.2])
        
        pyrosim.Send_Joint( name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg"  , type = "revolute", position = [-.5,.5,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLeg", pos=[-.5,0,0] , size=[1,.2,.2])
        
        pyrosim.Send_Joint( name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg"  , type = "revolute", position = [.5,.5,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLeg", pos=[.5,0,0] , size=[1,.2,.2])
        
        pyrosim.Send_Joint(name = "Frontleg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        
        pyrosim.Send_Joint(name = "Backleg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        
        pyrosim.Send_Joint(name = "Rightleg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])

        pyrosim.Send_Joint(name = "Leftleg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
        
        pyrosim.End()
        #Create Body
        '''pyrosim.Start_URDF("body.urdf")
		#torso
        pyrosim.Send_Cube(name="Torso", pos=[0,0,1] , size=[length,width,height])
		#backleg
        pyrosim.Send_Joint(name = "Torso_Backleg" , parent= "Torso" , child = "Backleg" , type = "revolute", position = [0,-.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Backleg", pos=[0,-0.5,0] , size=[.2,1,.2])
		#frontleg
        pyrosim.Send_Joint(name = "Torso_Frontleg" , parent= "Torso" , child = "Frontleg" , type = "revolute", position = [0,.5,1], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="Frontleg", pos=[0,.5,0] , size=[.2,1,.2])
		#left leg
        pyrosim.Send_Joint(name = "Torso_Leftleg" , parent= "Torso" , child = "Leftleg" , type = "revolute", position = [-.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Leftleg", pos=[-.5,0,0] , size=[1,.2,.2])
		#right leg
        pyrosim.Send_Joint(name = "Torso_Rightleg" , parent= "Torso" , child = "Rightleg" , type = "revolute", position = [.5,0,1], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="Rightleg", pos=[.5,0,0] , size=[1,.2,.2])
		#front lower leg
        pyrosim.Send_Joint(name = "Frontleg_FrontLowerLeg" , parent= "Frontleg" , child = "FrontLowerLeg" , type = "revolute", position = [0,1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="FrontLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
		#back lower leg
        pyrosim.Send_Joint(name = "Backleg_BackLowerLeg" , parent= "Backleg" , child = "BackLowerLeg" , type = "revolute", position = [0,-1,0], jointAxis = "1 0 0")
        pyrosim.Send_Cube(name="BackLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
		#right lower leg
        pyrosim.Send_Joint(name = "Rightleg_RightLowerLeg" , parent= "Rightleg" , child = "RightLowerLeg" , type = "revolute", position = [1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="RightLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
		#left lower leg
        pyrosim.Send_Joint(name = "Leftleg_LeftLowerLeg" , parent= "Leftleg" , child = "LeftLowerLeg" , type = "revolute", position = [-1,0,0], jointAxis = "0 1 0")
        pyrosim.Send_Cube(name="LeftLowerLeg", pos=[0,0,-.5] , size=[.2,.2,1])
		#end
        pyrosim.End()'''



        
    #Create_Brain
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "FrontLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "RightLowerLeg")
        pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLowerLeg")

        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "BackLeg_Torso")
        pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_RightLeg")
        pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_LeftLeg")

        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Frontleg_FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Backleg_BackLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Leftleg_LeftLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 11 , jointName = "Rightleg_RightLowerLeg")

        '''pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "BackLeg_Torso")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "LeftLeg")
        pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_LeftLeg")
        pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLeg")
        pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_RightLeg")
        #pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "FrontLowerLeg")
        pyrosim.Send_Motor_Neuron( name = 10 , jointName = "Frontleg_FrontLowerLeg")'''

        
        '''pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 3 )
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 5 )
        pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 8 #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 1 , weight = 10.0 )
        #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1 )
        #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.6 )
        #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1 )
        #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 7)'''
        for currentRow in range(c.numSensorNeurons):
            for currentColumn in range(c.numMotorNeurons):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])
        pyrosim.End()
        


    def Mutate(self):
            randomRow = random.randint(0,c.numSensorNeurons-1)
            randomColumn = random.randint(0,c.numMotorNeurons-1)
            self.weights[randomRow, randomColumn] = random.random()*2-1

    def Set_ID(self, availID):
        self.myID = availID

length = 1
width = 1
height = 1
x = .5
y = .5
z = .5

x2 = -5
y2 = 3
