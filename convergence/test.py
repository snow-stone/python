# -*- coding: utf-8 -*-                                                                                                                           
"""
Created on Thu Oct 18 09:06:42 2018

@author: hluo
"""

import matplotlib
matplotlib.use("agg")
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append('/home/hluo/work/git/thesis/Thesis_hluo_new/reference_database') # for rdb
import reference_database as rdb

from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def diffNormL2(v1,v2):
    from numpy import linalg as LA

    return LA.norm(v2-v1)/LA.norm(v2)

def main():
    fig, ax = plt.subplots()

    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UrRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    x = data[:,0]
    y = data[:,1]
    ax.plot(x,y,marker='o')

    z = np.polyfit(x, y, 4)
    functionPolynome = np.poly1d(z)

    ax.plot(x,functionPolynome(x),linestyle='-.')

    fig.savefig('test.png',dpi=100, bbox_inches='tight')

    print "diff : ", diffNormL2(functionPolynome(x),y)

main()
