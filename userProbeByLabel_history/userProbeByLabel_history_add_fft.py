# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt

def userProbeByLabel_forcing(ax, caseName, path2Data, fieldName, sample, positions, color, cut=0.):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName+".old"
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
#    print rawData.shape
    time = rawData[:,0]
    probeData = rawData[:,1:]
    
    position_in_D = str(positions[sample]/8.0)+"D"
#    std = np.std(probeData[:,sample])
#    mean = np.mean(probeData[:,sample])
#    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time, probeData[:,sample], color=color, linewidth=0.5, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[:])), linestyle='-')   

    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
#    print rawData.shape
    time = rawData[:,0]+0.2
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positions[sample]/8.0)+"D"
#    std = np.std(probeData[cutSliceIndex:,sample])
#    mean = np.mean(probeData[cutSliceIndex:,sample])
#    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=2, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=1)    

    return probeData[cutSliceIndex:,sample]
#    return std, mean

def userProbeByLabel(ax, caseName, path2Data, fieldName, sample, positions, color, cut=0.5):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
#    print rawData.shape
    time = rawData[:,0]
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positions[sample]/8.0)+"D"
#    std = np.std(probeData[cutSliceIndex:,sample])
#    mean = np.mean(probeData[cutSliceIndex:,sample])
#    print position_in_D + " std : ", std, " mean : ", mean
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=2, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=1)    
    
    return probeData[cutSliceIndex:,sample]
#    return std, mean

##==============================================================================
##   RMS 
##==============================================================================    
#def spatial_mean_rms(fieldName, cases, positions, mean , std, linestyleList, markerList):
#    fig_rms = plt.figure()
#    positions=[x/8.0 for x in positions]
#
#    ax1 = fig_rms.add_subplot(1,1,1)
#
#    for i, case in enumerate(cases):
#        ax1.plot(positions,std[:,i],label=cases[i],linestyle=linestyleList[i],marker=markerList[i])
#    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
#    ax1.set_xlabel(r"$x/D$")
##    ax1.set_ylabel(latexRMSName)
#    
#    fig_rms.savefig('../PICTURE_history_e/'+fieldName+'/RMS_xByD_oneFig.png', bbox_inches='tight',  dpi=300)
##==============================================================================
##   Mean
##==============================================================================
#    fig_rms = plt.figure()
#
#    ax1 = fig_rms.add_subplot(1,1,1)
#
#    for i, case in enumerate(cases):
#        ax1.plot(positions,mean[:,i],label=cases[i],linestyle=linestyleList[i],marker=markerList[i])
#    ax1.legend(bbox_to_anchor=(1., 1), ncol=1, shadow=True)
#    ax1.set_xlabel(r"$x/D$")
##    ax1.set_ylabel(latexMEANName)
#    
#    fig_rms.savefig('../PICTURE_history_e/'+fieldName+'/Mean_xByD_oneFig.png', bbox_inches='tight', dpi=300)

def main():
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 25})
    plt.rcParams['savefig.dpi'] = 100
    
    from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)

    print "README"
    print "postProcessing data using output from : "
    print "userProbeByLabelVector_noMean ; userProbeByLabelScalar_noMean"
    allProbePosition = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72]
    #       sampling = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    positionSubSet = [0,13,15,17]
    #positionSubSet =  [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    
    path2Data="/store/8simu_tmp/shape_square/2a_3_T/python_postProcessing"
    cases = [
             "BirdCarreau"+"/"+"inlet_0p3",
             "Newtonian"+"/"+"Re2400",
             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",  # j=6, involving userProbeByLabel_forcing
		    "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",   # j=7, involving userProbeByLabel_forcing
             "BirdCarreau"+"/"+"inlet_0p5",
             "Newtonian"+"/"+"Re4000",
             "BirdCarreau/inlet0p5_impinging",
             "Newtonian/Re4000_impinging"
            ]
    
    # it is possible to only show the first 4 cases
