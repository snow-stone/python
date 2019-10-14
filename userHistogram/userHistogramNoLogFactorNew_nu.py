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

    axis_x1 = np.linspace(0, 1.875, 16)
    axis_x2 = np.linspace(2, 9.5, 16)
    axis_x  = np.append(axis_x1, axis_x2)
    
    higherOrderStat=dict.fromkeys(casesNonNewtonian)
    for case in casesNonNewtonian:
        higherOrderStat[case]={'mean':[],'rms':[],'minimum':[],'maximum':[],'skew':[],'kurt':[],'factor0':[], 'factor1':[], 'factor2':[], 'factor3':[], 'factor4':[], 'mean_tail':[], 'rms_tail':[],'minimum_tail':[],'maximum_tail':[]}
        #higherOrderStat[case]={'mean':[],'rms':[],'minimum':[],'maximum':[],'skew':[],'kurt':[],'factor0':[], 'factor1':[], 'mean_tail':[], 'rms_tail':[],'minimum_tail':[],'maximum_tail':[]}

    for case in casesNonNewtonian:
        #for i, x in enumerate(axis_x):
        for statName in higherOrderStat[case].keys():
            data = np.genfromtxt(path2Data + "/" + case + "/nu_mean_" + statName, delimiter=' ')
            print data
            axis_x = data[:,0]
            higherOrderStat[case][statName]=data[:,1]
            print "========================"
            print "\n"
    
    return axis_x, higherOrderStat
    
