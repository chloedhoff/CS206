import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim

#This creates an object, physicsClient, which handles the physics,
#and draws the results to a Graphical User Interface (GUI).

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

for x in range(1000):
   #print(x)
   p.stepSimulation()
   FrontLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg") 
   print(FrontLegTouch)
   time.sleep(1/60)


p.disconnect()

