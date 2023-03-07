import pyrosim.pyrosim as pyrosim
import random as random

pyrosim.Start_SDF("world.sdf")

def Create_World():
   pyrosim.Start_SDF("world.sdf")
   pyrosim.Send_Cube(name="Box", pos=[x2,y2,z] , size=[length,width,height])
   pyrosim.End()

def Create_Robot():
   pyrosim.Start_URDF("body.urdf")
   pyrosim.Send_Cube(name="BackLeg", pos=[x,y,z] , size=[length,width,height])
   pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" , type = "revolute", position = [1,.5,1])
   pyrosim.Send_Cube(name="Torso", pos=[.5,0,.5] , size=[length,width,height])
   pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [1,0,0])  
   pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
   pyrosim.End()

def Generate_Body():
   pyrosim.Start_URDF("body.urdf")
   pyrosim.Send_Cube(name="BackLeg", pos=[x,y,z] , size=[length,width,height])
   pyrosim.Send_Joint( name = "BackLeg_Torso" , parent= "BackLeg" , child = "Torso" ,type = "revolute", position = [1,.5,1])
   pyrosim.Send_Cube(name="Torso", pos=[.5,0,.5] , size=[length,width,height])
   pyrosim.Send_Joint( name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg"  , type = "revolute", position = [1,0,0])
   pyrosim.Send_Cube(name="FrontLeg", pos=[.5,0,-.5] , size=[length,width,height])
   pyrosim.End()

def Generate_Brain():
   pyrosim.Start_NeuralNetwork("brain.nndf")
   pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
   pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
   pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
   pyrosim.Send_Motor_Neuron( name = 3 , jointName = "BackLeg_Torso")
   pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
   '''pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
   pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 3 )
   pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 5 )
   pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = 8 )
   #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 1 , weight = 10.0 )
   #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = -1 )
   #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.6 )
   #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = 1 )
   #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 7)'''
   for i in range(3):
      for j in range(3,5):
         pyrosim.Send_Synapse(sourceNeuronName = i , targetNeuronName = j , weight = random.randrange(-1,1))
   pyrosim.End()



length = 1
width = 1
height = 1
x = .5
y = .5
z = .5

x2 = -5
y2 = 3
 
Create_World()
#Create_Robot()
Generate_Body()
Generate_Brain()
