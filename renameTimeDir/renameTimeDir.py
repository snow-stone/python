
def convert2TimeDirName(string):
    if '.' in string:
        while string[-1] == '0':
            string = string[:-1] # remove the trailing '0'
        while string[-1] == '.': # then after that, remove the trailing '.'
            string = string.rstrip('.')
    else:
        print 'Integer timeStep here :', string
    return string

def getInterval(start,end,sorted_dir_list_in):
    sorted_dir_list_out=[]
    for dir_I in sorted_dir_list_in:
        if float(dir_I) < start or float(dir_I) > end :
            continue
        else :
            sorted_dir_list_out.append(dir_I)
    
    return sorted_dir_list_out

def formatOpenFOAM(start1,end1,start2,end2,step,path,ifRename):
    import os
    import numpy as np
#    path = './'
    
#    name_list = os.listdir(path)
#==============================================================================
#   Don't understand why this is not working
    dir_list = [directory for directory in os.listdir(path) if os.path.isdir(path+directory)]
#==============================================================================
#    dir_list = [name for name in name_list if os.path.isdir(path+name)]
#    for i in range(len(name_list)):
#        print 'name_list[i] ',path+name_list[i], os.path.isdir(path+name_list[i])
#    dir_list = name_list
#    print dir_list
    
#   Very Important here : remove dir named 'constant'
    dir_list.remove('constant')
    #print "dir_list is here : ", dir_list
#    print "sorted dir_list is here : ",sorted(dir_list,key=float)
    dir_before=[]
    dir_after=[]
    dir_calc=[]
    
#    print 'getInterval(1.09, 1.18, sorted(dir_list,key=float))'
#    print getInterval(1.09, 1.18, sorted(dir_list,key=float))
#    for dir_I in sorted(dir_list,key=float):
    sortedInterval = getInterval(start1, end1, sorted(dir_list,key=float))
    #print 'sortedInterval : ', sortedInterval
    #dir_calc_array = np.linspace(start2, end2, len(sortedInterval))
    dir_calc_array = np.arange(start2, end2, step)
    dir_calc = [convert2TimeDirName(str(x)) for x in dir_calc_array]
    for dir_I in sortedInterval:
        # only decimals are concerned, if integer, integers are naturally the right format
##        if "." in dir_I:
##            dir_before.append(dir_I)
##            dir_after.append(convert2TimeDirName(dir_I))
        dir_before.append(dir_I)
        dir_after.append(convert2TimeDirName(dir_I))
    
#    print dir_before
#    print sorted(dir_before,key=float)
    print 'len(dir_before), len(dir_after), len(dir_calc)'
    print len(dir_before), len(dir_after), len(dir_calc)
    for i in range(len(dir_before)):
        #info = "converting " + dir_before[i] + " to " + dir_after[i] + "    calculated " + dir_calc[i]
        info = "converting " + dir_before[i] + " to calculated " + dir_calc[i]
        # print for right align
        print info.rjust(100)
        if ifRename :
            #os.rename(path+dir_before[i], path+dir_after[i])
            os.rename(path+dir_before[i], path+dir_calc[i])
    
    if not ifRename :
        print "Not renamed yet."
        print "if the renamed dir name list is what you want."
        print "Change the ifrename flag to True"

#renameTimeDir("./", False)

def main():
    relativePath='./'
    pathList = [relativePath+'processor'+str(i)+'/' for i in range(32)]
#    pathList = relativePath+'processor'+str(0)+'/'
    for path in pathList:
        print "path = ", path
        formatOpenFOAM(127.9, 150.4, 127.9, 150.5, 0.045, path, True)
#    formatOpenFOAM(127.9, 150.4, 127.9, 150.5, 0.045, pathList, False)

main()
