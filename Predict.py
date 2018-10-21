from NodeStuff import SensorNodeHandler
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


style.use("fivethirtyeight")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


nodes = [SensorNodeHandler(UDP_PORT=5000,latitude=40,longitude=80,debug=True)]

for node in nodes:
    node.start()

time = []
data_over_time = []
t = 0
def animate(i):

    for node in nodes:
        if(len(time) <= 30):
            ax1.clear()
            ax1.plot(time, data_over_time)
            data_over_time.append(node.data['rads'])

            time.append(len(time) + 1)
            print(time)
            print(data_over_time)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()








