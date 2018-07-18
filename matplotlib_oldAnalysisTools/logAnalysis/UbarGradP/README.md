# UbarGradP.py

## source

## Functionality
grab info about Ubar's and gradP's output into logFile when using "userConstantExplicitPGradForce"

## Line

## Developpment Approaches

## Input
### Internal input
logFile   
n   
timeStepEnd   
timeStepStart

## Output
Two Two y-axis plot    
1. time vs Ubar/gradP : from initial timeStep to `timeStepEnd`   
2. time vs Ubar/gradP : from `timeStepStart` to end of simulation

## How
use the module like in function `getUbarGradP` with only two explosed argument `logFile, n`.   
take what is inside : reader and plot functions with an extra parameter to control `timeStepEnd timeStepStart`.

## Improvement
add two function to plot   

## Limit

# Cope with limit
