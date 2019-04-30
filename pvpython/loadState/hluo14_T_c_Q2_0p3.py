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
renderView1.CameraPosition = [-0.026584694229026866, 0.026567368838553623, 0.09421328149678593]
renderView1.CameraFocalPoint = [0.024234406354908228, -0.010401134201018987, 0.002298669923024629]
renderView1.CameraViewUp = [0.1922771356690952, 0.9426521851791163, -0.27283027851747954]
renderView1.CameraParallelScale = 0.09044328636212606

# save screenshot
SaveScreenshot(dirName+'/'+'hluo14_T_c_Q2_0p3.png', renderView1, ImageResolution=[2754, 1838],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

#### saving camera placements for all active views

# current camera placement for renderView1
#renderView1.CameraPosition = [-0.026584694229026866, 0.026567368838553623, 0.09421328149678593]
#renderView1.CameraFocalPoint = [0.024234406354908228, -0.010401134201018987, 0.002298669923024629]
#renderView1.CameraViewUp = [0.1922771356690952, 0.9426521851791163, -0.27283027851747954]
#renderView1.CameraParallelScale = 0.09044328636212606

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).

import os
print "Finalizing "+ os.path.basename(__file__) +" " + "@ dir : " + dirName 
import datetime
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print "==============================="
