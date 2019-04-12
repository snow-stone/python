import sys
import commands, os

def submitJob(cmd):
    print "submitting job using : %s" % cmd
    status, jobOutput = commands.getstatusoutput(cmd)
    print ""
    print "===================="
    if status == 0 :
        print "job return value : 0"
        print "job output :"
        print jobOutput
    else :
        print "job failed"
        print "job output :"
        print jobOutput

    return status, jobOutput

def tryJob(job_number):

    sourceDir="/store/lmfa/fct/hluo/zaurak/caseByGeometry/T/new-mesh/pointwise/postProcessing/1b_mirrorMerge/postProcessing"
    cmd = "rsync -av newton:%s 1b_mirrorMerge/" % sourceDir
    status, jobOutput = submitJob(cmd)

def main():
    #queue = sys.argv[1]
    tryJob(1)
    
main()
