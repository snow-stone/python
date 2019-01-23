
from PIL import Image
import sys
 
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
    dataBase = '/store/8simu_tmp/shape_square/2a_3_T'
    paths = [
            'BirdCarreau/inlet_0p5',
            'Newtonian/Re4000',
            'BirdCarreau/inlet0p5_impinging',
            'Newtonian/Re4000_impinging',
            'BirdCarreau/inlet_0p3',
            'Newtonian/Re2400',
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
    imageNames = ['Ux_mean_slice_yNomal_y_Eq_0mm_addInlet2']
    
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
            'Ux_mean_slice_yNomal_y_Eq_neg3mm_addInlet2' : (552, 732, 2238, 1080),
            'Ux_mean_slice_yNomal_y_Eq_0mm_addInlet2'    : (552, 732, 2238, 1080)
            }    
    
    
    for i, path in enumerate(paths):
        for imageName in imageNames:
            image = dataBase + '/' + path + '/' + imageName + '.png'
            crop(image, coords_dict[imageName], dataBase + '/' + path + '/' + imageName + '_cropped.png')

main()