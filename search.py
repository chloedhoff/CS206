import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER
import constants as c
import numpy as np

#for x in range(0,5):
    #os.system("python3 generate.py")
    #os.system("python3 simulate.py")
phc=PARALLEL_HILL_CLIMBER()
phc.Evolve()
best = phc.Show_Best()
print("DATA ARRAY---------------------------------------------------")
print(phc.data_array)
print("END DATA ARRAY---------------------------------------------------")
#np.savetxt("FinalProjData",phc.data_array)
np.save("dataB6.npy", phc.data_array)
print("saved data")

#phc.data_array[c.populationSize-1, c.numberOfGenerations] = best.fitness
