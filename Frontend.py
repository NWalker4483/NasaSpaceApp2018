import numpy as np
import matplotlib.pyplot as plt
import time
import matplotlib.animation as animation

class HazardMap:
    def __init__(self,RADES):
        self.__data = [[0,]*100 for i in range(100)]
        self.__RADES = RADES
        self.fig, self.ax = plt.subplots(1, 1)
        animation.(self.fig, self.update, interval=1.5)
        plt.show()
    def update(self,data):
        self.pull_sensors()
        data = self.__data
        self.ax.pcolor(data) #Heatmap
    def pull_sensors(self):
        for node in self.__RADES:
            x, y, rads = node.data
            self.__data[x][y] = rads