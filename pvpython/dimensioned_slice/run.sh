#!/bin/bash

BirdCarreau=/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau
Newtonian=/store/8simu_tmp/shape_square/2a_3_T/Newtonian

contourUx=Ux_mean_slice_yNormal.py

pvpython $contourUx $BirdCarreau/inlet_0p5 -0.003 neg3mm &&
pvpython $contourUx $BirdCarreau/inlet0p5_impinging -0.003 neg3mm &&
pvpython $contourUx $BirdCarreau/inlet_0p3 -0.003 neg3mm &&
pvpython $contourUx $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 -0.003 neg3mm &&
pvpython $contourUx $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 -0.003 neg3mm &&
pvpython $contourUx $Newtonian/Re2400 -0.003 neg3mm &&
pvpython $contourUx $Newtonian/Re4000 -0.003 neg3mm &&
pvpython $contourUx $Newtonian/Re4000_impinging -0.003 neg3mm
