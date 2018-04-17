
def convert2TimeDirName(string):
    while string[-1] == '0':
        string = string[:-1] # remove the trailing '0'
    while string[-1] == '.':
        string = string.rstrip('.')
    return string


def formatOpenFOAM(path, ifRename):
    import os
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
    
    dir_before=[]
    dir_after=[]
    
    for dir_I in dir_list:
        if "." in dir_I:
            dir_before.append(dir_I)
            dir_after.append(convert2TimeDirName(dir_I))
    
#    print dir_before
#    print sorted(dir_before,key=float)
    for i in range(len(dir_before)):
        info = "converting " + dir_before[i] + " to " + dir_after[i]
        print info.rjust(50)
        if ifRename :
            os.rename(path+dir_before[i], path+dir_after[i])
    
    if not ifRename :
        print "Not renamed yet."
        print "if the renamed dir name list is what you want."
        print "Change the ifrename flag to True"

#renameTimeDir("./", False)

def main():
    relativePath='./'
    pathList = [relativePath+'processor'+str(i)+'/' for i in range(32)]
#    pathList = relativePath+'processor'+str(0)+'/'
    print "pathList ", pathList
    for path in pathList:
        formatOpenFOAM(path, False)
#    formatOpenFOAM(relativePath, True)

main()