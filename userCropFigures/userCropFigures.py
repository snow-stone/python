
from PIL import Image
#import sys
 
def crop(image_path, coords, saved_location):
    """
    @param image_path: The path to the image to edit
    @param coords: A tuple of x/y coordinates (x1, y1, x2, y2)
    @param saved_location: Path to save the cropped image
    """
    image_obj = Image.open(image_path)
    cropped_image = image_obj.crop(coords)
    cropped_image.save(saved_location)
    cropped_image.show()
 
def main():
#    image = 'example.png'
#    Image.open(image).show()
#    dataBase = '/store/8simu_tmp/shape_square/2a_3_T'
    dataBase = '/store/T_c'
    
    paths1 = [
            'BirdCarreau/inlet_0p5',
            'Newtonian/Re4000',
            'BirdCarreau/inlet0p5_impinging',
            'Newtonian/Re4000_impinging',
            'BirdCarreau/inlet_0p3',
            'Newtonian/Re2400',
            'BirdCarreau/inlet_0p3-a_0p5-setT_St_1',
            'BirdCarreau/inlet_0p3-a_0p5-setT_St_5'
           ]

    paths2 = [
            '1j/D1-1j_mapped',
            '1j/D2-1j_mapped',
            '1j/D3-1j_mapped',
            '1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05',
            '1k/D2-NN-1k_syn_forcing'
            ]

    pathsNonNewtonian = [
            'BirdCarreau/inlet_0p5',
            'BirdCarreau/inlet0p5_impinging',
            'BirdCarreau/inlet_0p3',
            'BirdCarreau/inlet_0p3-a_0p5-setT_St_1',
            'BirdCarreau/inlet_0p3-a_0p5-setT_St_5'
           ]
