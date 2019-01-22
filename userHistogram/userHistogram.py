import numpy as np
import matplotlib.pyplot as plt


plt.style.use('seaborn-white') # from defaut
plt.rcParams.update({'font.size': 20})
plt.rcParams['savefig.dpi'] = 100
    
path2Data="/store/8simu_tmp/shape_square/2a_3_T/Newtonian/Re4000"

rawData = np.genfromtxt(path2Data+"/"+"slice_6D_T_mean0.csv", delimiter=',', skip_header=1)

T = rawData[:,0]

n, bins, patches = plt.hist(T, 50, facecolor='g', normed=1)

mean = np.mean(T)
rms  = np.std(T)

plt.xlabel(r'$T$')
plt.ylabel('The number of cells in '+r'$\%$')
#plt.text(0.5, 0.5, r'$\mu=%.2f,\ \sigma=%.2f$')
plt.xlim(0,1)
plt.grid(True)

plt.axvline(x=0.5, color='black', linewidth=1)
plt.axvline(x=mean, color='red', linewidth=2)
plt.axvline(x=mean-rms, color='red', linewidth=2, linestyle=':')
plt.axvline(x=mean+rms, color='red', linewidth=2, linestyle=':')

plt.savefig(path2Data+"/"+"slice_6D_T_mean_hist.png",  bbox_inches='tight')