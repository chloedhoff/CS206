from solution import SOLUTION
import constants as c
import copy
import os
import numpy as np

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
       os.system("rm brain*.nndf")
       os.system("rm fitness*.txt")
       self.data_array= np.zeros((c.populationSize, c.numberOfGenerations))

#index in self.parents is where it lays in the population
       

       self.parents = {}
       self.nextAvailableID = 0
       #loop of x in 0 to populationSize-1
       for x in range(c.populationSize):
           individual_parent = SOLUTION(self.nextAvailableID)
           self.nextAvailableID+=1
           self.parents[x] = individual_parent
       

    def Evolve(self):
        self.Evaluate(self.parents)
        for key in self.parents:
            self.parents[key].Start_Simulation("DIRECT")
            #self.parents[key].Wait_For_Simulation_To_End()

        #for key in self.parents:
            #self.parents[key].Wait_For_Simulation_To_End()
        #self.parent.Evaluate("DIRECT")
        #self.parent.Evaluate("GUI")
        for currentGeneration in range(c.numberOfGenerations):
            self.Evolve_For_One_Generation(currentGeneration)

    def Evolve_For_One_Generation(self, currentGeneration):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print(currentGeneration)
        self.Select(currentGeneration)
        #data_array[c.populationSize-1, c.numberOfGenerations] = best.fitness

    def Spawn(self):
        self.children= {}
        for key in self.parents:
            self.children[key] = copy.deepcopy(self.parents[key])
            self.children[key].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1
        #print(self.children)
        #exit()

    def Mutate(self):
        for key in self.children:
            self.children[key].Mutate()

        #self.child.Mutate()
        #print(self.child.weights)
        #print(self.parent.weights)

    def Evaluate(self,solutions):
        for key in solutions:
            solutions[key].Start_Simulation("DIRECT")

        for key in solutions:
            solutions[key].Wait_For_Simulation_To_End()

    def Select(self, currentGeneration):
        #print(self.child.fitness)
        #print(self.parent.fitness)
        for key in self.parents:
            if (self.parents[key].fitness>self.children[key].fitness):
                self.parents[key] = self.children[key]
                #self.data_array[key-1, currentGeneration-1] = self.parents[key].fitness       

    
    def Show_Best(self):
        self.best = self.parents[0]
        for key in self.parents:
            if self.parents[key].fitness < self.best.fitness:
                self.best = self.parents[key]
        self.best.Start_Simulation("GUI")
        #data_array[c.populationSize-1, c.numberOfGenerations] = best.fitness
        return self.best
        #self.parent.Evaluate("GUI")

    def Print(self, currentGeneration):
        print()
        for key in self.parents:
            print("parent: "+str(self.parents[key].fitness)+" child: "+str(self.children[key].fitness))
            self.data_array[key-1, currentGeneration-1] = self.parents[key].fitness 
        print()
