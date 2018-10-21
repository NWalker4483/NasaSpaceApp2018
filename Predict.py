from NodeStuff import SensorNodeHandler
import matplotlib.pyplot as plt
import matplotlib.animation as animation


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)


nodes = [SensorNodeHandler(UDP_PORT=5000,latitude=40,longitude=80,debug=True),
SensorNodeHandler(UDP_PORT=5000,latitude=40,longitude=80,debug=True),
SensorNodeHandler(UDP_PORT=5000,latitude=40,longitude=80,debug=True)]
for node in nodes:
    node.start()

max_view = 30
data_over_time = [[0,]*max_view for _ in range(len(nodes))]
steps = [i for i in range(max_view)]
def animate(i):
        if(len(steps) <= max_view):
            ax1.clear()
            for sense_data in data_over_time:
                ax1.plot(steps, sense_data)
            for i in range(len(nodes)):
                data_over_time[i].pop(0)
                data_over_time[i] += [nodes[i].data['rads']] 
                
ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()