#    cases = [
#             "BirdCarreau"+"/"+"inlet_0p5",
#             "Newtonian"+"/"+"Re4000",
#             "BirdCarreau"+"/"+"inlet_0p3",
#             "Newtonian"+"/"+"Re2400"
#            ]
              
    fieldNames=["U_y"]

    aliasDict={
        "BirdCarreau/inlet_0p3":r'$NN^{1}_{d}$',
        "Newtonian/Re2400"     :r'$N^{1}_{d}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":r'$NN^{1}_{d,St=1}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":r'$NN^{1}_{d,St=5}$',
        "BirdCarreau/inlet_0p5":r'$NN^{2}_{d}$',
        "Newtonian/Re4000"     :r'$N^{2}_{d}$',
        "BirdCarreau/inlet0p5_impinging"       :r'$NN^{2}_{i}$',
        "Newtonian/Re4000_impinging"           :r'$N^{2}_{i}$'
    }
    
    colorList = [
                  "blue",
                  "red",
                  "green",
                  "black"
                ]
    
    for k, position in enumerate(positionSubSet):
        p=positionSubSet[k]
        print "position : " , allProbePosition[p]
        #figsize should be in inches.
#        fig, axses_case = plt.subplots(len(cases), 1, sharex=True, figsize=(20,10))# figsize is an additional parameter for class matplotlib.pyplot.subplots: passed by **fig_kw
        fig, ax = plt.subplots(figsize=(20,10))
        mean = np.zeros((len(allProbePosition),len(cases)))
        std = np.zeros((len(allProbePosition),len(cases)))
        timeDomainData = np.zeros(len(cases))
        for j, case in enumerate(cases):
            for i, fieldName in enumerate(fieldNames):
        #        mean = np.zeros((len(positionList),4))
        #        std = np.zeros((len(positionList),4))
        #        mean, std = plotField(axarr, fieldName, cases, positionList, colorList, samples, field=i)
        #        plotField(axarr, fieldName, cases, positionList, colorList, samples, field=i)
        #        spatial_mean_rms(arrayName, cases, positionList, mean, std, linestyleList, markerList)
                ax.set_ylim(-0.5,2)
#                axses_case[j].set_yticks([0, 1])
                ax.tick_params(axis='y', direction='in', length=4, width=1.5)
                ax.set_xlim(0,0.85)
                
                print "axe number = ", j , fieldName
                if j == 0:
                    if allProbePosition[p] >= 24:
                        data0 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.6)
                    else:
                        data0 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.6)
                elif j == 1:
                    if allProbePosition[p] >= 24:
                        data1 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                    else:
                        data1 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)

                elif j == 2 :
                    data2 = userProbeByLabel_forcing(ax, case, path2Data,  fieldName, p, allProbePosition, colorList[i], cut=0.35)
                elif j == 3 :
                    data3 = userProbeByLabel_forcing(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.46)

                elif j == 4:
                    if allProbePosition[p] >= 7:
                        data4 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                    else :
                        data4 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                
                elif j == 5 :
                    if allProbePosition[p] >= 24:
                        data5 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                    else :
                        data5 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
               
                elif j == 6 :
                    data6 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)
                elif j == 7 :
                    data7 = userProbeByLabel(ax, case, path2Data, fieldName, p, allProbePosition, colorList[i], cut=0.5)            
                else :
                    print "There's a big problem"
        
#        spatial_mean_rms(fieldName, cases, allProbePosition, mean, std, linestyleList, markerList)
#        fig.text(0.5, 0.04, r'$t$', ha='center', va='center', fontsize=20)
        ax.set_xlabel(r'$t$')
        x = 0.82
        yStart = 0.82
        for i, case in enumerate(cases):
            y = yStart - i * 0.0975
            fig.text(x, y, aliasDict[case], fontsize=30)

#        fig.suptitle(r'Time history of $Ux,\, Uy,\, Uz,\, T$ @ position '+str(allProbePosition[p]/8.0)+'D')
        fig.savefig(path2Data+"/"+"PICTURE_history_FFT/"+"8simu/Uy_"+str(allProbePosition[p]/8.0)+"D.png", bbox_inches='tight') # bbox_inches = 'tight' is neccessary

        fig, ax = plt.subplots(figsize=(20,10))
        n=1 #removing mean
        m=10000
        sampling=1
        
        data=data0
        A = np.fft.rfft(data)
        print len(data)
