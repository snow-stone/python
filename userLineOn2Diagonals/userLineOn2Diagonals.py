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
    uTau=0.038

    simu_module = __import__("parameters_"+parameterFileBasename)
    simu_parameters = simu_module.parameters

    fig1,ax1 = plt.subplots(figsize=(16,10))
    l = reader.pre_check(simu_module.parameters,'lineOn2Diagonals','U')
    outerCoordData = reader.process(simu_module.parameters,validDataList=l,colonNb=1,innerVar=False)
    x=outerCoordData['rByD']*2
    y=outerCoordData['mean']/uTau#*max(outerCoordData['mean'])#/0.045    
    #ax1.plot(x,y,label='simu t=%.1f'%simu_module.parameters['dataEntry']['timeStep'],linewidth=2)
    output2Txt('Ux_spatialAvg',outerCoordData['rByD']*2,outerCoordData['mean']*max(outerCoordData['mean'])/0.045)
    y_sum = np.zeros(y.shape)
    counter=0

    for i in range(1,12,1):
        counter = counter + 1
        dict_=copy.deepcopy(simu_module.parameters)
        dict_['dataEntry']['timeStep']=i
        l_ = reader.pre_check(dict_,'lineOn2Diagonals','U')
        outerCoordData = reader.process(dict_,validDataList=l_,colonNb=1,innerVar=False)
        x=outerCoordData['rByD']*2
        y=outerCoordData['mean']/uTau
        y_sum = y_sum + y
        #ax1.plot(x,y,label='simu t=%.1f'%dict_['dataEntry']['timeStep'],linewidth=2)
    ax1.plot(x,y_sum/counter,label=r'$t_r$',linewidth=4,color='steelblue')

    x, y = rdb.Gavrilakis1992.Fig4a()
    ax1.plot(x,y,label=r'$DNS_G$',linewidth=1,linestyle='--',marker='s',color='mediumvioletred',markeredgecolor='mediumvioletred', markerfacecolor='none', markersize=16, markeredgewidth=4)
    ax1.legend(bbox_to_anchor=(1, 1), ncol=1, fancybox=True, shadow=True)
    ax1.set_ylim(0,25)
    ax1.set_xlabel(r'$Disantce \, along \, the \, diagonal$')
    ax1.set_ylabel(r'$u_x^+$')
    #ax1.set_title('spatial stat.')

    fig1.savefig(saveDir+'/'+'UxPlus_diagonal.png',bbox_inches='tight')

main()
