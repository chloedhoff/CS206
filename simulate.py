import pybullet as p
import time

#This creates an object, physicsClient, which handles the physics,
#and draws the results to a Graphical User Interface (GUI).
physicsClient = p.connect(p.GUI)

p.loadSDF("box.sdf")

for x in range(1000):
   print(x)
   p.stepSimulation()
   time.sleep(1/60)

p.disconnect()

