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

def plot_T_mean():

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
                "BirdCarreau/inlet_0p3"#,
                #"BirdCarreau/inlet_0p5",
                #"BirdCarreau/inlet0p5_impinging",
                #"BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
                #"BirdCarreau/inlet_0p3-a_0p5-setT_St_5"    
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

    #axis_x1 = np.linspace(0, 1.875, 16)
    #axis_x2 = np.linspace(2, 9.5, 16)
    #axis_x  = np.append(axis_x1, axis_x2)
    
    higherOrderStat=dict.fromkeys(casesNonNewtonian)
    for case in casesNonNewtonian:
        higherOrderStat[case]={'skew':[],'kurt':[]}

    for case in casesNonNewtonian:
        #for i, x in enumerate(axis_x):
        for statName in higherOrderStat[case].keys():
            data = np.genfromtxt(path2Data + "/" + case + "/T_mean_" + statName, delimiter=' ')
            print data
            axis_x = data[:,0]
            higherOrderStat[case][statName]=data[:,1]
            print "========================"
            print "\n"
    
    # One plot for these cases
    casesNonNewtonian=[
                "BirdCarreau/inlet_0p3"#,
                #"BirdCarreau/inlet_0p5",
                #"BirdCarreau/inlet0p5_impinging"
    ]
    markerDict={
        "BirdCarreau/inlet_0p3"                : '^',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": '',
        "BirdCarreau/inlet_0p5"                : 'v',
        "BirdCarreau/inlet0p5_impinging"       : 'o',
    }

    linestyleDict={
        "BirdCarreau/inlet_0p3"                : '-',
        "Newtonian/Re2400"                     : '--',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '-',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": '-',
        "BirdCarreau/inlet_0p5"                : '-.',
        "Newtonian/Re4000"                     : '-',
        "BirdCarreau/inlet0p5_impinging"       : '--',
        "Newtonian/Re4000_impinging"           : '-'
    }
    
    linewidthDict={
        "BirdCarreau/inlet_0p3"                : 4,
        "Newtonian/Re2400"                     : 1,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 4,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 4,
        "BirdCarreau/inlet_0p5"                : 4,
        "Newtonian/Re4000"                     : 1,
        "BirdCarreau/inlet0p5_impinging"       : 4,
        "Newtonian/Re4000_impinging"           : 1
    }

    fig, ax = plt.subplots(2, figsize=(10,10))
    for axis in ax:
        axis.tick_params(axis='both', direction='in', length=4, width=1.5)

    for case in casesNonNewtonian:
        #ax[0].plot(axis_x, higherOrderStat[case]['skew'],label='skew',marker=markerDict[case],markersize=16,linestyle='--',color=colorDict[case])
        ax[0].plot(axis_x, higherOrderStat[case]['skew'],label='skew', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
        #ax[1].plot(axis_x, higherOrderStat[case]['kurt'],label=aliasDict[case],marker=markerDict[case],markersize=16,linestyle='--',color=colorDict[case])
        ax[1].plot(axis_x, higherOrderStat[case]['kurt'],label=aliasDict[case], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])

    #ax[0].legend()
    ax[0].set_ylim(0,25)
    ax[0].set_ylabel(r"$\gamma_{\overline{\nu}}$")
    ax[1].axhline(y=0., linestyle='-.', color='black')
    #ax[1].legend(bbox_to_anchor=(1, 2.5), ncol=3, shadow=True, fontsize=20, handlelength=2.5)
    ax[1].set_ylim(-10,700)
    ax[1].set_ylabel(r"$\beta_{\overline{\nu}}$")
    ax[1].set_xlabel(r"$x/D$")

    ax[0].text(-0.12, 0.9,'(d)', transform=ax[0].transAxes)
    ax[1].text(-0.12, 1.0,'(e)', transform=ax[1].transAxes)
    ax[0].set_xticklabels([])
    fig.savefig("./"+"c_mean_higherOrderStat_noLog.png",  bbox_inches='tight')

    fig, ax = plt.subplots(3,figsize=(10,10))
    for axis in ax:
        axis.tick_params(axis='both', direction='in', length=4, width=1.5)

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
#    fig.savefig("./"+"c_mean_factor_noLog.png",  bbox_inches='tight')
    
