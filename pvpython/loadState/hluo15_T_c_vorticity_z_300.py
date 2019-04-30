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

# load state
LoadState('/store/T_c/1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05/hluo15_T_c_vorticity_z_300.pvsm', LoadStateDataFileOptions='Use File Names From State',
    DataDirectory='/store/T_c/1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05',
    OnlyUseFilesInDataDirectory=0,
    D2NN1k_syn_forcingfoamFileName='/store/T_c/1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05/D2-NN-1k_syn_forcing.foam')

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
SaveScreenshot('/store/T_c/1j/D2-NN-1j_test_from0p3_forcingSinus_St3p2_A_eq_0p05/hluo15_T_c_vorticity_z_300.png', renderView1, ImageResolution=[2754, 1838],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.026584694229026866, 0.026567368838553623, 0.09421328149678593]
renderView1.CameraFocalPoint = [0.024234406354908228, -0.010401134201018987, 0.002298669923024629]
renderView1.CameraViewUp = [0.1922771356690952, 0.9426521851791163, -0.27283027851747954]
renderView1.CameraParallelScale = 0.09044328636212606

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).