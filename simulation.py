import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import constants as c
import time
from world import WORLD
from robot import ROBOT


class SIMULATION:
    def __init__(self):
        self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)
        self.world = WORLD()
        self.robot = ROBOT()
        #pyrosim.Prepare_To_Simulate(robotId)

    def Run(self):
        for x in range(c.rounds):
            print(x)
            p.stepSimulation()
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

            time.sleep(c.sleep)



