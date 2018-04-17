# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 09:31:51 2017

@author: pjcigan

"""

import numpy as np
from scipy import polyfit
from scipy import interpolate
from matplotlib import pyplot as plt
 
plt.rc('font',family='serif') #Just because I prefer serif fonts on my plots
 
#Making the arrays as we did above
xvals=np.arange(-3,5,.2)
yvals_with_nans=xvals**2-7
for i in range( len(yvals_with_nans) ): yvals_with_nans[i]+=2*np.random.randn()
yvals_with_nans[3:10]=np.nan
 
#Masking the NaNs
y_masked=np.ma.masked_invalid(yvals_with_nans)
y_compressed=y_masked.compressed()
x_compressed=np.ma.masked_array(xvals,mask=y_masked.mask).compressed()
 
#Performing additional steps
interpval1=np.interp(-1.8,x_compressed,y_compressed) #let's interpolate when x-val is -1.8
interpval2f=interpolate.interp1d(x_compressed, y_compressed, kind='cubic') # this returns a function
interpval2=interpval2f(-1.8)

fitvals=polyfit(x_compressed,y_compressed,2)
yfit=fitvals[0]*xvals**2+fitvals[1]*xvals+fitvals[2] #Note that I am using xvals here to smoothly fill in the empty region
 
#Actually making the figure
fig1=plt.figure(1)
ax1=fig1.add_subplot(1,2,1)
plt.plot(xvals,yvals_with_nans,'.',color='#153E7E')
plt.xlabel('x'); plt.ylabel('y')
plt.xlim(-3.5,5.5)
plt.title('y_masked',size=10)
 
ax2=fig1.add_subplot(1,2,2)
plt.plot(x_compressed,y_compressed,'.',color='#347C17',label='Compressed Array')
plt.plot(-1.8,interpval1,'s',color='#990000',label='Interpolated Point numpy')
plt.plot(-1.8,interpval2,'s',color='purple',label='Interpolated Point scipy')
plt.plot(xvals,yfit,'--',color='k',label='Quadratic Fit')
leg2=plt.legend(loc=2,prop={'size':8},fancybox=True,handlelength=2.5,numpoints=1)
plt.xlabel('x'); plt.ylabel('y')
plt.xlim(-3.5,5.5)
plt.title('Fit on y_compressed',size=10)
 
#Adding text boxes below the plots with some diagnostic info
ax1.text(0,-.2,'np.min(yvals_with_nans)       = %.2f\nnp.nanmin(yvals_with_nans) = %.2f\nnp.min(y_masked)                 = %.2f'%(np.min(yvals_with_nans),np.nanmin(yvals_with_nans),np.min(y_masked)),ha='left',va='top',transform=ax1.transAxes,size=8,bbox=dict(boxstyle='round',fc='w'))
 
ax2.text(0,-.2,'Best fit:  y = %.2f x$^2$ + %.2f x + %.2f\nTrue function: y = x$^2$ - 7'%(fitvals[0],fitvals[1],fitvals[2]),ha='left',va='top',transform=ax2.transAxes,size=8,bbox=dict(boxstyle='round',fc='w'))
 
plt.suptitle('Sample Arrays with NaNs',size=16)
plt.subplots_adjust(bottom=.5,top=.9,wspace=.4)
 
#plt.show()
plt.savefig('NaN_plot_example1.png',bbox_inches='tight')
plt.clf()