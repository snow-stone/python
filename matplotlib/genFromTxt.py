import numpy as np
import matplotlib.pyplot as plt


def genFromTxt(dataFile,ax,colon):
    data=np.genfromtxt(dataFile,skip_header=1,delimiter=' ')
    x=data[:,0]
    y=data[:,colon]
    
    return x,y
    
def main():
    fig1,ax1 = plt.subplots()
    x1, y1 = genFromTxt('../fieldStatistics/TurbulentKineticEnergy', ax1, 2)
    ax1.plot(x1,y1,linewidth=1.5,label='Turbulent Kinietic Energy')
    
    fig2,ax2 = plt.subplots()
    x2, y2 = genFromTxt('../fieldStatistics/KineticEnergy', ax2, 1)
    ax2.plot(x2,y2,linewidth=1.5,label='Total Kinietic Energy')    
    
main()