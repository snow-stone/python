# trace generated using paraview version 5.6.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import sys

dirName                   = sys.argv[1]
xPositionInSlice          = float(sys.argv[2])
xPositionInSaveScreenShot = sys.argv[3]

# create a new 'OpenFOAMReader'
inlet_0p3foam = OpenFOAMReader(FileName=dirName+'/inlet_0p3.foam')
inlet_0p3foam.SkipZeroTime = 1
inlet_0p3foam.CaseType = 'Reconstructed Case'
inlet_0p3foam.LabelSize = '32-bit'
inlet_0p3foam.ScalarSize = '64-bit (DP)'
inlet_0p3foam.Createcelltopointfiltereddata = 1
inlet_0p3foam.Adddimensionalunitstoarraynames = 0
inlet_0p3foam.MeshRegions = ['internalMesh']
inlet_0p3foam.CellArrays = ['Q', 'T', 'T_mean', 'U', 'U_mean', 'k_mean', 'nu', 'nu_mean', 'p', 'reyTensor', 'reyTensor_mean', 'tt_mean', 'vorticity_U_mean']
inlet_0p3foam.PointArrays = []
inlet_0p3foam.LagrangianArrays = []
inlet_0p3foam.Cachemesh = 1
inlet_0p3foam.Decomposepolyhedra = 1
inlet_0p3foam.ListtimestepsaccordingtocontrolDict = 0
inlet_0p3foam.Lagrangianpositionswithoutextradata = 1
inlet_0p3foam.Readzones = 0
inlet_0p3foam.Copydatatocellzones = 0

# Properties modified on inlet_0p3foam
inlet_0p3foam.CellArrays = ['nu_mean']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1448, 919]

# show data in view
inlet_0p3foamDisplay = Show(inlet_0p3foam, renderView1)

