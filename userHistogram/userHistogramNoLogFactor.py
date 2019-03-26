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
    
def slice_nu_mean_hist_noLog(dataFileName, marker, path2Data, caseName, alias, ifPlotHist):
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 20})
    plt.rcParams['savefig.dpi'] = 100
    
    rawData = np.genfromtxt(path2Data+"/"+caseName+"/"+dataFileName+".csv", delimiter=',', skip_header=1)
    
    nu = rawData[:,0]
    mean = np.mean(nu)
    rms  = np.std(nu)
    print "casename : ", caseName
    print "mean     : ", mean

    if ifPlotHist :
	    fig, ax = plt.subplots()
	    
	    MIN, MAX = 2e-06, 3e-4
	#    ax.hist(nu, bins=10 ** np.linspace(np.log10(MIN), np.log10(MAX), 50), facecolor='g', normed=1)
	    n, bins, patches = ax.hist(nu, bins=np.linspace(MIN, MAX, 1000), weights=np.ones(len(nu)) / len(nu),facecolor='darkcyan')
	    
	#    print "bins :", bins
	#    print "n :", n
	    print "sum(n) : ", sum(n)
	
	#    ymin, ymax = ax.get_ylim()
	#    xmin, xmax = ax.get_xlim()
	#    ax.set_xlim(1e-06,1e-4)
	    ax.set_xlim(2e-06,2e-5)
	    ax.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
	    ax.set_ylim(0,0.15)
	#    xmax=1
	#    ymax=30
	#    ax.text(xmax*0.7, ymax*0.8, r'$\mu=%.2f$'% mean)
	#    ax.text(xmax*0.7, ymax*0.7, r'$\sigma=%.2f$'% rms)
	#    ax.grid(True)
	    ax.tick_params(axis='both', which='major', direction='out', length=8, width=4)
	#    ax.tick_params(axis='x', which='minor', direction='out', length=8, width=2)
	#    ax.set_xticklabels([''])
	#    ax.set_yticklabels([''])
	    
	#    import matplotlib
	##    locmin = matplotlib.ticker.LogLocator(base=10.0, subs=(0.1,0.2,0.4,0.6,0.8,1,2,4,6,8,10 ))
	#    locmin = matplotlib.ticker.LogLocator(base=10.0,subs=(0.2,0.4,0.6,0.8),numticks=4)
	#    ax.xaxis.set_minor_locator(locmin)
	#    ax.xaxis.set_minor_formatter(matplotlib.ticker.NullFormatter())
	    
	#    ax.axvline(x=0.5, color='blue', linewidth=1)
	    ax.axvline(x=MIN, color='orange', linewidth=5, linestyle='-.')
	#    ax.axvline(x=MAX, color='orange', linewidth=3, linestyle=':')
	    ax.axvline(x=mean, color='red', linewidth=5)
	    if (mean-rms) > MIN:
	        ax.axvline(x=mean-rms, color='black', linewidth=5, linestyle='--')
	    if (mean+rms) < MAX:
	        ax.axvline(x=mean+rms, color='black', linewidth=5, linestyle='--')
	    
	#    ax.set_title(r"$@%s$" % marker)
	#    ax.set_xlabel(r'$\overline{T}$')
	#    ax.set_ylabel('The number of cells in '+r'$\%$')
	#    ax.text(-0.1, -0.1, r'$0$', fontsize=40, transform=ax.transAxes)
	#    ax.text(6e-7, 0., r'$0$', fontsize=40)
	#    ax.text(3e-7, 0.13, r'$0.15$', fontsize=40)
	#    ax.text(1e-6, -0.03, r'$10^{-6}$', fontsize=40)
	#    ax.text(5e-6, -0.03, r'$10^{-5}$', fontsize=40)
	#    ax.text(3e-5, -0.03, r'$10^{-4}$', fontsize=40)
	    fig.savefig(path2Data+"/"+caseName+"/"+"hist_"+dataFileName[:-1]+"_noLog.png",  bbox_inches='tight')

    nu_Filtered = filter(lambda x: x > (mean+rms), nu)
    print "len(nu)", len(nu)
    print "len(nu_Filtered)", len(nu_Filtered)
    mean_Filtered = np.mean(nu_Filtered)
    rms_Filtered  = np.std(nu_Filtered)
    print "casename : ", caseName, " with ", dataFileName+".csv"
    print "mean     : ", mean_Filtered

    if ifPlotHist :
	    fig1, ax1 = plt.subplots()
	    n_Filtered, bins_Filetered, patches_Filtered = ax1.hist(nu_Filtered, bins=np.linspace(MIN, MAX, 1000), weights=np.ones(len(nu_Filtered)) / len(nu_Filtered),facecolor='darkcyan')
	    ax1.set_xlim(2e-06,5e-5)
	    ax1.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
	    ax1.set_ylim(0,0.15)
	    ax1.tick_params(axis='both', which='major', direction='out', length=8, width=4)
        # redraw what is in ax, fig
	    ax1.axvline(x=MIN, color='orange', linewidth=5, linestyle='-.')
	    ax1.axvline(x=mean, color='red', linewidth=5)
	    if (mean-rms) > MIN:
	        ax1.axvline(x=mean-rms, color='black', linewidth=5, linestyle='--')
	    if (mean+rms) < MAX:
	        ax1.axvline(x=mean+rms, color='black', linewidth=5, linestyle='--')
        # draw the filtered data
	    ax1.axvline(x=mean_Filtered, color='mediumvioletred', linewidth=5)
	    if (mean_Filtered-rms_Filtered) > MIN:
	        ax1.axvline(x=mean_Filtered-rms_Filtered, color='darkmagenta', linewidth=5, linestyle='--')
	    if (mean_Filtered+rms_Filtered) < MAX:
	        ax1.axvline(x=mean_Filtered+rms_Filtered, color='darkmagenta', linewidth=5, linestyle='--')
	
	    fig1.savefig(path2Data+"/"+caseName+"/"+"histFiltered_"+dataFileName[:-1]+"_noLog.png",  bbox_inches='tight')
    
    import scipy.stats as stats
    
    skew = stats.skew(nu)
    kurt = stats.kurtosis(nu)
    ratio0 = (mean+rms)/mean_Filtered
    ratio1 = mean+rms

    if ifPlotHist :
        ratio2 = sum(n[33:]) # approx= 1000/30.
        print "ratio2 :", ratio2
        return skew, kurt, ratio0, ratio1, ratio2
    else :
        return skew, kurt, ratio0, ratio1
    
