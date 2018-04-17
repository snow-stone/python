# renameTimeDir.py

## source

## Functionality
convert every time dir in `processor{0..31}`which has a `.` to the regular format that
it doesn't end with 0 nor `.`

## Line

## Developpment Approacheseses

## Input
### Internal input
bool flag in `formatOpenFOAM(path, False)` need to be set

## Output
renamed time dirs if bool flag in `formatOpenFOAM(path, False)` is set to `True`

## How
step 0 : set flag to `False` and see what will happen. If everything corresponds to what you are expecting. then follow step 1.   
step 1 : set flag to `True` and re-run.

## Limit
no sort function introduced, everything inside `processor{0..31}` is treated equally including the `constant` dir.

# Cope with limit
