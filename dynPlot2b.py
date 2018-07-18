#!/bin/env python

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np

#style.use('fivethirtyeight')

#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)

fig, ax = plt.subplots()

def animate(i):
    data = np.genfromtxt('logs/CourantMax_0')
    xs = data[:,0]
    ys = data[:,1]
    ax.clear()
    ax.plot(xs, ys)
    
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()
