import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt

def output2Txt(fileName, x, y):
    import os    
    if (os.path.exists('data')):
        print "path data exists\n"
    else:
        os.mkdir('data')
    
    f = open(fileName, "w+")
    for i in range(len(x)):
        f.write("%.6f %.6f\n" % (x[i], y[i]))
    print "writing to " + fileName
    f.close()

def slice_T_mean_hist(dataFileName, marker, path2Data, caseName, alias, ifPlotHist):
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['savefig.dpi'] = 100
    
    rawData = np.genfromtxt(path2Data+"/"+caseName+"/"+dataFileName+".csv", delimiter=',', skip_header=1)

    T = rawData[:,0]
    mean = np.mean(T)
    rms  = np.std(T)
    
    print "casename : ", caseName, " with ", dataFileName+".csv"
    print "mean     : ", mean
    
    if ifPlotHist :
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
        ax.tick_params(axis='both', direction='out', length=8, width=3)
        ax.set_xticklabels([''])
        ax.set_yticklabels([''])
        
    #    ax.axvline(x=0.5, color='blue', linewidth=1)
        ax.axvline(x=mean, color='red', linewidth=3)
        if (mean-rms) > 0:
            ax.axvline(x=mean-rms, color='black', linewidth=3, linestyle='--')
        if (mean+rms) < 1.0:
            ax.axvline(x=mean+rms, color='black', linewidth=3, linestyle='--')
        
    #    ax.set_title(r"$@%s$" % marker)
    #    ax.set_xlabel(r'$\overline{T}$')
    #    ax.set_ylabel('The number of cells in '+r'$\%$')
    #    plt.tick_params(
    #    axis='x',          # changes apply to the x-axis
    #    which='both',      # both major and minor ticks are affected
    #    bottom=False,      # ticks along the bottom edge are off
    #    top=False,         # ticks along the top edge are off
    #    labelbottom=False) # labels along the bottom edge are off
        ax.text(-0.17, 0.35, r'$0.4$', fontsize=30)
        ax.text(-0.17, 0.15, r'$0.2$', fontsize=30)
        ax.text(-0.1, -0, r'$0$', fontsize=30)
        ax.text(0, -0.05, r'$0$', fontsize=30)
        ax.text(0.45, -0.05, r'$0.5$', fontsize=30)
        ax.text(1, -0.05, r'$1$', fontsize=30)
        
        fig.savefig(path2Data+"/"+caseName+"/"+"hist_"+dataFileName[:-1]+".png",  bbox_inches='tight')

    import scipy.stats as stats
    
    skew = stats.skew(T)
    kurt = stats.kurtosis(T)

    return skew, kurt
    
    
def writeData_T_mean():

    from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)    
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['savefig.dpi'] = 100

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
#                "BirdCarreau/inlet_0p5",
#                "BirdCarreau/inlet0p5_impinging",
#                "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
#                "BirdCarreau/inlet_0p3-a_0p5-setT_St_5"    
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

    colorDict={
        "BirdCarreau/inlet_0p3"                : 'mediumvioletred',
        "Newtonian/Re2400"                     : 'darkred',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 'red',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 'red',
        "BirdCarreau/inlet_0p5"                : 'steelblue',
        "Newtonian/Re4000"                     : 'red',
        "BirdCarreau/inlet0p5_impinging"       : 'darkmagenta',
        "Newtonian/Re4000_impinging"           : 'darkcyan'
    }

    axis_x1 = np.linspace(0, 1.875, 16)
    axis_x2 = np.linspace(2, 9.5, 16)
    axis_x  = np.append(axis_x1, axis_x2)
    #axis_x  = np.linspace(0, 8, 5)
    
    higherOrderStat=dict.fromkeys(casesNonNewtonian)
    for case in casesNonNewtonian:
        #higherOrderStat[case]={'skew':[],'kurt':[],'factor0':[], 'factor1':[], 'factor2':[]}
        higherOrderStat[case]={'skew':[],'kurt':[]}

    for case in casesNonNewtonian:
        for i, x in enumerate(axis_x):
            #skew, kurt, factor0, factor1, factor2 = slice_nu_mean_hist_noLog("nu_mean_slice_"+str(x)+"D0",str(x)+"D",path2Data, case, aliasDict[case], ifPlotHist=True)
            skew, kurt = slice_T_mean_hist("T_mean_slice_"+str(x)+"D0",str(x)+"D_New",path2Data, case, aliasDict[case], ifPlotHist=True)
            higherOrderStat[case]['skew'].append(skew)
            higherOrderStat[case]['kurt'].append(kurt)
            #higherOrderStat[case]['factor0'].append(factor0)
            #higherOrderStat[case]['factor1'].append(factor1)
            #higherOrderStat[case]['factor2'].append(factor2)
            print "========================"
            print "\n"
    
    for case in casesNonNewtonian:
        for key, value in higherOrderStat[case].iteritems():
            output2Txt(path2Data + "/" + case + "/T_mean_" + key, axis_x, value) 

def main():
    writeData_T_mean()

main()