def plot_nu_mean():

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

    #axis_x1 = np.linspace(0, 1.875, 16)
    #axis_x2 = np.linspace(2, 9.5, 16)
    #axis_x  = np.append(axis_x1, axis_x2)
    
    higherOrderStat=dict.fromkeys(casesNonNewtonian)
    for case in casesNonNewtonian:
        higherOrderStat[case]={'skew':[],'kurt':[],'factor0':[], 'factor1':[], 'factor2':[]}

    for case in casesNonNewtonian:
        #for i, x in enumerate(axis_x):
        for statName in higherOrderStat[case].keys():
            data = np.genfromtxt(path2Data + "/" + case + "/nu_mean_" + statName, delimiter=' ')
            print data
            axis_x = data[:,0]
            higherOrderStat[case][statName]=data[:,1]
            print "========================"
            print "\n"
    
    # One plot for these cases
    casesNonNewtonian=[
                "BirdCarreau/inlet_0p3",
                "BirdCarreau/inlet_0p5",
                "BirdCarreau/inlet0p5_impinging"
    ]
    markerDict={
        "BirdCarreau/inlet_0p3"                : '^',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": '',
        "BirdCarreau/inlet_0p5"                : 'v',
        "BirdCarreau/inlet0p5_impinging"       : 'o',
    }

    linestyleDict={
        "BirdCarreau/inlet_0p3"                : '-',
        "Newtonian/Re2400"                     : '--',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '-',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": '-',
        "BirdCarreau/inlet_0p5"                : '-.',
        "Newtonian/Re4000"                     : '-',
        "BirdCarreau/inlet0p5_impinging"       : '--',
        "Newtonian/Re4000_impinging"           : '-'
    }
    
    linewidthDict={
        "BirdCarreau/inlet_0p3"                : 4,
        "Newtonian/Re2400"                     : 1,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 4,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 4,
        "BirdCarreau/inlet_0p5"                : 4,
        "Newtonian/Re4000"                     : 1,
        "BirdCarreau/inlet0p5_impinging"       : 4,
        "Newtonian/Re4000_impinging"           : 1
    }

    fig, ax = plt.subplots(2, figsize=(10,10))
    for axis in ax:
        axis.tick_params(axis='both', direction='in', length=4, width=1.5)

    for case in casesNonNewtonian:
        #ax[0].plot(axis_x, higherOrderStat[case]['skew'],label='skew',marker=markerDict[case],markersize=16,linestyle='--',color=colorDict[case])
        ax[0].plot(axis_x, higherOrderStat[case]['skew'],label='skew', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
        #ax[1].plot(axis_x, higherOrderStat[case]['kurt'],label=aliasDict[case],marker=markerDict[case],markersize=16,linestyle='--',color=colorDict[case])
        ax[1].plot(axis_x, higherOrderStat[case]['kurt'],label=aliasDict[case], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])

    #ax[0].legend()
    ax[0].set_ylim(0,25)
    ax[0].set_ylabel(r"$\gamma_{\overline{\nu}}$")
    ax[1].axhline(y=0., linestyle='-.', color='black')
    #ax[1].legend(bbox_to_anchor=(1, 2.5), ncol=3, shadow=True, fontsize=20, handlelength=2.5)
    ax[1].set_ylim(-10,700)
    ax[1].set_ylabel(r"$\beta_{\overline{\nu}}$")
    ax[1].set_xlabel(r"$x/D$")

    ax[0].text(-0.12, 0.9,'(d)', transform=ax[0].transAxes)
    ax[1].text(-0.12, 1.0,'(e)', transform=ax[1].transAxes)
    ax[0].set_xticklabels([])
    fig.savefig("./"+"higherOrderStat_noLog.png",  bbox_inches='tight')

    fig, ax = plt.subplots(3,figsize=(10,10))
    for axis in ax:
        axis.tick_params(axis='both', direction='in', length=4, width=1.5)

    for case in casesNonNewtonian:
        ax[0].plot(axis_x, higherOrderStat[case]['factor0'],label='factor0', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
        ax[1].plot(axis_x, np.asarray(higherOrderStat[case]['factor1'])/1e-5,label='factor1', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
        ax[2].plot(axis_x, higherOrderStat[case]['factor2'],label='factor2', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    ax[0].set_ylim(0.5,1)
    ax[0].axhline(y=0.7, linestyle='-.', color='black')
    ax[0].set_ylabel(r"$\zeta_{\overline{\nu}}$")
    ax[1].set_ylim(0,2.5)
    ax[1].axhline(y=1., linestyle='-.', color='black')
    ax[1].set_ylabel(r"$(\mu_{\overline{\nu}}+\sigma_{\overline{\nu}})/\nu_{ref}$")
    ax[2].set_ylim(0,0.5)
    ax[2].set_ylabel(r"$\psi(\nu_{ref})$")
    ax[2].set_xlabel(r"$x/D$")
    fig.savefig("./"+"factor_noLog.png",  bbox_inches='tight')
              
def main():
    #plot_nu_mean()
    plot_T_mean()


main()
