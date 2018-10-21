from NodeStuff import SensorNodeHandler
from Frontend import HazardMap
nodes = [SensorNodeHandler(UDP_PORT=5000),
SensorNodeHandler(UDP_PORT = 5001,latitude=50,longitude=40),
SensorNodeHandler(UDP_PORT = 5002,latitude=70,longitude=40)]
for node in nodes:
    node.start()
HazardMap(RADES=nodes)