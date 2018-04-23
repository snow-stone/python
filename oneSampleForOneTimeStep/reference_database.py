import numpy as np

def data_Niewstadt1995_pipe():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def Niewstadt1995_pipe_Fig9():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/Fig9/Fig9.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]    
    
    return x, y
    
def data_Eggels_pipe_DNS():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/DNS_Eggels.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def data_Eggels_pipe_LDA():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_LDA.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def data_Eggels_pipe_PIV():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_PIV.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def data_Eggels_pipe_HWA():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_HWA.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

def dataFitting_Niewstadt1995_pipe(deg,samplingSize):
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    x = data[:,0]
    y = data[:,1]
    
    z = np.polyfit(x, y, deg)
    functionPolynome = np.poly1d(z)
    
    x_polyFit = np.linspace(min(x),max(x),samplingSize)
    
    return x_polyFit, functionPolynome(x_polyFit)

def analytic_Uz_meanProfile(uTau,samplingSize):
    nu=1e-6
#    viscousLayer()
#    bufferLayer()
#    logLayer()
    def viscousLayer(yPlus):
        return yPlus
    def bufferLayer(yPlus):
        return 5.0 * np.log(yPlus) - 3.05
    def logLayer(yPlus):
        return 2.5 * np.log(yPlus) + 5.5
        
    yPlus=np.linspace(0,170,samplingSize)
    y=yPlus*nu/uTau
    Uz=np.zeros(len(y))
    for i in range(len(y)):
        if yPlus[i] < 5:
            Uz[i] = uTau * viscousLayer(yPlus[i])
        elif yPlus[i] >= 5 and yPlus[i] < 30:
            Uz[i] = uTau * bufferLayer(yPlus[i])
        else:
            Uz[i] = uTau * logLayer(yPlus[i])
            
#    fig,ax = plt.subplots()
#    ax.set_xscale('log')
#    ax.plot(yPlus,Uz/uTau,label='mean',color='red')
    return yPlus, Uz/uTau