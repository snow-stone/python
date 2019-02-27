def main():
    import numpy as np
    import general_settings as gs
    import UbarCalc
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt

    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 30})
    plt.rcParams['savefig.dpi'] = 100
    
    from matplotlib import rc
    #    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)
    
    import parameters_t_c as t_c

    fig,ax = plt.subplots(figsize=(16,10))
    
    logFileNameList=[]
    N=5
    for i in range(N):
        logFileNameList.append('log.patchIntegrateSerial_Inlet'+str(i))

    area1, time1, flux1 = UbarCalc.patchesIntegrate(t_c.parameters,logFileNameList)
    print "area1 = ", area1
    time1=time1[1:]
    ax.plot(time1,np.abs(flux1)/area1,label=r'$<u_x>_{inlet}$')
    
    ax.set_xlim(0,7)
#    ax.set_ylim(0.7,1.3)
    ax.set_xlabel(r'$t$')
    ax.set_ylabel(r'$<u_x>_{inlet}$')
    ax.legend(bbox_to_anchor=(1, 1), ncol=1, fancybox=True, shadow=True)

    fig.savefig('Ubar_t_c.png', bbox_inches='tight')

main()
