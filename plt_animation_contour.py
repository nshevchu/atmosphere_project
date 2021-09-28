import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import matplotlib.pyplot as plt
import numpy as np


xlist = np.linspace(0, 50, 100)
zlist = np.linspace(0, 20, 100)
X, Z = np.meshgrid(xlist, zlist)

print(X)
print(Z)




fig, ax =plt.subplots()
#cp = ax.contourf(X, Y, Z)

# W calculation
import math
lx = 200
lz = 5
T = 4
kx = 2*math.pi/lx
kz = 2*math.pi/lz
sigma = 2*math.pi/T
delta_t = 1
Wamp0 = 1


H=7


def Wamp(Z):
    return Wamp0*np.exp(Z/(2*H))

def z_function(i, X, Z):

    W = Wamp(Z)*np.cos(sigma*i*delta_t-kx*X-kz*Z)
    return W

lev=np.linspace(-7,7,16)

# animation function
def animate(i, cont,ax, X, Z):

    W = z_function(i, X, Z)
    for c in cont.collections:
        try:
            c.remove()  # removes only the contours, leaves the rest intact
        except:
            pass
    ax.cla()
    cont = plt.contourf(X, Z, W , levels = lev)

    plt.title('t = %.2f:  %.2f' % (i, W[5,5]))
    plt.ylabel('z height, km')
    plt.xlabel('x, km')
    return cont



cont = ax.contourf(X, Z, z_function(0, X, Z), levels = lev)



times = np.linspace(0, 10, 100)
animation = FuncAnimation(fig,
                        func=animate,
                        frames=times,
                        fargs=(cont,ax, X, Z),
                        interval=100,
                        repeat=True,
                        #blit=True
                        )

plt.colorbar(cont)
plt.show()