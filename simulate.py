
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

#variables
amplitude = np.pi/4
frequency = 1
phaseOffset = 0


#This creates an object, physicsClient, which handles the physics,
#and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

FrontLegSensorValues = np.zeros(1000)
TorsoSensorValues = np.zeros(1000)

targetAngles= amplitude* np.sin( np.linspace(phaseOffset,frequency*np.pi, 1000))
#np.save("data/targetAngles.npy", targetAngles)

for x in range(1000):
   #print(x)
   p.stepSimulation()
   FrontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") 
   TorsoSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")

#motor form joint BackLeg_Torso
   
   pyrosim.Set_Motor_For_Joint(

   bodyIndex = robotId,

   jointName = 'BackLeg_Torso',

   controlMode = p.POSITION_CONTROL,

   targetPosition = targetAngles[x],

   maxForce = 30)

#motor form joint Torso_FrontLeg

   pyrosim.Set_Motor_For_Joint(

   bodyIndex = robotId,

   jointName = 'Torso_FrontLeg',

   controlMode = p.POSITION_CONTROL,
   
   targetPosition = -targetAngles[x],
   
   maxForce = 30)

   time.sleep(1/60)



p.disconnect()
np.save("data/FrontLegSensorValues.npy", FrontLegSensorValues)
np.save("data/TorsoSensorValues.npy", TorsoSensorValues)
print(FrontLegSensorValues)
