
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-white') # from defaut
plt.rcParams.update({'font.size': 30})
plt.rcParams['savefig.dpi'] = 100

from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def read_case_after_foamLog(caseName):
    data = np.genfromtxt(caseName+'/logs/executionTime_0')
    x = data[:,0]
    y = data[:,1]
    
    return x,y

def read_cases():
    from scipy.stats import linregress    
    prefix='1b_mirrorMerge_mapped_NearestFace'+'_'
    n_procs=np.array([48, 96, 192, 768])

    fig0, ax0 = plt.subplots(figsize=(20,10))
    fig1, ax1 = plt.subplots(figsize=(20,10)) 
    fig2, ax2 = plt.subplots(figsize=(20,10))
    
    Sp=np.zeros(len(n_procs))
    E =np.zeros(len(n_procs))
    
    for i in range(len(n_procs)):
        x,y = read_case_after_foamLog(prefix+str(n_procs[i]))
        ax0.plot(x,y,label='np=%d'%n_procs[i],linewidth=2)
        slope, intercept, r_value, p_value, std_err = linregress(x,y)
        print "slope : ", slope
        if i == 0 :
            slope0 = slope
            np0    = n_procs[0]
        speed_up = slope0/slope
        eff      = speed_up/(n_procs[i]/np0)
        Sp[i] = speed_up
        E[i]  = eff
#        ax1.plot(n_procs[i],speed_up,marker='o')
#        ax2.plot(n_procs[i],eff,marker='o')
    
    ax1.plot(n_procs,Sp, '-o')
    ax1.set_xscale('log')
    ax2.plot(n_procs,E, '-o')
    ax2.set_xscale('log')
    
    
    ax0.legend(bbox_to_anchor=(0.3, 1.0), ncol=1, fancybox=True, shadow=True)
    ax0.set_xlabel('physic time')
    ax0.set_ylabel('cpu time')
    ax0.set_title('case with 1.5M cellule, saturated at 192 cpu\n\
                Tested on occigen HSW24')
                
    ax1.set_xlabel('nb. of processors')
    ax1.set_ylabel('Speed Up')
    ax1.set_xlim(0,1000)
    #ax1.set_title('annoatations : average nb of cells per proc')

    ax2.set_xlabel('nb. of processors')
    ax2.set_ylabel('Parallel Efficiency')
    #ax2.set_title('annoatations : average nb of cells per proc')
    ax2.set_ylim(0,1.2)
    ax2.set_xlim(0,1000)

    for i in range(len(n_procs)):
        nb_cell_per_proc = 1.5e6 / n_procs[i]
        print nb_cell_per_proc
        ax1.annotate('%.2g' % nb_cell_per_proc, xy=(n_procs[i], Sp[i]), xytext=(-20,20), 
            textcoords='offset points', ha='center', va='bottom',
            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5', 
                            color='red'))
        ax2.annotate('%.2g' % nb_cell_per_proc, xy=(n_procs[i], E[i]), xytext=(-20,20), 
            textcoords='offset points',
            bbox=dict(boxstyle='round,pad=0.2', fc='yellow', alpha=0.3),
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.5', 
                            color='red'))

    fig0.savefig("cpuTime.png", bbox_inches='tight')
    fig1.savefig("Sp.png", bbox_inches='tight')
    fig2.savefig("E.png", bbox_inches='tight')

read_cases()
