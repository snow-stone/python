
import numpy as np
import matplotlib.pyplot as plt


def reader():
    fileName='KineticEnergy'
    data = np.genfromtxt('postProcessing/fieldStatistics'+'/'+fileName)
    x = data[:,0]
    y = data[:,1]

    return x,y    

def plot():
    x, y = reader()
    
    fig, ax = plt.subplots()
    
    ax.plot(x,y)
    
plot()