def main():

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
    
    higherOrderStat=dict.fromkeys(casesNonNewtonian)
    for case in casesNonNewtonian:
        higherOrderStat[case]={'skew':[],'kurt':[],'factor0':[], 'factor1':[], 'factor2':[]}

    for case in casesNonNewtonian:
        for i, x in enumerate(axis_x):
            skew, kurt, factor0, factor1, factor2 = slice_nu_mean_hist_noLog("nu_mean_slice_"+str(x)+"D0",str(x)+"D",path2Data, case, aliasDict[case], ifPlotHist=True)
            #skew, kurt, factor0, factor1 = slice_nu_mean_hist_noLog("nu_mean_slice_"+str(x)+"D0",str(x)+"D",path2Data, case, aliasDict[case], ifPlotHist=False)
            higherOrderStat[case]['skew'].append(skew)
            higherOrderStat[case]['kurt'].append(kurt)
            higherOrderStat[case]['factor0'].append(factor0)
            higherOrderStat[case]['factor1'].append(factor1)
            higherOrderStat[case]['factor2'].append(factor2)
            print "========================"
            print "\n"
    
    # A plot for skew and kurt for each case
    # but before that, save data
    for case in casesNonNewtonian:
        for key, value in higherOrderStat[case].iteritems():
            output2Txt(path2Data + "/" + case + "/nu_mean_" + key, axis_x, value) 

    for case in casesNonNewtonian:
        fig, ax = plt.subplots(2,figsize=(16,10))
        ax[0].plot(higherOrderStat[case]['skew'],label='skew',marker='^',markersize=16,linestyle='--',color=colorDict[case])
        #ax[0].legend()
        ax[0].set_ylim(0,20)
        ax[0].set_ylabel("skew")
        ax[1].plot(higherOrderStat[case]['kurt'],label='kurt',marker='^',markersize=16,linestyle='--',color=colorDict[case])
        #ax[1].legend()
        ax[1].axhline(y=0., linestyle='-.', color='black')
        ax[1].set_ylim(-10,350)
        ax[1].set_ylabel("kurtosis")
        fig.suptitle(aliasDict[case])
        fig.savefig(path2Data+"/"+case+"/"+"higherOrderStat.png",  bbox_inches='tight')
     
