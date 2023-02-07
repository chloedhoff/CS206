import numpy as np
import matplotlib.pyplot



FrontLegSensorValues = np.load("data/FrontLegSensorValues.npy")

TorsoSensorValues = np.load("data/TorsoSensorValues.npy")

matplotlib.pyplot.plot(FrontLegSensorValues, label = "Front Leg sensor", linewidth = 4)
matplotlib.pyplot.plot(TorsoSensorValues, label = "Back Leg sensor")
matplotlib.pyplot.legend(loc = "upper right")

print(FrontLegSensorValues)
print(TorsoSensorValues)

matplotlib.pyplot.show()
