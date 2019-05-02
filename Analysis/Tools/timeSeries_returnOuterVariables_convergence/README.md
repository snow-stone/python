# timeSeries_returnOuterVariables

Input : `"postProcessing/sets/"+timeName+"/"+sampleNaming+"_U.xy"` which is output of sample utility

## 修改
把module timeSeriesReader_ReturnOuterVariables的输出改成了只有`rByD`才无量纲处理，其他的无量纲化都放在主程序里面。这样的话module里面不再有关于`uTau`的各种操作，具有通用性。

## limit


## cope with limit
reference speed is no longer hardcoded as `0.3m/s`
