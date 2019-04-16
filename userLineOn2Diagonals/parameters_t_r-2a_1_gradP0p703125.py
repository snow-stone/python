
# physical parameters

physics={
        'h':0.004,   # D=2h
        'nu':1.0e-6,
        'uTau':0.045
        }

#print physics

sampling={
        'raw_sample_size':128,
        'dataShape':(200,4)     
        }

# data entry parameters

dataEntry={
        'timeStep':20,
        'chunkStep':40,
        'NbOfFiles':161,
        'path':"/store/8simu_tmp/gradP0_1p0125",
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        }
