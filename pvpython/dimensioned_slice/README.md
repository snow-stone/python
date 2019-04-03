
# nu_mean_slice_zNormal-logScale_clipped_beta.py

Paraview steps :   
1. clip1,2,3   
2. slice1   
3. visu on nu_mean   
4. set fixed range for nu_mean  
5. change colorMap and change colormapping to logscale   
6. slice is set to be optional thus differ from parameter to parameter. reset the view to ensure exact output

# nu_mean_slice_yNormal-logScale_clipped.py

Paraview steps :   
1. clip1,2   
2. slice1   
3. visu on nu_mean   
4. set fixed range for nu_mean  
5. change colorMap and change colormapping to logscale   
6. slice is set to be optional thus differ from parameter to parameter. reset the view to ensure exact output

# k_mean_nonD_slice_zNormal-logScale_clipped_beta.py

1. copy nu_mean_slice_zNormal-logScale_clipped_beta.py   
2. raplace string "nu_mean" by "k_mean_nonD"   
3. rescale variable k_mean_nonD to [1e-6, 1]   
4. remove log-scale in color map   

Note : in scrpit name "logScale" is actually misleading for in step 4 we have removed that. But... the naming is retained anyhow.
