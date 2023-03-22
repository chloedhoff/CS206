from solution import SOLUTION
import constants as c
import copy

class HILL_CLIMBER:

    def __init__(self):
       self.parent = SOLUTION()

    def Evolve(self):
       self.parent.Evaluate("DIRECT")
       for currentGeneration in range(c.numberOfGenerations):
           self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate("DIRECT")
        self.Print()

        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()
        #print(self.child.weights)
        #print(self.parent.weights)

    def Select(self):
        #print(self.child.fitness)
        #print(self.parent.fitness)
        if (self.parent.fitness>self.child.fitness):
            self.parent = self.child

    def Print(self):
        print("parent: "+str(self.parent.fitness)+" child: "+str(self.child.fitness))
