
# physical parameters

physics={
        'h':0.004,   # D=2h
        'nu':1.0e-6,
        'uTau':0.045
        }

#print physics

sampling={
        'raw_sample_size':64,
        'dataShape':(79,2)     
        }

# data entry parameters

dataEntry={
	   'timeStep':1.95,
        'chunkStep':40,
        'NbOfFiles':161,
        'path':".",
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        }
