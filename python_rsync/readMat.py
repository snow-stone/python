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

#for alias in d:
#    printBijection(d, alias)

a = d['D1-1d']

print "a"
print a

print "a.dtype"
print a.dtype

print "a.size"
print a.size

print "a.shape"
print a.shape

print "a[0][0]"
print a[0][0]

print "a['sourceDir']"
print a['sourceDir']

