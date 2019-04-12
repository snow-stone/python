import json

def printBijection(database, aliasName):
    
    print "----------------------------"
    print "case alias : ", aliasName
    print "source : ", database[aliasName]['sourceDir']
    print "target : ", database[aliasName]['targetDir']
    print ""

d = json.load(open("database.txt"))

print ""
print "============================"
print "All keys are printed here: "
print d.keys()

for alias in d:
    printBijection(d, alias)
