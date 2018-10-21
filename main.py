from NodeStuff import SensorNodeHandler
from Frontend import HazardMap, MultiLineSensorPlot
nodes = [SensorNodeHandler(UDP_PORT=5000,latitude=40,longitude=80,debug=True),
SensorNodeHandler(UDP_PORT = 5001,latitude=50,longitude=40,debug=True),
SensorNodeHandler(UDP_PORT = 5002,latitude=70,longitude=60,debug=True)]

HazardMap(RADES=nodes)
MultiLineSensorPlot(RADES=nodes)