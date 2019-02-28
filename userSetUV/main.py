import numpy as np
import matplotlib
matplotlib.use('agg')
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
    l = reader.pre_check(set4uv.parameters,'set4uv','uv_mean')
    outerCoordData = reader.process(set4uv.parameters,validDataList=l,colonNb=1,innerVar=False)
    x=-outerCoordData['rByD']*2+1.0
    y=-outerCoordData['mean']/0.045**2#*max(outerCoordData['mean'])#/0.045    
    ax1.plot(x,y,label='simu t=%.1f'%set4uv.parameters['dataEntry']['timeStep'],linewidth=2)
    output2Txt('uv_reynoldsStress',outerCoordData['rByD']*2,outerCoordData['mean']*max(outerCoordData['mean'])/0.045)

    fig1.savefig('uv_reynoldsStress.png')

main()
