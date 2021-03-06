##!/bin/bash

BirdCarreau=/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau
Newtonian=/store/8simu_tmp/shape_square/2a_3_T/Newtonian

export_T=export_csv_slice_xNormal.py
export_nu=nu_mean_export_csv_slice_xNormal.py

#pvpython $export_nu $BirdCarreau/inlet_0p5 0.0041 0.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging 0.0041 0.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3 0.0041 0.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0041 0.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0041 0.0D &&
#echo "---------------" &&
#echo "Finish 0.0D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.005 0.125D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.005 0.125D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.005 0.125D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.005 0.125D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.005 0.125D &&
#echo "---------------" &&
#echo "Finish 0.125D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.006 0.25D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.006 0.25D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.006 0.25D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.006 0.25D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.006 0.25D &&
#echo "---------------" &&
#echo "Finish 0.25D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.007 0.375D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.007 0.375D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.007 0.375D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.007 0.375D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.007 0.375D &&
#echo "---------------" &&
#echo "Finish 0.375D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.008 0.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.008 0.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.008 0.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.008 0.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.008 0.5D &&
#echo "---------------" &&
#echo "Finish 0.5D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.009 0.625D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.009 0.625D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.009 0.625D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.009 0.625D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.009 0.625D &&
#echo "---------------" &&
#echo "Finish 0.625D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.01 0.75D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.01 0.75D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.01 0.75D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.01 0.75D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.01 0.75D &&
#echo "---------------" &&
#echo "Finish 0.75D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.011 0.875D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.011 0.875D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.011 0.875D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.011 0.875D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.011 0.875D &&
#echo "---------------" &&
#echo "Finish 0.875D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.012 1.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.012 1.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.012 1.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.012 1.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.012 1.0D &&
#echo "---------------" &&
#echo "Finish 1.0D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.013 1.125D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.013 1.125D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.013 1.125D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.013 1.125D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.013 1.125D &&
#echo "---------------" &&
#echo "Finish 1.125D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.014 1.25D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.014 1.25D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.014 1.25D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.014 1.25D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.014 1.25D &&
#echo "---------------" &&
#echo "Finish 1.25D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.015 1.375D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.015 1.375D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.015 1.375D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.015 1.375D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.015 1.375D &&
#echo "---------------" &&
#echo "Finish 1.375D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.016 1.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.016 1.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.016 1.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.016 1.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.016 1.5D &&
#echo "---------------" &&
#echo "Finish 1.5D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.017 1.625D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.017 1.625D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.017 1.625D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.017 1.625D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.017 1.625D &&
#echo "---------------" &&
#echo "Finish 1.625D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.018 1.75D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.018 1.75D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.018 1.75D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.018 1.75D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.018 1.75D &&
#echo "---------------" &&
#echo "Finish 1.75D" &&
#echo "---------------"
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.019 1.875D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.019 1.875D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.019 1.875D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.019 1.875D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.019 1.875D &&
#echo "---------------" &&
#echo "Finish 1.875D" &&
#echo "---------------"
#pvpython $export_nu $BirdCarreau/inlet_0p5 0.02 2.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging 0.02 2.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3 0.02 2.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.02 2.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.02 2.0D &&
#echo "---------------" &&
#echo "Finish 2.0D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.024 2.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.024 2.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.024 2.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.024 2.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.024 2.5D &&
#echo "---------------" &&
#echo "Finish 2.5D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.028 3.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.028 3.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.028 3.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.028 3.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.028 3.0D &&
#echo "---------------" &&
#echo "Finish 3.0D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.032 3.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.032 3.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.032 3.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.032 3.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.032 3.5D &&
#echo "---------------" &&
#echo "Finish 3.5D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5 0.036 4.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging 0.036 4.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3 0.036 4.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.036 4.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.036 4.0D &&
#echo "---------------" &&
#echo "Finish 4.0D" &&
#echo "---------------"
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.04 4.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.04 4.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.04 4.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.04 4.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.04 4.5D &&
#echo "---------------" &&
#echo "Finish 4.5D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.044 5.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.044 5.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.044 5.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.044 5.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.044 5.0D &&
#echo "---------------" &&
#echo "Finish 5.0D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.048 5.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.048 5.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.048 5.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.048 5.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.048 5.5D &&
#echo "---------------" &&
#echo "Finish 5.5D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5 0.052 6.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging 0.052 6.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3 0.052 6.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.052 6.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.052 6.0D &&
#echo "---------------" &&
#echo "Finish 6D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.056 6.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.056 6.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.056 6.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.056 6.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.056 6.5D &&
#echo "---------------" &&
#echo "Finish 6.5D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.06 7.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.06 7.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.06 7.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.06 7.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.06 7.0D &&
#echo "---------------" &&
#echo "Finish 7.0D" &&
#echo "---------------"
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.064 7.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.064 7.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.064 7.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.064 7.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.064 7.5D &&
#echo "---------------" &&
#echo "Finish 7.5D" &&
#echo "---------------" &&
#pvpython $export_nu $BirdCarreau/inlet_0p5 0.068 8.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging 0.068 8.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3 0.068 8.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.068 8.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.068 8.0D &&
#echo "---------------" &&
#echo "Finish 8D" &&
#echo "---------------"
#pvpython $export_nu $BirdCarreau/inlet_0p5                 0.072 8.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging        0.072 8.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3                 0.072 8.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.072 8.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.072 8.5D &&
#echo "---------------" &&
#echo "Finish 8.5D" &&
#echo "---------------"
#pvpython $export_nu $BirdCarreau/inlet_0p5 0.076 9.0D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging 0.076 9.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3 0.076 9.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.076 9.0D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.076 9.0D &&
#echo "---------------" &&
#echo "Finish 9D" &&
#echo "---------------"
#pvpython $export_nu $BirdCarreau/inlet_0p5 0.079 9.5D &&
#pvpython $export_nu $BirdCarreau/inlet0p5_impinging 0.079 9.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3 0.079 9.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.079 9.5D &&
#pvpython $export_nu $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.079 9.5D &&
#echo "---------------" &&
#echo "Finish 9.5D" &&
#echo "---------------"