#        print len(A)
        N = len(data)
        dt= 0.0005
        f=(np.arange(len(A))[n:m:sampling]/(dt*N))
        ax.plot(f, np.absolute(A)[n:m:sampling]/N, label=r'$NN^{1}_{d}$')
        
        data=data1
        A = np.fft.rfft(data)
        print len(data)
#        print len(A)
        N = len(data)
        dt= 0.0005
        f=(np.arange(len(A))[n:m:sampling]/(dt*N))
        ax.plot(f,np.absolute(A)[n:m:sampling]/N, label=r'$N^{1}_{d}$')

        data=data2
        A = np.fft.rfft(data)
        print len(data)
#        print len(A)
        N = len(data)
        dt= 0.0005
        f=(np.arange(len(A))[n:m:sampling]/(dt*N))
        ax.plot(f, np.absolute(A)[n:m:sampling]/N, label=r'$NN^{1}_{d,St=1}$')

        data=data3
        A = np.fft.rfft(data)
        print len(data)
#        print len(A)
        N = len(data)
        dt= 0.0005
        f=(np.arange(len(A))[n:m:sampling]/(dt*N))
        ax.plot(f, np.absolute(A)[n:m:sampling]/N, label=r'$NN^{1}_{d,St=5}$')

        data=data4
        A = np.fft.rfft(data)
        print len(data)
#        print len(A)
        N = len(data)
        dt= 0.0002
        f=(np.arange(len(A))[n:m:sampling]/(dt*N))
        ax.plot(f,np.absolute(A)[n:m:sampling]/N, label=r'$NN^{2}_{d}$')
        
        data=data5
        A = np.fft.rfft(data)
        print len(data)
#        print len(A)
        N = len(data)
        dt= 0.0005
        f=(np.arange(len(A))[n:m:sampling]/(dt*N))
        ax.plot(f,np.absolute(A)[n:m:sampling]/N, label=r'$N^{2}_{d}$')
        
        data=data6
        A = np.fft.rfft(data)
        print len(data)
#        print len(A)
        print data
        N = len(data)
        dt= 0.0005
        f=(np.arange(len(A))[n:m:sampling]/(dt*N))
        ax.plot(f,np.absolute(A)[n:m:sampling]/N, label=r'$NN^{2}_{i}$')

        data=data7
        A = np.fft.rfft(data)
        print len(data)
        print data
#        print len(A)
        N = len(data)
        dt= 0.0005
        f=(np.arange(len(A))[n:m:sampling]/(dt*N))
        ax.plot(f,np.absolute(A)[n:m:sampling]/N, label=r'$N^{2}_{i}$')        

        ax.set_xscale('log')
        ax.set_yscale('log')
#        ax.set_ylim(0,100)
        ax.legend()
        ax.set_xlabel('frequency (Hz)')
        ax.set_ylabel('fluctuation magnitude')
        x=np.arange(1000)
        ax.plot(x,x**(-5.0/3.0), linestyle='-.',color='blue')
        ax.plot(x,.05*x**(-1.0), linestyle='-.', color='red')
        fig.savefig(path2Data+"/"+"PICTURE_history_FFT/"+"8simu/Uy_FFT_"+str(allProbePosition[p]/8.0)+"D.png", bbox_inches='tight') # bbox_inches = 'tight' is neccessary
#            fig, ax = plt.subplots( figsize=(20,10))
#            ax.plot(A.real[:m])
#            fig.savefig(path2Data+"/"+"PICTURE_history_FFT/"+"8simu/FFT_real_"+str(allProbePosition[p]/8.0)+"D.png", bbox_inches='tight') # bbox_inches = 'tight' is neccessary
#            fig, ax = plt.subplots( figsize=(20,10))
#            ax.plot(A.imag[:m])
#            fig.savefig(path2Data+"/"+"PICTURE_history_FFT/"+"8simu/FFT__imag_"+str(allProbePosition[p]/8.0)+"D.png", bbox_inches='tight') # bbox_inches = 'tight' is neccessary

main()
