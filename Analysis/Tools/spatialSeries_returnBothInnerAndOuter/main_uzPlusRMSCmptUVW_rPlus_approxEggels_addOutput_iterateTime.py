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

def outputToFile(x,y,paraDict,fileName):
    import os
    directory=paraDict['dataEntry']['path']+'/postProcessing/'+'spatialAveragedProfiles'
    if not os.path.exists(directory):
        os.mkdir(directory)
    fileToWrite=directory+'/'+fileName
    f = open(fileToWrite,'a')
    for i in range(len(x)):
        f.write(str(x[i]) +'\t'+ str(y[i]) + '\n')  
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
        innerCoordData3 = ssR.process(p_appoxEggels.parameters,validDataList=l,colonNb=3,innerVar=True)
        outputToFile(innerCoordData3['rByD'][::-1],
                     innerCoordData3['std'],
                     p_appoxEggels.parameters,
                     'rms_time-'+convert2TimeDirName(str(time)))

#mainWriter()

def mainReader():
    import timeSeriesReader_ReturnBothInnerAndOuterVariables as tsR
    import parameters_pipe_periodic_approxEggels_addEntriesStartTime as p_appoxEggels
    
    fig2,ax2 = plt.subplots()
    sampleNaming='rms_time'
    
    l = tsR.pre_check_spatialAveragedProfiles(p_appoxEggels.parameters,sampleNaming)
    outerCoordData = tsR.process(p_appoxEggels.parameters,validDataList=l,colonNb=1)
    ax2.plot(outerCoordData['x'],outerCoordData['mean'],label=('t=%.1f '+r'$z$')%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)
#    for i in range(len(outerCoordData['chunkedMean'])):
#        ax2.plot(outerCoordData['x'],outerCoordData['chunkedMean'][i],label=('t=%.1f '+r'$z$')%p_appoxEggels.parameters['dataEntry']['timeStep'],linewidth=gs.lw)

    x3, y3 = rdb.Eggels_article_1994.Fig8b_DNS_E_cmpt_z()
    ax2.plot(x3,y3,label='DNS(E)'+r' $z$',marker='>')
    ax2.set_xlim(0,0.5)
    ax2.legend(bbox_to_anchor=(0.3, 1.0), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'$(U_z^+)_{rms}$',fontsize=gs.sizeLabel)
    ax2.set_title('Eggels_article_1994 Fig 8(a)')

#mainReader()