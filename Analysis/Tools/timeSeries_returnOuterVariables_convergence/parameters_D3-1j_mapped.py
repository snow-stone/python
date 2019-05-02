# static
import json

database=json.load(open("/home/hluo/work/git/python/python_rsync/database.txt"))
alias="D3-1j_mapped"

# physical parameters

physics={
        'R':0.004,
        'nu':1.0e-6,
        'uTau':0.0473
        }

#print physics

sampling={
        'raw_sample_size':160,
        'TdataShape3':(205,2),    # face 3
        'TdataShape2':(220,2),    # face 2
        'dataShape3':(205,4),    # face 3
        'dataShape2':(220,4),    # face 2
        'dataShape1':(220,4),    # face 1
        'dataShape': None
        }

# data entry parameters

dataEntry={
        'startTime':0.45,  
        'endTime':0.6,
        'chunkStep':50,
        'NbOfFiles':151,
        #data position :
        #newton:/store/lmfa/fct/hluo/zaurak/caseByMachine/occigen/T/passiveScalar/Newtonian/mapped/flowRate/min/1d_lR2/afterAugust/postProcessing
        #'path':'/store/T_c/1d_lR2'
	    'path':database[alias]['targetDir']
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        #'alias':alias
        'alias':database[alias]['name2plot']
        }

#plotSavePath="10D_5Dforced/"

# secondary physical parameters
#Retau=uTau*R/nu
