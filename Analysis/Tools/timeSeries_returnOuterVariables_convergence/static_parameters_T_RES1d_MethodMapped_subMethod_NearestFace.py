# static
import json

database=json.load(open("/home/hluo/work/git/python/python_rsync/database.txt"))
alias='D1-1d'

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
        'dataShape':(188,4)     # face 3
#        'dataShape':(195,4)     # face 2
#        'dataShape':(195,4)     # face 1
        }

# data entry parameters

dataEntry={
        'startTime':5.5,  # KinecticEnergy stationary
        'endTime':7.2,
        'chunkStep':50,
        'NbOfFiles':171,
        #old path : 
        #'path':"/store/caseByGeometry/T/new-mesh/pointwise/postProcessing/1d_mapped_NearestFace",
        #data position :
        #/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/
        #/home/lmfa/hluo/LocalSoftware/OpenFOAM/hluo-2.3.x/run/T/1d_mapped_NearestFace
        #'path':'/store/T_c/1d_mapped_NearestFace'
        'path':database[alias]['targetDir']
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        }

plotSavePath="10D_5Dforced/"

# secondary physical parameters
#Retau=uTau*R/nu
