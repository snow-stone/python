import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt

def slice_nu_mean_hist_noLog():
    from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)    
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 40})
    plt.rcParams['savefig.dpi'] = 100
    
    turb = np.genfromtxt("/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau/inlet_0p5/"+"nu_mean_slice_0.0D_New.csv", delimiter=',', skip_header=1)
    #lam  = np.genfromtxt("/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau/inlet_0p5/"+"Port3_inlet1_9D_down.csv", delimiter=',', skip_header=1)
    lam  = np.genfromtxt("/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau/inlet_0p5/"+"nu_mean_slice_m1.0D_New.csv", delimiter=',', skip_header=1)

    dS_data = np.genfromtxt("/store/8simu_tmp/shape_square/2a_3_T/sliceStore/dS.csv",delimiter=',', skip_header=0)
    
    #nu = turb[:,0]
    nu = lam[:,0]
    label = turb[:,1]
    mean = np.mean(nu)
    rms  = np.std(nu)

    #dS = dS_data[:,0] # IndexError: too many indices for array
    dS = dS_data
    S  = 0.008**2
    dS = dS/S

    real_mean = 0.0
    real_rms  = 0.0
    print "len = ", len(nu)
    for i in range(len(nu)):
        real_mean = real_mean + nu[i] * dS[i]
    for i in range(len(nu)):
        real_rms = real_rms + (nu[i]-real_mean)**2 * dS[i]
    real_rms = np.sqrt(real_rms)

    print "mean     : ", mean
    print "real_mean: ", real_mean

    fig, ax = plt.subplots()
    
    MIN, MAX = 2e-06, 3e-4
#    ax.hist(nu, bins=10 ** np.linspace(np.log10(MIN), np.log10(MAX), 50), facecolor='g', normed=1)
    n, bins, patches = ax.hist(nu, bins=np.linspace(MIN, MAX, 1000), weights=dS,facecolor='darkcyan')
    
    print "sum(n) : ", sum(n)

    #ax.set_xlim(2e-06,2e-5)
    ax.set_xlim(2e-06,3e-4)
    #ax.set_xlim(MIN,MAX)
    ax.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    #ax.set_ylim(0,0.15)
    ax.tick_params(axis='both', which='major', direction='out', length=8, width=4)
    ax.tick_params(axis='both', which='minor', direction='out', length=6, width=2)
    
    #ax.axvline(x=MIN, color='orange', linewidth=5, linestyle='-.')
    #ax.axvline(x=mean, color='red', linewidth=5)
    #if (mean-rms) > MIN:
    #    ax.axvline(x=mean-rms, color='black', linewidth=5, linestyle='--')
    #if (mean+rms) < MAX:
    #    ax.axvline(x=mean+rms, color='black', linewidth=5, linestyle='--')

    ax.text(MIN, 2e-7, r'$\nu_{\infty}$')
    ax.text(MAX, 2e-7, r'$\nu_0$')
    ax.set_yscale('log')
    ax.set_xscale('log')
    
    fig.savefig("noLog.png",  bbox_inches='tight')

slice_nu_mean_hist_noLog()
