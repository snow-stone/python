#!/bin/bash

module purge

# occigen-OF3
module load intel/17.2 openmpi/intel/2.0.1 openfoam/3.0.1 
source /opt/software/occigen/applications/OpenFOAM/3.0.1/intel/17.2/openmpi/intel/2.0.1/OpenFOAM-3.0.1/etc/bashrc

date >> log.reconstructParPython
reconstructPar -time $1 >> log.reconstructParPython 2>&1
