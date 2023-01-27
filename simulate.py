import pybullet as p
import time
import pybullet_data

#This creates an object, physicsClient, which handles the physics,
#and draws the results to a Graphical User Interface (GUI).

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
p.loadSDF("boxes.sdf")

for x in range(1000):
   print(x)
   p.stepSimulation()
   time.sleep(1/60)

p.disconnect()

