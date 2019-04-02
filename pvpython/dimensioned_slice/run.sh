#!/bin/bash

BirdCarreau=/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau
Newtonian=/store/8simu_tmp/shape_square/2a_3_T/Newtonian

contourUx=Ux_mean_slice_yNormal.py
contourUy=Uy_mean_slice_yNormal.py
contourUz=Uz_mean_slice_yNormal.py
contourNu_y=nu_mean_slice_yNormal-logScale.py
contourNu_z=nu_mean_slice_zNormal-logScale_clipped_beta.py
#contourNu_x=nu_mean_slice_xNormal-logScale.py
contourNu_x=nu_mean_slice_x-logScale.py
contourT_x=T_mean_slice_x.py
contourT_z=T_mean_slice_zNormal_noClipped.py

kidneyVortices_decked=kidneyVortices_decked.py

pvpython $contourNu_z $BirdCarreau/inlet_0p5                 0.0005 p0p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging        0.0005 p0p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3                 0.0005 p0p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0005 p0p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0005 p0p5mm &&
echo "---------------" &&
echo "Finish Nu_z p0p5mm" &&
echo "---------------" &&
pvpython $contourNu_z $BirdCarreau/inlet_0p5                 0.001 p1mm &&
pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging        0.001 p1mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3                 0.001 p1mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.001 p1mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.001 p1mm &&
echo "---------------" &&
echo "Finish Nu_z p1mm" &&
echo "---------------" &&
pvpython $contourNu_z $BirdCarreau/inlet_0p5                 0.0015 p1p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging        0.0015 p1p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3                 0.0015 p1p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0015 p1p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0015 p1p5mm &&
echo "---------------" &&
echo "Finish Nu_z p1p5mm" &&
echo "---------------" &&
pvpython $contourNu_z $BirdCarreau/inlet_0p5                 0.002 p2mm &&
pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging        0.002 p2mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3                 0.002 p2mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.002 p2mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.002 p2mm &&
echo "---------------" &&
echo "Finish Nu_z p2mm" &&
echo "---------------" &&
pvpython $contourNu_z $BirdCarreau/inlet_0p5                 0.0025 p2p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging        0.0025 p2p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3                 0.0025 p2p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0025 p2p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0025 p2p5mm &&
echo "---------------" &&
echo "Finish Nu_z p2p5mm" &&
echo "---------------" &&
pvpython $contourNu_z $BirdCarreau/inlet_0p5                 0.003 p3mm &&
pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging        0.003 p3mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3                 0.003 p3mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.003 p3mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.003 p3mm &&
echo "---------------" &&
echo "Finish Nu_z p3mm" &&
echo "---------------" &&
pvpython $contourNu_z $BirdCarreau/inlet_0p5                 0.0035 p3p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging        0.0035 p3p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3                 0.0035 p3p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0035 p3p5mm &&
pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0035 p3p5mm &&
echo "---------------" &&
echo "Finish Nu_z p3p5mm" &&
echo "---------------"

