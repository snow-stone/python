# UbarCalc

## Summarize for three way of calculating Ubar/flux
The following 3 ways generates data to either a log file of its own or the
openfoam simulation log or a simple raw data file. Get data from logs or 
raw file are implemented in UbarCalc for these 3 methods except for the 4th.

### patchIntegrate phi

### cellSetAverage
my own developpement. Origines from `Foam::fv::pressureGradientExplicitSource`

### pressureGradientExplicitSource
run time library

### patchAverage U
This... need to be verified
