#!/bin/env python

import scipy.io as io
import numpy as np

y1=np.array([1,2,3,4])
y2=np.array([10,20,30,40])
y3=np.array([100,200,300,400])

a={}
a['test1']=y1
a['test2']=y2
a['test3']=y3
io.savemat('temp',a)
b = io.loadmat('temp')

print b['test1']
print b['test2']
print b['test3']
