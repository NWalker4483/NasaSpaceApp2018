import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation
from itertools import combinations

class HazardMap:
    def __init__(self,RADES,size=(100,100)):
        self.__data = np.array([[1,]*size[0] for i in range(size[1])])
        self.__RADES = RADES
        self.size = size
        self.plt = plt
        self.fig, self.ax = self.plt.subplots(1, 1)

        self.ani = animation.FuncAnimation(self.fig, self.plot, interval=1)
        self.plt.show()

    def reset(self):
        self.__data = np.array([[0,]*self.size[0] for i in range(self.size[1])])

    def euclidean_distance(self,point1, point2):
        return (abs(point1[0]-point2[0])**2+abs(point1[1]-point2[1])**2)**.5
        
    def plot(self,data):
        self.pull_sensors_data()
        data = self.__data
        self.ax.pcolorfast(data,cmap="jet") # Heatmap
        self.reset() # Reset Map Data

    def get_neighbors(self,node,rads):
        neigh=set()
        for y, x in combinations(list(range(-(rads//2),(rads//2)+1))*2, 2):
            if (0<=(node[0]+y)<self.size[1]) and (0<=(node[1]+x)<self.size[0]):
                neigh.add((node[0]+y,node[1]+x))
        return neigh

    def pull_sensors_data(self):
        for node in self.__RADES:
            self.update_rads(node)

    def update_rads(self,node):
        rads = node.data['rads']
        for x2,y2 in self.get_neighbors([node.longitude,node.latitude],rads):
            distance = self.euclidean_distance([node.longitude,node.latitude],[x2,y2])

            self.__data[x2][y2] += 6*(rads/(distance if distance != 0 else 1))
        self.__data[node.longitude][node.latitude] += rads
