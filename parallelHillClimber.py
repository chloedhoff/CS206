from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self):
       self.parents = {}
       self.nextAvailableID = 0
       #loop of x in 0 to populationSize-1
       for x in range(c.populationSize):
           individual_parent = SOLUTION(self.nextAvailableID)
           self.nextAvailableID+=1
           self.parents[x] = individual_parent
       

    def Evolve(self):
        for key in self.parents:
            self.parents[key].Start_Simulation("GUI")

        for key in self.parents:
            self.parents[key].Wait_For_Simulation_To_End()
        #self.parent.Evaluate("DIRECT")
        #self.parent.Evaluate("GUI")
        #for currentGeneration in range(c.numberOfGenerations):
        #    self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)
        self.child.Set_ID(self.nextAvailableID)
        self.nextAvailableID+=1

    def Mutate(self):
        self.child.Mutate()
        #print(self.child.weights)
        #print(self.parent.weights)

    def Select(self):
        #print(self.child.fitness)
        #print(self.parent.fitness)
        if (self.parent.fitness>self.child.fitness):
            self.parent = self.child


    def Show_Best(self):
        pass
        #self.parent.Evaluate("GUI")

    def Print(self):
        print("parent: "+str(self.parent.fitness)+" child: "+str(self.child.fitness))
