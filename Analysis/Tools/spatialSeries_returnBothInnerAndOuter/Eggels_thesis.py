import numpy as np

def Fig4p5_DNS():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.5/DNS_E.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def Fig4p5_HWA():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.5/HWA.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def Fig4p7_DNS():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/DNS_Eggels.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def Fig4p7_LDA():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_LDA.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def Fig4p7_PIV():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_PIV.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y
    
def Fig4p7_HWA():
    string='/home/hluo/Pictures/Thesis.Eggels1994/pipe/Fig4.7/EXP_HWA.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

