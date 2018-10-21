import main
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use("fivethirtyeight")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    #data
    nodes = main.nodes
    node1 = nodes[0]
    node2 = nodes[1]
    node3 = nodes[2]





