import matplotlib.pyplot
import numpy as np
import constants as c


A = np.load("dataA6.npy")
plotA = A[0,:]

B = np.load("dataB6.npy")
plotB = B[0,:]

#for row in range(A.shape[0]):
   #matplotlib.pyplot.plot(A[row,:], label = "A Sin()", linewidth = 4)


#for row in range(B.shape[0]):
   #matplotlib.pyplot.plot(B[row,:], label = "B NO Sin()")


#generation is by column so axis goes down
A_avg_array = np.mean(A, axis = 0)
matplotlib.pyplot.plot(A_avg_array, label = "A Sin() average fitness", linewidth = 5)

B_avg_array = np.mean(B, axis = 0)
matplotlib.pyplot.plot(B_avg_array, label = "B NO Sin() average fitness", linewidth = 1)  

#matplotlib.pyplot.plot(plotA, label = "A Sin()", linewidth = 4)
#matplotlib.pyplot.plot(plotB, label = "B NO Sin()")


matplotlib.pyplot.legend(loc = "upper right")
   
matplotlib.pyplot.show()
