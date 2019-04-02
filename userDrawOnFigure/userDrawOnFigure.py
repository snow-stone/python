
from PIL import Image, ImageDraw
 
def addInlet2(fullPathToImg, xy, saveLocation, saveAs):
    img = Image.open(fullPathToImg)
    draw = ImageDraw.Draw(img)
    draw.rectangle(xy, outline='black')
    
    img.show()
    img.save(saveLocation+'/'+saveAs)
    

def main():
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
           
    pathsNonNewtonian = [
            'BirdCarreau/inlet_0p5',
            'BirdCarreau/inlet0p5_impinging',
            'BirdCarreau/inlet_0p3',
            'BirdCarreau/inlet_0p3-a_0p5-setT_St_1',
            'BirdCarreau/inlet_0p3-a_0p5-setT_St_5'
           ]
           
    imageNames = ['nu_mean_slice_yNomal_y_Eq_neg3mm',
                  'nu_mean_slice_yNomal_y_Eq_0mm',
                  'nu_mean_slice_yNomal_y_Eq_pos3mm']
    
    xy_dict= {
            'Ux_mean_slice_yNomal_y_Eq_neg3mm' : [(888,755), (1219.5, 1078.5)],
            'Ux_mean_slice_yNomal_y_Eq_0mm'    : [(888,755), (1219.5, 1078.5)],
            'Ux_mean_slice_yNomal_y_Eq_pos3mm' : [(888,755), (1219.5, 1078.5)],
            'Uy_mean_slice_yNomal_y_Eq_neg3mm' : [(909,760.5), (1215, 1072.5)],
            'Uy_mean_slice_yNomal_y_Eq_0mm'    : [(909,760.5), (1215, 1072.5)],
            'Uy_mean_slice_yNomal_y_Eq_pos3mm' : [(909,760.5), (1215, 1072.5)],
            'Uz_mean_slice_yNomal_y_Eq_neg3mm' : [(909,760.5), (1215, 1072.5)],
            'Uz_mean_slice_yNomal_y_Eq_0mm'    : [(909,760.5), (1215, 1072.5)],
            'Uz_mean_slice_yNomal_y_Eq_pos3mm' : [(909,760.5), (1215, 1072.5)],
            'nu_mean_slice_yNomal_y_Eq_neg3mm' : [(928.5, 760), (1234.5, 1075)],
            'nu_mean_slice_yNomal_y_Eq_0mm'    : [(928.5, 760), (1234.5, 1075)],
            'nu_mean_slice_yNomal_y_Eq_pos3mm' : [(928.5, 760), (1234.5, 1075)]                                                  
            }
            
#    for i, path in enumerate(paths):
    for i, path in enumerate(pathsNonNewtonian):
        for imageName in imageNames:
            imageFullPath = dataBase + '/' + path + '/' + imageName + '.png'
            addInlet2(imageFullPath, xy_dict[imageName], saveLocation = dataBase + '/' + path, saveAs= imageName +'_addInlet2'+'.png')
            
main()