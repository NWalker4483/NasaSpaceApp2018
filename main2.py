from NodeStuff import SensorNodeHandler
from Frontend import HazardMap, MultiLineSensorPlot
import matplotlib.pyplot as plt
import time
nodes = [SensorNodeHandler(UDP_PORT=5000,latitude=25,longitude=75,debug=True),
SensorNodeHandler(UDP_PORT = 5001,latitude=25,longitude=25,debug=True),
SensorNodeHandler(UDP_PORT = 5002,latitude=50,longitude=75,debug=True)]
ax = fig=plt.figure()
HazardMap(RADES=nodes)
#MultiLineSensorPlot(RADES=nodes)