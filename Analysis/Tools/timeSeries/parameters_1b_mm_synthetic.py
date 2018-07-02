
# physical parameters

physics={
        'R':0.004,
        'nu':1.0e-6,
        'uTau':0.0473
        }

#print physics

sampling={
        'raw_sample_size':160,
#        'dataShape':(199,4)     # uniform
#        'dataShape':(97,4)     # face 3
#        'dataShape':(103,4)     # face 2
        'dataShape':(104,4)     # face 1
        }

# data entry parameters

dataEntry={
        'startTime':5.01,
        'endTime':7.01,
        'chunkStep':40,
        'NbOfFiles':161,
        'path':"/store/caseByGeometry/T-new-mesh/1b_mirrorMerge",
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        }

plotSavePath="10D_5Dforced/"

# secondary physical parameters
#Retau=uTau*R/nu