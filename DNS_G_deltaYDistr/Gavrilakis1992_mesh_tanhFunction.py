# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:06:42 2018

@author: hluo
"""

import numpy as np
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

plt.style.use('seaborn-white') # from defaut
plt.rcParams.update({'font.size': 30})
plt.rcParams['savefig.dpi'] = 100

from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

h=0.004
nksi= 127

ksi = np.zeros(nksi)
x = np.zeros(nksi)
dx = np.zeros(nksi)

dksi= 2.0/(nksi-1)
c = 1.8417


for i in range(nksi):
    ksi[i]=i*dksi -1
    x[i]=h*(1+np.tanh(c*ksi[i])/np.tanh(c))
    if i != 0:
        dx[i]= x[i] - x[i-1]
    else :
        dx[i]= 0.
    
#print ksi

fig,ax = plt.subplots(figsize=(16,10))

ax.plot(dx[1:],linestyle='-',linewidth=4)
ax.set_xlim(0,nksi)
#ax.set_ylim(0,nksi)
ax.set_xlabel(r'$No. \; de \; cellule$')
ax.set_ylabel(r'$\Delta x$')
ax.text(0.8, 0.8, r'$\frac{\Delta x_{max}}{\Delta x_{min}} \approx %.2f$'%(max(dx[1:]) / min(dx[1:])), horizontalalignment='center',verticalalignment='center', transform=ax.transAxes)

print max(dx[1:]) / min(dx[1:])

fig.savefig('deltaY_distribution.png')
