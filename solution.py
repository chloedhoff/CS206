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
        self.weights = np.random.rand(3,2)
        self.weights= self.weights*2 -1
        #print(self.weights)

    #def Evaluate(self, directOrGUI):
    
    def Start_Simulation(self, directOrGUI):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system("python3 simulate.py " + directOrGUI +" "+str(self.myID)+" &")



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
        pyrosim.Send_Cube(name="BackLeg", pos=[x,y,z] , size=[length,width,height])
        pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" ,type = "revolute", position = [1,.5,1])
        pyrosim.Send_Cube(name="Torso", pos=[.5,0,.5] , size=[length,width,height])
        pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg"  , type = "revolute", position = [1,0,0])
        pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
        pyrosim.End()

        
    #Create_Brain
    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork("brain"+str(self.myID)+".nndf")
        pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
        pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
        pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
        pyrosim.Send_Motor_Neuron( name = 3 , jointName = "BackLeg_Torso")
        pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
        '''pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0
        pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 3 )
        pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 5 )
        pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 8 #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 1 , weight = 10.0 )
        #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1 )
        #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.6 )
        #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1 )
        #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 7)'''
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn])
        pyrosim.End()


    def Mutate(self):
            randomRow = random.randint(0,2)
            randomColumn = random.randint(0,1)
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
