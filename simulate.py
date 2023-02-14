
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random

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

#variables
amplitude = np.pi/4
frequency = 10
phaseOffset = 0

targetAngles= amplitude* np.sin( np.linspace(phaseOffset,frequency*2*np.pi, 1000))
#np.save("data/targetAngles.npy", targetAngles)

#FronLeg- FL sin func

#variables
FLamplitude = np.pi/6
FLfrequency =10
FLphaseOffset = np.pi/2 

FLtargetAngles=FLamplitude* np.sin( np.linspace(FLphaseOffset,FLfrequency*2*np.pi, 1000))
np.save("data/FLtargetAngles.npy", FLtargetAngles)

#BackLeg- BL sin func 

#variables
BLamplitude = np.pi/3   
BLfrequency = 5
BLphaseOffset = 0

BLtargetAngles= BLamplitude* np.sin( np.linspace(BLphaseOffset,BLfrequency*2*np.pi, 
1000))
np.save("data/BLtargetAngles.npy", BLtargetAngles)

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

   targetPosition = BLtargetAngles[x],

   maxForce = 15)

#motor form joint Torso_FrontLeg

   pyrosim.Set_Motor_For_Joint(

   bodyIndex = robotId,

   jointName = 'Torso_FrontLeg',

   controlMode = p.POSITION_CONTROL,
   
   targetPosition = -FLtargetAngles[x],
   
   maxForce = 15)

   time.sleep(1/60)



p.disconnect()
np.save("data/FrontLegSensorValues.npy", FrontLegSensorValues)
np.save("data/TorsoSensorValues.npy", TorsoSensorValues)
print(FrontLegSensorValues)
