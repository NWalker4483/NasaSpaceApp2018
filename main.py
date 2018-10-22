from NodeStuff import SensorNodeHandler
from Frontend import HazardMap, MultiLineSensorPlot
import matplotlib.pyplot as plt
import time
nodes = [SensorNodeHandler(UDP_PORT=5000,latitude=50,longitude=25,debug=False),
SensorNodeHandler(UDP_PORT = 5001,latitude=25,longitude=50,debug=True)]
HazardMap(RADES=nodes)
MultiLineSensorPlot(RADES=nodes)