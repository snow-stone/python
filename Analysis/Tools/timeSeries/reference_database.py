import numpy as np

def data_Niewstadt1995_pipe():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UzRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

def Niewstadt1995_pipe_UrRMS():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UrRMS.csv'
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

def dataFitting_Niewstadt1995_pipe_UrRMS(deg,samplingSize):
    string='/home/hluo/Pictures/Niewstadt1995_pipe/rmsProfile_velocity/pipeFlow_UrRMS.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    x = data[:,0]
    y = data[:,1]
    
    z = np.polyfit(x, y, deg)
    functionPolynome = np.poly1d(z)
    
    x_polyFit = np.linspace(min(x),max(x),samplingSize)
    
    return x_polyFit, functionPolynome(x_polyFit)
    
def Niewstadt1995_pipe_Fig9():
    string='/home/hluo/Pictures/Niewstadt1995_pipe/Fig9/Fig9.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]    
    
    return x, y

import Dai_thesis

#def Dai_thesis_Fig4p8a_water():
#    string='/home/hluo/Pictures/Dai_T/meanProfile_velocity/XEqM4_debitMin/profile_XEqM4_debitMin.csv'
#    data=np.genfromtxt(string,skip_header=1,delimiter=',')
#    
#    x = data[:,0]
#    y = data[:,1]
#    
#    return x, y
#
#def Dai_thesis_Fig4p9a_water():
#    string='/home/hluo/Pictures/Dai_T/meanProfile_velocity/XEqP12_debitMin/profile_XEqP12_debitMin.csv'
#    data=np.genfromtxt(string,skip_header=1,delimiter=',')
#    
#    x = data[:,0]
#    y = data[:,1]
#    
#    return x, y
#    
#def Dai_thesis_Fig4p10a_water():
#    string='/home/hluo/Pictures/Dai_T/meanProfile_velocity/XEqP33_debitMin/profile_XEqP33_debitMin.csv'
#    data=np.genfromtxt(string,skip_header=1,delimiter=',')
#    
#    x = data[:,0]
#    y = data[:,1]
#    
#    return x, y

def Eggels1994_thesis_Fig4p5_DNS():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.5/DNS_E.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def Eggels1994_thesis_Fig4p5_HWA():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.5/HWA.csv'
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
#
#def analytic_Uz_meanProfile(uTau,samplingSize):
#    nu=1e-6
##    viscousLayer()
##    bufferLayer()
##    logLayer()
#    def viscousLayer(yPlus):
#        return yPlus
#    def bufferLayer(yPlus):
#        return 5.0 * np.log(yPlus) - 3.05
#    def logLayer(yPlus):
#        return 2.5 * np.log(yPlus) + 5.5
#        
#    yPlus=np.linspace(0,170,samplingSize)
#    y=yPlus*nu/uTau
#    Uz=np.zeros(len(y))
#    for i in range(len(y)):
#        if yPlus[i] < 5:
#            Uz[i] = uTau * viscousLayer(yPlus[i])
#        elif yPlus[i] >= 5 and yPlus[i] < 30:
#            Uz[i] = uTau * bufferLayer(yPlus[i])
#        else:
#            Uz[i] = uTau * logLayer(yPlus[i])
#            
#    return yPlus, Uz/uTau
    
#def analytic_Uz_meanProfile(ifwallcoor, uTau,samplingSize):
#    nu=1e-6
##    viscousLayer()
##    bufferLayer()
##    logLayer()
#    def viscousLayer(yPlus):
#        return yPlus
#    def bufferLayer(yPlus):
#        return 5.0 * np.log(yPlus) - 3.05
#    def logLayer(yPlus):
#        return 2.5 * np.log(yPlus) + 5.5
#        
#    yPlus=np.linspace(0,170,samplingSize)
#    y=yPlus*nu/uTau
#    Uz=np.zeros(len(y))
#    for i in range(len(y)):
#        if yPlus[i] < 5:
#            Uz[i] = uTau * viscousLayer(yPlus[i])
#        elif yPlus[i] >= 5 and yPlus[i] < 30:
#            Uz[i] = uTau * bufferLayer(yPlus[i])
#        else:
#            Uz[i] = uTau * logLayer(yPlus[i])
#            
#    if not ifwallcoor :
#        return y, Uz/uTau
#    elif ifwallcoor :
#        return yPlus, Uz/uTau
        
def analytic_Uz_meanProfile(yPlusMax,samplingSize):
#    viscousLayer()
#    bufferLayer()
#    logLayer()
    def viscousLayer(yPlus):
        return yPlus
    def bufferLayer(yPlus):
        return 5.0 * np.log(yPlus) - 3.05
    def logLayer(yPlus):
        return 2.5 * np.log(yPlus) + 5.5
        
    yPlus=np.linspace(0,yPlusMax,samplingSize)

    UzPlus=np.zeros(len(yPlus))
    for i in range(len(yPlus)):
        if yPlus[i] < 5:
            UzPlus[i] = viscousLayer(yPlus[i])
        elif yPlus[i] >= 5 and yPlus[i] < 30:
            UzPlus[i] = bufferLayer(yPlus[i])
        else:
            UzPlus[i] = logLayer(yPlus[i])
            
    return yPlus, UzPlus