# static
import json

database=json.load(open("/home/hluo/work/git/python/python_rsync/database.txt"))
alias='D2-NN-1j_test_from0'

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
#        'dataShape':(321,4)     # face 3
#        'dataShape':(195,4)     # face 1
        'dataShape':(332,4)     # face 2
        }

# data entry parameters

dataEntry={
        'startTime':0.24,  
        'endTime':0.30,
        'chunkStep':30,
        'NbOfFiles':61,
        #data position :
        #newton:/store/lmfa/fct/hluo/zaurak/caseByMachine/occigen/T/passiveScalar/Newtonian/mapped/flowRate/min/1d_lR2/afterAugust/postProcessing
        #'path':'/store/T_c/1d_lR2'
	    'path':database[alias]['targetDir']
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        'alias':alias
        }

#plotSavePath="10D_5Dforced/"

# secondary physical parameters
#Retau=uTau*R/nu
