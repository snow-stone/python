#!/bin/bash

dirBase=/store/T_c

contour_vort_z=hluo15_T_c_vorticity_z_300.py

#pvpython $contour_vort_z $dirBase/1k/D2-NN-1k_syn_forcing
#pvpython $contour_vort_z $dirBase/1j/D2-NN-1j_test_from0
#pvpython $contour_vort_z $dirBase/1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05
pvpython $contour_vort_z $dirBase/1j/D1-1j_mapped
pvpython $contour_vort_z $dirBase/1j/D2-1j_mapped
pvpython $contour_vort_z $dirBase/1j/D3-1j_mapped
