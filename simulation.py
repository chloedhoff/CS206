import pyrosim.pyrosim as pyrosim
import pybullet as p
import pybullet_data
import constants as c
import time
from world import WORLD
from robot import ROBOT
from motor import MOTOR
from sensor import SENSOR
import os


class SIMULATION:
    def __init__(self, directOrGUI, solutionID):
        self.directOrGUI = directOrGUI
        if(self.directOrGUI == "DIRECT"):
            #self.physicsClient = p.connect(p.DIRECT)
            p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,c.gravity)
        self.world = WORLD()
        self.robot = ROBOT(solutionID)
        #pyrosim.Prepare_To_Simulate(robotId)

    def Run(self):
        for x in range(c.rounds):
            #print(x)
            p.stepSimulation()
            self.robot.Sense(x)
            self.robot.Think()
            self.robot.Act(self.robot, x)
            if (self.directOrGUI == "GUI"):
                time.sleep(c.sleep)

    def Get_Fitness(self):
        self.robot.Get_Fitness()

    def __del__(self):
        #for x in range(c.populationSize):
         #   os.system("rm fitness"+str(x)+".txt")
        p.disconnect()    



