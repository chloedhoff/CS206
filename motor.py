import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import numpy as np

class MOTOR:

    def __init__(self, jointName):
        self.jointName = jointName
        #print(jointName)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):    
        if (self.jointName == "BackLeg_Torso"):
            self.frequency = 10
        if (self.jointName == "Torso_FrontLeg"):
            self.frequency = 5
        self.amplitude = np.pi/4
        self.offset = 0
        self.motorValue = self.amplitude* np.sin( np.linspace(self.offset,self.frequency*2*np.pi, c.rounds))
        #self.motor_values_2 = self.amplitude* np.sin( np.linspace(self.offset,self.frequency*2*np.pi,c.rounds))


    def Set_Value(self, robot, x):
   
        pyrosim.Set_Motor_For_Joint(

        bodyIndex = robot.robotId,

        jointName = self.jointName,

        controlMode = p.POSITION_CONTROL,
        
        targetPosition = self.motorValue[x],

        maxForce =c.force)

    def Save_Values(self):
         numpy.save('data/MotorValue.npy',self.motorValue)
            
