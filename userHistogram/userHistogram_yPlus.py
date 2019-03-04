import numpy as np
import matplotlib.pyplot as plt

def slice_yPlus_hist(dataFileName, path2Data, caseName, alias):
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['savefig.dpi'] = 100
    
    rawData = np.genfromtxt(path2Data+"/"+caseName+"/postProcessing/"+dataFileName, delimiter=' ', skip_header=1)
    
    yPlus = rawData[:,1]
    
    fig, ax = plt.subplots()

    n, bins, patches = ax.hist(yPlus, np.linspace(0,2,50), weights=np.ones(len(yPlus)) / len(yPlus), color='darkcyan', normed=False, histtype='stepfilled', alpha=1)
    
    print "sum(n) : ", sum(n)
    
    mean = np.mean(yPlus)
    rms  = np.std(yPlus)
    
    #ax.set_xlim(-0.02,1.02)
    ax.set_ylim(0,0.4)
    ax.tick_params(axis='both', direction='out', length=8, width=3)
#    ax.set_xticklabels([''])
#    ax.set_yticklabels([''])
    
    ax.axvline(x=mean, color='red', linewidth=3)
    if (mean-rms) > 0:
        ax.axvline(x=mean-rms, color='black', linewidth=3, linestyle='--')
    if (mean+rms) < 1.0:
        ax.axvline(x=mean+rms, color='black', linewidth=3, linestyle='--')
    
    ax.set_xlabel(r'$y^+$')
    ax.set_ylabel(r'$Probabilit\'e$')
    
    fig.savefig(path2Data+"/"+caseName+"/"+"hist_"+dataFileName+".png",  bbox_inches='tight')
    
    
def main():

    from matplotlib import rc
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)    

    path2Data="/store/8simu_tmp/shape_square/2a_3_T"
    
    caseList=[
#                "BirdCarreau/inlet_0p3",
#                "BirdCarreau/inlet_0p5",
#                "BirdCarreau/inlet0p5_impinging",
                "Newtonian/Re2400",
                "Newtonian/Re4000",
                "Newtonian/Re4000_impinging"
#                "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
#                "BirdCarreau/inlet_0p3-a_0p5-setT_St_5"
              ]
    
    casesNonNewtonian=[
                "BirdCarreau/inlet_0p3",
                "BirdCarreau/inlet_0p5",
                "BirdCarreau/inlet0p5_impinging",
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
        slice_yPlus_hist("yPlus_U_mean",path2Data, case, aliasDict[case])

main()
