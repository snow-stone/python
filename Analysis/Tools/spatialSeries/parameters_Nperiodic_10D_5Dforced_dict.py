

# physical parameters

physics={
        'R':0.004,
        'nu':1.0e-6,
        'uTau':0.051
        }

#print physics

sampling={
        'raw_sample_size':160,
        'dataShape':(200,4)
        }

# data entry parameters

dataEntry={
        'timeStep':139.5,
        'path':"/store/caseByGeometry/pipe/blockMesh/Nperiodic/5patchIn_5patchOut/3_gradP=1.3/allPatches_mapped/lengthVariation/10D_5Dforced",
        }


parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry
        }

plotSavePath="10D_5Dforced/"

# secondary physical parameters
#Retau=uTau*R/nu