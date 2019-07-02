
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
            #'ch3/images/lines/FIG2',
            #'ch3/images/lines/FIG3',
            'ch3/images/lines/FIG46',
            'ch3/images/lines/FIG57'
           ]
    imageNames = [
            'cut2a',
            'cut2b',
            'cut3a',
            'cut3b'
                ]
    coords_dict = {
            'cut2a': (0, 220, 1200, 1120),
            'cut2b': (0, 220, 1240, 1120),
            'cut3a': (0, 220, 1200, 1120),
            'cut3b': (0, 220, 1240, 1120)
                }
    
    for i, path in enumerate(paths):
        for imageName in imageNames:
            image = dataBase + '/' + path + '/' + imageName + '.png'
            crop(image, coords_dict[imageName], dataBase + '/' + path + '/' + imageName + '_cropped.png')

main()
