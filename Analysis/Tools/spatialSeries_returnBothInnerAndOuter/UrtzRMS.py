import numpy as np
import sys
sys.path.append('/home/hluo/work/git/thesis/Thesis_hluo') # for rdb
import reference_database as rdb
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

def convert2TimeDirName(string):
    if '.' in string:
        while string[-1] == '0':
            string = string[:-1] # remove the trailing '0'
        while string[-1] == '.': # then after that, remove the trailing '.'
            string = string.rstrip('.')
    else:
        print 'Integer timeStep here :', string
    return string

def outputToFile(x,cmpt_1,cmpt_2,cmpt_3,paraDict,fileName):
    import os
    directory=paraDict['dataEntry']['path']+'/postProcessing/'+'spatialAveragedProfiles'
    if not os.path.exists(directory):
        os.mkdir(directory)
    fileToWrite=directory+'/'+fileName
    f = open(fileToWrite,'a')
    for i in range(len(x)):
        f.write(str(x[i]) 
                +'\t'+ str(cmpt_1[i])
                +'\t'+ str(cmpt_2[i])
                +'\t'+ str(cmpt_3[i])
                + '\n')  
    f.close()

def mainWriter():
    import spatialSeriesReader_returnBothInnerAndOuter as ssR
#    import parameters_pipe_periodic_approxEggels as p_appoxEggels
    import parameters_t_c as p_appoxEggels
#    import copy

    sampleNaming='lines_typeFace_cell' 

    times=np.linspace(p_appoxEggels.parameters['dataEntry']['startTime'],
                      p_appoxEggels.parameters['dataEntry']['endTime'],
                      p_appoxEggels.parameters['dataEntry']['NbOfFiles'])
    
    for time in times:
        print time, convert2TimeDirName(str(time))
        p_appoxEggels.parameters['dataEntry']['timeStep']=time
        l = ssR.pre_check(p_appoxEggels.parameters,sampleNaming)
        innerCoordData_cmpt_z = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=3,innerVar=True)
        innerCoordData_cmpt_r = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=1,innerVar=True)
        innerCoordData_cmpt_theta = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=2,innerVar=True)
        outputToFile(innerCoordData_cmpt_r['rByD'][::-1],
                     innerCoordData_cmpt_r['std'],
                     innerCoordData_cmpt_theta['std'],
                     innerCoordData_cmpt_z['std'],
                     p_appoxEggels.parameters,
                     'rms_time-'+convert2TimeDirName(str(time)))

#mainWriter()

def mainReader():

    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 30})
    plt.rcParams['savefig.dpi'] = 100
    
    from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)

    colorDict={
            'r':'mediumvioletred',
            'theta':'forestgreen',
            'z':'darkcyan'
            }

    import timeSeriesReader_ReturnBothInnerAndOuterVariables as tsR
    import parameters_t_c as p_appoxEggels
    
    fig2,ax2 = plt.subplots(figsize=(20,10))
    sampleNaming='rms_time'
    
    l = tsR.pre_check_spatialAveragedProfiles(p_appoxEggels.parameters,sampleNaming)
    cmpt_r = tsR.process(p_appoxEggels.parameters,validDataList=l,colonNb=1)
    cmpt_theta = tsR.process(p_appoxEggels.parameters,validDataList=l,colonNb=2)
    cmpt_z = tsR.process(p_appoxEggels.parameters,validDataList=l,colonNb=3)
    ax2.plot(cmpt_r['x'],cmpt_r['mean'],label=r'$simu :\,$ '+r'$u_r$',linewidth=4,color=colorDict['r'])
    ax2.plot(cmpt_theta['x'],cmpt_theta['mean'],label=r'$simu :\,$ '+r'$u_{\theta}$',linewidth=4,color=colorDict['theta'])
    ax2.plot(cmpt_z['x'],cmpt_z['mean'],label=r'$simu :\,$ '+r'$u_z$',linewidth=4,color=colorDict['z'])
#    for i in range(len(outerCoordData['chunkedMean'])):
#        ax2.plot(outerCoordData['x'],outerCoordData['chunkedMean'][i],label=('t=%.1f '+r'$z$')%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)

    x1, y1 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_r()
    x2, y2 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_theta()
    x3, y3 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_z()
    ax2.plot(x1,y1,label=r'$DNS_E :\,$'+r' $u_r$',marker='s',linestyle='--',color=colorDict['r'],markeredgecolor=colorDict['r'], markerfacecolor='none', markersize=16, markeredgewidth=4)
    ax2.plot(x2,y2,label=r'$DNS_E :\,$'+r' $u_{\theta}$',marker='<',linestyle='--',color=colorDict['theta'],markeredgecolor=colorDict['theta'], markerfacecolor='none', markersize=16, markeredgewidth=4)
    ax2.plot(x3,y3,label=r'$DNS_E :\,$'+r' $u_z$',marker='>',linestyle='--',color=colorDict['z'],markeredgecolor=colorDict['z'], markerfacecolor='none', markersize=16, markeredgewidth=4)
    ax2.set_xlim(0,0.5)
    ax2.legend(bbox_to_anchor=(0.3, 1.0), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$')
    ax2.set_ylabel(r'$rms[u^+_{\{r,\theta,z\}}]$')
    #ax2.set_title('Eggels_article_1994 Fig 8(a)')

    fig2.savefig("UrtzRMS.png", bbox_inches='tight')

#mainReader()

def main():
    #mainWriter() # 1st : execute Writer (write down spatial averaged data) while commmenting Reader
    mainReader() # 2rd : execute only reader to plot data

main()
