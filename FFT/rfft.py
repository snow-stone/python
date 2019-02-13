import numpy as np
import matplotlib.pyplot as plt

N = 100

i = np.arange(N)
a = np.sin(i * 2*np.pi/N)# + 2*np.sin(i * 2*np.pi/N)
#a = np.append(a, a[0]) # symmetry

print "plot data in time domain"
print "len(a):", len(a)
print "a[0],a[-1]", a[0], a[-1]
print "sampling frequency", N
print "time interval [", (i * 2*np.pi/N)[0], ",", (i * 2*np.pi/N)[-1], "]"

#plt.subplot(211)
#plt.plot(a)

fig, ax = plt.subplots(3)
ax[0].plot(a)

print "=============="
print "begin rFFT"
A = np.fft.rfft(a)

print "plot data in time domain"
print "len(A):", len(A)
print "A[0],A[-1]", A[0], A[-1]
#print "sampling frequency", N
#print "time interval [", (i * 2*np.pi/N)[0], ",", (i * 2*np.pi/N)[-1], "]"

# visualisation de A
# on ajoute a droite la valeur de gauche pour la periodicite
#B = np.append(A, A[0])
ax[1].plot(np.real(A),color='forestgreen',marker='^',markeredgecolor='forestgreen',markerfacecolor='none',label='real')
ax[1].plot(np.imag(A),color='mediumvioletred',label='imag')

#ax[1].set_xlim(0,10)
ax[1].legend(loc=4)

ax[2].plot(np.real(A),color='forestgreen',marker='^',markeredgecolor='forestgreen',markerfacecolor='none',label='real')
ax[2].plot(np.imag(A),color='mediumvioletred',label='imag')

ax[2].set_xlim(0,10)
ax[2].legend(loc=4)

plt.show()