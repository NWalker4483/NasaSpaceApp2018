
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import time
import matplotlib.animation as animation

NUMBER_X: int = 1
NUMBER_Y: int = 1

CANVAS_WIDTH:  int = 100
CANVAS_HEIGHT: int = 100

def heatmap_animation1():
    fig, ax_lst = plt.subplots(NUMBER_X, NUMBER_Y)
    ax_lst = ax_lst

    def plot(data):
        data = np.random.rand(CANVAS_WIDTH, CANVAS_HEIGHT)
        ax_lst.pcolor(data) #Heatmap
    ani = animation.FuncAnimation(fig, plot, interval=1)
    plt.show()
heatmap_animation1()