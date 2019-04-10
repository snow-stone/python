import matplotlib
matplotlib.use('agg')
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('seaborn-white') # from defaut
plt.rcParams.update({'font.size': 30})
plt.rcParams['savefig.dpi'] = 100

from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
## for Palatino and other serif fonts use:
rc('font',**{'family':'serif','serif':['Palatino']})
rc('text', usetex=True)

def plotCase(path2Data,dataDir,cut):
    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/"+"boundaryMean_p")
    time =  data[:,0]
    port1 = data[:,1]
    port2 = data[:,2]
    port3 = data[:,3]

    cutIndex = int(len(time)*cut) 
    
    fig, ax_in_case = plt.subplots()
    p = ax_in_case.plot(time[cutIndex:], port1[cutIndex:], label='Port1')
    ax_in_case.plot(time[:cutIndex],port1[:cutIndex],linestyle=':',color=p[0].get_color())
    
    p = ax_in_case.plot(time[cutIndex:], port2[cutIndex:], label='Port2')
    ax_in_case.plot(time[:cutIndex],port2[:cutIndex],linestyle=':',color=p[0].get_color())
    
    p = ax_in_case.plot(time[cutIndex:], port3[cutIndex:], label='Port3')
    ax_in_case.plot(time[:cutIndex],port3[:cutIndex],linestyle=':',color=p[0].get_color())

    pressureDrop_main = np.mean(port3[cutIndex:]) - np.mean(port2[cutIndex:])
    pressureDrop_b    = np.mean(port1[cutIndex:]) - np.mean(port2[cutIndex:])
    
#    ax_in_case.set_ylim(9.5,12)
    ax_in_case.set_title(dataDir)
    ax_in_case.legend()
    
    return pressureDrop_b, pressureDrop_main

def main():
    plt.style.use('seaborn-white')
    plt.rcParams['font.size'] = 10 # defaut value is 10
    plt.rcParams['savefig.dpi'] = 100
    caseList=[
              "BirdCarreau/inlet_0p3",
              "Newtonian/Re2400",    
              "BirdCarreau/inlet_0p5",
              "Newtonian/Re4000",
              "BirdCarreau/inlet0p5_impinging",
              "Newtonian/Re4000_impinging"
#              "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
#		   "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",
              ]

    path2Data = "/store/8simu_tmp/shape_square/2a_3_T/python_postProcessing"
    pressureDropList_main = []
    pressureDropList_b = []
    labelTuple = (
                r'$NN^{1}_{d}$',
                r'$N^{1}_{d}$',
                r'$NN^{2}_{d}$',
                r'$N^{2}_{d}$',
                r'$NN^{2}_{i}$',
                r'$N^{2}_{i}$'
                )      
    colorList = [
                "red",
                "blue",
                "red",
                "blue",
                "red",
                "blue"
                ]

    for i, caseDir in enumerate(caseList):
        pressureDrop_main, pressureDrop_b = plotCase(path2Data,caseDir, cut=0.7)
        print caseDir + " : " + str(pressureDrop_main)
        pressureDropList_main.append(pressureDrop_main)
        print caseDir + " : " + str(pressureDrop_b)
        pressureDropList_b.append(pressureDrop_b)

#    plt.figure(7) # 6 figures already there !!
    bar_width=0.35
    shift = 0.6
    fig, ax = plt.subplots()
    x = np.arange(len(labelTuple)) 
    ax.bar(x+shift, pressureDropList_main, bar_width, color=colorList)
    ax.bar(x+bar_width+shift, pressureDropList_b, bar_width, color=colorList, alpha=0.4)
#    ax.xticks(x+0.75, labelTuple) # xticks can only chagned by plt object. axes don't work !!
#    ax.set_xlim(0,6.5)
    
    ax.set_xticks(x+0.75)
    ax.set_xticklabels(labelTuple)
    ax.set_ylabel(r'$\Delta p/\rho \quad (m^2/s^2)$')
    ax.legend(bbox_to_anchor=(0.5, 1))
    fig.savefig(path2Data+"/"+'pressureDrop/pressureDrop.png', bbox_inches='tight', dpi=300)
    
    print pressureDropList_main[0]/pressureDropList_main[1]
    print pressureDropList_main[2]/pressureDropList_main[3]
    
main()
