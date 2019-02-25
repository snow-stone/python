import numpy as np
import general_settings as gs
import reference_database as rdb
import matplotlib
matplotlib.use("agg") 
import matplotlib.pyplot as plt

def addToFig1(ax):        
    DNS_x, DNS_y = rdb.Eggels1994_thesis_Fig4p7_DNS()
    
    ax.plot(DNS_x,DNS_y,linewidth=2,label=r'$DNS_{E}$')
    
#    a_x1, a_y = rdb.analytic_Uz_meanProfile(True, 0.1, 100)
#    ax.plot(a_x,a_y,linewidth=1.5,label='Analytic')
    
    x1 = np.arange(1,15,1)
    ax.plot(x1, x1, linewidth=4, linestyle='--', color='black')#,label='viscous layer')
    
    x2 = np.arange(5,200,1)
    ax.plot(x2, 2.5*np.log(x2)+5.5, linewidth=4, linestyle='--',color='black')#, label='log layer')
    
#    print "DNS_x[0],DNS_y[0]",DNS_x[0],DNS_y[0]
#    print "DNS_x[1],DNS_y[1]",DNS_x[1],DNS_y[1]
#    print "(DNS_y[1]-DNS_y[0])/(DNS_x[1]-DNS_x[0])",(DNS_y[1]-DNS_y[0])/(DNS_x[1]-DNS_x[0])
    corr=(DNS_y[1]-DNS_y[0])/(DNS_x[1]-DNS_x[0])
    
#    ax.plot(DNS_x,DNS_y/corr,linewidth=gs.lw,label='Eggels_corr') 


def main():

    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 30})
    plt.rcParams['savefig.dpi'] = 100
    
    from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)

    import spatialSeriesReader0_module as ssR

    import parameters_periodic_M1_dict as M1
    import copy

    fig1,ax1 = plt.subplots(figsize=(20,10))
    l = ssR.pre_check(M1.parameters,'lines_typeUniform_cell')
    innerCoordData = ssR.process(M1.parameters,validDataList=l,colonNb=3,innerVar=True)
    ax1.plot(innerCoordData['rPlus'],innerCoordData['mean'],label='run0 t=%.1f M1 unif'%M1.parameters['dataEntry']['timeStep'],linewidth=gs.lw)
    for i in range(0, len(l), -40):
        ax1.plot(innerCoordData['rPlus'],innerCoordData['dataCmptArray'][i],label=str(i))

#    same case another timeStep or dataShape ?
#    dict_F=M1.parameters.copy()    # shallow
#    dict_F=dict(M1.parameters)     # shallow
    dict_F=copy.deepcopy(M1.parameters)
    print "dict_F.keys() = ", dict_F.keys()
    print "dict_F['sampling'].get('dataShape')", dict_F['sampling'].get('dataShape')
    dict_F['sampling']['dataShape']=(93,4)
    print "dict_F['sampling'].get('dataShape')", dict_F['sampling'].get('dataShape')
    print "M1.parameters['sampling'].get('dataShape')", M1.parameters['sampling'].get('dataShape')

    l = ssR.pre_check(dict_F,'lines_typeFace_cell')
    innerCoordData = ssR.process(dict_F,validDataList=l,colonNb=3,innerVar=True) 
    ax1.plot(innerCoordData['rPlus'],innerCoordData['mean'],label='run0 t=%.1f M1 face'%dict_F['dataEntry']['timeStep'],linewidth=gs.lw)

    ax1.tick_params(axis='both', which='major', direction='out', length=8, width=4)
    ax1.tick_params(axis='x', which='minor', direction='out', length=8, width=2)

    addToFig1(ax1)
    ax1.legend(bbox_to_anchor=(0.55, 1.0), ncol=1, fancybox=True, shadow=True)
    ax1.set_xscale('log')
    ax1.set_xlim(1,200)
    ax1.set_xlabel(r'$r^+$')
    ax1.set_ylabel(r'$U_z^+$')
    ax1.set_title('spatial stat.')

    #plt.show()
    fig1.savefig("U_x.png",bbox_inches='tight')

main()
