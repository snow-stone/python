# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 10:35:19 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt


def calcU(w, h, N, X, Y):
#Reexamination of Hagen–Poiseuille flow:
#shape-dependence of the hydraulic resistance in microchannels

# change y coord to symmetric
    U = np.zeros(shape=(X.shape))
    for i in range(N):
        n = 2*i-1
        U = U                    \
           + 4*w**2/np.pi**3     \
           * 1.0/n**3            \
           * (1.0                \
             - np.cosh(n*np.pi*X/h) \
               /np.cosh(n*np.pi*w/(2.0*h))   \
             ) \
           * np.sin(n*np.pi*(Y+0.5)/w)
        print "i = ", i
        print U[:,0]
        print U[:,-1]
        print U[0,:]
        print U[-1,:]
    return U



def hagenPoiseuille_squareDuct():
    w = 1.0
    h = 1.0
    
    nx0= 10
    ny0= 10

#    dx= w/nx
#    dy= h/ny
    
    nx=nx0+1
    ny=ny0+1
    
    x = np.zeros(nx)
    y = np.zeros(ny)
    
    #for i in range(nx):
    #    x[i]=i*dx - 0.5
    
    x = np.linspace(-0.5,0.5,nx)
    
    #for i in range(ny):
    #    y[i]=i*dy
    
#    y = np.linspace(0,1,ny)
    y = np.linspace(-0.5,0.5,ny)
        
    print x
    print y
    
    X, Y = np.meshgrid(x, y)
    N = 20
    Uz = np.zeros(shape=(X.shape))
    Uz = calcU(w, h, N, X, Y)
    
    dS = w/(nx-1)**2
    flux = np.sum(Uz*dS)
    print "flux ", flux
    
    fig, ax = plt.subplots()
    
    ax.contour(X, Y, Uz) #draw iso-lines
    img = ax.imshow(Uz, extent=[-0.6, 0.6, -0.6, 0.6], cmap='Greys') # without extend... integers on both x and y axes
    fig.colorbar(img)
    plt.grid()    
    
    print "max(U)"
    
    u_ = 0.0
    for i in range(20):
        n = 2*i-1
        print u_
        u_ = u_                  \
           + 4*w**2/np.pi**3     \
           * 1.0/n**3            \
           * (1.0                \
             - np.cosh(0.0) \
               /np.cosh(n*np.pi*w/(2.0*h))   \
             ) \
           * np.sin(n*np.pi*0.5)

hagenPoiseuille_squareDuct()