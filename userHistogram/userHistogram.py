import numpy as np
import matplotlib.pyplot as plt

def slice_T_mean_hist(dataFileName, marker, path2Data, caseName, alias):
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['savefig.dpi'] = 100
    
    rawData = np.genfromtxt(path2Data+"/"+caseName+"/"+dataFileName+".csv", delimiter=',', skip_header=1)
    
    T = rawData[:,0]
    
    fig, ax = plt.subplots()
    
    n, bins, patches = ax.hist(T, 50, facecolor='g', normed=1)
    
    mean = np.mean(T)
    rms  = np.std(T)
    
    ax.set_xlabel(r'$\overline{T}$')
    ax.set_ylabel('The number of cells in '+r'$\%$')
#    ymin, ymax = ax.get_ylim()
#    xmin, xmax = ax.get_xlim()
    ax.set_xlim(-0.2,1.2)
    ax.set_ylim(0,30)
    xmax=1.2
    ymax=30
    ax.text(xmax*0.7, ymax*0.8, r'$\mu=%.2f$'% mean)
    ax.text(xmax*0.7, ymax*0.7, r'$\sigma=%.2f$'% rms)
#    ax.set_xlim(0,1)
    ax.grid(True)
    
#    ax.axvline(x=0.5, color='blue', linewidth=1)
    ax.axvline(x=mean, color='red', linewidth=2)
    ax.axvline(x=mean-rms, color='red', linewidth=2, linestyle=':')
    ax.axvline(x=mean+rms, color='red', linewidth=2, linestyle=':')
    
    ax.set_title(r"$@%s$" % marker)
    fig.savefig(path2Data+"/"+caseName+"/"+"hist_"+dataFileName[:-1]+".png",  bbox_inches='tight')
    
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
        slice_T_mean_hist("T_mean_slice_6.0D0","6D",path2Data, case, aliasDict[case])
    
main()