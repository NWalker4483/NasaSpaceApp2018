import matplotlib.pyplot as plt
# draw the figure so the animations will work
fig = plt.gcf()
fig.show()
fig.canvas.draw()
x=[0]
y=[0]
while True:
    # compute something
    plt.plot(x, y) # plot something
    x.append(x[-1]+1)
    y.append(y[-1]+1)
    # update canvas immediately
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.pause(0.2)  # I ain't needed!!!
    fig.canvas.draw()