import sys
import commands, os
import scipy.io as io

def makeDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print directory, " exists"

def runJob(cmd):
    print "running Job using bash command : %s" % cmd
    status, jobOutput = commands.getstatusoutput(cmd)
    if status == 0 :
        print "Job return value : 0"
        print "Job output :"
        print jobOutput
    else :
        print "Job failed"
        print "Job output :"
        print jobOutput

    return status, jobOutput

def tryJob(sourceDir, targetDir):

    cmd = "rsync -av %s %s/" % (sourceDir, targetDir)

    return runJob(cmd)

def create_write_database_NoSync():

    # naming
    # begin by D1, D2, D3 : debit min, medium, max
    # then : dash
    # if NN then NN, if not, directly get into resolution : 1b, 1d, 1j, 1k... 
    caseByAlias=[
        #1b
        "D1-1b",
        #1d
        "D1-1d",
        #1d_lR2
        "D1-1d_lR2_afterAugust",
        #1j
        "D2-NN-1j_test_from0",
        "D2-NN-1j_test_from0p3_forcingStep_St1_A_eq_0p05",
        "D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05",
        "D1-1j_mapped", # test_from_0p45_of3
        "D2-1j_mapped", # test_from_0p45_of3
        "D3-1j_mapped", # test_from_0p45_of3
        "D2-1j_syn",
        "D2-NN-1j_syn",
        #1k_4x4x4.pw : note that this is not "1k.pw"
        "D2-NN-1k_syn",
        "D2-NN-1k_syn_forcing",
        # t_r
        "t_r-2a_1_gradP0p703125"
    ]

    caseInfo=dict.fromkeys(caseByAlias)
    for case in caseByAlias:
        caseInfo[case]={
            'sourceDir':[],
            'targetDir':[],
            'name2plot':[],
            'latestTime':[]
            }

    # IMPORTANT COMMENT HRER :
    # sourceDir need to include machie name like "newton:"
    # targetDir doesn't need to exit before running

    # dirName will be rsync-ed
    # IMPORTANT : no backslash at the end
    #dirName="/postProcessing"

    alias="D1-1b"
    caseInfo[alias]['sourceDir']="newton:/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1b_mirrorMerge"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1b"+"/"+alias
    caseInfo[alias]['name2plot']=alias
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D1-1d"
    caseInfo[alias]['sourceDir']="newton:/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1d_mapped_NearestFace"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1d"+"/"+alias
    caseInfo[alias]['name2plot']=alias
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D1-1d_lR2_afterAugust"
    caseInfo[alias]['sourceDir']="newton:/store/lmfa/fct/hluo/zaurak/caseByMachine/occigen/T/passiveScalar/Newtonian/mapped/flowRate/min/1d_lR2/afterAugust"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1d_lR2"+"/"+alias
    caseInfo[alias]['name2plot']="D1-1d_{lR2,afterAugust}"
    makeDirectory(caseInfo[alias]['targetDir'])

    base_1j="newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/BirdCarreau/synthetic/flowRate/medium/fluctuation_off/1j"

    alias="D2-NN-1j_test_from0"
    caseInfo[alias]['sourceDir']=base_1j+"/"+"test_from0"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1j"+"/"+alias
    caseInfo[alias]['name2plot']="D2-NN-1j_{testFrom0}"
    caseInfo[alias]['latestTime']="0.3"
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D2-NN-1j_test_from0p3_forcingStep_St1_A_eq_0p05"
    caseInfo[alias]['sourceDir']=base_1j+"/"+"synthetic_phasedStepFrom_test_from_0/From0p3_3_of3"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1j"+"/"+alias
    caseInfo[alias]['name2plot']="D2-NN-1j_{testFrom0.3;Step,St=1,A=0.05}"
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05"
    caseInfo[alias]['sourceDir']=base_1j+"/"+"synthetic_phasedSinusFrom_test_from_0/From0p3_2_of3"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1j"+"/"+alias
    caseInfo[alias]['name2plot']="D2-NN-1j_{testFrom0.3;Sinus,St=3.2,A=0.05}"
    caseInfo[alias]['latestTime']="0.6"
    makeDirectory(caseInfo[alias]['targetDir'])

    base_1jN="newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/Newtonian/mapped/flowRate"

    alias="D1-1j_mapped"
    caseInfo[alias]['sourceDir']=base_1jN+"/"+"min/test_from_0p45_of3/syntheticMedium_FluctuationOff"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1j"+"/"+alias
    caseInfo[alias]['name2plot']="D1-1j_{mapped}"
    caseInfo[alias]['latestTime']="0.6"
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D2-1j_mapped"
    caseInfo[alias]['sourceDir']=base_1jN+"/"+"medium/test_from_0p45_of3/syntheticMedium_FluctuationOff"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1j"+"/"+alias
    caseInfo[alias]['name2plot']="D2-1j_{mapped}"
    caseInfo[alias]['latestTime']="0.9"
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D3-1j_mapped"
    caseInfo[alias]['sourceDir']=base_1jN+"/"+"max/test_from_0p45_of3/syntheticMedium_FluctuationOff"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1j"+"/"+alias
    caseInfo[alias]['name2plot']="D3-1j_{mapped}"
    caseInfo[alias]['latestTime']="0.6"
    makeDirectory(caseInfo[alias]['targetDir'])

    base_1jN="newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/Newtonian/synthetic/flowRate/medium/fluctuation_off/1j"

    alias="D2-1j_syn"
    caseInfo[alias]['sourceDir']=base_1jN+"/"+"test_from_0"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1j"+"/"+alias
    caseInfo[alias]['name2plot']="D2-1j_{syn}"
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D2-NN-1j_syn"
    caseInfo[alias]['sourceDir']="newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/BirdCarreau/synthetic/flowRate/medium/fluctuation_on/medium_cmptStream"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1j"+"/"+alias
    caseInfo[alias]['name2plot']="D2-NN-1j_{syn}"
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D2-NN-1k_syn"
    caseInfo[alias]['sourceDir']="newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/testMesh/T/flux_medium/1k_4x4x4_BC_phasedOff"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1k"+"/"+alias
    caseInfo[alias]['name2plot']="D2-NN-1k_{syn}"
    caseInfo[alias]['latestTime']="0.3"
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="D2-NN-1k_syn_forcing"
    caseInfo[alias]['sourceDir']="newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/testMesh/T/flux_medium/1k_4x4x4_BC_phasedOn"#+dirName
    caseInfo[alias]['targetDir']="/store/T_c/1k"+"/"+alias
    caseInfo[alias]['name2plot']="D2-NN-1k_{syn,forcing}"
    caseInfo[alias]['latestTime']="0.6"
    makeDirectory(caseInfo[alias]['targetDir'])

    alias="t_r-2a_1_gradP0p703125"
    caseInfo[alias]['sourceDir']="newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/pipes/shape_square/pw/2a_1/Newtonian/CASE_mapFields_From2b/gradP0_0p703125"#+dirName
    caseInfo[alias]['targetDir']="/store/t_r/2a_1"+"/"+alias
    caseInfo[alias]['name2plot']="2a\_1_{gradP0p703125}"
    makeDirectory(caseInfo[alias]['targetDir'])

    #for case in caseByAlias:
    #    print ""
    #    print "===================="
    #    print "running Job for case with alias : %s" % case
    #    stat, output = tryJob(caseInfo[case]['sourceDir'], caseInfo[case]['targetDir'])
    
    #print "--------------------"
    #print "print keys : ", caseInfo.keys()
    #print "writing database to dataBase.mat"
    #print "--------------------"
    #io.savemat("dataBase",caseInfo)

    import json
    print "--------------------"
    print "print keys : ", caseInfo.keys()
    print "writing database to json"
    print "--------------------"
    json.dump(caseInfo, open("database.txt",'w'))

def read_database_and_rsync(database, case, dirName):

    print ""
    print "===================="
    print "running Job for case with alias : %s" % case
    print "sourceDir : " + database[case]['sourceDir']
    stat, output = tryJob(database[case]['sourceDir']+'/'+dirName, database[case]['targetDir'])


def main():

    import json

    create_write_database_NoSync()
    database=json.load(open("/home/hluo/work/git/python/python_rsync/database.txt"))

    caseByAlias=[
        "D1-1j_mapped", # test_from_0p45_of3
        "D2-1j_mapped", # test_from_0p45_of3
        "D3-1j_mapped", # test_from_0p45_of3
        "D2-NN-1j_test_from0",
        "D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05",
        "D2-NN-1k_syn",
        "D2-NN-1k_syn_forcing",
    ]

    for case in caseByAlias :
        read_database_and_rsync(database, case, 'postProcessing')
        read_database_and_rsync(database, case, '{'+database[case]['latestTime']+','+'constant,system}')

main()
