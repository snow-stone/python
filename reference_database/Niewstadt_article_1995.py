import numpy as np

def Fig7():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

def Fig8():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UrRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

def dataFitting_Fig7(samplingSize,deg=6):
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    x = data[:,0]
    y = data[:,1]
    
    z = np.polyfit(x, y, deg)
    functionPolynome = np.poly1d(z)
    
    x_polyFit = np.linspace(min(x),max(x),samplingSize)
    
    return x_polyFit, functionPolynome(x_polyFit)

def dataFitting_Fig8(samplingSize,deg=4):
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UrRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    x = data[:,0]
    y = data[:,1]
    
    z = np.polyfit(x, y, deg)
    functionPolynome = np.poly1d(z)
    
    x_polyFit = np.linspace(min(x),max(x),samplingSize)
    
    return x_polyFit, functionPolynome(x_polyFit)
    
def Fig9():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/Fig9/Fig9.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]    
    
    return x, y