#    #
#    # One plot for these cases
#    casesNonNewtonian=[
#                "BirdCarreau/inlet_0p3",
#                "BirdCarreau/inlet_0p5",
#                "BirdCarreau/inlet0p5_impinging"
#    ]
#    markerDict={
#        "BirdCarreau/inlet_0p3"                : '^',
#        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '',
#        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": '',
#        "BirdCarreau/inlet_0p5"                : 'v',
#        "BirdCarreau/inlet0p5_impinging"       : 'o',
#    }
#
#    linestyleDict={
#        "BirdCarreau/inlet_0p3"                : '-',
#        "Newtonian/Re2400"                     : '--',
#        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '-',
#        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": '-',
#        "BirdCarreau/inlet_0p5"                : '-.',
#        "Newtonian/Re4000"                     : '-',
#        "BirdCarreau/inlet0p5_impinging"       : '--',
#        "Newtonian/Re4000_impinging"           : '-'
#    }
#    
#    linewidthDict={
#        "BirdCarreau/inlet_0p3"                : 4,
#        "Newtonian/Re2400"                     : 1,
#        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 4,
#        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 4,
#        "BirdCarreau/inlet_0p5"                : 4,
#        "Newtonian/Re4000"                     : 1,
#        "BirdCarreau/inlet0p5_impinging"       : 4,
#        "Newtonian/Re4000_impinging"           : 1
#    }
#
#    fig, ax = plt.subplots(2, figsize=(10,10))
#    for axis in ax:
#        axis.tick_params(axis='both', direction='in', length=4, width=1.5)
#
#    for case in casesNonNewtonian:
#        #ax[0].plot(axis_x, higherOrderStat[case]['skew'],label='skew',marker=markerDict[case],markersize=16,linestyle='--',color=colorDict[case])
#        ax[0].plot(axis_x, higherOrderStat[case]['skew'],label='skew', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
#        #ax[1].plot(axis_x, higherOrderStat[case]['kurt'],label=aliasDict[case],marker=markerDict[case],markersize=16,linestyle='--',color=colorDict[case])
#        ax[1].plot(axis_x, higherOrderStat[case]['kurt'],label=aliasDict[case], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
#
#    #ax[0].legend()
#    ax[0].set_ylim(0,25)
#    ax[0].set_ylabel(r"$\gamma_{\overline{\nu}}$")
#    ax[1].axhline(y=0., linestyle='-.', color='black')
#    #ax[1].legend(bbox_to_anchor=(1, 2.5), ncol=3, shadow=True, fontsize=20, handlelength=2.5)
#    ax[1].set_ylim(-10,700)
#    ax[1].set_ylabel(r"$\beta_{\overline{\nu}}$")
#    ax[1].set_xlabel(r"$x/D$")
#
#    ax[0].text(-0.12, 0.9,'(d)', transform=ax[0].transAxes)
#    ax[1].text(-0.12, 1.0,'(e)', transform=ax[1].transAxes)
#    ax[0].set_xticklabels([])
#    fig.savefig("./"+"higherOrderStat_noLog.png",  bbox_inches='tight')
#
#    fig, ax = plt.subplots(3,figsize=(10,10))
#    for axis in ax:
#        axis.tick_params(axis='both', direction='in', length=4, width=1.5)
#
#    for case in casesNonNewtonian:
#        ax[0].plot(axis_x, higherOrderStat[case]['factor0'],label='factor0', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
#        ax[1].plot(axis_x, np.asarray(higherOrderStat[case]['factor1'])/1e-5,label='factor1', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
#        ax[2].plot(axis_x, higherOrderStat[case]['factor2'],label='factor2', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
#    ax[0].set_ylim(0.5,1)
#    ax[0].axhline(y=0.7, linestyle='-.', color='black')
#    ax[0].set_ylabel(r"$\zeta_{\overline{\nu}}$")
#    ax[1].set_ylim(0,2.5)
#    ax[1].axhline(y=1., linestyle='-.', color='black')
#    ax[1].set_ylabel(r"$(\mu_{\overline{\nu}}+\sigma_{\overline{\nu}})/\nu_{ref}$")
#    ax[2].set_ylim(0,0.5)
#    ax[2].set_ylabel(r"$\psi(\nu_{ref})$")
#    ax[2].set_xlabel(r"$x/D$")
#    fig.savefig("./"+"factor_noLog.png",  bbox_inches='tight')
              
main()