#pvpython $contourUx $BirdCarreau/inlet_0p5 -0.003 neg3mm &&
#pvpython $contourUx $BirdCarreau/inlet0p5_impinging -0.003 neg3mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3 -0.003 neg3mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 -0.003 neg3mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 -0.003 neg3mm &&
#pvpython $contourUx $Newtonian/Re2400 -0.003 neg3mm &&
#pvpython $contourUx $Newtonian/Re4000 -0.003 neg3mm &&
#pvpython $contourUx $Newtonian/Re4000_impinging -0.003 neg3mm &&
#echo "---------------" &&
#echo "Finish Ux -3mm" &&
#echo "---------------" &&
#pvpython $contourUx $BirdCarreau/inlet_0p5 0 0mm &&
#pvpython $contourUx $BirdCarreau/inlet0p5_impinging 0 0mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3 0 0mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0 0mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0 0mm &&
#pvpython $contourUx $Newtonian/Re2400 0 0mm &&
#pvpython $contourUx $Newtonian/Re4000 0 0mm &&
#pvpython $contourUx $Newtonian/Re4000_impinging 0 0mm &&
#echo "---------------" &&
#echo "Finish Ux 0mm" &&
#echo "---------------" &&
#pvpython $contourUx $BirdCarreau/inlet_0p5 0.003 pos3mm &&
#pvpython $contourUx $BirdCarreau/inlet0p5_impinging 0.003 pos3mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3 0.003 pos3mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.003 pos3mm &&
#pvpython $contourUx $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.003 pos3mm &&
#pvpython $contourUx $Newtonian/Re2400 0.003 pos3mm &&
#pvpython $contourUx $Newtonian/Re4000 0.003 pos3mm &&
#pvpython $contourUx $Newtonian/Re4000_impinging 0.003 pos3mm &&
#echo "---------------" &&
#echo "Finish Ux 3mm" &&
#echo "---------------" &&
#pvpython $contourUy $BirdCarreau/inlet_0p5 -0.003 neg3mm &&
#pvpython $contourUy $BirdCarreau/inlet0p5_impinging -0.003 neg3mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3 -0.003 neg3mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 -0.003 neg3mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 -0.003 neg3mm &&
#pvpython $contourUy $Newtonian/Re2400 -0.003 neg3mm &&
#pvpython $contourUy $Newtonian/Re4000 -0.003 neg3mm &&
#pvpython $contourUy $Newtonian/Re4000_impinging -0.003 neg3mm &&
#echo "---------------" &&
#echo "Finish Uy -3mm" &&
#echo "---------------" &&
#pvpython $contourUy $BirdCarreau/inlet_0p5 0 0mm &&
#pvpython $contourUy $BirdCarreau/inlet0p5_impinging 0 0mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3 0 0mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0 0mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0 0mm &&
#pvpython $contourUy $Newtonian/Re2400 0 0mm &&
#pvpython $contourUy $Newtonian/Re4000 0 0mm &&
#pvpython $contourUy $Newtonian/Re4000_impinging 0 0mm &&
#echo "---------------" &&
#echo "Finish Uy 0mm" &&
#echo "---------------" &&
#pvpython $contourUy $BirdCarreau/inlet_0p5 0.003 pos3mm &&
#pvpython $contourUy $BirdCarreau/inlet0p5_impinging 0.003 pos3mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3 0.003 pos3mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.003 pos3mm &&
#pvpython $contourUy $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.003 pos3mm &&
#pvpython $contourUy $Newtonian/Re2400 0.003 pos3mm &&
#pvpython $contourUy $Newtonian/Re4000 0.003 pos3mm &&
#pvpython $contourUy $Newtonian/Re4000_impinging 0.003 pos3mm &&
#echo "---------------" &&
#echo "Finish Uy 3mm" &&
#echo "---------------" &&
#pvpython $contourUz $BirdCarreau/inlet_0p5 -0.003 neg3mm &&
#pvpython $contourUz $BirdCarreau/inlet0p5_impinging -0.003 neg3mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3 -0.003 neg3mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 -0.003 neg3mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 -0.003 neg3mm &&
#pvpython $contourUz $Newtonian/Re2400 -0.003 neg3mm &&
#pvpython $contourUz $Newtonian/Re4000 -0.003 neg3mm &&
#pvpython $contourUz $Newtonian/Re4000_impinging -0.003 neg3mm &&
#echo "---------------" &&
#echo "Finish Uz -3mm" &&
#echo "---------------" &&
#pvpython $contourUz $BirdCarreau/inlet_0p5 0 0mm &&
#pvpython $contourUz $BirdCarreau/inlet0p5_impinging 0 0mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3 0 0mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0 0mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0 0mm &&
#pvpython $contourUz $Newtonian/Re2400 0 0mm &&
#pvpython $contourUz $Newtonian/Re4000 0 0mm &&
#pvpython $contourUz $Newtonian/Re4000_impinging 0 0mm &&
#echo "---------------" &&
#echo "Finish Uz 0mm" &&
#echo "---------------" &&
#pvpython $contourUz $BirdCarreau/inlet_0p5 0.003 pos3mm &&
#pvpython $contourUz $BirdCarreau/inlet0p5_impinging 0.003 pos3mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3 0.003 pos3mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.003 pos3mm &&
#pvpython $contourUz $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.003 pos3mm &&
#pvpython $contourUz $Newtonian/Re2400 0.003 pos3mm &&
#pvpython $contourUz $Newtonian/Re4000 0.003 pos3mm &&
#pvpython $contourUz $Newtonian/Re4000_impinging 0.003 pos3mm &&
#echo "---------------" &&
#echo "Finish Uz 3mm" &&
#echo "---------------" &&
#pvpython $contourNu $BirdCarreau/inlet_0p5 -0.003 neg3mm &&
#pvpython $contourNu $BirdCarreau/inlet0p5_impinging -0.003 neg3mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3 -0.003 neg3mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 -0.003 neg3mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 -0.003 neg3mm &&
##pvpython $contourNu $Newtonian/Re2400 -0.003 neg3mm &&
##pvpython $contourNu $Newtonian/Re4000 -0.003 neg3mm &&
##pvpython $contourNu $Newtonian/Re4000_impinging -0.003 neg3mm &&
#echo "---------------" &&
#echo "Finish Nu -3mm" &&
#echo "---------------" &&
#pvpython $contourNu $BirdCarreau/inlet_0p5 0 0mm &&
#pvpython $contourNu $BirdCarreau/inlet0p5_impinging 0 0mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3 0 0mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0 0mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0 0mm &&
##pvpython $contourNu $Newtonian/Re2400 0 0mm &&
##pvpython $contourNu $Newtonian/Re4000 0 0mm &&
##pvpython $contourNu $Newtonian/Re4000_impinging 0 0mm &&
#echo "---------------" &&
#echo "Finish Nu 0mm" &&
#echo "---------------" &&
#pvpython $contourNu $BirdCarreau/inlet_0p5 0.003 pos3mm &&
#pvpython $contourNu $BirdCarreau/inlet0p5_impinging 0.003 pos3mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3 0.003 pos3mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.003 pos3mm &&
#pvpython $contourNu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.003 pos3mm &&
##pvpython $contourNu $Newtonian/Re2400 0.003 pos3mm &&
##pvpython $contourNu $Newtonian/Re4000 0.003 pos3mm &&
##pvpython $contourNu $Newtonian/Re4000_impinging 0.003 pos3mm &&
#echo "---------------" &&
#echo "Finish Nu 3mm" &&
#echo "---------------" 


