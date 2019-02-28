import numpy as np

def uPlus_yPlus(samplingSize,yPlusMax=200,yPlusMin=0):
    
    def viscousLayer(yPlus):
        return yPlus
    def bufferLayer(yPlus):
        return 5.0 * np.log(yPlus) - 3.05
    def logLayer(yPlus):
        return 2.5 * np.log(yPlus) + 5.5
        
    yPlus=np.linspace(yPlusMin,yPlusMax,samplingSize)

    UzPlus=np.zeros(len(yPlus))
    for i in range(len(yPlus)):
        if yPlus[i] < 5:
            UzPlus[i] = viscousLayer(yPlus[i])
        elif yPlus[i] >= 5 and yPlus[i] < 30:
            UzPlus[i] = bufferLayer(yPlus[i])
        else:
            UzPlus[i] = logLayer(yPlus[i])
            
    return yPlus, UzPlus