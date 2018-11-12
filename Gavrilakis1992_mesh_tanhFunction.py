# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:06:42 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt


h=0.004
nksi= 256

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
    
print ksi

fig2,ax2 = plt.subplots()

ax2.plot(dx,'o')
