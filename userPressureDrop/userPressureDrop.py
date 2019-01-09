import numpy as np
import matplotlib.pyplot as plt

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

    pressureDrop = np.mean(port3[cutIndex:]) - np.mean(port2[cutIndex:])
    
#    ax_in_case.set_ylim(9.5,12)
    ax_in_case.set_title(dataDir)
    ax_in_case.legend()
    
    return pressureDrop

def main():
    plt.style.use('seaborn-white')
    caseList=["BirdCarreau/inlet_0p5",
              "Newtonian/Re4000",
              "BirdCarreau/inlet_0p3",
              "Newtonian/Re2400",
#              "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
#		   "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",
              "BirdCarreau/inlet0p5_impinging",
              "Newtonian/Re4000_impinging"]

    path2Data = "/home/hluo/Downloads/tmp/shape_square/2a_3_T/python_postProcessing"
    pressureDropList = []
    labelTuple = (
                "case1a",
                "case1b",
                "case2a",
                "case2b",
                "case1ai",
                "case1bi"                
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
        pressureDrop = plotCase(path2Data,caseDir, cut=0.7)
        print caseDir + " : " + str(pressureDrop)
        pressureDropList.append(pressureDrop)

    plt.figure(7) # 6 figures already there !!
    x = np.arange(len(labelTuple))
    plt.bar(x+0.5, height = pressureDropList, width=0.4, color=colorList)
    plt.xticks(x+0.75, labelTuple) # xticks can only chagned by plt object. axes don't work !!
    plt.xlim(0,7)
    plt.ylabel(r'$\Delta p/\rho \quad (m^2/s^2)$')
    plt.savefig(path2Data+"/"+'pressureDrop/pressureDrop.png', bbox_inches='tight', dpi=300)
    
    print pressureDropList[0]/pressureDropList[1]
    print pressureDropList[2]/pressureDropList[3]
    
main()