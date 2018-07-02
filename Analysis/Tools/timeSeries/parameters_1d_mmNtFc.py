
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
#        'dataShape':(188,4)     # face 3
#        'dataShape':(195,4)     # face 2
        'dataShape':(195,4)     # face 1
        }

# data entry parameters

dataEntry={
        'startTime':5.01,
        'endTime':5.6,
        'chunkStep':20,
        'NbOfFiles':60,
        'path':"/store/caseByGeometry/T/pointwise/pw-2ndTry_block/SameGeo_as_Dai_actually/old_strategy/2nd/fix_NonUniformDistributedConnectors/60blocks/1d_mapped_NearestFace",
        }

parameters={
        'physics':physics,
        'sampling':sampling,
        'dataEntry':dataEntry,
        }

plotSavePath="10D_5Dforced/"

# secondary physical parameters
#Retau=uTau*R/nu