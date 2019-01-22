
from PIL import Image, ImageDraw
 
img = Image.open('/store/8simu_tmp/shape_square/2a_3_T/Newtonian/Re4000/slice_yNomal_y_Eq_neg3mm.png')

draw = ImageDraw.Draw(img)

draw.rectangle([(888,755), (1219.5, 1078.5)], outline='black')

#img.show()

img.save('/store/8simu_tmp/shape_square/2a_3_T/Newtonian/Re4000/slice_yNomal_y_Eq_neg3mm_addInlet2.png')