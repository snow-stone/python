#!/bin/bash

T_c=/store/T_c
T_r=/store/8simu_tmp/shape_square/2a_3_T

contour_vort_z=hluo15_T_c_vorticity_z_300.py

#pvpython $contour_vort_z $T_c/1k/D2-NN-1k_syn_forcing
#pvpython $contour_vort_z $T_c/1j/D2-NN-1j_test_from0
#pvpython $contour_vort_z $T_c/1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05
#pvpython $contour_vort_z $T_c/1j/D1-1j_mapped
#pvpython $contour_vort_z $T_c/1j/D2-1j_mapped
#pvpython $contour_vort_z $T_c/1j/D3-1j_mapped


pvpython $contour_vort_z $T_r/BirdCarreau/inlet_0p3
pvpython $contour_vort_z $T_r/Newtonian/Re2400
pvpython $contour_vort_z $T_r/BirdCarreau/inlet_0p3-a_0p5-setT_St_1
pvpython $contour_vort_z $T_r/BirdCarreau/inlet_0p3-a_0p5-setT_St_5
pvpython $contour_vort_z $T_r/BirdCarreau/inlet_0p5
pvpython $contour_vort_z $T_r/Newtonian/Re4000
pvpython $contour_vort_z $T_r/BirdCarreau/inlet0p5_impinging
pvpython $contour_vort_z $T_r/Newtonian/Re4000_impinging
