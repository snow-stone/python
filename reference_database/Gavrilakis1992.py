import numpy as np

def Fig4a():                                                                                                                                                                                                                         
    string='/home/hluo/Pictures/Gavrilakis1992/Fig4a/UPlus.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

def Fig9a_DNS_G():
    string='/home/hluo/Pictures/Gavrilakis1992/Fig9a/DNS_G.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    x = data[:,0]
    y = data[:,1]
    return x, y

def Fig9a_Kim1987():
    string='/home/hluo/Pictures/Gavrilakis1992/Fig9a/Kim1987.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    x = data[:,0]
    y = data[:,1]
    return x, y

def Fig9a_Niederschulte1989():
    string='/home/hluo/Pictures/Gavrilakis1992/Fig9a/Niederschulte1989.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    x = data[:,0]
    y = data[:,1]
    return x, y

def Fig9a_Nishino1989():
    string='/home/hluo/Pictures/Gavrilakis1992/Fig9a/Nishino1989.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    x = data[:,0]
    y = data[:,1]
    return x, y