def plot_nu_mean_Figures(x, higherOrderStat):
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

    def nu_mean_moment12(x, databaseDict):
        # mean and rms
        fig, ax = plt.subplots(3, 1, figsize=(10,10))
        for axis in ax:
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
            axis.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['mean'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['rms'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[2].plot(x, np.asarray(databaseDict[case]['rms'])/np.asarray(higherOrderStat[case]['mean']), linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].set_ylabel(r"$\mu_{\overline{\nu}}$")
        ax[1].set_ylabel(r"$\sigma_{\overline{\nu}}$")
        ax[2].set_ylabel(r"$\sigma_{\overline{\nu}} / \mu_{\overline{\nu}}$")
        ax[2].set_xlabel(r"$x/D$")
        
        ax[0].text(-0.1,3.4,'(a)',size=20, transform=ax[2].transAxes)
        ax[1].text(-0.1,2.2,'(b)',size=20, transform=ax[2].transAxes)
        ax[2].text(-0.1,1,'(c)',size=20, transform=ax[2].transAxes)  
        ax[2].set_ylim(0.2,1.2)
        fig.savefig("./"+"nu_mean_moment12.png",  bbox_inches='tight')

    def nu_mean_moment34(x, databaseDict):
        fig, ax = plt.subplots(2, figsize=(10,10))
        for axis in ax:
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
    
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['skew'],label='skew', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['kurt'],label=aliasDict[case], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].set_ylim(0,8)
        ax[0].set_ylabel(r"$\gamma_{\overline{\nu}}$")
        ax[1].axhline(y=0., linestyle='-.', color='black')
        ax[1].set_ylim(-10,250)
        ax[1].set_ylabel(r"$\beta_{\overline{\nu}}$")
        ax[1].set_xlabel(r"$x/D$")
    
        ax[0].text(-0.12, 0.9,'(d)', transform=ax[0].transAxes)
        ax[1].text(-0.12, 1.0,'(e)', transform=ax[1].transAxes)
        ax[0].set_xticklabels([])
        fig.savefig("./"+"nu_mean_moment34.png",  bbox_inches='tight')

    def nu_mean_moment34_ratio(x, databaseDict):
        fig, ax = plt.subplots(3, figsize=(10,10))
        for i, axis in enumerate(ax):
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
            axis.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
            if i != (len(ax)-1) :
                axis.set_xticklabels([])
            else :
                axis.set_xlabel(r"$x/D$")
    
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['skew'],label='skew', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['kurt'],label=aliasDict[case], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[2].plot(x, databaseDict[case]['maximum']/databaseDict[case]['minimum'],label=aliasDict[case], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].set_ylim(0,25)
        ax[0].set_ylabel(r"$\gamma_{\overline{\nu}}$")
        ax[1].axhline(y=0., linestyle='-.', color='black')
        ax[1].set_ylim(-100,700)
        ax[1].set_ylabel(r"$\beta_{\overline{\nu}}$")
        ax[2].set_ylim(0,75)
        ax[2].set_ylabel(r"$\overline{\nu}_{max}/\overline{\nu}_{min}$")
    
        ax[0].text(-0.12, 0.9,'(d)', transform=ax[0].transAxes)
        ax[1].text(-0.12, 1.0,'(e)', transform=ax[1].transAxes)
        ax[2].text(-0.12, 1.0,'(f)', transform=ax[2].transAxes)
        fig.savefig("./"+"nu_mean_moment34_ratio.png",  bbox_inches='tight')
        
    def nu_mean_MinMax0(x, databaseDict):
        fig, ax = plt.subplots(4, figsize=(10,10))
        for i, axis in enumerate(ax):
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
            axis.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
            if i != (len(ax)-1) :
                axis.set_xticklabels([])
            else :
                axis.set_xlabel(r"$x/D$")
    
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['maximum'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['minimum'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[2].plot(x, databaseDict[case]['maximum_tail'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[3].plot(x, databaseDict[case]['minimum_tail'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].set_ylabel(r"$max(\overline{\nu})$")
        ax[1].set_ylabel(r"$min(\overline{\nu})$")
        ax[2].set_ylabel(r"$max(tail)$")
        ax[3].set_ylabel(r"$min(tail)$")
    
        ax[0].text(-0.12, 0.9,'(f)', transform=ax[0].transAxes)
        ax[1].text(-0.12, 0.9,'(g)', transform=ax[1].transAxes)
        ax[2].text(-0.12, 0.9,'(h)', transform=ax[2].transAxes)
        ax[3].text(-0.12, 0.9,'(i)', transform=ax[3].transAxes)
        fig.savefig("./"+"nu_mean_MinMax0.png",  bbox_inches='tight')

    def nu_mean_MinMax1(x, databaseDict):
        fig, ax = plt.subplots(2, figsize=(10,10))
        for i, axis in enumerate(ax):
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
            axis.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
            if i != (len(ax)-1) :
                axis.set_xticklabels([])
            else :
                axis.set_xlabel(r"$x/D$")
    
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['maximum']/higherOrderStat[case]['minimum'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['maximum_tail']/higherOrderStat[case]['minimum_tail'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].set_ylabel(r"$max/min$")
        ax[1].set_ylabel(r"$max/min(tail)$")
    
        ax[0].text(-0.12, 0.9,'(j)', transform=ax[0].transAxes)
        ax[1].text(-0.12, 0.9,'(k)', transform=ax[1].transAxes)
        fig.savefig("./"+"nu_mean_MinMax1.png",  bbox_inches='tight')

    def nu_mean_tail0(x, databaseDict):
        fig, ax = plt.subplots(3, figsize=(10,10))
        for i, axis in enumerate(ax):
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
            axis.ticklabel_format(axis='y',style='sci',scilimits=(0,0))
            if i != (len(ax)-1) :
                axis.set_xticklabels([])
            else :
                axis.set_xlabel(r"$x/D$")
    
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['mean_tail'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['rms_tail'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[2].plot(x, higherOrderStat[case]['mean_tail']/(databaseDict[case]['mean']+higherOrderStat[case]['rms']), linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].set_ylabel(r"$\mu^t_{\overline{\nu}}$")
        ax[1].set_ylabel(r"$\sigma^t_{\overline{\nu}}$")
        ax[2].set_ylabel(r"$\zeta$")
    
        ax[0].text(-0.12, 0.9,'(a)', transform=ax[0].transAxes)
        ax[1].text(-0.12, 0.9,'(b)', transform=ax[1].transAxes)
        ax[2].text(-0.12, 0.9,'(c)', transform=ax[2].transAxes)
        fig.savefig("./"+"nu_mean_tail0.png",  bbox_inches='tight')

    def nu_mean_tail1(x, databaseDict):
        from matplotlib.ticker import FuncFormatter
        def to_percent(y, position):
            # Ignore the passed in position. This has the effect of scaling the default
            # tick locations.
            s = str(round((100 * y)))
        
            # The percent symbol needs escaping in latex
            if matplotlib.rcParams['text.usetex'] is True:
                return s + r'$\%$'
            else:
                return s + '%'
        formatter = FuncFormatter(to_percent)

        fig, ax = plt.subplots(2, figsize=(10,10))
        for i, axis in enumerate(ax):
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
            if i != (len(ax)-1) :
                axis.set_xticklabels([])
            else :
                axis.set_xlabel(r"$x/D$")
    
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['mean']+databaseDict[case]['rms'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['factor2'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].ticklabel_format(axis='y',style='sci',scilimits=(0,0))
        ax[0].set_ylabel(r"$\mu_{\overline{\nu}}+\sigma_{\overline{\nu}}$")
        ax[1].set_ylim(0,0.5)
        ax[1].yaxis.set_major_formatter(formatter)
        ax[1].set_ylabel(r"$P(\overline{\nu} \ge \nu_{ref})$")
    
        ax[0].text(-0.16, 1.0,'(d)', transform=ax[0].transAxes)
        ax[1].text(-0.16, 1.0,'(e)', transform=ax[1].transAxes)
        fig.savefig("./"+"nu_mean_tail1.png",  bbox_inches='tight')

    def nu_mean_tail1a(x, databaseDict):
        from matplotlib.ticker import FuncFormatter
        def to_percent(y, position):
            # Ignore the passed in position. This has the effect of scaling the default
            # tick locations.
            s = str(round((100 * y)))
        
            # The percent symbol needs escaping in latex
            if matplotlib.rcParams['text.usetex'] is True:
                return s + r'$\%$'
            else:
                return s + '%'
        formatter = FuncFormatter(to_percent)

        fig, ax = plt.subplots(2, figsize=(10,10))
        for i, axis in enumerate(ax):
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
            if i != (len(ax)-1) :
                axis.set_xticklabels([])
            else :
                axis.set_xlabel(r"$x/D$")
    
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['mean']+databaseDict[case]['rms'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['factor3'], linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].ticklabel_format(axis='y',style='sci',scilimits=(0,0))
        ax[0].set_ylabel(r"$\overline{\nu}_{ex}$")
        ax[1].set_ylim(0,0.5)
        ax[1].yaxis.set_major_formatter(formatter)
        ax[1].set_ylabel(r"$P(\overline{\nu} \ge \overline{\nu}_{ex}(x=0))$")
    
        ax[0].text(-0.16, 1.0,'(a)', transform=ax[0].transAxes)
        ax[1].text(-0.16, 1.0,'(b)', transform=ax[1].transAxes)
        fig.savefig("./"+"nu_mean_tail1a.png",  bbox_inches='tight')

    def nu_mean_factors(x, databaseDict):
        fig, ax = plt.subplots(5,figsize=(10,10))
        for axis in ax:
            axis.tick_params(axis='both', direction='in', length=4, width=1.5)
    
        for case in casesNonNewtonian:
            ax[0].plot(x, databaseDict[case]['factor0'],label='factor0', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[1].plot(x, databaseDict[case]['factor1']/1e-5,label='factor1', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[2].plot(x, databaseDict[case]['factor2'],label='factor2', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[3].plot(x, databaseDict[case]['factor3'],label='factor3', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
            ax[4].plot(x, databaseDict[case]['factor4'],label='factor4', linestyle=linestyleDict[case], linewidth=linewidthDict[case], color=colorDict[case])
    
        ax[0].set_ylim(0.5,1)
        ax[0].axhline(y=0.7, linestyle='-.', color='black')
        ax[0].set_ylabel(r"$\zeta_{\overline{\nu}}$")
        ax[1].set_ylim(0,2.5)
        ax[1].axhline(y=1., linestyle='-.', color='black')
        ax[1].set_ylabel(r"$(\mu_{\overline{\nu}}+\sigma_{\overline{\nu}})/\nu_{ref}$")
        ax[2].set_ylim(0,0.5)
        ax[2].set_ylabel(r"$P(\nu \ge \nu_{ref})$")
        ax[2].set_xlabel(r"$x/D$")
        ax[3].set_ylim(0,0.5)
        ax[3].set_ylabel(r"$P_1(\nu \ge \nu_{ref})$")
        ax[3].set_xlabel(r"$x/D$")
        ax[4].set_ylim(0,0.5)
        ax[4].set_ylabel(r"$P(\nu \ge \mu_{\nu}+\sigma_{\nu})$")
        ax[4].set_xlabel(r"$x/D$")
        fig.savefig("./"+"nu_mean_factors.png",  bbox_inches='tight')


    nu_mean_moment12(x, higherOrderStat)
    nu_mean_moment34(x, higherOrderStat)
    nu_mean_moment34_ratio(x, higherOrderStat)
    nu_mean_MinMax0(x, higherOrderStat)
    nu_mean_MinMax1(x, higherOrderStat)
    nu_mean_tail0(x, higherOrderStat)
    nu_mean_tail1(x, higherOrderStat)
    nu_mean_tail1a(x, higherOrderStat)
    nu_mean_factors(x, higherOrderStat)
    
              
def main():
    x, database = plot_nu_mean()
    plot_nu_mean_Figures(x, database)

main()
