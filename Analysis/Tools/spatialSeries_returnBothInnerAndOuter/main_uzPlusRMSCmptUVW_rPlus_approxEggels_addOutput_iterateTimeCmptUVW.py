import numpy as np
import general_settings as gs
import reference_database as rdb
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
    import parameters_pipe_periodic_approxEggels_addEntriesStartTime as p_appoxEggels
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
    import timeSeriesReader_ReturnBothInnerAndOuterVariables as tsR
    import parameters_pipe_periodic_approxEggels_addEntriesStartTime as p_appoxEggels
    
    fig2,ax2 = plt.subplots()
    sampleNaming='rms_time'
    
    l = tsR.pre_check_spatialAveragedProfiles(p_appoxEggels.parameters,sampleNaming)
    cmpt_r = tsR.process(p_appoxEggels.parameters,validDataList=l,colonNb=1)
    cmpt_theta = tsR.process(p_appoxEggels.parameters,validDataList=l,colonNb=2)
    cmpt_z = tsR.process(p_appoxEggels.parameters,validDataList=l,colonNb=3)
    ax2.plot(cmpt_r['x'],cmpt_r['mean'],label='simu '+r'$r$',linewidth=gs.lw)
    ax2.plot(cmpt_theta['x'],cmpt_theta['mean'],label='simu '+r'$\theta$',linewidth=gs.lw)
    ax2.plot(cmpt_z['x'],cmpt_z['mean'],label='simu '+r'$z$',linewidth=gs.lw)
#    for i in range(len(outerCoordData['chunkedMean'])):
#        ax2.plot(outerCoordData['x'],outerCoordData['chunkedMean'][i],label=('t=%.1f '+r'$z$')%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)

    x1, y1 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_r()
    x2, y2 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_theta()
    x3, y3 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_z()
    ax2.plot(x1,y1,label='DNS(E)'+r' $r$',marker='s')
    ax2.plot(x2,y2,label='DNS(E)'+r' $\theta$',marker='<')
    ax2.plot(x3,y3,label='DNS(E)'+r' $z$',marker='>')
    ax2.set_xlim(0,0.5)
    ax2.legend(bbox_to_anchor=(0.3, 1.0), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'$(U_z^+)_{rms}$',fontsize=gs.sizeLabel)
    ax2.set_title('Eggels_article_1994 Fig 8(a)')

mainReader()