pvpython $export_T $Newtonian/Re2400                      0.0041 0.0D &&
pvpython $export_T $Newtonian/Re4000                      0.0041 0.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.0041 0.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.0041 0.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.0041 0.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.0041 0.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.0041 0.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.0041 0.0D &&
echo "---------------" &&
echo "Finish 0.0D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.005 0.125D &&
pvpython $export_T $Newtonian/Re4000                      0.005 0.125D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.005 0.125D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.005 0.125D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.005 0.125D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.005 0.125D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.005 0.125D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.005 0.125D &&
echo "---------------" &&
echo "Finish 0.125D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.006 0.25D &&
pvpython $export_T $Newtonian/Re4000                      0.006 0.25D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.006 0.25D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.006 0.25D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.006 0.25D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.006 0.25D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.006 0.25D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.006 0.25D &&
echo "---------------" &&
echo "Finish 0.25D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.007 0.375D &&
pvpython $export_T $Newtonian/Re4000                      0.007 0.375D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.007 0.375D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.007 0.375D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.007 0.375D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.007 0.375D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.007 0.375D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.007 0.375D &&
echo "---------------" &&
echo "Finish 0.375D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.008 0.5D &&
pvpython $export_T $Newtonian/Re4000                      0.008 0.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.008 0.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.008 0.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.008 0.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.008 0.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.008 0.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.008 0.5D &&
echo "---------------" &&
echo "Finish 0.5D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.009 0.625D &&
pvpython $export_T $Newtonian/Re4000                      0.009 0.625D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.009 0.625D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.009 0.625D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.009 0.625D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.009 0.625D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.009 0.625D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.009 0.625D &&
echo "---------------" &&
echo "Finish 0.625D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.01 0.75D &&
pvpython $export_T $Newtonian/Re4000                      0.01 0.75D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.01 0.75D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.01 0.75D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.01 0.75D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.01 0.75D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.01 0.75D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.01 0.75D &&
echo "---------------" &&
echo "Finish 0.75D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.011 0.875D &&
pvpython $export_T $Newtonian/Re4000                      0.011 0.875D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.011 0.875D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.011 0.875D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.011 0.875D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.011 0.875D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.011 0.875D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.011 0.875D &&
echo "---------------" &&
echo "Finish 0.875D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.012 1.0D &&
pvpython $export_T $Newtonian/Re4000                      0.012 1.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.012 1.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.012 1.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.012 1.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.012 1.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.012 1.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.012 1.0D &&
echo "---------------" &&
echo "Finish 1.0D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.013 1.125D &&
pvpython $export_T $Newtonian/Re4000                      0.013 1.125D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.013 1.125D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.013 1.125D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.013 1.125D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.013 1.125D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.013 1.125D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.013 1.125D &&
echo "---------------" &&
echo "Finish 1.125D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.014 1.25D &&
pvpython $export_T $Newtonian/Re4000                      0.014 1.25D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.014 1.25D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.014 1.25D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.014 1.25D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.014 1.25D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.014 1.25D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.014 1.25D &&
echo "---------------" &&
echo "Finish 1.25D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.015 1.375D &&
pvpython $export_T $Newtonian/Re4000                      0.015 1.375D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.015 1.375D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.015 1.375D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.015 1.375D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.015 1.375D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.015 1.375D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.015 1.375D &&
echo "---------------" &&
echo "Finish 1.375D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.016 1.5D &&
pvpython $export_T $Newtonian/Re4000                      0.016 1.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.016 1.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.016 1.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.016 1.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.016 1.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.016 1.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.016 1.5D &&
echo "---------------" &&
echo "Finish 1.5D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.017 1.625D &&
pvpython $export_T $Newtonian/Re4000                      0.017 1.625D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.017 1.625D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.017 1.625D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.017 1.625D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.017 1.625D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.017 1.625D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.017 1.625D &&
echo "---------------" &&
echo "Finish 1.625D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.018 1.75D &&
pvpython $export_T $Newtonian/Re4000                      0.018 1.75D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.018 1.75D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.018 1.75D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.018 1.75D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.018 1.75D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.018 1.75D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.018 1.75D &&
echo "---------------" &&
echo "Finish 1.75D" &&
echo "---------------"
pvpython $export_T $Newtonian/Re2400                      0.019 1.875D &&
pvpython $export_T $Newtonian/Re4000                      0.019 1.875D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.019 1.875D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.019 1.875D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.019 1.875D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.019 1.875D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.019 1.875D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.019 1.875D &&
echo "---------------" &&
echo "Finish 1.875D" &&
echo "---------------"
pvpython $export_T $Newtonian/Re2400                      0.02 2.0D &&
pvpython $export_T $Newtonian/Re4000                      0.02 2.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.02 2.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.02 2.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.02 2.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.02 2.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.02 2.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.02 2.0D &&
echo "---------------" &&
echo "Finish 2.0D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.024 2.5D &&
pvpython $export_T $Newtonian/Re4000                      0.024 2.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.024 2.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.024 2.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.024 2.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.024 2.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.024 2.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.024 2.5D &&
echo "---------------" &&
echo "Finish 2.5D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.028 3.0D &&
pvpython $export_T $Newtonian/Re4000                      0.028 3.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.028 3.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.028 3.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.028 3.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.028 3.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.028 3.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.028 3.0D &&
echo "---------------" &&
echo "Finish 3.0D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.032 3.5D &&
pvpython $export_T $Newtonian/Re4000                      0.032 3.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.032 3.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.032 3.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.032 3.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.032 3.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.032 3.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.032 3.5D &&
echo "---------------" &&
echo "Finish 3.5D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.036 4.0D &&
pvpython $export_T $Newtonian/Re4000                      0.036 4.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.036 4.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.036 4.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.036 4.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.036 4.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.036 4.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.036 4.0D &&
echo "---------------" &&
echo "Finish 4.0D" &&
echo "---------------"
pvpython $export_T $Newtonian/Re2400                      0.04 4.5D &&
pvpython $export_T $Newtonian/Re4000                      0.04 4.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.04 4.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.04 4.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.04 4.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.04 4.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.04 4.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.04 4.5D &&
echo "---------------" &&
echo "Finish 4.5D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.044 5.0D &&
pvpython $export_T $Newtonian/Re4000                      0.044 5.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.044 5.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.044 5.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.044 5.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.044 5.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.044 5.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.044 5.0D &&
echo "---------------" &&
echo "Finish 5.0D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.048 5.5D &&
pvpython $export_T $Newtonian/Re4000                      0.048 5.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.048 5.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.048 5.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.048 5.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.048 5.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.048 5.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.048 5.5D &&
echo "---------------" &&
echo "Finish 5.5D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.052 6.0D &&
pvpython $export_T $Newtonian/Re4000                      0.052 6.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.052 6.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.052 6.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.052 6.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.052 6.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.052 6.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.052 6.0D &&
echo "---------------" &&
echo "Finish 6D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.056 6.5D &&
pvpython $export_T $Newtonian/Re4000                      0.056 6.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.056 6.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.056 6.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.056 6.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.056 6.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.056 6.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.056 6.5D &&
echo "---------------" &&
echo "Finish 6.5D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.06 7.0D &&
pvpython $export_T $Newtonian/Re4000                      0.06 7.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.06 7.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.06 7.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.06 7.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.06 7.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.06 7.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.06 7.0D &&
echo "---------------" &&
echo "Finish 7.0D" &&
echo "---------------"
pvpython $export_T $Newtonian/Re2400                      0.064 7.5D &&
pvpython $export_T $Newtonian/Re4000                      0.064 7.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.064 7.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.064 7.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.064 7.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.064 7.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.064 7.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.064 7.5D &&
echo "---------------" &&
echo "Finish 7.5D" &&
echo "---------------" &&
pvpython $export_T $Newtonian/Re2400                      0.068 8.0D &&
pvpython $export_T $Newtonian/Re4000                      0.068 8.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.068 8.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.068 8.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.068 8.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.068 8.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.068 8.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.068 8.0D &&
echo "---------------" &&
echo "Finish 8D" &&
echo "---------------"
pvpython $export_T $Newtonian/Re2400                      0.072 8.5D &&
pvpython $export_T $Newtonian/Re4000                      0.072 8.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.072 8.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.072 8.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.072 8.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.072 8.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.072 8.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.072 8.5D &&
echo "---------------" &&
echo "Finish 8.5D" &&
echo "---------------"
pvpython $export_T $Newtonian/Re2400                      0.076 9.0D &&
pvpython $export_T $Newtonian/Re4000                      0.076 9.0D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.076 9.0D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.076 9.0D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.076 9.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.076 9.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.076 9.0D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.076 9.0D &&
echo "---------------" &&
echo "Finish 9D" &&
echo "---------------"
pvpython $export_T $Newtonian/Re2400                      0.079 9.5D &&
pvpython $export_T $Newtonian/Re4000                      0.079 9.5D &&
pvpython $export_T $Newtonian/Re4000_impinging            0.079 9.5D &&
pvpython $export_T $BirdCarreau/inlet_0p5                 0.079 9.5D &&
pvpython $export_T $BirdCarreau/inlet0p5_impinging        0.079 9.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3                 0.079 9.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_1 0.079 9.5D &&
pvpython $export_T $BirdCarreau/inlet_0p3-a_0p5-setT_St_5 0.079 9.5D &&
echo "---------------" &&
echo "Finish 9.5D" &&
echo "---------------"