# trace defaults for the display properties.
inlet_0p3foamDisplay.Representation = 'Surface'
inlet_0p3foamDisplay.AmbientColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.ColorArrayName = [None, '']
inlet_0p3foamDisplay.DiffuseColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.LookupTable = None
inlet_0p3foamDisplay.MapScalars = 1
inlet_0p3foamDisplay.MultiComponentsMapping = 0
inlet_0p3foamDisplay.InterpolateScalarsBeforeMapping = 1
inlet_0p3foamDisplay.Opacity = 1.0
inlet_0p3foamDisplay.PointSize = 2.0
inlet_0p3foamDisplay.LineWidth = 1.0
inlet_0p3foamDisplay.RenderLinesAsTubes = 0
inlet_0p3foamDisplay.RenderPointsAsSpheres = 0
inlet_0p3foamDisplay.Interpolation = 'Gouraud'
inlet_0p3foamDisplay.Specular = 0.0
inlet_0p3foamDisplay.SpecularColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.SpecularPower = 100.0
inlet_0p3foamDisplay.Luminosity = 0.0
inlet_0p3foamDisplay.Ambient = 0.0
inlet_0p3foamDisplay.Diffuse = 1.0
inlet_0p3foamDisplay.EdgeColor = [0.0, 0.0, 0.5]
inlet_0p3foamDisplay.BackfaceRepresentation = 'Follow Frontface'
inlet_0p3foamDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.BackfaceOpacity = 1.0
inlet_0p3foamDisplay.Position = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.Scale = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.Orientation = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.Origin = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.Pickable = 1
inlet_0p3foamDisplay.Texture = None
inlet_0p3foamDisplay.Triangulate = 0
inlet_0p3foamDisplay.UseShaderReplacements = 0
inlet_0p3foamDisplay.ShaderReplacements = ''
inlet_0p3foamDisplay.NonlinearSubdivisionLevel = 1
inlet_0p3foamDisplay.UseDataPartitions = 0
inlet_0p3foamDisplay.OSPRayUseScaleArray = 0
inlet_0p3foamDisplay.OSPRayScaleArray = 'nu_mean'
inlet_0p3foamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
inlet_0p3foamDisplay.OSPRayMaterial = 'None'
inlet_0p3foamDisplay.Orient = 0
inlet_0p3foamDisplay.OrientationMode = 'Direction'
inlet_0p3foamDisplay.SelectOrientationVectors = 'None'
inlet_0p3foamDisplay.Scaling = 0
inlet_0p3foamDisplay.ScaleMode = 'No Data Scaling Off'
inlet_0p3foamDisplay.ScaleFactor = 0.015999999642372132
inlet_0p3foamDisplay.SelectScaleArray = 'None'
inlet_0p3foamDisplay.GlyphType = 'Arrow'
inlet_0p3foamDisplay.UseGlyphTable = 0
inlet_0p3foamDisplay.GlyphTableIndexArray = 'None'
inlet_0p3foamDisplay.UseCompositeGlyphTable = 0
inlet_0p3foamDisplay.UseGlyphCullingAndLOD = 0
inlet_0p3foamDisplay.LODValues = []
inlet_0p3foamDisplay.ColorByLODIndex = 0
inlet_0p3foamDisplay.GaussianRadius = 0.0007999999821186066
inlet_0p3foamDisplay.ShaderPreset = 'Sphere'
inlet_0p3foamDisplay.CustomTriangleScale = 3
inlet_0p3foamDisplay.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
inlet_0p3foamDisplay.Emissive = 0
inlet_0p3foamDisplay.ScaleByArray = 0
inlet_0p3foamDisplay.SetScaleArray = ['POINTS', 'nu_mean']
inlet_0p3foamDisplay.ScaleArrayComponent = ''
inlet_0p3foamDisplay.UseScaleFunction = 1
inlet_0p3foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
inlet_0p3foamDisplay.OpacityByArray = 0
inlet_0p3foamDisplay.OpacityArray = ['POINTS', 'nu_mean']
inlet_0p3foamDisplay.OpacityArrayComponent = ''
inlet_0p3foamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
inlet_0p3foamDisplay.DataAxesGrid = 'GridAxesRepresentation'
inlet_0p3foamDisplay.SelectionCellLabelBold = 0
inlet_0p3foamDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
inlet_0p3foamDisplay.SelectionCellLabelFontFamily = 'Arial'
inlet_0p3foamDisplay.SelectionCellLabelFontFile = ''
inlet_0p3foamDisplay.SelectionCellLabelFontSize = 18
inlet_0p3foamDisplay.SelectionCellLabelItalic = 0
inlet_0p3foamDisplay.SelectionCellLabelJustification = 'Left'
inlet_0p3foamDisplay.SelectionCellLabelOpacity = 1.0
inlet_0p3foamDisplay.SelectionCellLabelShadow = 0
inlet_0p3foamDisplay.SelectionPointLabelBold = 0
inlet_0p3foamDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
inlet_0p3foamDisplay.SelectionPointLabelFontFamily = 'Arial'
inlet_0p3foamDisplay.SelectionPointLabelFontFile = ''
inlet_0p3foamDisplay.SelectionPointLabelFontSize = 18
inlet_0p3foamDisplay.SelectionPointLabelItalic = 0
inlet_0p3foamDisplay.SelectionPointLabelJustification = 'Left'
inlet_0p3foamDisplay.SelectionPointLabelOpacity = 1.0
inlet_0p3foamDisplay.SelectionPointLabelShadow = 0
inlet_0p3foamDisplay.PolarAxes = 'PolarAxesRepresentation'
inlet_0p3foamDisplay.ScalarOpacityFunction = None
inlet_0p3foamDisplay.ScalarOpacityUnitDistance = 0.0006064726018038802
inlet_0p3foamDisplay.SelectMapper = 'Projected tetra'
inlet_0p3foamDisplay.SamplingDimensions = [128, 128, 128]
inlet_0p3foamDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
inlet_0p3foamDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
inlet_0p3foamDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
inlet_0p3foamDisplay.GlyphType.TipResolution = 6
inlet_0p3foamDisplay.GlyphType.TipRadius = 0.1
inlet_0p3foamDisplay.GlyphType.TipLength = 0.35
inlet_0p3foamDisplay.GlyphType.ShaftResolution = 6
inlet_0p3foamDisplay.GlyphType.ShaftRadius = 0.03
inlet_0p3foamDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
inlet_0p3foamDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
inlet_0p3foamDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
inlet_0p3foamDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
inlet_0p3foamDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
inlet_0p3foamDisplay.DataAxesGrid.XTitle = 'X Axis'
inlet_0p3foamDisplay.DataAxesGrid.YTitle = 'Y Axis'
inlet_0p3foamDisplay.DataAxesGrid.ZTitle = 'Z Axis'
inlet_0p3foamDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
inlet_0p3foamDisplay.DataAxesGrid.XTitleFontFile = ''
inlet_0p3foamDisplay.DataAxesGrid.XTitleBold = 0
inlet_0p3foamDisplay.DataAxesGrid.XTitleItalic = 0
inlet_0p3foamDisplay.DataAxesGrid.XTitleFontSize = 12
inlet_0p3foamDisplay.DataAxesGrid.XTitleShadow = 0
inlet_0p3foamDisplay.DataAxesGrid.XTitleOpacity = 1.0
inlet_0p3foamDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
inlet_0p3foamDisplay.DataAxesGrid.YTitleFontFile = ''
inlet_0p3foamDisplay.DataAxesGrid.YTitleBold = 0
inlet_0p3foamDisplay.DataAxesGrid.YTitleItalic = 0
inlet_0p3foamDisplay.DataAxesGrid.YTitleFontSize = 12
inlet_0p3foamDisplay.DataAxesGrid.YTitleShadow = 0
inlet_0p3foamDisplay.DataAxesGrid.YTitleOpacity = 1.0
inlet_0p3foamDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
inlet_0p3foamDisplay.DataAxesGrid.ZTitleFontFile = ''
inlet_0p3foamDisplay.DataAxesGrid.ZTitleBold = 0
inlet_0p3foamDisplay.DataAxesGrid.ZTitleItalic = 0
inlet_0p3foamDisplay.DataAxesGrid.ZTitleFontSize = 12
inlet_0p3foamDisplay.DataAxesGrid.ZTitleShadow = 0
inlet_0p3foamDisplay.DataAxesGrid.ZTitleOpacity = 1.0
inlet_0p3foamDisplay.DataAxesGrid.FacesToRender = 63
inlet_0p3foamDisplay.DataAxesGrid.CullBackface = 0
inlet_0p3foamDisplay.DataAxesGrid.CullFrontface = 1
inlet_0p3foamDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.DataAxesGrid.ShowGrid = 0
inlet_0p3foamDisplay.DataAxesGrid.ShowEdges = 1
inlet_0p3foamDisplay.DataAxesGrid.ShowTicks = 1
inlet_0p3foamDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
inlet_0p3foamDisplay.DataAxesGrid.AxesToLabel = 63
inlet_0p3foamDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
inlet_0p3foamDisplay.DataAxesGrid.XLabelFontFile = ''
inlet_0p3foamDisplay.DataAxesGrid.XLabelBold = 0
inlet_0p3foamDisplay.DataAxesGrid.XLabelItalic = 0
inlet_0p3foamDisplay.DataAxesGrid.XLabelFontSize = 12
inlet_0p3foamDisplay.DataAxesGrid.XLabelShadow = 0
inlet_0p3foamDisplay.DataAxesGrid.XLabelOpacity = 1.0
inlet_0p3foamDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
inlet_0p3foamDisplay.DataAxesGrid.YLabelFontFile = ''
inlet_0p3foamDisplay.DataAxesGrid.YLabelBold = 0
inlet_0p3foamDisplay.DataAxesGrid.YLabelItalic = 0
inlet_0p3foamDisplay.DataAxesGrid.YLabelFontSize = 12
inlet_0p3foamDisplay.DataAxesGrid.YLabelShadow = 0
inlet_0p3foamDisplay.DataAxesGrid.YLabelOpacity = 1.0
inlet_0p3foamDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
inlet_0p3foamDisplay.DataAxesGrid.ZLabelFontFile = ''
inlet_0p3foamDisplay.DataAxesGrid.ZLabelBold = 0
inlet_0p3foamDisplay.DataAxesGrid.ZLabelItalic = 0
inlet_0p3foamDisplay.DataAxesGrid.ZLabelFontSize = 12
inlet_0p3foamDisplay.DataAxesGrid.ZLabelShadow = 0
inlet_0p3foamDisplay.DataAxesGrid.ZLabelOpacity = 1.0
inlet_0p3foamDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
inlet_0p3foamDisplay.DataAxesGrid.XAxisPrecision = 2
inlet_0p3foamDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
inlet_0p3foamDisplay.DataAxesGrid.XAxisLabels = []
inlet_0p3foamDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
inlet_0p3foamDisplay.DataAxesGrid.YAxisPrecision = 2
inlet_0p3foamDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
inlet_0p3foamDisplay.DataAxesGrid.YAxisLabels = []
inlet_0p3foamDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
inlet_0p3foamDisplay.DataAxesGrid.ZAxisPrecision = 2
inlet_0p3foamDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
inlet_0p3foamDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
inlet_0p3foamDisplay.PolarAxes.Visibility = 0
inlet_0p3foamDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
inlet_0p3foamDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
inlet_0p3foamDisplay.PolarAxes.EnableCustomRange = 0
inlet_0p3foamDisplay.PolarAxes.CustomRange = [0.0, 1.0]
inlet_0p3foamDisplay.PolarAxes.PolarAxisVisibility = 1
inlet_0p3foamDisplay.PolarAxes.RadialAxesVisibility = 1
inlet_0p3foamDisplay.PolarAxes.DrawRadialGridlines = 1
inlet_0p3foamDisplay.PolarAxes.PolarArcsVisibility = 1
inlet_0p3foamDisplay.PolarAxes.DrawPolarArcsGridlines = 1
inlet_0p3foamDisplay.PolarAxes.NumberOfRadialAxes = 0
inlet_0p3foamDisplay.PolarAxes.AutoSubdividePolarAxis = 1
inlet_0p3foamDisplay.PolarAxes.NumberOfPolarAxis = 0
inlet_0p3foamDisplay.PolarAxes.MinimumRadius = 0.0
inlet_0p3foamDisplay.PolarAxes.MinimumAngle = 0.0
inlet_0p3foamDisplay.PolarAxes.MaximumAngle = 90.0
inlet_0p3foamDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
inlet_0p3foamDisplay.PolarAxes.Ratio = 1.0
inlet_0p3foamDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleVisibility = 1
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
inlet_0p3foamDisplay.PolarAxes.PolarLabelVisibility = 1
inlet_0p3foamDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
inlet_0p3foamDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
inlet_0p3foamDisplay.PolarAxes.RadialLabelVisibility = 1
inlet_0p3foamDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
inlet_0p3foamDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
inlet_0p3foamDisplay.PolarAxes.RadialUnitsVisibility = 1
inlet_0p3foamDisplay.PolarAxes.ScreenSize = 10.0
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleBold = 0
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleItalic = 0
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleShadow = 0
inlet_0p3foamDisplay.PolarAxes.PolarAxisTitleFontSize = 12
inlet_0p3foamDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
inlet_0p3foamDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
inlet_0p3foamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
inlet_0p3foamDisplay.PolarAxes.PolarAxisLabelBold = 0
inlet_0p3foamDisplay.PolarAxes.PolarAxisLabelItalic = 0
inlet_0p3foamDisplay.PolarAxes.PolarAxisLabelShadow = 0
inlet_0p3foamDisplay.PolarAxes.PolarAxisLabelFontSize = 12
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTextBold = 0
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTextItalic = 0
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTextShadow = 0
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
inlet_0p3foamDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
inlet_0p3foamDisplay.PolarAxes.EnableDistanceLOD = 1
inlet_0p3foamDisplay.PolarAxes.DistanceLODThreshold = 0.7
inlet_0p3foamDisplay.PolarAxes.EnableViewAngleLOD = 1
inlet_0p3foamDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
inlet_0p3foamDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
inlet_0p3foamDisplay.PolarAxes.PolarTicksVisibility = 1
inlet_0p3foamDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
inlet_0p3foamDisplay.PolarAxes.TickLocation = 'Both'
inlet_0p3foamDisplay.PolarAxes.AxisTickVisibility = 1
inlet_0p3foamDisplay.PolarAxes.AxisMinorTickVisibility = 0
inlet_0p3foamDisplay.PolarAxes.ArcTickVisibility = 1
inlet_0p3foamDisplay.PolarAxes.ArcMinorTickVisibility = 0
inlet_0p3foamDisplay.PolarAxes.DeltaAngleMajor = 10.0
inlet_0p3foamDisplay.PolarAxes.DeltaAngleMinor = 5.0
inlet_0p3foamDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
inlet_0p3foamDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
inlet_0p3foamDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
inlet_0p3foamDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
inlet_0p3foamDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
inlet_0p3foamDisplay.PolarAxes.ArcMajorTickSize = 0.0
inlet_0p3foamDisplay.PolarAxes.ArcTickRatioSize = 0.3
inlet_0p3foamDisplay.PolarAxes.ArcMajorTickThickness = 1.0
inlet_0p3foamDisplay.PolarAxes.ArcTickRatioThickness = 0.5
inlet_0p3foamDisplay.PolarAxes.Use2DMode = 0
inlet_0p3foamDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=inlet_0p3foam)
slice1.SliceType = 'Plane'
slice1.Crinkleslice = 0
slice1.Triangulatetheslice = 1
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.0, -0.037999999010935426, 0.0]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]
slice1.SliceType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.0041, -0.037999999010935426, 0.0]

