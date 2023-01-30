import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

length = 1
width = 1
height = 1

x = -1
y = -1
z = .5

for xrange in range(5): 
    x=x+1
    y=-1
    for yrange in range(5):
    	y=y+1
    	length = 1
    	width = 1
    	height = 1
    	z = .5
    	for i in range(10):
            pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
            z=z+1
            length = length*.9
            width = width*.9
            height = height*.9
      

#pyrosim.Send_Cube(name="Box2", pos=[x2,y2,z2] , size=[length,width,height])

pyrosim.End()
