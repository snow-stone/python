import matplotlib.pyplot as plt
import general_settings as gs
import reference_database as rdb


def Uz():
    import timeSeriesReader0 as tsR
#    import parameters_periodic as ps
    import parameters_1b_mmNtFc as ps
#    import copy
    
    l = \
        tsR.pre_check(ps.parameters,"Dai_lines_typeFace_cell-2")
    

    outerCoordData = \
        tsR.process(ps.parameters,validDataList=l,ifPlotAllTimes=False,colonNb=1,innerVar=False)   
    
#==============================================================================

    fig1,ax1 = plt.subplots()
    ax1.plot(outerCoordData['rByD'],outerCoordData['mean'],label='mean',color='red',linewidth=2)
#    for i in range(0, len(outerCoordData['chunkedMean'])):
#        ax1.plot(outerCoordData['rPlus'],outerCoordData['chunkedMean'][i],label=str(i))
    for i in range(0, len(l), -20):
        ax1.plot(outerCoordData['rByD'],outerCoordData['dataCmptArray'][i],label=str(i))
    
    x1,y1 = rdb.Dai_thesis.Fig4p9a('EAU')
    ax1.plot(x1+0.5, y1[::-1], label='Dai', marker='s', markerfacecolor='none', linewidth=2)
    
    ax1.set_xlim(0,1)
    ax1.legend(bbox_to_anchor=(0.6, 0.3), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$<U_x>$',fontsize=gs.sizeLabel)


def main():
#    print '\n'.join(sys.path)
    Uz()

main()