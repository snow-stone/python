# trace generated using paraview version 5.6.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1377, 919]

# destroy renderView1
Delete(renderView1)
del renderView1

import sys

dirName = sys.argv[1]

# load state
LoadState(dirName+'/'+'hluo14_T_c_Q2_0p3.pvsm', LoadStateDataFileOptions='Use File Names From State',
    DataDirectory=dirName,
    OnlyUseFilesInDataDirectory=0,
    D2NN1k_syn_forcingfoamFileName=dirName+'/'+'toto.foam')

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1377, 919]

# current camera placement for renderView1
renderView1.CameraPosition = [0.009733900417193858, -0.04062097882611073, -0.0003757332760348916]
renderView1.CameraFocalPoint = [0.009733900417193858, -0.03816327080130577, -0.0003757332760348916]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.09035374257103915

# save screenshot
SaveScreenshot(dirName+'/'+'hluo14_T_c_Q2_0p3_bas.png', renderView1, ImageResolution=[2754, 1838],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

#### saving camera placements for all active views

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

import os
print "Finalizing "+ os.path.basename(__file__) +" " + "@ dir : " + dirName 
import datetime
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print "==============================="
