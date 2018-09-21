#!/bin/bash

module purge

EASYBUILD_PREFIX=$HOME/.local/easybuild
module use $EASYBUILD_PREFIX/modules/all
module load EasyBuild
EASYBUILD_MODULES_TOOL=EnvironmentModules

module load OpenFOAM/2.3.1-foss-2016a
source $FOAM_BASH

reconstructPar -time $1
