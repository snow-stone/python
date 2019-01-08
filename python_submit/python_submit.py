
import sys
import commands, os

def submitJob(cmd, slurmFile):
    if os.path.exists(slurmFile):
        print "submitting job using : %s" % cmd
        status, jobnum = commands.getstatusoutput(cmd)
        return status, jobnum.split()[-1]
    else:
        print "FATAL ERROR!"
        print "file %s doesnt exits" % slurmFile
        return (1, '0000')

def tryJob(someIndex, queue):

    simuLogFile = "log.userLabelListOp_DaiT_0_0p6_"+str(someIndex)
    
    slurmFile   = queue
    if queue == 'test' :
        with open(slurmFile,'w') as sf:
            sf.write("#!/bin/bash\n")
            sf.write("##SBATCH --job-name=someName\n")
            sf.write("#SBATCH --output=job.%j.out\n")
            sf.write("#SBATCH --error=job.%j.err\n")
            sf.write("#SBATCH --mail-user=haining.luo@doctorant.ec-lyon.fr\n\n")
            
            sf.write("#SBATCH --partition=mononode\n")
            sf.write("#SBATCH --mem-per-cpu=4000\n")
            sf.write("#SBATCH --nodes=1\n")
            sf.write("#SBATCH --ntasks-per-node=1\n")
            sf.write("##SBATCH --exclusive\n")
            sf.write("#SBATCH --cpus-per-task=1")
            sf.write("#SBATCH --time=00:10:00\n\n")      # min is the smallest unit here

            sf.write("module purge\n")
            sf.write("module load OpenMPI/1.6.5-GCC-4.8.3 \n")
            sf.write(". /home/lmfa/hluo/LocalSoftware/OpenFOAM/OpenFOAM-2.3.x/etc/bashrc.Opt\n\n")
            
            sf.write("sliceStore=/store/lmfa/fct/hluo/occigen/caseByGeometry/T/shape_square/2a_3_T/sliceStore\n")
            sf.write("userLabelListOp_Dai T $sliceStore slice"+str(someIndex)+" -time '0:0.6' > %s\n" % simuLogFile)
        sf.close()

    cmd = "sbatch %s" % slurmFile
    status, jobID = submitJob(cmd, slurmFile)

def main():
    queue = sys.argv[1]
#    sliceList = [0,1,2,3,4,5,6,7,8,9,10,11,12,16,24,32,40,48,56,64,72,73,74,75]
    sliceList = [0, 1]
    for slicei in sliceList:
        tryJob(slicei, queue)
    
main()