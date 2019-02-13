import numpy as np
import matplotlib.pyplot as plt

N = 100

i = np.arange(N)
a = np.sin(i * 2*np.pi/N) + 2*np.sin(i * 4*np.pi/N)
#a = np.append(a, a[0]) # symmetry

print "plot data in time domain"
print "len(a):", len(a)
print "a[0],a[-1]", a[0], a[-1]
print "sampling frequency", N
print "time interval [", (i * 2*np.pi/N)[0], ",", (i * 2*np.pi/N)[-1], "]"

#plt.subplot(211)
#plt.plot(a)

print "=============="
print "FIG1"
print "plot data in time domain"
fig, ax = plt.subplots(5,figsize=(10,10))
ax[0].plot(a)

print "begin rFFT"
A = np.fft.rfft(a)

print "normalization y-axis by N//2"
A = A/(N//2)

print "len(A):", len(A)
print "A[0],A[-1]", A[0], A[-1]
#print "sampling frequency", N
#print "time interval [", (i * 2*np.pi/N)[0], ",", (i * 2*np.pi/N)[-1], "]"

# visualisation de A
# on ajoute a droite la valeur de gauche pour la periodicite
#B = np.append(A, A[0])
print "=============="
print "FIG2"
print "plot data in frequency domain : rfft defaut output"
ax[1].plot(np.real(A),color='forestgreen',marker='^',markeredgecolor='forestgreen',markerfacecolor='none',label='real')
ax[1].plot(np.imag(A),color='mediumvioletred',marker='s',markeredgecolor='mediumvioletred',markerfacecolor='none',label='imag')

ax[1].legend(loc=4)

print "=============="
print "FIG3"
print "zoom"
ax[2].plot(np.real(A),color='forestgreen',marker='^',markeredgecolor='forestgreen',markerfacecolor='none',label='real')
ax[2].plot(np.imag(A),color='mediumvioletred',marker='s',markeredgecolor='mediumvioletred',markerfacecolor='none',label='imag')

ax[2].set_xlim(0,10)
ax[2].legend(loc=4)

print "============="
print "FIG4"
print "plot magnitude"
print "||c||"
B = np.absolute(A)

#ax[3].plot(np.real(B),color='black',marker='^',markeredgecolor='black',markerfacecolor='none')
ax[3].plot(np.arange(len(B)), B,color='black',marker='^',markeredgecolor='black',markerfacecolor='none',label='mag')

#ax[3].set_xlim(0,10)
ax[3].legend(loc=1)

print "============="
print "FIG5"
print "||c|| => normalise now x-axis : frequency"

ax[4].plot((np.arange(len(B))/float(N))[1:], B[1:],color='black',marker='^',markeredgecolor='black',markerfacecolor='none',label='mag')

ax[4].set_xscale('log')
ax[4].set_xlim(10**-3,10)
ax[4].legend(loc=4)

plt.show()
print "Finish plot"

import scipy.io as io
signal={}
x=(np.arange(len(B))/float(N))[1:]
y=B[1:]

signal['fn']=x
signal['Bn']=y
io.savemat('signal',signal)

b = io.loadmat('signal')
print b['fn']