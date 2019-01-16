
from PIL import Image
 
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
 
 
if __name__ == '__main__':
#    image = 'example.png'
#    Image.open(image).show()
    dataBase = '/store/8simu_tmp/shape_square/2a_3_T'
    relativePath = 'BirdCarreau/inlet_0p5'
    imageName = 'k_mean_nonD'
    image = dataBase + '/' + relativePath + '/' + imageName + '.png'
    crop(image, (480, 567, 2277, 1281), dataBase+'/'+imageName+'_cropped.png')