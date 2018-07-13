import numpy as np

def Fig8b_DNS_E_cmpt_r():
    string='/home/hluo/Pictures/Eggels.Article.1994/Fig8/b_Eggels_cmpt_r.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

def Fig8b_DNS_E_cmpt_theta():
    string='/home/hluo/Pictures/Eggels.Article.1994/Fig8/b_Eggels_cmpt_theta.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y

def Fig8b_DNS_E_cmpt_z():
    string='/home/hluo/Pictures/Eggels.Article.1994/Fig8/b_Eggels_cmpt_z.csv'
    data=np.genfromtxt(string,skip_header=1,delimiter=',')

    x = data[:,0]
    y = data[:,1]
    
    return x, y        