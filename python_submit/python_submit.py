
import sys

def tryJob(job_number, queue):

    simuLogFile = "logSimulation_"+str(job_number)
    
    slurmFile   = queue
    if queue == 'test' :
        with open(slurmFile,'w') as sf:
            sf.write("#!/bin/bash\n")
            sf.write("#SBATCH --job-name=0p5_St0\n")
            sf.write("#SBATCH --nodes=20\n")
            sf.write("#SBATCH --ntasks-per-node=24\n")
            sf.write("#SBATCH --cpus-per-task=1\n")
            sf.write("#SBATCH --time=00:10:00\n")      # min is the smallest unit here
            sf.write("#SBATCH -C %s\n" % "test")
            sf.write("#SBATCH --mem=50GB\n")
            sf.write("#SBATCH --output=hsw_mpi.%j.out\n")
            sf.write("#SBATCH --error=hsw_mpi.%j.err")
            sf.write("\n")
            sf.write("set -e\n")
            sf.write("ulimit -s 500000\n")
            sf.write("srun -n 480 pimpleFoamPS_profiling -parallel > %s\n" % simuLogFile)
        sf.close()

def main():
    queue = sys.argv[1]
    tryJob(1, queue)
    
main()