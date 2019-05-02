# static
import json

database=json.load(open("/home/hluo/work/git/python/python_rsync/database.txt"))
alias='D1-1b'

# physical parameters

physics={
        'R':0.004,
        'nu':1.0e-6,
        'uTau':0.0473
        }

#print physics

sampling={
        'raw_sample_size':160,
        'dataShape3':(97,4),      # face 3
        'dataShape2':(103,4),     # face 2
        'dataShape1':(104,4),     # face 1
        'dataShape': None
        }

# data entry parameters

dataEntry={
        'startTime':5.01,
        'endTime':7.01,
        'chunkStep':40,
        'NbOfFiles':161,
        # old path :
        #'path':"/store/caseByGeometry/T/new-mesh/pointwise/postProcessing/1b_mirrorMerge",
        # data position :
        # /store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1b_mirrorMerge/postProcessing
        #'path':'/store/T_c/1b_mirrorMerge'
        'path':database[alias]['targetDir']
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        'alias':database[alias]['name2plot']
        }


# secondary physical parameters
#Retau=uTau*R/nu
