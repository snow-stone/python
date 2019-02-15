# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:08:57 2018

@author: hluo
"""

import numpy as np
import matplotlib.pyplot as plt

def userProbeByLabel_forcing(ax, caseName, path2Data, fieldName, sample, positions, color, cut):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName+".old"
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
    time = rawData[:,0]
    probeData = rawData[:,1:]
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[:,sample])
    mean = np.mean(probeData[:,sample])
    cutSliceIndex=int(0.565*len(time))
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=1, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[:])), linestyle='-')   

    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
    time = rawData[:,0]+0.2
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    position_in_D = str(positions[sample]/8.0)+"D"
    std = np.std(probeData[cutSliceIndex:,sample])
    mean = np.mean(probeData[cutSliceIndex:,sample])
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=2, label=caseName+"_"+position_in_D+"\nNbSampleEq_"+str(len(time[cutSliceIndex:])), linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=1)    

    return probeData[cutSliceIndex:,sample], std, mean

def userProbeByLabel(ax, caseName, path2Data, fieldName, sample, positions, color, cut, fieldNameAliasDict):
    RelativeDataFile = "./"+"userDefinedLog/history_labelGroup_"+fieldName
    rawData = np.genfromtxt(path2Data+"/"+caseName+'/'+RelativeDataFile)
    time = rawData[:,0]
    probeData = rawData[:,1:]
    cutSliceIndex = int(cut*len(time))
    
    std = np.std(probeData[cutSliceIndex:,sample])
    mean = np.mean(probeData[cutSliceIndex:,sample])
    ax.plot(time[cutSliceIndex:], probeData[cutSliceIndex:,sample], color=color, linewidth=2, label=fieldNameAliasDict[fieldName], linestyle='-')
    ax.plot(time[:cutSliceIndex], probeData[:cutSliceIndex,sample], color=color, linewidth=1)    
    
    return probeData[cutSliceIndex:,sample], std, mean

def FFT_plot(ax, originalTimeSeries, samplingFrequency, startIndex, endIndex, labelAlias, resamplingStep, linestyle, color, linewidth, marker):
    A = np.fft.rfft(originalTimeSeries)
    print "data length", len(originalTimeSeries)
    N = len(originalTimeSeries)
    f=(np.arange(len(A))[startIndex:endIndex:resamplingStep]/(samplingFrequency*N))
    ax.plot(f, np.absolute(A)[startIndex:endIndex:resamplingStep]/N, label=labelAlias, linestyle=linestyle, color=color, linewidth=linewidth, marker=marker, markersize=8, markeredgecolor=color, markerfacecolor='none')

def FFT_plot_simple(ax, originalTimeSeries, samplingFrequency, startIndex, endIndex, labelAlias, resamplingStep, zorder):
    A = np.fft.rfft(originalTimeSeries)
    print "data length", len(originalTimeSeries)
    N = len(originalTimeSeries)
    f=(np.arange(len(A))[startIndex:endIndex:resamplingStep]/(samplingFrequency*N))
    ax.plot(f, np.absolute(A)[startIndex:endIndex:resamplingStep]/N, label=labelAlias, zorder=zorder, linewidth=2)

def main():
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 30})
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
             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
		    "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",
             "BirdCarreau"+"/"+"inlet_0p5",
             "Newtonian"+"/"+"Re4000",
             "BirdCarreau/inlet0p5_impinging",
             "Newtonian/Re4000_impinging"
            ]

    fieldNames=["U_y", "T"]
    
    fieldNameAliasDict = {
              "U_x" : r"$u_x$",
              "U_y" : r"$u_y$",
              "U_z" : r"$u_z$",
              "T"   : r"$c$"
    }
    
    colorDictForfieldNames = {
                  "U_x" : "blue",
                  "U_y" : "red",
                  "U_z" : "green",
                  "T"   : "black"
                }
    
    cutDict = {
        "BirdCarreau/inlet_0p3"                :0.6,
        "Newtonian/Re2400"                     :0.5,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":0.35,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":0.46,
        "BirdCarreau/inlet_0p5"                :0.5,
        "Newtonian/Re4000"                     :0.5,
        "BirdCarreau/inlet0p5_impinging"       :0.5,
        "Newtonian/Re4000_impinging"           :0.5
    }

    samplingFrequencyDict = {
        "BirdCarreau/inlet_0p3"                :0.0005,
        "Newtonian/Re2400"                     :0.0005,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":0.0005,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":0.0005,
        "BirdCarreau/inlet_0p5"                :0.0002,
        "Newtonian/Re4000"                     :0.0005,
        "BirdCarreau/inlet0p5_impinging"       :0.0005,
        "Newtonian/Re4000_impinging"           :0.0005
    }

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
    
    for k, position in enumerate(positionSubSet):
        p=positionSubSet[k]
        print "position : " , allProbePosition[p]
        #figsize should be in inches.
        fig, axses_case = plt.subplots(len(cases), 1, sharex=True, figsize=(20,10))# figsize is an additional parameter for class matplotlib.pyplot.subplots: passed by **fig_kw
        mean = np.zeros((len(allProbePosition),len(cases)))
        std = np.zeros((len(allProbePosition),len(cases)))
        
        dataDict=dict.fromkeys(fieldNames)
        for fieldName in fieldNames:
            dataDict[fieldName]={}
        print dataDict
        
        for j, case in enumerate(cases):
            for i, fieldName in enumerate(fieldNames):
        #        mean = np.zeros((len(positionList),4))
        #        std = np.zeros((len(positionList),4))
        #        mean, std = plotField(axarr, fieldName, cases, positionList, colorList, samples, field=i)
        #        plotField(axarr, fieldName, cases, positionList, colorList, samples, field=i)
        #        spatial_mean_rms(arrayName, cases, positionList, mean, std, linestyleList, markerList)
                axses_case[j].set_ylim(-0.5,2)
                axses_case[j].set_yticks([0, 1])
                axses_case[j].tick_params(axis='y', direction='in', length=4, width=1.5)
                axses_case[j].set_xlim(0,0.85)
                
                print "axe number = ", j , fieldName
                
                if case == "BirdCarreau/inlet_0p3-a_0p5-setT_St_1" or case == "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":
                    data, std[i,j], mean[i,j] = userProbeByLabel_forcing(axses_case[j], case, path2Data,  fieldName, p, allProbePosition, colorDictForfieldNames[fieldName], cutDict[case])
                else:
                    data, std[i,j], mean[i,j] = userProbeByLabel(axses_case[j], case, path2Data, fieldName, p, allProbePosition, colorDictForfieldNames[fieldName], cutDict[case], fieldNameAliasDict)
                
                dataDict[fieldName][case]=data
                
        axses_case[-1].set_xlabel(r'$t$',fontsize=40)
        x = 0.82
        yStart = 0.82
        for i, case in enumerate(cases):
            y = yStart - i * 0.0975
            fig.text(x, y, aliasDict[case], fontsize=30)

        axses_case[0].legend(bbox_to_anchor=(1, 2.6), ncol=2, shadow=True)
        fig.suptitle('Probe signal at '+r'$x=%.1fD$'%(allProbePosition[p]/8.0))
        fig.savefig(path2Data+"/"+"PICTURE_history/"+"8simu/"+str(allProbePosition[p]/8.0).replace('.','p')+"D.png", bbox_inches='tight') # bbox_inches = 'tight' is neccessary
        
# =============================================================================
#       FFT : still in loop of position
# =============================================================================
        start=1   # removing mode 0 : average (in time domain)
        end=10000 # big enough
#        resample=1# no resampling defaut value : 1
        cases_FFT = [
             "BirdCarreau"+"/"+"inlet_0p3",
             "Newtonian"+"/"+"Re2400",
             "BirdCarreau"+"/"+"inlet_0p5",
             "Newtonian"+"/"+"Re4000",
             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
		    "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",
             "BirdCarreau/inlet0p5_impinging",
             "Newtonian/Re4000_impinging"
        ]
        lineStyleDict={
            "BirdCarreau/inlet_0p3"                : '-',
            "Newtonian/Re2400"                     : 'none',
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '-',
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": '-',
            "BirdCarreau/inlet_0p5"                : '-.',
            "Newtonian/Re4000"                     : 'none',
            "BirdCarreau/inlet0p5_impinging"       : '-.',
            "Newtonian/Re4000_impinging"           : 'none'
        }
        colorDict={
            "BirdCarreau/inlet_0p3"                : 'darkcyan',
            "Newtonian/Re2400"                     : 'darkred',
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 'red',
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 'red',
            "BirdCarreau/inlet_0p5"                : 'mediumvioletred',
            "Newtonian/Re4000"                     : 'forestgreen',
            "BirdCarreau/inlet0p5_impinging"       : 'darkmagenta',
            "Newtonian/Re4000_impinging"           : 'mediumvioletred'
        }
        lineWidthDict={
            "BirdCarreau/inlet_0p3"                : 4,
            "Newtonian/Re2400"                     : 1,
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 2,
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 2,
            "BirdCarreau/inlet_0p5"                : 4,
            "Newtonian/Re4000"                     : 1,
            "BirdCarreau/inlet0p5_impinging"       : 2,
            "Newtonian/Re4000_impinging"           : 1
        }
        markerDict={
            "BirdCarreau/inlet_0p3"                : '',
            "Newtonian/Re2400"                     : '^',
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": '',
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": '',
            "BirdCarreau/inlet_0p5"                : '',
            "Newtonian/Re4000"                     : 'o',
            "BirdCarreau/inlet0p5_impinging"       : '',
            "Newtonian/Re4000_impinging"           : 's'
        }
        resampleDict={
            "BirdCarreau/inlet_0p3"                : 1,
            "Newtonian/Re2400"                     : 1,
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_1": 1,
            "BirdCarreau/inlet_0p3-a_0p5-setT_St_5": 1,
            "BirdCarreau/inlet_0p5"                : 1,
            "Newtonian/Re4000"                     : 1,
            "BirdCarreau/inlet0p5_impinging"       : 1,
            "Newtonian/Re4000_impinging"           : 1                
        }
        fieldNameAliasFFTDict = {
                  "U_x" : r"$FFT(u^{\prime}_x)$",
                  "U_y" : r"$FFT(u^{\prime}_y)$",
                  "U_z" : r"$FFT(u^{\prime}_z)$",
                  "T"   : r"$FFT(c^{\prime})$"
        }
        for fieldName in fieldNames:
            fig, ax = plt.subplots(figsize=(20,12))
            zorders = np.arange(len(cases_FFT),0,-1)
            for i, case in enumerate(cases_FFT):
                print "data length", len(dataDict[fieldName][case])
#                FFT_plot(ax, dataDict[fieldName][case], samplingFrequencyDict[case], start, end, aliasDict[case], resampleDict[case], lineStyleDict[case], colorDict[case], lineWidthDict[case], markerDict[case])
                FFT_plot_simple(ax, dataDict[fieldName][case], samplingFrequencyDict[case], start, end, aliasDict[case], resampleDict[case], zorder=zorders[i])
            
            if position == 13:
                x=np.arange(50,5e3)
                ax.plot(x,30*x**(-5.0/3.0), linestyle='-.',color='black', linewidth=4, zorder=10)
                ax.text(3e3, 1e-4, r'$ \propto k^{-5/3}$', fontsize=30)
            ax.tick_params(axis='both', which='both', direction='out', length=4, width=1, labelsize=30)#major and minor ticks
            ax.set_xscale('log')
            ax.set_yscale('log')
            ax.set_xlim(1,end)
            ax.legend()
            ax.set_xlabel('frequency (Hz)')
            ax.set_ylabel(fieldNameAliasFFTDict[fieldName])
            fig.savefig(path2Data+"/"+"PICTURE_history_FFT/"+"8simu/"+fieldName+"_new_FFT_"+str(allProbePosition[p]/8.0).replace('.','p')+"D.png", bbox_inches='tight')

main()
