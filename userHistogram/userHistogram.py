import numpy as np
import matplotlib.pyplot as plt

def slice_T_mean_hist(dataFileName, marker, path2Data, caseName, alias):
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['savefig.dpi'] = 100
    
    rawData = np.genfromtxt(path2Data+"/"+caseName+"/"+dataFileName+".csv", delimiter=',', skip_header=1)
    
    T = rawData[:,0]
    
    fig, ax = plt.subplots()

#    n, bins, patches = ax.hist(T, bins=40, weights=np.ones(len(T)) / len(T), color='g')    
    n, bins, patches = ax.hist(T, np.linspace(-0.05,1.05,50), weights=np.ones(len(T)) / len(T), color='darkcyan', normed=False, histtype='stepfilled', alpha=1)
#    n, bins, patches = ax.hist(T, bins=np.linspace(0,1,40), weights=np.ones(len(T)) / len(T), color='g')
#    n, bins, patches = ax.hist(T, bins=40, color='g', normed=True)
    
#    print "bins :", bins
#    print "n :", n
    print "sum(n) : ", sum(n)
#    print "n*bins :", n*1./50
#    print "sum :", sum(n*1./50)
    
    mean = np.mean(T)
    rms  = np.std(T)
    
#    ymin, ymax = ax.get_ylim()
#    xmin, xmax = ax.get_xlim()
    ax.set_xlim(-0.02,1.02)
#    ax.set_xlim(-0.02,1.02)
    ax.set_ylim(0,0.4)
#    xmax=1
#    ymax=30
#    ax.text(xmax*0.7, ymax*0.8, r'$\mu=%.2f$'% mean)
#    ax.text(xmax*0.7, ymax*0.7, r'$\sigma=%.2f$'% rms)
#    ax.grid(True)
    
#    ax.axvline(x=0.5, color='blue', linewidth=1)
    ax.axvline(x=mean, color='red', linewidth=3)
    if (mean-rms) > 0:
        ax.axvline(x=mean-rms, color='black', linewidth=3, linestyle='--')
    if (mean+rms) < 1.0:
        ax.axvline(x=mean+rms, color='black', linewidth=3, linestyle='--')
    
#    ax.set_title(r"$@%s$" % marker)
#    ax.set_xlabel(r'$\overline{T}$')
#    ax.set_ylabel('The number of cells in '+r'$\%$')
    fig.savefig(path2Data+"/"+caseName+"/"+"hist_"+dataFileName[:-1]+".png",  bbox_inches='tight')
    
def slice_nu_mean_hist(dataFileName, marker, path2Data, caseName, alias):
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['savefig.dpi'] = 100
    
    rawData = np.genfromtxt(path2Data+"/"+caseName+"/"+dataFileName+".csv", delimiter=',', skip_header=1)
    
    nu = rawData[:,0]
    
    fig, ax = plt.subplots()
    
    MIN, MAX = 2e-06, 3e-4
#    ax.hist(nu, bins=10 ** np.linspace(np.log10(MIN), np.log10(MAX), 50), facecolor='g', normed=1)
    n, bins, patches = ax.hist(nu, bins=10 ** np.linspace(np.log10(MIN), np.log10(MAX), 50), weights=np.ones(len(nu)) / len(nu),facecolor='darkcyan')
    
#    print "bins :", bins
#    print "n :", n
#    print "sum(n) : ", sum(n)

    mean = np.mean(nu)
    rms  = np.std(nu)
    
#    ymin, ymax = ax.get_ylim()
#    xmin, xmax = ax.get_xlim()
    ax.set_xscale("log")
    ax.set_xlim(1e-06,1e-3)
#    ax.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    ax.set_ylim(0,0.15)
#    xmax=1
#    ymax=30
#    ax.text(xmax*0.7, ymax*0.8, r'$\mu=%.2f$'% mean)
#    ax.text(xmax*0.7, ymax*0.7, r'$\sigma=%.2f$'% rms)
#    ax.grid(True)
    ax.tick_params(axis='both', direction='in', length=4, width=1.5)
    
#    import matplotlib
##    locmin = matplotlib.ticker.LogLocator(base=10.0, subs=(0.1,0.2,0.4,0.6,0.8,1,2,4,6,8,10 ))
#    locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.2,0.4,0.6,0.8),numticks=4)
#    ax.xaxis.set_minor_locator(locmin)
#    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
    
#    ax.axvline(x=0.5, color='blue', linewidth=1)
    ax.axvline(x=MIN, color='orange', linewidth=3, linestyle=':')
    ax.axvline(x=MAX, color='orange', linewidth=3, linestyle=':')
    ax.axvline(x=mean, color='red', linewidth=3)
    if (mean-rms) > MIN:
        ax.axvline(x=mean-rms, color='black', linewidth=3, linestyle='--')
    if (mean+rms) < MAX:
        ax.axvline(x=mean+rms, color='black', linewidth=3, linestyle='--')
    
#    ax.set_title(r"$@%s$" % marker)
#    ax.set_xlabel(r'$\overline{T}$')
#    ax.set_ylabel('The number of cells in '+r'$\%$')
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

#    for case in caseList:
#        slice_T_mean_hist("T_mean_slice_0.0D0","0D",path2Data, case, aliasDict[case])
#        slice_T_mean_hist("T_mean_slice_2.0D0","2D",path2Data, case, aliasDict[case])
#        slice_T_mean_hist("T_mean_slice_4.0D0","4D",path2Data, case, aliasDict[case])
#        slice_T_mean_hist("T_mean_slice_6.0D0","6D",path2Data, case, aliasDict[case])
#        slice_T_mean_hist("T_mean_slice_8.0D0","6D",path2Data, case, aliasDict[case])
        
    for case in casesNonNewtonian:
        slice_nu_mean_hist("nu_mean_slice_0.0D0","0D",path2Data, case, aliasDict[case])
        slice_nu_mean_hist("nu_mean_slice_2.0D0","2D",path2Data, case, aliasDict[case])
        slice_nu_mean_hist("nu_mean_slice_4.0D0","4D",path2Data, case, aliasDict[case])
        slice_nu_mean_hist("nu_mean_slice_6.0D0","6D",path2Data, case, aliasDict[case])
        slice_nu_mean_hist("nu_mean_slice_8.0D0","8D",path2Data, case, aliasDict[case])
        
main()