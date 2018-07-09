import numpy as np

def Fig4p8a(fluid):
    string='/home/hluo/Pictures/Dai_T/meanProfile_velocity/XEqM4_debitMin/profile_XEqM4_debitMin.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    switcher={
        'EAU':1,
        'PAA':2,
        'XG':3
    }
    
    x = data[:,0]
    y = data[:,switcher[fluid]]
    
    return x, y

def Fig4p9a(fluid):
    string='/home/hluo/Pictures/Dai_T/meanProfile_velocity/XEqP12_debitMin/profile_XEqP12_debitMin.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    switcher={
        'EAU':1,
        'PAA':2,
        'XG':3
    }
    
    x = data[:,0]
    y = data[:,switcher[fluid]]
    
    return x, y
    
def Fig4p10a(fluid):
    string='/home/hluo/Pictures/Dai_T/meanProfile_velocity/XEqP33_debitMin/profile_XEqP33_debitMin.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    switcher={
        'EAU':1,
        'PAA':2,
        'XG':3
    }
    
    x = data[:,0]
    y = data[:,switcher[fluid]]
    
    return x, y

def Fig4p11a(fluid):
    string='/home/hluo/Pictures/Dai_T/rmsProfile_velocity/profileRMS_XEqM4_debitMin.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    switcher={
        'EAU':1,
        'PAA':2,
        'XG':3
    }
    
    x = data[:,0]
    y = data[:,switcher[fluid]]
    
    return x, y

def Fig4p12a(fluid):
    string='/home/hluo/Pictures/Dai_T/rmsProfile_velocity/profileRMS_XEqP12_debitMin.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    switcher={
        'EAU':1,
        'PAA':2,
        'XG':3
    }
    
    x = data[:,0]
    y = data[:,switcher[fluid]]
    
    return x, y
    
def Fig4p13a(fluid):
    string='/home/hluo/Pictures/Dai_T/rmsProfile_velocity/profileRMS_XEqP33_debitMin.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')
    
    switcher={
        'EAU':1,
        'PAA':2,
        'XG':3
    }
    
    x = data[:,0]
    y = data[:,switcher[fluid]]
    
    return x, y