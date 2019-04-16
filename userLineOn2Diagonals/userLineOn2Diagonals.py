import numpy as np
import sys
sys.path.append('/home/hluo/work/git/thesis/Thesis_hluo_new/reference_database') # for rdb
import reference_database as rdb
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

plt.style.use('seaborn-white') # from defaut
plt.rcParams.update({'font.size': 30})
plt.rcParams['savefig.dpi'] = 100

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def output2Txt(fileName, x, y):
    import os    
    if (os.path.exists('data')):
        print "path data exists\n"
    else:
        os.mkdir('data')
    
    f = open("data/"+fileName, "w+")
    for i in range(len(x)):
        f.write("%.6f %.6f\n" % (x[i], y[i]))
    f.close()

def main():
    import spatialSeriesReader0_module as reader
    import copy

    parameterFileBasename = sys.argv[1]
    saveDir = sys.argv[2]

    simu_module = __import__("parameters_"+parameterFileBasename)
    simu_parameters = simu_module.parameters

    fig1,ax1 = plt.subplots()
    l = reader.pre_check(simu_module.parameters,'lineOn2Diagonals','U')
    outerCoordData = reader.process(simu_module.parameters,validDataList=l,colonNb=1,innerVar=False)
    x=outerCoordData['rByD']*2
    y=outerCoordData['mean']/0.045#*max(outerCoordData['mean'])#/0.045    
    ax1.plot(x,y,label='simu t=%.1f'%simu_module.parameters['dataEntry']['timeStep'],linewidth=2)
    output2Txt('Ux_spatialAvg',outerCoordData['rByD']*2,outerCoordData['mean']*max(outerCoordData['mean'])/0.045)

    for i in range(10,20,1):
        dict_=copy.deepcopy(simu_module.parameters)
        dict_['dataEntry']['timeStep']=i
        l_ = reader.pre_check(dict_,'lineOn2Diagonals','U')
        outerCoordData = reader.process(dict_,validDataList=l_,colonNb=1,innerVar=False)
        x=outerCoordData['rByD']*2
        y=outerCoordData['mean']/0.045
        ax1.plot(x,y,label='simu t=%.1f'%dict_['dataEntry']['timeStep'],linewidth=2)

    x, y = rdb.Gavrilakis1992.Fig4a()
    ax1.plot(x,y,'o',label='Gavrilakis1992')
    ax1.legend(bbox_to_anchor=(1.5, 1.0), ncol=1, fancybox=True, shadow=True)
    ax1.set_ylim(0,25)
    ax1.set_xlabel(r'$Disantce \, along \, the \, diagonal$',fontsize=20)
    ax1.set_ylabel(r'$U_x^+$',fontsize=20)
    ax1.set_title('spatial stat.')

    fig1.savefig(saveDir+'/'+'mean.png',bbox_inches='tight')

main()
