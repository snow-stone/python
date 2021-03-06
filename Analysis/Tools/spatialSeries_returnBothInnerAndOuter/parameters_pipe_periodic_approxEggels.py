
# physical parameters

physics={
        'R':0.004,
        'nu':1.0e-6,
        'uTau':0.051
        }

#print physics

sampling={
        'raw_sample_size':160,
        #'dataShape':(200,4)     # uniform
        'dataShape':(99,4)       # face
        }

# data entry parameters

dataEntry={
        'timeStep':5,
        'path':"/store/caseByGeometry/pipe/blockMesh/periodic/pipe4/prototype_artificiallyReducedViscosity",
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        }


# secondary physical parameters
#Retau=uTau*R/nu
