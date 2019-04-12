import sys
import commands, os
import scipy.io as io

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

def main():

    caseByAlias=[
        #1b
        "D1-1b",
        #1d
        "D1-1d",
        #1d_lR2
        "D1-1d_lR2_afterAugust",
        #1j
        "D2-NN-1j_test_from0",
        "D2-NN-1j_test_from0p3_forcingStep_St1_A_eq_0p05"
    ]

    caseInfo=dict.fromkeys(caseByAlias)
    for case in caseByAlias:
        caseInfo[case]={
            'sourceDir':[],
            'targetDir':[]
            }

    # IMPORTANT COMMENT HRER :
    # sourceDir need to include machie name like "newton:"
    # targetDir doesn't need to exit before running

    # dirName will be rsync-ed
    # IMPORTANT : no backslash at the end
    dirName="/postProcessing"

    caseInfo["D1-1b"]['sourceDir']="newton:/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1b_mirrorMerge"+dirName
    caseInfo["D1-1b"]['targetDir']="/store/T_c/1b_mirrorMerge"

    caseInfo["D1-1d"]['sourceDir']="newton:/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1d_mapped_NearestFace"+dirName
    caseInfo["D1-1d"]['targetDir']="/store/T_c/1d_mapped_NearestFace"

    caseInfo["D1-1d_lR2_afterAugust"]['sourceDir']="newton:/store/lmfa/fct/hluo/zaurak/caseByMachine/occigen/T/passiveScalar/Newtonian/mapped/flowRate/min/1d_lR2/afterAugust"+dirName
    caseInfo["D1-1d_lR2_afterAugust"]['targetDir']="/store/T_c/1d_lR2"

    base_1j="newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/BirdCarreau/synthetic/flowRate/medium/fluctuation_off/1j"

    caseInfo["D2-NN-1j_test_from0"]['sourceDir']=base_1j+"/"+"test_from0"+dirName
    caseInfo["D2-NN-1j_test_from0"]['targetDir']="/store/T_c/1j/D2-NN_test_from0"

    caseInfo["D2-NN-1j_test_from0p3_forcingStep_St1_A_eq_0p05"]['sourceDir']=base_1j+"/"+"synthetic_phasedStepFrom_test_from_0/From0p3_3_of3"+dirName
    caseInfo["D2-NN-1j_test_from0p3_forcingStep_St1_A_eq_0p05"]['targetDir']="/store/T_c/1j/D2-NN_test_from0p3_forcingStep_St1_A_eq_0p05"

    for case in caseByAlias:
        print ""
        print "===================="
        print "running Job for case with alias : %s" % case
        stat, output = tryJob(caseInfo[case]['sourceDir'], caseInfo[case]['targetDir'])
    
    print "--------------------"
    print "writing database to dataBase.mat"
    print "--------------------"
    io.savemat("dataBase",caseInfo)

main()
