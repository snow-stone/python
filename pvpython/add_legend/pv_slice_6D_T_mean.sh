#!/bin/bash

BirdCarreau=/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau
Newtonian=/store/8simu_tmp/shape_square/2a_3_T/Newtonian

pvpython pv_T_mean_6D_4.py $BirdCarreau/inlet_0p5 &&
pvpython pv_T_mean_6D_4.py $BirdCarreau/inlet0p5_impinging &&
pvpython pv_T_mean_6D_4.py $BirdCarreau/inlet_0p3 &&
pvpython pv_T_mean_6D_4.py $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 &&
pvpython pv_T_mean_6D_4.py $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 &&
pvpython pv_T_mean_6D_4.py $Newtonian/Re2400 &&
pvpython pv_T_mean_6D_4.py $Newtonian/Re4000 &&
pvpython pv_T_mean_6D_4.py $Newtonian/Re4000_impinging
