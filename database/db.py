#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:48:57 2019

@author: hluo
"""

import sys

def chapter2():
    caseList = [
            "pipe_c",
            "pipe_r",
            "T_c",
            "T_r"
            ]
    
    whereis = {
            "pipe_c"     : "newton:/store/lmfa/fct/hluo/LocalSoftware/OpenFOAM/hluo-2.3.x/run/pipes/periodic/pipe4/Newtonian/prototype_artificiallyReducedViscosity",
            "pipe_r1"    : "newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/pipes/shape_square/pw/2a_1/Newtonian/CASE_mapFields_From2b/gradP0_1p0125/system/sampleDicts/sets/lineOn2Diagonals",
            "pipe_r2"    : "newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/pipes/shape_square/pw/2a_1/Newtonian/CASE_mapFields_From2b/gradP0_0p703125/system/sampleDicts/sets/lineOn2Diagonals",
            "T_c/1d_lR2" : "newton:/store/lmfa/fct/hluo/zaurak/caseByMachine/occigen/T/passiveScalar/Newtonian/mapped/flowRate/min/1d_lR2", #beforeAugust/afterAugust
            "T_c/1j_NN_off"  : "newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/BirdCarreau/synthetic/flowRate/medium/fluctuation_off/1j",
            "T_c/1j_NN_on:":"newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/BirdCarreau/synthetic/flowRate/medium/fluctuation_on/medium_cmptStream",
            "T_c/1j_N"   : "newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/Newtonian/mapped/flowRate",
            "T_c/1j_syn" : "newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/Newtonian/synthetic/flowRate/medium/fluctuation_off/1j",
            "T_c/1k_4x4x4" : "newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/testMesh/T",
            "T_r"        : "newton:/store/lmfa/fct/hluo/occigen/caseByGeometry/T/shape_square/2a_3_T"
            }
    
    datasize = {
            "pipe_c" :        "203G",
            "pipe_r1":        "171G",
            "pipe_r1":        " 24G",
            "T_c/1d_lR2":     "184G",
            "T_c/1j_NN_off":  "2,2T",
            "T_c/1j_NN_on ":  "308G",
            "T_c/1j_N"     :  "1,2T",
            "T_c/1j_N_syn" :  "675G",
            "T_c/1k_4x4x4" :  "1.5T",
            "T_r"          :  "24 T"
            }
    
    case = sys.argv[1]
    print whereis[case]
    
chapter2()
