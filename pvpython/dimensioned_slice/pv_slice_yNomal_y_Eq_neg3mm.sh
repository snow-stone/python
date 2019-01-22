#!/bin/bash

BirdCarreau=/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau
Newtonian=/store/8simu_tmp/shape_square/2a_3_T/Newtonian

pvpython pv_slice_yNomal_y_Eq_neg3mm_2.py $BirdCarreau/inlet_0p5 -0.003 neg3mm &&
pvpython pv_slice_yNomal_y_Eq_neg3mm_2.py $BirdCarreau/inlet0p5_impinging -0.003 neg3mm &&
pvpython pv_slice_yNomal_y_Eq_neg3mm_2.py $BirdCarreau/inlet_0p3 -0.003 neg3mm &&
pvpython pv_slice_yNomal_y_Eq_neg3mm_2.py $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 -0.003 neg3mm &&
pvpython pv_slice_yNomal_y_Eq_neg3mm_2.py $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 -0.003 neg3mm &&
pvpython pv_slice_yNomal_y_Eq_neg3mm_2.py $Newtonian/Re2400 -0.003 neg3mm &&
pvpython pv_slice_yNomal_y_Eq_neg3mm_2.py $Newtonian/Re4000 -0.003 neg3mm &&
pvpython pv_slice_yNomal_y_Eq_neg3mm_2.py $Newtonian/Re4000_impinging -0.003 neg3mm
