import numpy as np
import scipy.io as io
import matplotlib.pyplot as plt

def FFT_plot(ax, originalTimeSeries, samplingFrequency, startIndex, endIndex, labelAlias, resamplingStep):
#    n=1 #removing mean
#    m=10000
#    sampling=1
#    data=data0
    A = np.fft.rfft(originalTimeSeries)
    print "data length", len(originalTimeSeries)
#    print len(data)
    N = len(originalTimeSeries)
#    dt= 0.0005
    f=(np.arange(len(A))[startIndex:endIndex:resamplingStep]/(samplingFrequency*N))
    ax.plot(f, np.absolute(A)[startIndex:endIndex:resamplingStep]/N, label=labelAlias)
    
def main():
    plt.style.use('seaborn-white') # from defaut
    plt.rcParams.update({'font.size': 25})
    plt.rcParams['savefig.dpi'] = 100
    
    from matplotlib import rc
#    rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
    ## for Palatino and other serif fonts use:
    rc('font',**{'family':'serif','serif':['Palatino']})
    rc('text', usetex=True)
    
    signal = io.loadmat("signal_U_y_2D")
    
    cases = [
#             "BirdCarreau"+"/"+"inlet_0p3",
#             "Newtonian"+"/"+"Re2400",
#             "BirdCarreau/inlet_0p3-a_0p5-setT_St_1",
#             "BirdCarreau/inlet_0p3-a_0p5-setT_St_5",
#             "BirdCarreau"+"/"+"inlet_0p5",
#             "Newtonian"+"/"+"Re4000",
             "BirdCarreau/inlet0p5_impinging",
             "Newtonian/Re4000_impinging"
            ]
    
    samplingFrequencyDict = {
        "BirdCarreau/inlet_0p3"                :0.0005,
        "Newtonian/Re2400"                     :0.0005,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":0.0005,
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":0.0005,
        "BirdCarreau/inlet_0p5"                :0.0002,
        "Newtonian/Re4000"                     :0.0005,
        "BirdCarreau/inlet0p5_impinging"       :0.0005,
        "Newtonian/Re4000_impinging"           :0.0005
    }
    
    aliasDict={
        "BirdCarreau/inlet_0p3"                :r'$NN^{1}_{d}$',
        "Newtonian/Re2400"                     :r'$N^{1}_{d}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_1":r'$NN^{1}_{d,St=1}$',
        "BirdCarreau/inlet_0p3-a_0p5-setT_St_5":r'$NN^{1}_{d,St=5}$',
        "BirdCarreau/inlet_0p5"                :r'$NN^{2}_{d}$',
        "Newtonian/Re4000"                     :r'$N^{2}_{d}$',
        "BirdCarreau/inlet0p5_impinging"       :r'$NN^{2}_{i}$',
        "Newtonian/Re4000_impinging"           :r'$N^{2}_{i}$'
    }
    
    fig, ax = plt.subplots(figsize=(20,10))
    start=1   # removing mode 0 : average (in time domain)
    end=10000 # big enough
    resample=1# no resampling defaut value : 1
    
    for case in cases:
        data = signal[case][0]
        print data
        print type(data)
        print "data length", len(data)
        FFT_plot(ax, data, samplingFrequencyDict[case], start, end, aliasDict[case], resample)

    x=np.arange(1000)
    ax.plot(x,x**(-5.0/3.0), linestyle='-.',color='blue')
    ax.plot(x,.05*x**(-1.0), linestyle='-.', color='red')    
    
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.legend()
    ax.set_xlabel('frequency (Hz)')
    ax.set_ylabel('fluctuation magnitude')
    fig.savefig("signal_U_y_2D.png", bbox_inches='tight')
        
main()
        