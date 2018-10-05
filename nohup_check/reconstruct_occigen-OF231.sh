#!/bin/bash

module purge

# occigen-OF231
module use $SCRATCHDIR/git/eb-setup/build/easybuild/modules/all
module load OpenFOAM/2.3.1-foss-2016a
source $FOAM_BASH

date >> log.reconstructParPython
reconstructPar -time $1 >> log.reconstructParPython 2>&1
