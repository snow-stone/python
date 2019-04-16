# static
import json

database=json.load(open("/home/hluo/work/git/python/python_rsync/database.txt"))
alias="t_r-2a_1_gradP0p703125"

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
        'timeStep':12,
        'chunkStep':40,
        'NbOfFiles':161,
        'path':database[alias]['targetDir']
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        'alias':database[alias]['name2plot']
        }
