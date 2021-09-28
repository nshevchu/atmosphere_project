import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()
ax.set_xlim(0, 105)
ax.set_ylim(-1, 1)

line, = ax.plot(0,0)


def animation_frame(i):
    x_data.append(i*10)
    y_data.append(np.sin(i**2))

    line.set_xdata(x_data)
    line.set_ydata(y_data)
    return line,

animation = FuncAnimation(fig=fig,
                          func=animation_frame,
                          frames=np.arange(0, 1, 0.01),
                          interval=1
                          )
plt.show()