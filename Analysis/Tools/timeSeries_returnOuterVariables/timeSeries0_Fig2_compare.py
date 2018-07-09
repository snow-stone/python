import matplotlib.pyplot as plt
import general_settings as gs
import reference_database as rdb


def main():
    import timeSeriesReader1_onlyOuter as tsR
    import parameters_1b_mm_synthetic as ps_synthetic
    import parameters_1d_mmNtFc as ps
#    import copy
    
    fig1,ax1 = plt.subplots()
    fig2,ax2 = plt.subplots()
    
    l = tsR.pre_check(ps.parameters,"Dai_lines_typeFace_cell-2")
    outerCoordData = tsR.process(ps.parameters,validDataList=l,ifPlotAllTimes=False,colonNb=1)
    
    ax1.plot(outerCoordData['rByD'],outerCoordData['mean'],label='mapped',linewidth=2)
    for i in range(0, len(outerCoordData['chunkedMean']), -1):
        ax1.plot(outerCoordData['rByD'],outerCoordData['chunkedMean'][i],label=str(i),linewidth=2)

    ax2.plot(outerCoordData['rByD'],outerCoordData['std'],label='mapped',linewidth=2)
    for i in range(0, len(outerCoordData['chunkedStd']), -1):
        ax2.plot(outerCoordData['rByD'],outerCoordData['chunkedStd'][i],label=str(i),linewidth=2)
#    ax2.plot(outerCoordData['rByD'],outerCoordData['chunkedStd'][-1],label='mapped last chunk stat.',linewidth=2)

    l = tsR.pre_check(ps_synthetic.parameters,"Dai_lines_typeFace_cell-2")
    outerCoordData = tsR.process(ps_synthetic.parameters,validDataList=l,ifPlotAllTimes=False,colonNb=1)    
    ax1.plot(outerCoordData['rByD'],outerCoordData['mean'],label='synthetic',linewidth=2)
    for i in range(0, len(outerCoordData['chunkedMean']), -1):
        ax1.plot(outerCoordData['rByD'],outerCoordData['chunkedMean'][i],label=str(i),linewidth=2)
    
    ax2.plot(outerCoordData['rByD'],outerCoordData['std'],label='synthetic',linewidth=2)
#    for i in range(0, len(outerCoordData['chunkedStd']), 1):
#        ax2.plot(outerCoordData['rByD'],outerCoordData['chunkedStd'][i],label=str(i),linewidth=2)
    
    x1,y1 = rdb.Dai_thesis.Fig4p9a('EAU')
    ax1.plot(x1+0.5, y1[::-1], label='Dai', marker='s', markerfacecolor='none', linewidth=2)
    x2,y2 = rdb.Dai_thesis.Fig4p12a('EAU')
    ax2.plot(x2+0.5, y2, label='Dai', marker='s', markerfacecolor='none', linewidth=2)
    
    ax1.set_xlim(0,1)
    ax1.legend(bbox_to_anchor=(0.35, 1), ncol=1, fancybox=True, shadow=True)
    ax1.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax1.set_ylabel(r'$<U_x>$',fontsize=gs.sizeLabel)
    ax1.set_title('time stat. @'+r'$8mm$'+' cut')

    ax2.set_xlim(0,1)
    ax2.legend(bbox_to_anchor=(1, 1), ncol=1, fancybox=True, shadow=True)
    ax2.set_xlabel(r'$r/D$',fontsize=gs.sizeLabel)
    ax2.set_ylabel(r'${U_x}_{rms}$',fontsize=gs.sizeLabel)

main()