# Properties modified on slice1
slice1.Triangulatetheslice = 0

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [xPositionInSlice, -0.037999999010935426, 0.0]

# show data in view
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.AmbientColor = [1.0, 1.0, 1.0]
slice1Display.ColorArrayName = [None, '']
slice1Display.DiffuseColor = [1.0, 1.0, 1.0]
slice1Display.LookupTable = None
slice1Display.MapScalars = 1
slice1Display.MultiComponentsMapping = 0
slice1Display.InterpolateScalarsBeforeMapping = 1
slice1Display.Opacity = 1.0
slice1Display.PointSize = 2.0
slice1Display.LineWidth = 1.0
slice1Display.RenderLinesAsTubes = 0
slice1Display.RenderPointsAsSpheres = 0
slice1Display.Interpolation = 'Gouraud'
slice1Display.Specular = 0.0
slice1Display.SpecularColor = [1.0, 1.0, 1.0]
slice1Display.SpecularPower = 100.0
slice1Display.Luminosity = 0.0
slice1Display.Ambient = 0.0
slice1Display.Diffuse = 1.0
slice1Display.EdgeColor = [0.0, 0.0, 0.5]
slice1Display.BackfaceRepresentation = 'Follow Frontface'
slice1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
slice1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
slice1Display.BackfaceOpacity = 1.0
slice1Display.Position = [0.0, 0.0, 0.0]
slice1Display.Scale = [1.0, 1.0, 1.0]
slice1Display.Orientation = [0.0, 0.0, 0.0]
slice1Display.Origin = [0.0, 0.0, 0.0]
slice1Display.Pickable = 1
slice1Display.Texture = None
slice1Display.Triangulate = 0
slice1Display.UseShaderReplacements = 0
slice1Display.ShaderReplacements = ''
slice1Display.NonlinearSubdivisionLevel = 1
slice1Display.UseDataPartitions = 0
slice1Display.OSPRayUseScaleArray = 0
slice1Display.OSPRayScaleArray = 'nu_mean'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.OSPRayMaterial = 'None'
slice1Display.Orient = 0
slice1Display.OrientationMode = 'Direction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.Scaling = 0
slice1Display.ScaleMode = 'No Data Scaling Off'
slice1Display.ScaleFactor = 0.000800000037997961
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.UseGlyphTable = 0
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.UseCompositeGlyphTable = 0
slice1Display.UseGlyphCullingAndLOD = 0
slice1Display.LODValues = []
slice1Display.ColorByLODIndex = 0
slice1Display.GaussianRadius = 4.0000001899898055e-05
slice1Display.ShaderPreset = 'Sphere'
slice1Display.CustomTriangleScale = 3
slice1Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
slice1Display.Emissive = 0
slice1Display.ScaleByArray = 0
slice1Display.SetScaleArray = ['POINTS', 'nu_mean']
slice1Display.ScaleArrayComponent = ''
slice1Display.UseScaleFunction = 1
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityByArray = 0
slice1Display.OpacityArray = ['POINTS', 'nu_mean']
slice1Display.OpacityArrayComponent = ''
slice1Display.OpacityTransferFunction = 'PiecewiseFunction'
slice1Display.DataAxesGrid = 'GridAxesRepresentation'
slice1Display.SelectionCellLabelBold = 0
slice1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
slice1Display.SelectionCellLabelFontFamily = 'Arial'
slice1Display.SelectionCellLabelFontFile = ''
slice1Display.SelectionCellLabelFontSize = 18
slice1Display.SelectionCellLabelItalic = 0
slice1Display.SelectionCellLabelJustification = 'Left'
slice1Display.SelectionCellLabelOpacity = 1.0
slice1Display.SelectionCellLabelShadow = 0
slice1Display.SelectionPointLabelBold = 0
slice1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
slice1Display.SelectionPointLabelFontFamily = 'Arial'
slice1Display.SelectionPointLabelFontFile = ''
slice1Display.SelectionPointLabelFontSize = 18
slice1Display.SelectionPointLabelItalic = 0
slice1Display.SelectionPointLabelJustification = 'Left'
slice1Display.SelectionPointLabelOpacity = 1.0
slice1Display.SelectionPointLabelShadow = 0
slice1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
slice1Display.GlyphType.TipResolution = 6
slice1Display.GlyphType.TipRadius = 0.1
slice1Display.GlyphType.TipLength = 0.35
slice1Display.GlyphType.ShaftResolution = 6
slice1Display.GlyphType.ShaftRadius = 0.03
slice1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice1Display.DataAxesGrid.XTitle = 'X Axis'
slice1Display.DataAxesGrid.YTitle = 'Y Axis'
slice1Display.DataAxesGrid.ZTitle = 'Z Axis'
slice1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.XTitleFontFile = ''
slice1Display.DataAxesGrid.XTitleBold = 0
slice1Display.DataAxesGrid.XTitleItalic = 0
slice1Display.DataAxesGrid.XTitleFontSize = 12
slice1Display.DataAxesGrid.XTitleShadow = 0
slice1Display.DataAxesGrid.XTitleOpacity = 1.0
slice1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.YTitleFontFile = ''
slice1Display.DataAxesGrid.YTitleBold = 0
slice1Display.DataAxesGrid.YTitleItalic = 0
slice1Display.DataAxesGrid.YTitleFontSize = 12
slice1Display.DataAxesGrid.YTitleShadow = 0
slice1Display.DataAxesGrid.YTitleOpacity = 1.0
slice1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
slice1Display.DataAxesGrid.ZTitleFontFile = ''
slice1Display.DataAxesGrid.ZTitleBold = 0
slice1Display.DataAxesGrid.ZTitleItalic = 0
slice1Display.DataAxesGrid.ZTitleFontSize = 12
slice1Display.DataAxesGrid.ZTitleShadow = 0
slice1Display.DataAxesGrid.ZTitleOpacity = 1.0
slice1Display.DataAxesGrid.FacesToRender = 63
slice1Display.DataAxesGrid.CullBackface = 0
slice1Display.DataAxesGrid.CullFrontface = 1
slice1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
slice1Display.DataAxesGrid.ShowGrid = 0
slice1Display.DataAxesGrid.ShowEdges = 1
slice1Display.DataAxesGrid.ShowTicks = 1
slice1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
slice1Display.DataAxesGrid.AxesToLabel = 63
slice1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.XLabelFontFile = ''
slice1Display.DataAxesGrid.XLabelBold = 0
slice1Display.DataAxesGrid.XLabelItalic = 0
slice1Display.DataAxesGrid.XLabelFontSize = 12
slice1Display.DataAxesGrid.XLabelShadow = 0
slice1Display.DataAxesGrid.XLabelOpacity = 1.0
slice1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.YLabelFontFile = ''
slice1Display.DataAxesGrid.YLabelBold = 0
slice1Display.DataAxesGrid.YLabelItalic = 0
slice1Display.DataAxesGrid.YLabelFontSize = 12
slice1Display.DataAxesGrid.YLabelShadow = 0
slice1Display.DataAxesGrid.YLabelOpacity = 1.0
slice1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
slice1Display.DataAxesGrid.ZLabelFontFile = ''
slice1Display.DataAxesGrid.ZLabelBold = 0
slice1Display.DataAxesGrid.ZLabelItalic = 0
slice1Display.DataAxesGrid.ZLabelFontSize = 12
slice1Display.DataAxesGrid.ZLabelShadow = 0
slice1Display.DataAxesGrid.ZLabelOpacity = 1.0
slice1Display.DataAxesGrid.XAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.XAxisPrecision = 2
slice1Display.DataAxesGrid.XAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.XAxisLabels = []
slice1Display.DataAxesGrid.YAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.YAxisPrecision = 2
slice1Display.DataAxesGrid.YAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.YAxisLabels = []
slice1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
slice1Display.DataAxesGrid.ZAxisPrecision = 2
slice1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
slice1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice1Display.PolarAxes.Visibility = 0
slice1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
slice1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
slice1Display.PolarAxes.EnableCustomRange = 0
slice1Display.PolarAxes.CustomRange = [0.0, 1.0]
slice1Display.PolarAxes.PolarAxisVisibility = 1
slice1Display.PolarAxes.RadialAxesVisibility = 1
slice1Display.PolarAxes.DrawRadialGridlines = 1
slice1Display.PolarAxes.PolarArcsVisibility = 1
slice1Display.PolarAxes.DrawPolarArcsGridlines = 1
slice1Display.PolarAxes.NumberOfRadialAxes = 0
slice1Display.PolarAxes.AutoSubdividePolarAxis = 1
slice1Display.PolarAxes.NumberOfPolarAxis = 0
slice1Display.PolarAxes.MinimumRadius = 0.0
slice1Display.PolarAxes.MinimumAngle = 0.0
slice1Display.PolarAxes.MaximumAngle = 90.0
slice1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
slice1Display.PolarAxes.Ratio = 1.0
slice1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
slice1Display.PolarAxes.PolarAxisTitleVisibility = 1
slice1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
slice1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
slice1Display.PolarAxes.PolarLabelVisibility = 1
slice1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
slice1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
slice1Display.PolarAxes.RadialLabelVisibility = 1
slice1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
slice1Display.PolarAxes.RadialLabelLocation = 'Bottom'
slice1Display.PolarAxes.RadialUnitsVisibility = 1
slice1Display.PolarAxes.ScreenSize = 10.0
slice1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
slice1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
slice1Display.PolarAxes.PolarAxisTitleFontFile = ''
slice1Display.PolarAxes.PolarAxisTitleBold = 0
slice1Display.PolarAxes.PolarAxisTitleItalic = 0
slice1Display.PolarAxes.PolarAxisTitleShadow = 0
slice1Display.PolarAxes.PolarAxisTitleFontSize = 12
slice1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
slice1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
slice1Display.PolarAxes.PolarAxisLabelFontFile = ''
slice1Display.PolarAxes.PolarAxisLabelBold = 0
slice1Display.PolarAxes.PolarAxisLabelItalic = 0
slice1Display.PolarAxes.PolarAxisLabelShadow = 0
slice1Display.PolarAxes.PolarAxisLabelFontSize = 12
slice1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
slice1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
slice1Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice1Display.PolarAxes.LastRadialAxisTextBold = 0
slice1Display.PolarAxes.LastRadialAxisTextItalic = 0
slice1Display.PolarAxes.LastRadialAxisTextShadow = 0
slice1Display.PolarAxes.LastRadialAxisTextFontSize = 12
slice1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
slice1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
slice1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
slice1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
slice1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
slice1Display.PolarAxes.EnableDistanceLOD = 1
slice1Display.PolarAxes.DistanceLODThreshold = 0.7
slice1Display.PolarAxes.EnableViewAngleLOD = 1
slice1Display.PolarAxes.ViewAngleLODThreshold = 0.7
slice1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
slice1Display.PolarAxes.PolarTicksVisibility = 1
slice1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
slice1Display.PolarAxes.TickLocation = 'Both'
slice1Display.PolarAxes.AxisTickVisibility = 1
slice1Display.PolarAxes.AxisMinorTickVisibility = 0
slice1Display.PolarAxes.ArcTickVisibility = 1
slice1Display.PolarAxes.ArcMinorTickVisibility = 0
slice1Display.PolarAxes.DeltaAngleMajor = 10.0
slice1Display.PolarAxes.DeltaAngleMinor = 5.0
slice1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
slice1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
slice1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
slice1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
slice1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
slice1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
slice1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
slice1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
slice1Display.PolarAxes.ArcMajorTickSize = 0.0
slice1Display.PolarAxes.ArcTickRatioSize = 0.3
slice1Display.PolarAxes.ArcMajorTickThickness = 1.0
slice1Display.PolarAxes.ArcTickRatioThickness = 0.5
slice1Display.PolarAxes.Use2DMode = 0
slice1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(inlet_0p3foam, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'nu_mean'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'nu_mean'
nu_meanLUT = GetColorTransferFunction('nu_mean')
nu_meanLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
nu_meanLUT.InterpretValuesAsCategories = 0
nu_meanLUT.AnnotationsInitialized = 0
nu_meanLUT.ShowCategoricalColorsinDataRangeOnly = 0
nu_meanLUT.RescaleOnVisibilityChange = 0
nu_meanLUT.EnableOpacityMapping = 0
nu_meanLUT.RGBPoints = [2.5088913844228955e-06, 0.231373, 0.298039, 0.752941, 9.48039235026954e-06, 0.865003, 0.865003, 0.865003, 1.6451893316116184e-05, 0.705882, 0.0156863, 0.14902]
nu_meanLUT.UseLogScale = 0
nu_meanLUT.ColorSpace = 'Diverging'
nu_meanLUT.UseBelowRangeColor = 0
nu_meanLUT.BelowRangeColor = [0.0, 0.0, 0.0]
nu_meanLUT.UseAboveRangeColor = 0
nu_meanLUT.AboveRangeColor = [0.5, 0.5, 0.5]
nu_meanLUT.NanColor = [1.0, 1.0, 0.0]
nu_meanLUT.NanOpacity = 1.0
nu_meanLUT.Discretize = 1
nu_meanLUT.NumberOfTableValues = 256
nu_meanLUT.ScalarRangeInitialized = 1.0
nu_meanLUT.HSVWrap = 0
nu_meanLUT.VectorComponent = 0
nu_meanLUT.VectorMode = 'Magnitude'
nu_meanLUT.AllowDuplicateScalars = 1
nu_meanLUT.Annotations = []
nu_meanLUT.ActiveAnnotatedValues = []
nu_meanLUT.IndexedColors = []
nu_meanLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'nu_mean'
nu_meanPWF = GetOpacityTransferFunction('nu_mean')
nu_meanPWF.Points = [2.5088913844228955e-06, 0.0, 0.5, 0.0, 1.6451893316116184e-05, 1.0, 0.5, 0.0]
nu_meanPWF.AllowDuplicateScalars = 1
nu_meanPWF.UseLogScale = 0
nu_meanPWF.ScalarRangeInitialized = 1

# Rescale transfer function
nu_meanLUT.RescaleTransferFunction(2e-06, 0.0003)

# Rescale transfer function
nu_meanPWF.RescaleTransferFunction(2e-06, 0.0003)

# Apply a preset using its name. Note this may not work as expected when presets have duplicate names.
nu_meanLUT.ApplyPreset('Yellow - Gray - Blue', True)

# convert to log space
nu_meanLUT.MapControlPointsToLogSpace()

# Properties modified on nu_meanLUT
nu_meanLUT.UseLogScale = 1

# get color legend/bar for nu_meanLUT in view renderView1
nu_meanLUTColorBar = GetScalarBar(nu_meanLUT, renderView1)
nu_meanLUTColorBar.AutoOrient = 1
nu_meanLUTColorBar.Orientation = 'Vertical'
nu_meanLUTColorBar.WindowLocation = 'LowerRightCorner'
nu_meanLUTColorBar.Position = [0.89, 0.02]
nu_meanLUTColorBar.Title = 'nu_mean'
nu_meanLUTColorBar.ComponentTitle = ''
nu_meanLUTColorBar.TitleJustification = 'Centered'
nu_meanLUTColorBar.HorizontalTitle = 0
nu_meanLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
nu_meanLUTColorBar.TitleOpacity = 1.0
nu_meanLUTColorBar.TitleFontFamily = 'Arial'
nu_meanLUTColorBar.TitleFontFile = ''
nu_meanLUTColorBar.TitleBold = 0
nu_meanLUTColorBar.TitleItalic = 0
nu_meanLUTColorBar.TitleShadow = 0
nu_meanLUTColorBar.TitleFontSize = 16
nu_meanLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
nu_meanLUTColorBar.LabelOpacity = 1.0
nu_meanLUTColorBar.LabelFontFamily = 'Arial'
nu_meanLUTColorBar.LabelFontFile = ''
nu_meanLUTColorBar.LabelBold = 0
nu_meanLUTColorBar.LabelItalic = 0
nu_meanLUTColorBar.LabelShadow = 0
nu_meanLUTColorBar.LabelFontSize = 16
nu_meanLUTColorBar.AutomaticLabelFormat = 1
nu_meanLUTColorBar.LabelFormat = '%-#6.3g'
nu_meanLUTColorBar.DrawTickMarks = 1
nu_meanLUTColorBar.DrawTickLabels = 1
nu_meanLUTColorBar.UseCustomLabels = 0
nu_meanLUTColorBar.CustomLabels = []
nu_meanLUTColorBar.AddRangeLabels = 1
nu_meanLUTColorBar.RangeLabelFormat = '%-#6.1e'
nu_meanLUTColorBar.DrawAnnotations = 1
nu_meanLUTColorBar.AddRangeAnnotations = 0
nu_meanLUTColorBar.AutomaticAnnotations = 0
nu_meanLUTColorBar.DrawNanAnnotation = 0
nu_meanLUTColorBar.NanAnnotation = 'NaN'
nu_meanLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
nu_meanLUTColorBar.ReverseLegend = 0
nu_meanLUTColorBar.ScalarBarThickness = 16
nu_meanLUTColorBar.ScalarBarLength = 0.33

# change scalar bar placement
nu_meanLUTColorBar.Orientation = 'Horizontal'
nu_meanLUTColorBar.WindowLocation = 'AnyLocation'
nu_meanLUTColorBar.Position = [0.32953038674033164, 0.043525571273122954]
nu_meanLUTColorBar.ScalarBarLength = 0.33000000000000007

# reset view to fit data
renderView1.ResetCamera()

# Properties modified on t_meanLUTColorBar
nu_meanLUTColorBar.TitleFontSize = 4
nu_meanLUTColorBar.LabelFontSize = 4
nu_meanLUTColorBar.ScalarBarThickness = 5
nu_meanLUTColorBar.ScalarBarLength = 0.5

# current camera placement for renderView1
renderView1.CameraPosition = [-0.017756407478558053, 0.0, 0.0]
renderView1.CameraFocalPoint = [0.004100000020116568, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, 1.0, 2.220446049250313e-16]
renderView1.CameraParallelScale = 0.005656854518178539

# reset view to fit data
renderView1.ResetCamera()

# save screenshot
SaveScreenshot(dirName+'/nu_mean_slice_x_Eq_'+xPositionInSaveScreenShot+'.png', renderView1, ImageResolution=[2896, 1835],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

print "Finalizing nu_mean_slice_x-logScale.py " + "@ dir : " + dirName + " " + " @ " + xPositionInSaveScreenShot
import datetime
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print "==============================="
