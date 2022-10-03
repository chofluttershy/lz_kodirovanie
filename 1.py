import matplotlib.pyplot as plt
from matplotlib import animation as ani
import numpy as np

f, ax = plt.subplots()
ax.axis([-25, 25, -25, 25])
l, = ax.plot([], [])


def animate(i):
    if i > 100:
        i = 200 - i
    t = np.linspace(-50, 50, 200) * (i / 200)
    t = np.hstack([t, -t])
    x = np.sqrt(2500 - (np.linspace(-50, 50, 200)) ** 2) * (i / 200)
    x = np.hstack([x, -x])
    l.set_data(t, x)


a = ani.FuncAnimation(f, animate, frames=600, interval=2000.0 / 60)

a.save('gifka.gif', writer='pillow', fps=60)
