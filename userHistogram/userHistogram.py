import numpy as np
import matplotlib.pyplot as plt

def slice_6D_T_mean_hist(path2Data, caseName):
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['savefig.dpi'] = 100
    
    rawData = np.genfromtxt(path2Data+"/"+caseName+"/"+"slice_6D_T_mean0.csv", delimiter=',', skip_header=1)
    
    T = rawData[:,0]
    
    fig, ax = plt.subplots()
    
    n, bins, patches = ax.hist(T, 50, facecolor='g', normed=1)
    
    mean = np.mean(T)
    rms  = np.std(T)
    
    ax.set_xlabel(r'$T$')
    ax.set_ylabel('The number of cells in '+r'$\%$')
    ymin, ymax = ax.get_ylim()
    ax.text(0.75, ymax*0.8, r'$\mu=%.2f$'% mean)
    ax.text(0.75, ymax*0.7, r'$\sigma=%.2f$'% rms)
    ax.set_xlim(0,1)
    ax.grid(True)
    
    ax.axvline(x=0.5, color='blue', linewidth=1)
    ax.axvline(x=mean, color='red', linewidth=2)
    ax.axvline(x=mean-rms, color='red', linewidth=2, linestyle=':')
    ax.axvline(x=mean+rms, color='red', linewidth=2, linestyle=':')
    
    fig.savefig(path2Data+"/"+caseName+"/"+"slice_6D_T_mean_hist.png",  bbox_inches='tight')
    
def main():
    path2Data="/store/8simu_tmp/shape_square/2a_3_T"
    caseName="Newtonian/Re4000"
    slice_6D_T_mean_hist(path2Data, caseName)
    
main()