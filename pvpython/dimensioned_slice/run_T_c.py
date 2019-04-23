#!/bin/bash

res_1j=/store/T_c/1j
res_1k=/store/T_c/1k

contourk_mean_nonD_z=k_mean_nonD_slice_zNormal-logScale_clipped_beta.py
contourk_mean_nonD_y=k_mean_nonD_slice_yNormal-logScale_clipped.py

#userRescaleScalarByMax -case $res_1j/D1-1j_mapped k_mean
#userRescaleScalarByMax -case $res_1j/D2-1j_mapped k_mean
#userRescaleScalarByMax -case $res_1j/D3-1j_mapped k_mean
#userRescaleScalarByMax -case $res_1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05 k_mean
#userRescaleScalarByMax -case $res_1k/D2-NN-1k_syn_forcing k_mean

#pvpython $contourk_mean_nonD_z $res_1j/D1-1j_mapped 0 0mm &&
#pvpython $contourk_mean_nonD_z $res_1j/D2-1j_mapped 0 0mm &&
#pvpython $contourk_mean_nonD_z $res_1j/D3-1j_mapped 0 0mm &&
#pvpython $contourk_mean_nonD_z $res_1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05 0 0mm &&
#pvpython $contourk_mean_nonD_z $res_1k/D2-NN-1k_syn_forcing 0 0mm

filename=k_mean_nonD_slice_zNormal_z_Eq_0mm_cropped
destination=/home/hluo/work/git/thesis/Thesis_hluo_new/ch3/images/contours/k_mean_nonD

rsync -av $res_1j/D1-1j_mapped/$filename.png $destination/N1A.png
rsync -av $res_1j/D2-1j_mapped/$filename.png $destination/N2A.png
rsync -av $res_1j/D3-1j_mapped/$filename.png $destination/N3A.png
rsync -av $res_1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05/$filename.png $destination/NN2A_forcing.png
rsync -av $res_1k/D2-NN-1k_syn_forcing/$filename.png $destination/NN2B_forcing.png