#pvpython $contourNu_z $BirdCarreau/inlet_0p5 &&
#pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging &&
#pvpython $contourNu_z $BirdCarreau/inlet_0p3 &&
#pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 &&
#pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5


#pvpython $contourNu_y $BirdCarreau/inlet_0p5 -0.003 neg3mm &&
#pvpython $contourNu_y $BirdCarreau/inlet0p5_impinging -0.003 neg3mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3 -0.003 neg3mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 -0.003 neg3mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 -0.003 neg3mm &&
#echo "---------------" &&
#echo "Finish Nu_y -3mm" &&
#echo "---------------" &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p5 0 0mm &&
#pvpython $contourNu_y $BirdCarreau/inlet0p5_impinging 0 0mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3 0 0mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0 0mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0 0mm &&
#echo "---------------" &&
#echo "Finish Nu_y 0mm" &&
#echo "---------------" &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p5 0.003 pos3mm &&
#pvpython $contourNu_y $BirdCarreau/inlet0p5_impinging 0.003 pos3mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3 0.003 pos3mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.003 pos3mm &&
#pvpython $contourNu_y $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.003 pos3mm &&
#echo "---------------" &&
#echo "Finish Nu_y 3mm" &&
#echo "---------------" 


#pvpython $contourNu_x $BirdCarreau/inlet_0p5 0.0041 0.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging 0.0041 0.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3 0.0041 0.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0041 0.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0041 0.0D &&
#echo "---------------" &&
#echo "Finish Nu_x 0.0D" &&
#echo "---------------" &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p5 0.006 0.25D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging 0.006 0.25D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3 0.006 0.25D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.006 0.25D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.006 0.25D &&
#echo "---------------" &&
#echo "Finish Nu_x 0.25D" &&
#echo "---------------" &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p5                 0.0072 0.4D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging        0.0072 0.4D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3                 0.0072 0.4D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0072 0.4D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0072 0.4D &&
#echo "---------------" &&
#echo "Finish Nu_x 0.4D" &&
#echo "---------------"
#pvpython $contourNu_x $BirdCarreau/inlet_0p5 0.008 0.5D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging 0.008 0.5D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3 0.008 0.5D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.008 0.5D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.008 0.5D &&
#echo "---------------" &&
#echo "Finish Nu_x 0.5D" &&
#echo "---------------" &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p5                 0.012 1.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging        0.012 1.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3                 0.012 1.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.012 1.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.012 1.0D &&
#echo "---------------" &&
#echo "Finish Nu_x 1.0D" &&
#echo "---------------" &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p5                 0.018 1.75D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging        0.018 1.75D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3                 0.018 1.75D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.018 1.75D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.018 1.75D &&
#echo "---------------" &&
#echo "Finish Nu_x 1.75D" &&
#echo "---------------" 
#pvpython $contourNu_x $BirdCarreau/inlet_0p5 0.02 2.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging 0.02 2.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3 0.02 2.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.02 2.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.02 2.0D &&
#echo "---------------" &&
#echo "Finish Nu_x 2.0D" &&
#echo "---------------" &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p5 0.036 4.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging 0.036 4.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3 0.036 4.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.036 4.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.036 4.0D &&
#echo "---------------" &&
#echo "Finish Nu_x 4.0D" &&
#echo "---------------" &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p5 0.052 6.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging 0.052 6.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3 0.052 6.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.052 6.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.052 6.0D &&
#echo "---------------" &&
#echo "Finish Nu_x 6.0D" &&
#echo "---------------" &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p5 0.068 8.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet0p5_impinging 0.068 8.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3 0.068 8.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.068 8.0D &&
#pvpython $contourNu_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.068 8.0D &&
#echo "---------------" &&
#echo "Finish Nu_x 8.0D" &&
#echo "---------------" 



