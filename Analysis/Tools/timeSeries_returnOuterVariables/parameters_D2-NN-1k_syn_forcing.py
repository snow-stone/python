# static
import json

database=json.load(open("/home/hluo/work/git/python/python_rsync/database.txt"))
alias="D2-NN-1k_syn_forcing"

# physical parameters

physics={
        'R':0.004,
        'nu':1.0e-6,
        'uTau':0.0473
        }

#print physics

sampling={
        'raw_sample_size':160,
        'TdataShape3':(147,2),    # face 3
        'TdataShape2':(167,2),    # face 2
        'nudataShape5':(169,2),    
        'nudataShape4':(157,2),    
        'nudataShape3':(144,2),    
        'nudataShape2':(129,2),    
        'nudataShape1':(116,2),    
        'dataShape3':(147,4),    # face 3
        'dataShape2':(167,4),    # face 2
        'dataShape1':(167,4),    # face 1
        'dataShape': None
        }

# data entry parameters

dataEntry={
        'startTime':0,  
        'endTime':0.6,
        'chunkStep':100,
        'NbOfFiles':601,
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
