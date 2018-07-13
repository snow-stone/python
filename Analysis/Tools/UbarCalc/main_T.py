def main():
    import numpy as np
    import general_settings as gs
    import UbarCalc
    import matplotlib.pyplot as plt
    
    import parameters_T_RES1b_MethodSynthetic as T_1b_syn
    import parameters_T_RES1d_MethodMapped_subMethod_NearestFace as T_1d_mapNF

    fig,ax = plt.subplots()

#    area,time,flux = UbarCalc.patchIntegrate(T_1b_syn.parameters,'log.patchIntegrate_Port1_phi')
#    time=time[1:]
#    print "area : ", area
#    print "len(time1) : ", len(time)
#    print "len(flux1) : ", len(flux)
#    ax.plot(time,np.abs(flux)/area,label='1b_synthetic')

    area,time,flux = UbarCalc.patchIntegrate(T_1d_mapNF.parameters,'log.patchIntegrate_Port1_phi')
    time=time[1:]
    print "area : ", area
    print "len(time1) : ", len(time)
    print "len(flux1) : ", len(flux)
    ax.plot(time[::10],np.abs(flux)[::10]/area,label='1d_mapped_Port1',marker='o')
    
    area,time,flux = UbarCalc.patchIntegrate(T_1d_mapNF.parameters,'log.patchIntegrate_Port2_phi')
    time=time[1:]
    print "area : ", area
    print "len(time1) : ", len(time)
    print "len(flux1) : ", len(flux)
    ax.plot(time[::10],np.abs(flux)[::10]/area,label='1d_mapped_Port2',marker='s')
    
    area,time,flux = UbarCalc.patchIntegrate(T_1d_mapNF.parameters,'log.patchIntegrate_Port3_phi')
    time=time[1:]
    print "area : ", area
    print "len(time1) : ", len(time)
    print "len(flux1) : ", len(flux)
    ax.plot(time[::15],np.abs(flux)[::15]/area,label='1d_mapped_Port3',marker='^') 

#    ax.set_xlim(104,120)
    ax.set_ylim(0,1)
    ax.set_xlabel(r'$t$',fontsize=gs.sizeLabel)
    ax.set_ylabel(r'$<U>_{Port_i}$',fontsize=gs.sizeLabel)
    ax.legend(bbox_to_anchor=(1, 1), ncol=1, fancybox=True, shadow=True)
    ax.set_title('patchIntegrate over Ports for TJunction')

main()