#    paths = [
#            'BirdCarreau/inlet_0p5',
#            'BirdCarreau/inlet_0p3'
#           ]
#    imageName = sys.argv[1]
#    imageNames = [
#            '2DstreamLines_0p0D',
#            '2DstreamLines_2p0D',
#            '2DstreamLines_4p0D',
#            '2DstreamLines_6p0D'            
#            ]
    imageNames = [
            'k_mean_nonD_slice_zNormal_z_Eq_0mm'
                ]
    
    coords_dict= {
            'k_mean' : (729, 660, 2496, 1173),
            'k_mean_nonD' : (480, 567, 2277, 1281),
            'k_mean_nonD_add_streamTracer_green_vertical' : (513, 594, 2232, 1227),
            'k_mean_nonD_add_streamTracer_green_horizontal' : (486, 591, 2235, 1236),
            '2DstreamLines_0p0D' : (522, 408, 1695, 1491),
            '2DstreamLines_2p0D' : (522, 408, 1695, 1491),
            '2DstreamLines_4p0D' : (522, 408, 1695, 1491),
            '2DstreamLines_6p0D' : (522, 408, 1695, 1491),
            'slice_6D_T_mean'    : (792, 264, 2097, 1566),
            'nu_mean_slice_zNomal_z_Eq_0mm' : (600, 684, 2300, 1176),
            'nu_mean_slice_x_Eq_0.0D'       : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_0.25D'      : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_0.4D'       : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_0.5D'       : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_1.0D'       : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_1.75D'      : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_2.0D'       : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_4.0D'       : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_6.0D'       : (810, 285, 2082, 1551),
            'nu_mean_slice_x_Eq_8.0D'       : (810, 285, 2082, 1551),
            'T_mean_slice_0.0D'             : (816, 286, 2080, 1552),
            'T_mean_slice_0.25D'            : (816, 286, 2080, 1552),
            'T_mean_slice_0.5D'             : (816, 286, 2080, 1552),
            'T_mean_slice_2.0D'             : (816, 286, 2080, 1552),
            'T_mean_slice_4.0D'             : (816, 286, 2080, 1552),
            'T_mean_slice_6.0D'             : (816, 286, 2080, 1552),
            'T_mean_slice_8.0D'             : (816, 286, 2080, 1552),
#            'Ux_mean_slice_yNomal_y_Eq_neg3mm_addInlet2' : (552, 732, 2238, 1080),
#            'Ux_mean_slice_yNomal_y_Eq_0mm_addInlet2'    : (552, 732, 2238, 1080),
#            'Ux_mean_slice_yNomal_y_Eq_pos3mm_addInlet2' : (552, 732, 2238, 1080),
#            'Uy_mean_slice_yNomal_y_Eq_neg3mm_addInlet2'    : (594, 750, 2298, 1077),
#            'Uy_mean_slice_yNomal_y_Eq_0mm_addInlet2'       : (594, 750, 2298, 1077),
#            'Uy_mean_slice_yNomal_y_Eq_pos3mm_addInlet2'    : (594, 750, 2298, 1077),
#            'Uz_mean_slice_yNomal_y_Eq_neg3mm_addInlet2'    : (594, 750, 2298, 1077),
#            'Uz_mean_slice_yNomal_y_Eq_0mm_addInlet2'       : (594, 750, 2298, 1077),
#            'Uz_mean_slice_yNomal_y_Eq_pos3mm_addInlet2'    : (594, 750, 2298, 1077),
#            'nu_mean_slice_yNomal_y_Eq_neg3mm_addInlet2'    : (621, 765, 2280, 1076),
#            'nu_mean_slice_yNomal_y_Eq_0mm_addInlet2'       : (621, 765, 2280, 1076),
#            'nu_mean_slice_yNomal_y_Eq_pos3mm_addInlet2'    : (621, 765, 2280, 1076),
#            'T_mean_slice_zNomal_z_Eq_0mm'                  : (1369,506, 2232,  622),
#            'nu_mean_slice_zNomal_z_Eq_0mm'                 : (1377,505, 2233,  624),
            'nu_mean_slice_zNormal_z_Eq_p3p5mm'             : (402, 681, 2130, 1155),
            'nu_mean_slice_zNormal_z_Eq_p3mm'               : (402, 681, 2130, 1155),
            'nu_mean_slice_zNormal_z_Eq_p2p5mm'             : (402, 681, 2130, 1155),
            'nu_mean_slice_zNormal_z_Eq_p2mm'               : (402, 681, 2130, 1155),
            'nu_mean_slice_zNormal_z_Eq_p1p5mm'             : (402, 681, 2130, 1155),
            'nu_mean_slice_zNormal_z_Eq_p1mm'               : (402, 681, 2130, 1155),
            'nu_mean_slice_zNormal_z_Eq_p0p5mm'             : (402, 681, 2130, 1155),
            'nu_mean_slice_zNormal_z_Eq_0mm'                : (402, 681, 2130, 1155),
            'nu_mean_slice_yNormal_y_Eq_p3mm_addInlet2'     : (387, 756, 2142, 1080),
            'nu_mean_slice_yNormal_y_Eq_p2mm_addInlet2'     : (387, 756, 2142, 1080),
            'nu_mean_slice_yNormal_y_Eq_p1mm_addInlet2'     : (387, 756, 2142, 1080),
            'nu_mean_slice_yNormal_y_Eq_0mm_addInlet2'      : (387, 756, 2142, 1080),
            'nu_mean_slice_yNormal_y_Eq_n1mm_addInlet2'     : (387, 756, 2142, 1080),
            'nu_mean_slice_yNormal_y_Eq_n2mm_addInlet2'     : (387, 756, 2142, 1080),
            'nu_mean_slice_yNormal_y_Eq_n3mm_addInlet2'     : (387, 756, 2142, 1080),
            'k_mean_nonD_slice_zNormal_z_Eq_p3p5mm'             : (402, 681, 2130, 1155),
            'k_mean_nonD_slice_zNormal_z_Eq_p3mm'               : (402, 681, 2130, 1155),
            'k_mean_nonD_slice_zNormal_z_Eq_p2p5mm'             : (402, 681, 2130, 1155),
            'k_mean_nonD_slice_zNormal_z_Eq_p2mm'               : (402, 681, 2130, 1155),
            'k_mean_nonD_slice_zNormal_z_Eq_p1p5mm'             : (402, 681, 2130, 1155),
            'k_mean_nonD_slice_zNormal_z_Eq_p1mm'               : (402, 681, 2130, 1155),
            'k_mean_nonD_slice_zNormal_z_Eq_p0p5mm'             : (402, 681, 2130, 1155),
            'k_mean_nonD_slice_zNormal_z_Eq_0mm'                : (402, 681, 2130, 1155),
            'k_mean_nonD_slice_yNormal_y_Eq_p3mm_addInlet2'     : (387, 756, 2142, 1080),
            'k_mean_nonD_slice_yNormal_y_Eq_p2mm_addInlet2'     : (387, 756, 2142, 1080),
            'k_mean_nonD_slice_yNormal_y_Eq_p1mm_addInlet2'     : (387, 756, 2142, 1080),
            'k_mean_nonD_slice_yNormal_y_Eq_0mm_addInlet2'      : (387, 756, 2142, 1080),
            'k_mean_nonD_slice_yNormal_y_Eq_n1mm_addInlet2'     : (387, 756, 2142, 1080),
            'k_mean_nonD_slice_yNormal_y_Eq_n2mm_addInlet2'     : (387, 756, 2142, 1080),
            'k_mean_nonD_slice_yNormal_y_Eq_n3mm_addInlet2'     : (387, 756, 2142, 1080),
            }    
    
    
    for i, path in enumerate(paths2):
#    for i, path in enumerate(pathsNonNewtonian):
        for imageName in imageNames:
            image = dataBase + '/' + path + '/' + imageName + '.png'
            crop(image, coords_dict[imageName], dataBase + '/' + path + '/' + imageName + '_cropped.png')

main()
