# static
import json

database=json.load(open("/home/hluo/work/git/python/python_rsync/database.txt"))
alias="D1-1d_lR2_afterAugust"

# physical parameters

physics={
        'R':0.004,
        'nu':1.0e-6,
        'uTau':0.0473
        }

#print physics

sampling={
        'raw_sample_size':160,
        'dataShape3':(321,4),     # face 3
        'dataShape2':(332,4),     # face 2
        'dataShape1':(195,4),     # face 1
        'dataShape': None
        }

# data entry parameters

dataEntry={
        'startTime':8,  
        'endTime':11,
        'chunkStep':30,
        'NbOfFiles':121,
        #data position :
        #newton:/store/lmfa/fct/hluo/zaurak/caseByMachine/occigen/T/passiveScalar/Newtonian/mapped/flowRate/min/1d_lR2/afterAugust/postProcessing
        'path':database[alias]['targetDir']
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        'alias':database[alias]['name2plot']
        }

#plotSavePath="10D_5Dforced/"

# secondary physical parameters
#Retau=uTau*R/nu
