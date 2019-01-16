
from PIL import Image

img = Image.open("example.png")

coords = (887, 129, 1146, 426)

img.show()
cropped = img.crop(coords)

cropped.show()