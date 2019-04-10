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


#def plotCase(path2Data,dataDir,cut):
#    data = np.genfromtxt(path2Data+"/"+dataDir+"/"+"userDefinedLog/"+"boundaryMean_p")
#    time =  data[:,0]
#    port1 = data[:,1]
#    port2 = data[:,2]
#    port3 = data[:,3]
#
#    cutIndex = int(len(time)*cut) 
#    
#    fig, ax_in_case = plt.subplots()
#    p = ax_in_case.plot(time[cutIndex:], port1[cutIndex:], label='Port1')
#    ax_in_case.plot(time[:cutIndex],port1[:cutIndex],linestyle=':',color=p[0].get_color())
#    
#    p = ax_in_case.plot(time[cutIndex:], port2[cutIndex:], label='Port2')
#    ax_in_case.plot(time[:cutIndex],port2[:cutIndex],linestyle=':',color=p[0].get_color())
#    
#    p = ax_in_case.plot(time[cutIndex:], port3[cutIndex:], label='Port3')
#    ax_in_case.plot(time[:cutIndex],port3[:cutIndex],linestyle=':',color=p[0].get_color())
#
#    pressureDrop = np.mean(port3[cutIndex:]) - np.mean(port2[cutIndex:])
#    
##    ax_in_case.set_ylim(9.5,12)
#    ax_in_case.set_title(dataDir)
#    ax_in_case.legend()
#    
#    return pressureDrop

def main():
    plt.style.use('seaborn-white')
    plt.rcParams['font.size'] = 10 # defaut value is 10
    plt.rcParams['savefig.dpi'] = 100
    caseList=[
              "BirdCarreau/inlet_0p3",
              "Newtonian/Re2400",
              "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
		   "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",
              "BirdCarreau/inlet_0p5",
              "Newtonian/Re4000",
              "BirdCarreau/inlet0p5_impinging",
              "Newtonian/Re4000_impinging"
              ]

    path2Data = "/store/8simu_tmp/shape_square/2a_3_T/python_postProcessing"

    labelTuple = (
                r'$NN^{1}_{d}$',
                r'$N^{1}_{d}$',
                r'$NN^{1}_{d,St=1}$',
                r'$NN^{1}_{d,St=5}$',
                r'$NN^{2}_{d}$',
                r'$N^{2}_{d}$',
                r'$NN^{2}_{i}$',
                r'$N^{2}_{i}$'
                )      
    colorList = [
                "red",
                "blue",
                "red",
                "red",
                "red",
                "blue",
                "red",
                "blue"
                ]
    k_mean_peak = [
                0.0083,
                0.08,
                0.05,
                0.098,
                0.16,
                0.26,
                0.476,
                0.6
                ]

    plt.figure(1)
    x = np.linspace(0, len(labelTuple)*1.5, len(labelTuple))
    plt.bar(x+0.5, height = k_mean_peak, width=0.4, color=colorList)
    plt.xticks(x+0.75, labelTuple) # xticks can only chagned by plt object. axes don't work !!
#    plt.xlim(0,8.5)
    plt.ylim(0,0.7)
    plt.ylabel(r'$\overline{k}_{max}$')
    plt.savefig(path2Data+"/"+'bar_k_mean_peakValue/k_mean_peakValue.png', bbox_inches='tight', dpi=300)
    
#    print pressureDropList[0]/pressureDropList[1]
#    print pressureDropList[2]/pressureDropList[3]
    
main()
