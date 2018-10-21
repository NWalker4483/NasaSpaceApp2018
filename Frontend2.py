import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

class LineGraphMap:
    def __init__(self,RADES):

        self.__data = [[0,]*100 for i in range(100)]
        self.__RADES = RADES

        style.use('fivethirtyeight')

        self.fig = plt.figure()
        self.ax = fig.add_subplot(1,1,1)
        animation.FuncAnimation(self.fig, self.update, interval=1.5)

        plt.show()

    def update(self,data):

        self.pull_sensors()
        data = self.__data

        self.ax.clear()
        self.ax.plot(data)

    def pull_sensors(self):
        
        for node in self.__RADES:
            x, y, rads = node.data
            self.__data[x][y] = rads





