
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
    dataBase = '/home/hluo/work/git/thesis/Thesis_hluo_new'
    
    paths = [
            'ch3/images/contours/hluo14_T_c_Q2_0p3'
           ]

    imageNames = [
            'D1-1j_mapped',
            'D2-1j_mapped',
            'D3-1j_mapped',
            'D2-NN-1j_test_from0',
            'D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05',
            'D2-NN-1k_syn_forcing'
                ]

    coords_dict = {
            'D1-1j_mapped': (657, 21, 2631, 846),
            'D2-1j_mapped': (657, 21, 2631, 846),
            'D3-1j_mapped': (657, 21, 2631, 846),
            'D2-NN-1j_test_from0': (657, 21, 2631, 846),
            'D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05': (657, 21, 2631, 846),
            'D2-NN-1k_syn_forcing': (657, 21, 2631, 846)
                }
    
    for i, path in enumerate(paths):
        for imageName in imageNames:
            image = dataBase + '/' + path + '/' + imageName + '.png'
            crop(image, coords_dict[imageName], dataBase + '/' + path + '/' + imageName + '_cropped.png')

main()
