# sampleLinesStatistics3.py

## source

## Functionality
read in one sample per time step and do a chunked statistics (moving average/rms in time) to check convergence of numerical solutions.

## Line
`getChunkedStd` is the right implementation while `getChunkedStd1` is the wrong one resulting in a very big rms !

## Developpment Approaches
check_data_shape(startTime, endTime, NbOfTimeSteps,dataShape_In2D_Tuple)   
sampleLinesStatistics1d(validDataList=[return of the last function], chunkStep=NbOfTimeStep_PerChunk, uTau=[friction velocity], ifPlotAllTimes=[flag for choose whether to plot the non-avergaed profiles (raw samples) of Uz or not in the 1st plot])

## Input
### Internal input
principle:   
time Interval of interest   
uTau   
for others, look into `Developpment Approaches`

## Output
one plot on x-log for average profile of Uz   
one chart plot for visulization of every chunk   
one Plot on rms of Uz (based on the first plot on average Uz)

## How

## Improvement
add import from `../` functionality, seperating from main module

## Limit
Didn't see how to merge this one-sample-per-timeStep tool with the big-sampleSizde-spatialAverage-at-only-one-timeStep.

# Cope with limit
