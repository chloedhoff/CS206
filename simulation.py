import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import constants as c
import time
from world import WORLD
from robot import ROBOT
from motor import MOTOR
from sensor import SENSOR


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
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(self.robot, x)
            time.sleep(c.sleep)

    def __del__(self):

        p.disconnect()    