#pvpython $contourT_x $BirdCarreau/inlet_0p5 0.0041 0.0D &&
#pvpython $contourT_x $BirdCarreau/inlet0p5_impinging 0.0041 0.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3 0.0041 0.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0041 0.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0041 0.0D &&
#pvpython $contourT_x $Newtonian/Re2400 0.0041 0.0D &&
#pvpython $contourT_x $Newtonian/Re4000 0.0041 0.0D &&
#pvpython $contourT_x $Newtonian/Re4000_impinging 0.0041 0.0D &&
#echo "---------------" &&
#echo "Finish T_x 0.0D" &&
#echo "---------------" &&
#pvpython $contourT_x $BirdCarreau/inlet_0p5 0.006 0.25D &&
#pvpython $contourT_x $BirdCarreau/inlet0p5_impinging 0.006 0.25D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3 0.006 0.25D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.006 0.25D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.006 0.25D &&
#pvpython $contourT_x $Newtonian/Re2400 0.006 0.25D &&
#pvpython $contourT_x $Newtonian/Re4000 0.006 0.25D &&
#pvpython $contourT_x $Newtonian/Re4000_impinging 0.006 0.25D &&
#echo "---------------" &&
#echo "Finish T_x 0.25D" &&
#echo "---------------" &&
#pvpython $contourT_x $BirdCarreau/inlet_0p5 0.008 0.5D &&
#pvpython $contourT_x $BirdCarreau/inlet0p5_impinging 0.008 0.5D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3 0.008 0.5D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.008 0.5D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.008 0.5D &&
#pvpython $contourT_x $Newtonian/Re2400 0.008 0.5D &&
#pvpython $contourT_x $Newtonian/Re4000 0.008 0.5D &&
#pvpython $contourT_x $Newtonian/Re4000_impinging 0.008 0.5D &&
#echo "---------------" &&
#echo "Finish T_x 0.5D" &&
#echo "---------------" &&
#pvpython $contourT_x $BirdCarreau/inlet_0p5 0.02 2.0D &&
#pvpython $contourT_x $BirdCarreau/inlet0p5_impinging 0.02 2.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3 0.02 2.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.02 2.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.02 2.0D &&
#pvpython $contourT_x $Newtonian/Re2400 0.02 2.0D &&
#pvpython $contourT_x $Newtonian/Re4000 0.02 2.0D &&
#pvpython $contourT_x $Newtonian/Re4000_impinging 0.02 2.0D &&
#echo "---------------" &&
#echo "Finish T_x 2.0D" &&
#echo "---------------" &&
#pvpython $contourT_x $BirdCarreau/inlet_0p5 0.036 4.0D &&
#pvpython $contourT_x $BirdCarreau/inlet0p5_impinging 0.036 4.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3 0.036 4.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.036 4.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.036 4.0D &&
#pvpython $contourT_x $Newtonian/Re2400 0.036 4.0D &&
#pvpython $contourT_x $Newtonian/Re4000 0.036 4.0D &&
#pvpython $contourT_x $Newtonian/Re4000_impinging 0.036 4.0D &&
#echo "---------------" &&
#echo "Finish T_x 4.0D" &&
#echo "---------------" &&
#pvpython $contourT_x $BirdCarreau/inlet_0p5 0.052 6.0D &&
#pvpython $contourT_x $BirdCarreau/inlet0p5_impinging 0.052 6.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3 0.052 6.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.052 6.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.052 6.0D &&
#pvpython $contourT_x $Newtonian/Re2400 0.052 6.0D &&
#pvpython $contourT_x $Newtonian/Re4000 0.052 6.0D &&
#pvpython $contourT_x $Newtonian/Re4000_impinging 0.052 6.0D &&
#echo "---------------" &&
#echo "Finish T_x 6.0D" &&
#echo "---------------" &&
#pvpython $contourT_x $BirdCarreau/inlet_0p5 0.068 8.0D &&
#pvpython $contourT_x $BirdCarreau/inlet0p5_impinging 0.068 8.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3 0.068 8.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.068 8.0D &&
#pvpython $contourT_x $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.068 8.0D &&
#pvpython $contourT_x $Newtonian/Re2400 0.068 8.0D &&
#pvpython $contourT_x $Newtonian/Re4000 0.068 8.0D &&
#pvpython $contourT_x $Newtonian/Re4000_impinging 0.068 8.0D &&
#echo "---------------" &&
#echo "Finish T_x 8.0D" &&
#echo "---------------" 

