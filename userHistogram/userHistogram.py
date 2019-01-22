import numpy as np
import matplotlib.pyplot as plt

def slice_6D_T_mean_hist(path2Data, caseName, alias):
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
    xmin, xmax = ax.get_xlim()
    ax.text((xmax+xmin)/2.0, ymax*0.8, r'$\mu=%.2f$'% mean)
    ax.text((xmax+xmin)/2.0, ymax*0.7, r'$\sigma=%.2f$'% rms)
#    ax.set_xlim(0,1)
    ax.grid(True)
    
#    ax.axvline(x=0.5, color='blue', linewidth=1)
    ax.axvline(x=mean, color='red', linewidth=2)
    ax.axvline(x=mean-rms, color='red', linewidth=2, linestyle=':')
    ax.axvline(x=mean+rms, color='red', linewidth=2, linestyle=':')
    
    ax.set_title(r"$@6D$")
    fig.savefig(path2Data+"/"+caseName+"/"+"slice_6D_T_mean_hist.png",  bbox_inches='tight')
    
def main():
    path2Data="/store/8simu_tmp/shape_square/2a_3_T"
    
    caseList=[
                "BirdCarreau/inlet_0p3",
                "BirdCarreau/inlet_0p5",
                "BirdCarreau/inlet0p5_impinging",
                "Newtonian/Re2400",
                "Newtonian/Re4000",
                "Newtonian/Re4000_impinging",
                "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
                "BirdCarreau/inlet_0p3-a_0p5-setT_St_5"
              ]
              
    aliasDict={
        "BirdCarreau/inlet_0p3"                :r'$NN^{1}_{d}$',
        "Newtonian/Re2400"                     :r'$N^{1}_{d}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":r'$NN^{1}_{d,St=1}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":r'$NN^{1}_{d,St=5}$',
        "BirdCarreau/inlet_0p5"                :r'$NN^{2}_{d}$',
        "Newtonian/Re4000"                     :r'$N^{2}_{d}$',
        "BirdCarreau/inlet0p5_impinging"       :r'$NN^{2}_{i}$',
        "Newtonian/Re4000_impinging"           :r'$N^{2}_{i}$'
    }

    for case in caseList:
        slice_6D_T_mean_hist(path2Data, case, aliasDict[case])
    
main()