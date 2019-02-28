import numpy as np
import matplotlib.pyplot as plt

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
    import para_statistic_set4uv as set4uv
    import copy

    fig1,ax1 = plt.subplots()
#    l = reader.pre_check(twoD.parameters,'lineOn2Diagonals','U_mean')
    l = reader.pre_check(set4uv.parameters,'set4uv','uv_mean')
    outerCoordData = reader.process(set4uv.parameters,validDataList=l,colonNb=1,innerVar=False)
#    ax1.plot(innerCoordData['rPlus'],innerCoordData['mean'],label='run0 t=%.1f M1 unif'%twoD.parameters['dataEntry']['timeStep'],linewidth=20)
    x=-outerCoordData['rByD']*2+1.0
    y=-outerCoordData['mean']/0.045**2#*max(outerCoordData['mean'])#/0.045    
    ax1.plot(x,y,label='simu t=%.1f'%set4uv.parameters['dataEntry']['timeStep'],linewidth=2)
    output2Txt('uv_reynoldsStress',outerCoordData['rByD']*2,outerCoordData['mean']*max(outerCoordData['mean'])/0.045)

#    dict_19=copy.deepcopy(twoD.parameters)
#    dict_19['dataEntry']['timeStep']=0.55
#    l_19 = reader.pre_check(dict_19,'lineOn2Diagonals','U')
#    outerCoordData = reader.process(dict_19,validDataList=l_19,colonNb=1,innerVar=False)
#    x=outerCoordData['rByD']*2
#    y=outerCoordData['mean']/0.0375#*max(outerCoordData['mean'])#/0.0375
#    ax1.plot(x,y,label='run0 t=%.1f'%dict_19['dataEntry']['timeStep'],linewidth=2)
#    for i in range(10,20,1):
#        dict_=copy.deepcopy(twoD.parameters)
#        dict_['dataEntry']['timeStep']=i
#        l_ = reader.pre_check(dict_,'lineOn2Diagonals','U')
#        outerCoordData = reader.process(dict_,validDataList=l_,colonNb=1,innerVar=False)
#        x=outerCoordData['rByD']*2
#        y=outerCoordData['mean']/0.045
#        ax1.plot(x,y,label='simu t=%.1f'%dict_['dataEntry']['timeStep'],linewidth=2)

#    addToFig1(ax1)
#    x, y = Gavrilakis1992()
#    ax1.plot(x,y,'o',label='Gavrilakis1992')
#    ax1.legend(bbox_to_anchor=(1.5, 1.0), ncol=1, fancybox=True, shadow=True)
#    ax1.set_ylim(0,25)
#    ax1.set_xlabel(r'$Disantce \, along \, the \, diagonal$',fontsize=20)
#    ax1.set_ylabel(r'$U_x^+$',fontsize=20)
#    ax1.set_title('spatial stat.')


main()