#pvpython $contourNu_z $BirdCarreau/inlet_0p5 0 0mm &&
#pvpython $contourNu_z $BirdCarreau/inlet0p5_impinging 0 0mm &&
#pvpython $contourNu_z $BirdCarreau/inlet_0p3 0 0mm &&
#pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0 0mm &&
#pvpython $contourNu_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0 0mm


#pvpython $contourT_z $BirdCarreau/inlet_0p5 0 0mm &&
#pvpython $contourT_z $BirdCarreau/inlet0p5_impinging 0 0mm &&
#pvpython $contourT_z $BirdCarreau/inlet_0p3 0 0mm &&
#pvpython $contourT_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0 0mm &&
#pvpython $contourT_z $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0 0mm &&
#pvpython $contourT_z $Newtonian/Re2400 0 0mm &&
#pvpython $contourT_z $Newtonian/Re4000 0 0mm &&
#pvpython $contourT_z $Newtonian/Re4000_impinging 0 0mm 

#pvpython $contourNu_z $BirdCarreau/inlet_0p5 
#pvpython $contourT_z $BirdCarreau/inlet_0p5 0 0mm 

#pvpython $kidneyVortices_decked $BirdCarreau/inlet_0p5 &&
#pvpython $kidneyVortices_decked $BirdCarreau/inlet0p5_impinging &&
#pvpython $kidneyVortices_decked $BirdCarreau/inlet_0p3 &&
#pvpython $kidneyVortices_decked $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 &&
#pvpython $kidneyVortices_decked $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 &&
#pvpython $kidneyVortices_decked $Newtonian/Re2400 &&
#pvpython $kidneyVortices_decked $Newtonian/Re4000 &&
#pvpython $kidneyVortices_decked $Newtonian/Re4000_impinging 
