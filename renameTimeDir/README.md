# renameTimeDir.py

## source
modified from last version

## Functionality
for the fact that OF sometimes produces `109.00000000011951` instead of `109` as expected:   
convert chosed interval of time dirs in `processor{0..31}` to the calculated(expected) time dirs

## Line
```python
os.rename(path+dir_before[i], path+dir_calc[i])
# converting path+dir_before[i] to path+dir_calc[i]
```

## Developpment Approacheseses
function `formatOpenFOAM(start1,end1,start2,end2,step,path,ifRename)`:   
start1 and end1 is for indicating the time interval that we are interested in of course the dirs in this case must be sorted numerically (thus `constant` must be removed from `dir_list`).   
start2 and end2 is for indicating the target time dir names with strictly EQUAL step. 

## Input
### Internal input
bool flag in `formatOpenFOAM(127.9, 150.4, 127.9, 150.5, 0.045, path, True)` need to be set

## Output

renamed time dirs if bool flag in formatOpenFOAM(127.9, 150.4, 127.9, 150.5, 0.045, path, True)` is set to `True`

## How
step 0 : set flag to `False` and see what will happen. If everything corresponds to what you are expecting. then follow step 1.   
step 1 : set flag to `True` and re-run.

## Improvement
sort function added   
`constant` dir excluded from consideration   
move the `if '.' in string` inside `convert2TimeDirName` and add output for Integer outputSteps.

## Limit
need to tune the function `formatOpenFOAM(start1,end1,start2,end2,step,path,ifRename)` to get the right `expected time dirs` manually. Be careful.   
didn't remove the part concerning `dir_after`.

# Cope with limit
