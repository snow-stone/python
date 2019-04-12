import scipy.io as io

def printBijection(database, aliasName):
    
    print "============================"
    print "case alias : ", aliasName
    print "source : "
    print database[aliasName]['sourceDir']
    print "target : "
    print database[aliasName]['targetDir']
    print ""

d = io.loadmat('dataBase')

print "read from *.mat"
print "keys : ", d.keys()

d.pop("__header__")
d.pop("__globals__")
d.pop("__version__")

print "after removing extra keys other than case alias"
print "keys : ", d.keys()

for alias in d:
    printBijection(d, alias)
