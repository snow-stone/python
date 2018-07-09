def main():
    import numpy as np
    import general_settings as gs
    import UbarCalc
    import matplotlib.pyplot as plt
    
    import parameters_T_RES1b_MethodSynthetic as T_1b_syn

    fig,ax = plt.subplots()

    area,time,flux = UbarCalc.patchIntegrate(T_1b_syn.parameters,'log.patchIntegrate_Port1_phi')
    time=time[1:]
    print "area : ", area
    print "len(time1) : ", len(time)
    print "len(flux1) : ", len(flux)
    ax.plot(time,np.abs(flux)/area,label='1b_synthetic')    

#    ax.set_xlim(104,120)
    ax.set_ylim(0,1)
    ax.set_xlabel(r'$t$',fontsize=gs.sizeLabel)
    ax.set_ylabel(r'$<Uz>_{volume}$',fontsize=gs.sizeLabel)
    ax.legend(bbox_to_anchor=(1, 1), ncol=1, fancybox=True, shadow=True)
    ax.set_title('patchIntegrate over Port1 for TJunction')

main()