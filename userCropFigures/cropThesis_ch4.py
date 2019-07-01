
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
            'ch4/images/contours/hluo14_T_r_Q2_0p3'
           ]

    imageNames = [
            'N1d',
            'N2d',
            'N2i',
            'NN1d',
            'NN1dSt1',
            'NN1dSt5',
            'NN2d',
            'NN2i'
                ]

    coords_dict = {
            'N1d': (303, 12, 2710, 1176),
            'N2d': (303, 12, 2710, 1176),
            'N2i': (303, 12, 2710, 1176),
            'NN1d': (303, 12, 2710, 1176),
            'NN1dSt1': (303, 12, 2710, 1176),
            'NN1dSt5': (303, 12, 2710, 1176),
            'NN2d': (303, 12, 2710, 1176),
            'NN2i': (303, 12, 2710, 1176)
                }
    
    for i, path in enumerate(paths):
        for imageName in imageNames:
            image = dataBase + '/' + path + '/' + imageName + '.png'
            crop(image, coords_dict[imageName], dataBase + '/' + path + '/' + imageName + '_cropped.png')

main()
