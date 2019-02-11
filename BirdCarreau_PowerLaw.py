# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 09:06:42 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt

gama = np.linspace(0.1,100000,10000000)

nu0=3e-4
nuInf=2e-6

k=1
n=0.326

a=2 # defaut BirdCarreau in OpenFOAM

#nu = gama**2
nu = nuInf + (nu0-nuInf)*(1.0+(k*gama)**a)**((n-1.0)/a)

n1=0.6
nu1= nu0 * gama**(n-1.0)



fig,ax = plt.subplots(figsize=(10,5),frameon=True)

ax.set_xlim(0.1,100000)
ax.set_ylim(1e-6,5e-4)
ax.set_xscale("log")
ax.set_yscale("log")
ax.tick_params(axis='both', direction='out', length=4, width=1, labelsize=25)
ax.set_xlabel(r'$\dot{\gamma}$',fontsize=25)
ax.set_ylabel(r'$\nu$',fontsize=25)

font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 25,
        }
ax.text(5, 1e-5, r'$\nu \propto \dot{\gamma}^{1-n}$', fontdict=font)
ax.plot(gama,nu,linewidth=4, label='Xanthan gum')
ax.plot(gama,nu1,linewidth=4,linestyle='--',color='darkred')
ax.legend(fancybox=True, bbox_to_anchor=(1, 1), ncol=1,frameon=False, fontsize=25)
fig.savefig('BirdCarreau.png',dpi=100, bbox_inches='tight')

########################################################################
#fig1,ax1 = plt.subplots()
#
#gama = np.linspace(0.1,100000,10000000)
#
#nu0=5e-6
#nuInf=2e-7
#
#k=1
#n=0.326
#
#a=2 # defaut BirdCarreau in OpenFOAM
#
##nu = gama**2
#nu = nuInf + (nu0-nuInf)*(1.0+(k*gama)**a)**((n-1.0)/a)
#
#n=0.6
#nu1 = nuInf + (nu0-nuInf)*(1.0+(k*gama)**a)**((n-1.0)/a)
#
##n1=0.6
##nu1= nu0 * gama**(n1-1.0)
#ax1.plot(gama,nu,linewidth=2,label='nu')
#ax1.plot(gama,nu1,linewidth=2,label='nu1')
#ax1.set_xscale("log")
#ax1.set_yscale("log")
#ax1.legend()

