def main():
    import numpy as np
    import general_settings as gs
    import UbarCalc
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt
    
#    import parameters_periodic_M1_bNV as pp_M1_bNV
#    import parameters_periodic_M0_bNV as pp_M0_bNV
    import parameters_t_c as pp_M0_bNV

    fig,ax = plt.subplots()
    
    logFileNameList=[]
    N=5
    for i in range(N):
        logFileNameList.append('log.patchIntegrate_Inlet'+str(i))

    area1, time1, flux1 = UbarCalc.patchesIntegrate(pp_M0_bNV.parameters,logFileNameList)
    print "area1 = ", area1
    time1=time1[1:]
#    print "len(time1) : ", len(time1)
#    print "len(flux1) : ", len(flux1)
    ax.plot(time1,np.abs(flux1)/area1,label='run2 M0 patchIntegrate')
    
#    area2, time2, flux2 = UbarCalc.patchesIntegrate(pp_M1_bNV.parameters,logFileNameList)
#    print "area2 = ", area2
#    time2=time2[1:]
#    ax.plot(time2,np.abs(flux2)/area2,label='run1 M1 patchIntegrate')

#    ax.set_xlim(104,120)
#    ax.set_ylim(0.7,1.3)
    ax.set_xlabel(r'$t$',fontsize=gs.sizeLabel)
    ax.set_ylabel(r'$<Uz>_{volume}$',fontsize=gs.sizeLabel)
    ax.legend(bbox_to_anchor=(1.6, 1), ncol=1, fancybox=True, shadow=True)
#    ax.set_title('Volumic average on Uz through whole volume')

    fig.savefig('Ubar_t_c.png', bbox_inches='tight')

main()
