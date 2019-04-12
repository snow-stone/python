import sys
import commands, os

def runJob(cmd):
    print "running job using : %s" % cmd
    status, jobOutput = commands.getstatusoutput(cmd)
    print ""
    print "===================="
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

    #sourceDir="/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1b_mirrorMerge/postProcessing"
    #targetDir="1b_mirrorMerge"
    cmd = "rsync -av newton:%s %s/" % (sourceDir, targetDir)
    status, jobOutput = runJob(cmd)

def main():

    sourceDir="/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1b_mirrorMerge/postProcessing"
    targetDir="1b_mirrorMerge"
    tryJob(sourceDir, targetDir)
    
main()
