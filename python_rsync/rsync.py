import sys
import commands, os

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
        "1b_1"
    ]

    caseInfo=dict.fromkeys(caseByAlias)
    for case in caseByAlias:
        caseInfo[case]={
            'sourceDir':[],
            'targetDir':[]
            }

    caseInfo["1b_1"]['sourceDir']="newton:/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1b_mirrorMerge/postProcessing/"
    caseInfo["1b_1"]['targetDir']="1b_mirrorMerge"

    for case in caseByAlias:
        print ""
        print "===================="
        print "running Job for case with alias : %s" % case
        stat, output = tryJob(caseInfo[case]['sourceDir'], caseInfo[case]['targetDir'])
    
main()
