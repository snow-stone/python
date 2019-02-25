
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
        'timeStep':4.5,
        'startTime':4.5,  # KinecticEnergy stationary
        'endTime':5,
        'chunkStep':10,
        'NbOfFiles':51,
        'path':"pipe4",
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        }


# secondary physical parameters
#Retau=uTau*R/nu
