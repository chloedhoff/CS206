
import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
import random
import constants as c
from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]
solutionID = sys.argv[2]

simulation = SIMULATION(directOrGUI , solutionID)

simulation.Run()
simulation.Get_Fitness()



#FrontLegSensorValues = np.zeros(c.rounds)
#TorsoSensorValues = np.zeros(c.rounds)


#targetAngles= c.amplitude* np.sin(np.linspace(c.phaseOffset,c.frequency*2*np.pi, c.rounds))
#np.save("data/targetAngles.npy", targetAngles)

#FronLeg- FL sin func

#FLtargetAngles=c.FLamplitude* np.sin( np.linspace(c.FLphaseOffset,c.FLfrequency*2*np.pi, c.rounds))
#np.save("data/FLtargetAngles.npy", FLtargetAngles)

#BackLeg- BL sin func

#BLtargetAngles= c.BLamplitude* np.sin( np.linspace(c.BLphaseOffset,c.BLfrequency*2*np.pi,c.rounds))
#np.save("data/BLtargetAngles.npy", BLtargetAngles)

#for x in range(c.rounds):
   #print(x)
   #p.stepSimulation()
   #FrontLegSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") 
   #TorsoSensorValues[x] = pyrosim.Get_Touch_Sensor_Value_For_Link("Torso")

#motor form joint BackLeg_Torso
   
   #pyrosim.Set_Motor_For_Joint(

   #bodyIndex = robotId,

   #jointName = 'BackLeg_Torso',

   #controlMode = p.POSITION_CONTROL,

   #targetPosition = BLtargetAngles[x],

   #maxForce =c.force)

#motor form joint Torso_FrontLeg

   #pyrosim.Set_Motor_For_Joint(

   #bodyIndex = robotId,

   #jointName = 'Torso_FrontLeg',

   #controlMode = p.POSITION_CONTROL,
   
   #targetPosition = -FLtargetAngles[x],
   
   #maxForce = c.force)

   #time.sleep(c.sleep)



#p.disconnect()
#np.save("data/FrontLegSensorValues.npy", FrontLegSensorValues)
#np.save("data/TorsoSensorValues.npy", TorsoSensorValues)
#print(FrontLegSensorValues)
