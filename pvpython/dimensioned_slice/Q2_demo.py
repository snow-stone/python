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

# create a new 'OpenFOAMReader'
re4000foam = OpenFOAMReader(FileName=dirName+'/Re4000.foam')
re4000foam.SkipZeroTime = 1
re4000foam.CaseType = 'Reconstructed Case'
re4000foam.LabelSize = '32-bit'
re4000foam.ScalarSize = '64-bit (DP)'
re4000foam.Createcelltopointfiltereddata = 1
re4000foam.Adddimensionalunitstoarraynames = 0
re4000foam.MeshRegions = ['internalMesh']
re4000foam.CellArrays = ['Q', 'Q1', 'Q2', 'T', 'T_mean', 'U', 'U_mean', 'k_mean', 'k_mean_nonD', 'p', 'reyTensor', 'reyTensor_mean', 'strainRate_U', 'tt_mean', 'vorticity_U', 'vorticity_U_mean', 'yPlus_U', 'yPlus_U_mean']
re4000foam.PointArrays = []
re4000foam.LagrangianArrays = []
re4000foam.Cachemesh = 1
re4000foam.Decomposepolyhedra = 1
re4000foam.ListtimestepsaccordingtocontrolDict = 0
re4000foam.Lagrangianpositionswithoutextradata = 1
re4000foam.Readzones = 0
re4000foam.Copydatatocellzones = 0

# Properties modified on re4000foam
re4000foam.CellArrays = ['Q2', 'vorticity_U_mean']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1267, 919]

# show data in view
re4000foamDisplay = Show(re4000foam, renderView1)

# trace defaults for the display properties.
re4000foamDisplay.Representation = 'Surface'
re4000foamDisplay.AmbientColor = [1.0, 1.0, 1.0]
re4000foamDisplay.ColorArrayName = [None, '']
re4000foamDisplay.DiffuseColor = [1.0, 1.0, 1.0]
re4000foamDisplay.LookupTable = None
re4000foamDisplay.MapScalars = 1
re4000foamDisplay.MultiComponentsMapping = 0
re4000foamDisplay.InterpolateScalarsBeforeMapping = 1
re4000foamDisplay.Opacity = 1.0
re4000foamDisplay.PointSize = 2.0
re4000foamDisplay.LineWidth = 1.0
re4000foamDisplay.RenderLinesAsTubes = 0
re4000foamDisplay.RenderPointsAsSpheres = 0
re4000foamDisplay.Interpolation = 'Gouraud'
re4000foamDisplay.Specular = 0.0
re4000foamDisplay.SpecularColor = [1.0, 1.0, 1.0]
re4000foamDisplay.SpecularPower = 100.0
re4000foamDisplay.Luminosity = 0.0
re4000foamDisplay.Ambient = 0.0
re4000foamDisplay.Diffuse = 1.0
re4000foamDisplay.EdgeColor = [0.0, 0.0, 0.5]
re4000foamDisplay.BackfaceRepresentation = 'Follow Frontface'
re4000foamDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
re4000foamDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
re4000foamDisplay.BackfaceOpacity = 1.0
re4000foamDisplay.Position = [0.0, 0.0, 0.0]
re4000foamDisplay.Scale = [1.0, 1.0, 1.0]
re4000foamDisplay.Orientation = [0.0, 0.0, 0.0]
re4000foamDisplay.Origin = [0.0, 0.0, 0.0]
re4000foamDisplay.Pickable = 1
re4000foamDisplay.Texture = None
re4000foamDisplay.Triangulate = 0
re4000foamDisplay.UseShaderReplacements = 0
re4000foamDisplay.ShaderReplacements = ''
re4000foamDisplay.NonlinearSubdivisionLevel = 1
re4000foamDisplay.UseDataPartitions = 0
re4000foamDisplay.OSPRayUseScaleArray = 0
re4000foamDisplay.OSPRayScaleArray = 'Q2'
re4000foamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
re4000foamDisplay.OSPRayMaterial = 'None'
re4000foamDisplay.Orient = 0
re4000foamDisplay.OrientationMode = 'Direction'
re4000foamDisplay.SelectOrientationVectors = 'None'
re4000foamDisplay.Scaling = 0
re4000foamDisplay.ScaleMode = 'No Data Scaling Off'
re4000foamDisplay.ScaleFactor = 0.015999999642372132
re4000foamDisplay.SelectScaleArray = 'None'
re4000foamDisplay.GlyphType = 'Arrow'
re4000foamDisplay.UseGlyphTable = 0
re4000foamDisplay.GlyphTableIndexArray = 'None'
re4000foamDisplay.UseCompositeGlyphTable = 0
re4000foamDisplay.UseGlyphCullingAndLOD = 0
re4000foamDisplay.LODValues = []
re4000foamDisplay.ColorByLODIndex = 0
re4000foamDisplay.GaussianRadius = 0.0007999999821186066
re4000foamDisplay.ShaderPreset = 'Sphere'
re4000foamDisplay.CustomTriangleScale = 3
re4000foamDisplay.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
re4000foamDisplay.Emissive = 0
re4000foamDisplay.ScaleByArray = 0
re4000foamDisplay.SetScaleArray = ['POINTS', 'Q2']
re4000foamDisplay.ScaleArrayComponent = ''
re4000foamDisplay.UseScaleFunction = 1
re4000foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
re4000foamDisplay.OpacityByArray = 0
re4000foamDisplay.OpacityArray = ['POINTS', 'Q2']
re4000foamDisplay.OpacityArrayComponent = ''
re4000foamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
re4000foamDisplay.DataAxesGrid = 'GridAxesRepresentation'
re4000foamDisplay.SelectionCellLabelBold = 0
re4000foamDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
re4000foamDisplay.SelectionCellLabelFontFamily = 'Arial'
re4000foamDisplay.SelectionCellLabelFontFile = ''
re4000foamDisplay.SelectionCellLabelFontSize = 18
re4000foamDisplay.SelectionCellLabelItalic = 0
re4000foamDisplay.SelectionCellLabelJustification = 'Left'
re4000foamDisplay.SelectionCellLabelOpacity = 1.0
re4000foamDisplay.SelectionCellLabelShadow = 0
re4000foamDisplay.SelectionPointLabelBold = 0
re4000foamDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
re4000foamDisplay.SelectionPointLabelFontFamily = 'Arial'
re4000foamDisplay.SelectionPointLabelFontFile = ''
re4000foamDisplay.SelectionPointLabelFontSize = 18
re4000foamDisplay.SelectionPointLabelItalic = 0
re4000foamDisplay.SelectionPointLabelJustification = 'Left'
re4000foamDisplay.SelectionPointLabelOpacity = 1.0
re4000foamDisplay.SelectionPointLabelShadow = 0
re4000foamDisplay.PolarAxes = 'PolarAxesRepresentation'
re4000foamDisplay.ScalarOpacityFunction = None
re4000foamDisplay.ScalarOpacityUnitDistance = 0.0006064726018038802
re4000foamDisplay.SelectMapper = 'Projected tetra'
re4000foamDisplay.SamplingDimensions = [128, 128, 128]
re4000foamDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
re4000foamDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
re4000foamDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
re4000foamDisplay.GlyphType.TipResolution = 6
re4000foamDisplay.GlyphType.TipRadius = 0.1
re4000foamDisplay.GlyphType.TipLength = 0.35
re4000foamDisplay.GlyphType.ShaftResolution = 6
re4000foamDisplay.GlyphType.ShaftRadius = 0.03
re4000foamDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
re4000foamDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
re4000foamDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
re4000foamDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
re4000foamDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
re4000foamDisplay.DataAxesGrid.XTitle = 'X Axis'
re4000foamDisplay.DataAxesGrid.YTitle = 'Y Axis'
re4000foamDisplay.DataAxesGrid.ZTitle = 'Z Axis'
re4000foamDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
re4000foamDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
re4000foamDisplay.DataAxesGrid.XTitleFontFile = ''
re4000foamDisplay.DataAxesGrid.XTitleBold = 0
re4000foamDisplay.DataAxesGrid.XTitleItalic = 0
re4000foamDisplay.DataAxesGrid.XTitleFontSize = 12
re4000foamDisplay.DataAxesGrid.XTitleShadow = 0
re4000foamDisplay.DataAxesGrid.XTitleOpacity = 1.0
re4000foamDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
re4000foamDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
re4000foamDisplay.DataAxesGrid.YTitleFontFile = ''
re4000foamDisplay.DataAxesGrid.YTitleBold = 0
re4000foamDisplay.DataAxesGrid.YTitleItalic = 0
re4000foamDisplay.DataAxesGrid.YTitleFontSize = 12
re4000foamDisplay.DataAxesGrid.YTitleShadow = 0
re4000foamDisplay.DataAxesGrid.YTitleOpacity = 1.0
re4000foamDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
re4000foamDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
re4000foamDisplay.DataAxesGrid.ZTitleFontFile = ''
re4000foamDisplay.DataAxesGrid.ZTitleBold = 0
re4000foamDisplay.DataAxesGrid.ZTitleItalic = 0
re4000foamDisplay.DataAxesGrid.ZTitleFontSize = 12
re4000foamDisplay.DataAxesGrid.ZTitleShadow = 0
re4000foamDisplay.DataAxesGrid.ZTitleOpacity = 1.0
re4000foamDisplay.DataAxesGrid.FacesToRender = 63
re4000foamDisplay.DataAxesGrid.CullBackface = 0
re4000foamDisplay.DataAxesGrid.CullFrontface = 1
re4000foamDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
re4000foamDisplay.DataAxesGrid.ShowGrid = 0
re4000foamDisplay.DataAxesGrid.ShowEdges = 1
re4000foamDisplay.DataAxesGrid.ShowTicks = 1
re4000foamDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
re4000foamDisplay.DataAxesGrid.AxesToLabel = 63
re4000foamDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
re4000foamDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
re4000foamDisplay.DataAxesGrid.XLabelFontFile = ''
re4000foamDisplay.DataAxesGrid.XLabelBold = 0
re4000foamDisplay.DataAxesGrid.XLabelItalic = 0
re4000foamDisplay.DataAxesGrid.XLabelFontSize = 12
re4000foamDisplay.DataAxesGrid.XLabelShadow = 0
re4000foamDisplay.DataAxesGrid.XLabelOpacity = 1.0
re4000foamDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
re4000foamDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
re4000foamDisplay.DataAxesGrid.YLabelFontFile = ''
re4000foamDisplay.DataAxesGrid.YLabelBold = 0
re4000foamDisplay.DataAxesGrid.YLabelItalic = 0
re4000foamDisplay.DataAxesGrid.YLabelFontSize = 12
re4000foamDisplay.DataAxesGrid.YLabelShadow = 0
re4000foamDisplay.DataAxesGrid.YLabelOpacity = 1.0
re4000foamDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
re4000foamDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
re4000foamDisplay.DataAxesGrid.ZLabelFontFile = ''
re4000foamDisplay.DataAxesGrid.ZLabelBold = 0
re4000foamDisplay.DataAxesGrid.ZLabelItalic = 0
re4000foamDisplay.DataAxesGrid.ZLabelFontSize = 12
re4000foamDisplay.DataAxesGrid.ZLabelShadow = 0
re4000foamDisplay.DataAxesGrid.ZLabelOpacity = 1.0
re4000foamDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
re4000foamDisplay.DataAxesGrid.XAxisPrecision = 2
re4000foamDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
re4000foamDisplay.DataAxesGrid.XAxisLabels = []
re4000foamDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
re4000foamDisplay.DataAxesGrid.YAxisPrecision = 2
re4000foamDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
re4000foamDisplay.DataAxesGrid.YAxisLabels = []
re4000foamDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
re4000foamDisplay.DataAxesGrid.ZAxisPrecision = 2
re4000foamDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
re4000foamDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
re4000foamDisplay.PolarAxes.Visibility = 0
re4000foamDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
re4000foamDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
re4000foamDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
re4000foamDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
re4000foamDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
re4000foamDisplay.PolarAxes.EnableCustomRange = 0
re4000foamDisplay.PolarAxes.CustomRange = [0.0, 1.0]
re4000foamDisplay.PolarAxes.PolarAxisVisibility = 1
re4000foamDisplay.PolarAxes.RadialAxesVisibility = 1
re4000foamDisplay.PolarAxes.DrawRadialGridlines = 1
re4000foamDisplay.PolarAxes.PolarArcsVisibility = 1
re4000foamDisplay.PolarAxes.DrawPolarArcsGridlines = 1
re4000foamDisplay.PolarAxes.NumberOfRadialAxes = 0
re4000foamDisplay.PolarAxes.AutoSubdividePolarAxis = 1
re4000foamDisplay.PolarAxes.NumberOfPolarAxis = 0
re4000foamDisplay.PolarAxes.MinimumRadius = 0.0
re4000foamDisplay.PolarAxes.MinimumAngle = 0.0
re4000foamDisplay.PolarAxes.MaximumAngle = 90.0
re4000foamDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
re4000foamDisplay.PolarAxes.Ratio = 1.0
re4000foamDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
re4000foamDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
re4000foamDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
re4000foamDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
re4000foamDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
re4000foamDisplay.PolarAxes.PolarAxisTitleVisibility = 1
re4000foamDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
re4000foamDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
re4000foamDisplay.PolarAxes.PolarLabelVisibility = 1
re4000foamDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
re4000foamDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
re4000foamDisplay.PolarAxes.RadialLabelVisibility = 1
re4000foamDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
re4000foamDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
re4000foamDisplay.PolarAxes.RadialUnitsVisibility = 1
re4000foamDisplay.PolarAxes.ScreenSize = 10.0
re4000foamDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
re4000foamDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
re4000foamDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
re4000foamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
re4000foamDisplay.PolarAxes.PolarAxisTitleBold = 0
re4000foamDisplay.PolarAxes.PolarAxisTitleItalic = 0
re4000foamDisplay.PolarAxes.PolarAxisTitleShadow = 0
re4000foamDisplay.PolarAxes.PolarAxisTitleFontSize = 12
re4000foamDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
re4000foamDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
re4000foamDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
re4000foamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
re4000foamDisplay.PolarAxes.PolarAxisLabelBold = 0
re4000foamDisplay.PolarAxes.PolarAxisLabelItalic = 0
re4000foamDisplay.PolarAxes.PolarAxisLabelShadow = 0
re4000foamDisplay.PolarAxes.PolarAxisLabelFontSize = 12
re4000foamDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
re4000foamDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
re4000foamDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
re4000foamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
re4000foamDisplay.PolarAxes.LastRadialAxisTextBold = 0
re4000foamDisplay.PolarAxes.LastRadialAxisTextItalic = 0
re4000foamDisplay.PolarAxes.LastRadialAxisTextShadow = 0
re4000foamDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
re4000foamDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
re4000foamDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
re4000foamDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
re4000foamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
re4000foamDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
re4000foamDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
re4000foamDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
re4000foamDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
re4000foamDisplay.PolarAxes.EnableDistanceLOD = 1
re4000foamDisplay.PolarAxes.DistanceLODThreshold = 0.7
re4000foamDisplay.PolarAxes.EnableViewAngleLOD = 1
re4000foamDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
re4000foamDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
re4000foamDisplay.PolarAxes.PolarTicksVisibility = 1
re4000foamDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
re4000foamDisplay.PolarAxes.TickLocation = 'Both'
re4000foamDisplay.PolarAxes.AxisTickVisibility = 1
re4000foamDisplay.PolarAxes.AxisMinorTickVisibility = 0
re4000foamDisplay.PolarAxes.ArcTickVisibility = 1
re4000foamDisplay.PolarAxes.ArcMinorTickVisibility = 0
re4000foamDisplay.PolarAxes.DeltaAngleMajor = 10.0
re4000foamDisplay.PolarAxes.DeltaAngleMinor = 5.0
re4000foamDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
re4000foamDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
re4000foamDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
re4000foamDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
re4000foamDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
re4000foamDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
re4000foamDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
re4000foamDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
re4000foamDisplay.PolarAxes.ArcMajorTickSize = 0.0
re4000foamDisplay.PolarAxes.ArcTickRatioSize = 0.3
re4000foamDisplay.PolarAxes.ArcMajorTickThickness = 1.0
re4000foamDisplay.PolarAxes.ArcTickRatioThickness = 0.5
re4000foamDisplay.PolarAxes.Use2DMode = 0
re4000foamDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Contour'
contour1 = Contour(Input=re4000foam)
contour1.ContourBy = ['POINTS', 'Q2']
contour1.ComputeNormals = 1
contour1.ComputeGradients = 0
contour1.ComputeScalars = 0
contour1.OutputPointsPrecision = 'Same as input'
contour1.GenerateTriangles = 1
contour1.Isosurfaces = [-0.0016052722930908203]
contour1.PointMergeMethod = 'Uniform Binning'

# init the 'Uniform Binning' selected for 'PointMergeMethod'
contour1.PointMergeMethod.Divisions = [50, 50, 50]
contour1.PointMergeMethod.Numberofpointsperbucket = 8

# Properties modified on contour1
contour1.Isosurfaces = [0.3]

# show data in view
contour1Display = Show(contour1, renderView1)

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'
contour1Display.AmbientColor = [1.0, 1.0, 1.0]
contour1Display.ColorArrayName = [None, '']
contour1Display.DiffuseColor = [1.0, 1.0, 1.0]
contour1Display.LookupTable = None
contour1Display.MapScalars = 1
contour1Display.MultiComponentsMapping = 0
contour1Display.InterpolateScalarsBeforeMapping = 1
contour1Display.Opacity = 1.0
contour1Display.PointSize = 2.0
contour1Display.LineWidth = 1.0
contour1Display.RenderLinesAsTubes = 0
contour1Display.RenderPointsAsSpheres = 0
contour1Display.Interpolation = 'Gouraud'
contour1Display.Specular = 0.0
contour1Display.SpecularColor = [1.0, 1.0, 1.0]
contour1Display.SpecularPower = 100.0
contour1Display.Luminosity = 0.0
contour1Display.Ambient = 0.0
contour1Display.Diffuse = 1.0
contour1Display.EdgeColor = [0.0, 0.0, 0.5]
contour1Display.BackfaceRepresentation = 'Follow Frontface'
contour1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
contour1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
contour1Display.BackfaceOpacity = 1.0
contour1Display.Position = [0.0, 0.0, 0.0]
contour1Display.Scale = [1.0, 1.0, 1.0]
contour1Display.Orientation = [0.0, 0.0, 0.0]
contour1Display.Origin = [0.0, 0.0, 0.0]
contour1Display.Pickable = 1
contour1Display.Texture = None
contour1Display.Triangulate = 0
contour1Display.UseShaderReplacements = 0
contour1Display.ShaderReplacements = ''
contour1Display.NonlinearSubdivisionLevel = 1
contour1Display.UseDataPartitions = 0
contour1Display.OSPRayUseScaleArray = 0
contour1Display.OSPRayScaleArray = 'Normals'
contour1Display.OSPRayScaleFunction = 'PiecewiseFunction'
contour1Display.OSPRayMaterial = 'None'
contour1Display.Orient = 0
contour1Display.OrientationMode = 'Direction'
contour1Display.SelectOrientationVectors = 'None'
contour1Display.Scaling = 0
contour1Display.ScaleMode = 'No Data Scaling Off'
contour1Display.ScaleFactor = 0.008729085745289923
contour1Display.SelectScaleArray = 'None'
contour1Display.GlyphType = 'Arrow'
contour1Display.UseGlyphTable = 0
contour1Display.GlyphTableIndexArray = 'None'
contour1Display.UseCompositeGlyphTable = 0
contour1Display.UseGlyphCullingAndLOD = 0
contour1Display.LODValues = []
contour1Display.ColorByLODIndex = 0
contour1Display.GaussianRadius = 0.0004364542872644961
contour1Display.ShaderPreset = 'Sphere'
contour1Display.CustomTriangleScale = 3
contour1Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
contour1Display.Emissive = 0
contour1Display.ScaleByArray = 0
contour1Display.SetScaleArray = ['POINTS', 'Normals']
contour1Display.ScaleArrayComponent = 'X'
contour1Display.UseScaleFunction = 1
contour1Display.ScaleTransferFunction = 'PiecewiseFunction'
contour1Display.OpacityByArray = 0
contour1Display.OpacityArray = ['POINTS', 'Normals']
contour1Display.OpacityArrayComponent = 'X'
contour1Display.OpacityTransferFunction = 'PiecewiseFunction'
contour1Display.DataAxesGrid = 'GridAxesRepresentation'
contour1Display.SelectionCellLabelBold = 0
contour1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
contour1Display.SelectionCellLabelFontFamily = 'Arial'
contour1Display.SelectionCellLabelFontFile = ''
contour1Display.SelectionCellLabelFontSize = 18
contour1Display.SelectionCellLabelItalic = 0
contour1Display.SelectionCellLabelJustification = 'Left'
contour1Display.SelectionCellLabelOpacity = 1.0
contour1Display.SelectionCellLabelShadow = 0
contour1Display.SelectionPointLabelBold = 0
contour1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
contour1Display.SelectionPointLabelFontFamily = 'Arial'
contour1Display.SelectionPointLabelFontFile = ''
contour1Display.SelectionPointLabelFontSize = 18
contour1Display.SelectionPointLabelItalic = 0
contour1Display.SelectionPointLabelJustification = 'Left'
contour1Display.SelectionPointLabelOpacity = 1.0
contour1Display.SelectionPointLabelShadow = 0
contour1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
contour1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
contour1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
contour1Display.GlyphType.TipResolution = 6
contour1Display.GlyphType.TipRadius = 0.1
contour1Display.GlyphType.TipLength = 0.35
contour1Display.GlyphType.ShaftResolution = 6
contour1Display.GlyphType.ShaftRadius = 0.03
contour1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
contour1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
contour1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
contour1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
contour1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
contour1Display.DataAxesGrid.XTitle = 'X Axis'
contour1Display.DataAxesGrid.YTitle = 'Y Axis'
contour1Display.DataAxesGrid.ZTitle = 'Z Axis'
contour1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.XTitleFontFile = ''
contour1Display.DataAxesGrid.XTitleBold = 0
contour1Display.DataAxesGrid.XTitleItalic = 0
contour1Display.DataAxesGrid.XTitleFontSize = 12
contour1Display.DataAxesGrid.XTitleShadow = 0
contour1Display.DataAxesGrid.XTitleOpacity = 1.0
contour1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.YTitleFontFile = ''
contour1Display.DataAxesGrid.YTitleBold = 0
contour1Display.DataAxesGrid.YTitleItalic = 0
contour1Display.DataAxesGrid.YTitleFontSize = 12
contour1Display.DataAxesGrid.YTitleShadow = 0
contour1Display.DataAxesGrid.YTitleOpacity = 1.0
contour1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
contour1Display.DataAxesGrid.ZTitleFontFile = ''
contour1Display.DataAxesGrid.ZTitleBold = 0
contour1Display.DataAxesGrid.ZTitleItalic = 0
contour1Display.DataAxesGrid.ZTitleFontSize = 12
contour1Display.DataAxesGrid.ZTitleShadow = 0
contour1Display.DataAxesGrid.ZTitleOpacity = 1.0
contour1Display.DataAxesGrid.FacesToRender = 63
contour1Display.DataAxesGrid.CullBackface = 0
contour1Display.DataAxesGrid.CullFrontface = 1
contour1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
contour1Display.DataAxesGrid.ShowGrid = 0
contour1Display.DataAxesGrid.ShowEdges = 1
contour1Display.DataAxesGrid.ShowTicks = 1
contour1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
contour1Display.DataAxesGrid.AxesToLabel = 63
contour1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.XLabelFontFile = ''
contour1Display.DataAxesGrid.XLabelBold = 0
contour1Display.DataAxesGrid.XLabelItalic = 0
contour1Display.DataAxesGrid.XLabelFontSize = 12
contour1Display.DataAxesGrid.XLabelShadow = 0
contour1Display.DataAxesGrid.XLabelOpacity = 1.0
contour1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.YLabelFontFile = ''
contour1Display.DataAxesGrid.YLabelBold = 0
contour1Display.DataAxesGrid.YLabelItalic = 0
contour1Display.DataAxesGrid.YLabelFontSize = 12
contour1Display.DataAxesGrid.YLabelShadow = 0
contour1Display.DataAxesGrid.YLabelOpacity = 1.0
contour1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
contour1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
contour1Display.DataAxesGrid.ZLabelFontFile = ''
contour1Display.DataAxesGrid.ZLabelBold = 0
contour1Display.DataAxesGrid.ZLabelItalic = 0
contour1Display.DataAxesGrid.ZLabelFontSize = 12
contour1Display.DataAxesGrid.ZLabelShadow = 0
contour1Display.DataAxesGrid.ZLabelOpacity = 1.0
contour1Display.DataAxesGrid.XAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.XAxisPrecision = 2
contour1Display.DataAxesGrid.XAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.XAxisLabels = []
contour1Display.DataAxesGrid.YAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.YAxisPrecision = 2
contour1Display.DataAxesGrid.YAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.YAxisLabels = []
contour1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
contour1Display.DataAxesGrid.ZAxisPrecision = 2
contour1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
contour1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
contour1Display.PolarAxes.Visibility = 0
contour1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
contour1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
contour1Display.PolarAxes.EnableCustomRange = 0
contour1Display.PolarAxes.CustomRange = [0.0, 1.0]
contour1Display.PolarAxes.PolarAxisVisibility = 1
contour1Display.PolarAxes.RadialAxesVisibility = 1
contour1Display.PolarAxes.DrawRadialGridlines = 1
contour1Display.PolarAxes.PolarArcsVisibility = 1
contour1Display.PolarAxes.DrawPolarArcsGridlines = 1
contour1Display.PolarAxes.NumberOfRadialAxes = 0
contour1Display.PolarAxes.AutoSubdividePolarAxis = 1
contour1Display.PolarAxes.NumberOfPolarAxis = 0
contour1Display.PolarAxes.MinimumRadius = 0.0
contour1Display.PolarAxes.MinimumAngle = 0.0
contour1Display.PolarAxes.MaximumAngle = 90.0
contour1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
contour1Display.PolarAxes.Ratio = 1.0
contour1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
contour1Display.PolarAxes.PolarAxisTitleVisibility = 1
contour1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
contour1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
contour1Display.PolarAxes.PolarLabelVisibility = 1
contour1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
contour1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
contour1Display.PolarAxes.RadialLabelVisibility = 1
contour1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
contour1Display.PolarAxes.RadialLabelLocation = 'Bottom'
contour1Display.PolarAxes.RadialUnitsVisibility = 1
contour1Display.PolarAxes.ScreenSize = 10.0
contour1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
contour1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
contour1Display.PolarAxes.PolarAxisTitleFontFile = ''
contour1Display.PolarAxes.PolarAxisTitleBold = 0
contour1Display.PolarAxes.PolarAxisTitleItalic = 0
contour1Display.PolarAxes.PolarAxisTitleShadow = 0
contour1Display.PolarAxes.PolarAxisTitleFontSize = 12
contour1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
contour1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
contour1Display.PolarAxes.PolarAxisLabelFontFile = ''
contour1Display.PolarAxes.PolarAxisLabelBold = 0
contour1Display.PolarAxes.PolarAxisLabelItalic = 0
contour1Display.PolarAxes.PolarAxisLabelShadow = 0
contour1Display.PolarAxes.PolarAxisLabelFontSize = 12
contour1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
contour1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
contour1Display.PolarAxes.LastRadialAxisTextFontFile = ''
contour1Display.PolarAxes.LastRadialAxisTextBold = 0
contour1Display.PolarAxes.LastRadialAxisTextItalic = 0
contour1Display.PolarAxes.LastRadialAxisTextShadow = 0
contour1Display.PolarAxes.LastRadialAxisTextFontSize = 12
contour1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
contour1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
contour1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
contour1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
contour1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
contour1Display.PolarAxes.EnableDistanceLOD = 1
contour1Display.PolarAxes.DistanceLODThreshold = 0.7
contour1Display.PolarAxes.EnableViewAngleLOD = 1
contour1Display.PolarAxes.ViewAngleLODThreshold = 0.7
contour1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
contour1Display.PolarAxes.PolarTicksVisibility = 1
contour1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
contour1Display.PolarAxes.TickLocation = 'Both'
contour1Display.PolarAxes.AxisTickVisibility = 1
contour1Display.PolarAxes.AxisMinorTickVisibility = 0
contour1Display.PolarAxes.ArcTickVisibility = 1
contour1Display.PolarAxes.ArcMinorTickVisibility = 0
contour1Display.PolarAxes.DeltaAngleMajor = 10.0
contour1Display.PolarAxes.DeltaAngleMinor = 5.0
contour1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
contour1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
contour1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
contour1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
contour1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
contour1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
contour1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
contour1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
contour1Display.PolarAxes.ArcMajorTickSize = 0.0
contour1Display.PolarAxes.ArcTickRatioSize = 0.3
contour1Display.PolarAxes.ArcMajorTickThickness = 1.0
contour1Display.PolarAxes.ArcTickRatioThickness = 0.5
contour1Display.PolarAxes.Use2DMode = 0
contour1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(re4000foam, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(re4000foam)

# change representation type
re4000foamDisplay.SetRepresentationType('Feature Edges')

# change solid color
re4000foamDisplay.DiffuseColor = [0.0, 0.0, 0.0]

# create a new 'OpenFOAMReader'
re4000foam_1 = OpenFOAMReader(FileName='/store/8simu_tmp/shape_square/2a_3_T/Newtonian/Re4000/Re4000.foam')
re4000foam_1.SkipZeroTime = 1
re4000foam_1.CaseType = 'Reconstructed Case'
re4000foam_1.LabelSize = '32-bit'
re4000foam_1.ScalarSize = '64-bit (DP)'
re4000foam_1.Createcelltopointfiltereddata = 1
re4000foam_1.Adddimensionalunitstoarraynames = 0
re4000foam_1.MeshRegions = ['internalMesh']
re4000foam_1.CellArrays = ['Q', 'Q1', 'Q2', 'T', 'T_mean', 'U', 'U_mean', 'k_mean', 'k_mean_nonD', 'p', 'reyTensor', 'reyTensor_mean', 'strainRate_U', 'tt_mean', 'vorticity_U', 'vorticity_U_mean', 'yPlus_U', 'yPlus_U_mean']
re4000foam_1.PointArrays = []
re4000foam_1.LagrangianArrays = []
re4000foam_1.Cachemesh = 1
re4000foam_1.Decomposepolyhedra = 1
re4000foam_1.ListtimestepsaccordingtocontrolDict = 0
re4000foam_1.Lagrangianpositionswithoutextradata = 1
re4000foam_1.Readzones = 0
re4000foam_1.Copydatatocellzones = 0

# Properties modified on re4000foam_1
re4000foam_1.MeshRegions = ['wall']
re4000foam_1.CellArrays = []

# show data in view
re4000foam_1Display = Show(re4000foam_1, renderView1)

# trace defaults for the display properties.
re4000foam_1Display.Representation = 'Surface'
re4000foam_1Display.AmbientColor = [1.0, 1.0, 1.0]
re4000foam_1Display.ColorArrayName = [None, '']
re4000foam_1Display.DiffuseColor = [1.0, 1.0, 1.0]
re4000foam_1Display.LookupTable = None
re4000foam_1Display.MapScalars = 1
re4000foam_1Display.MultiComponentsMapping = 0
re4000foam_1Display.InterpolateScalarsBeforeMapping = 1
re4000foam_1Display.Opacity = 1.0
re4000foam_1Display.PointSize = 2.0
re4000foam_1Display.LineWidth = 1.0
re4000foam_1Display.RenderLinesAsTubes = 0
re4000foam_1Display.RenderPointsAsSpheres = 0
re4000foam_1Display.Interpolation = 'Gouraud'
re4000foam_1Display.Specular = 0.0
re4000foam_1Display.SpecularColor = [1.0, 1.0, 1.0]
re4000foam_1Display.SpecularPower = 100.0
re4000foam_1Display.Luminosity = 0.0
re4000foam_1Display.Ambient = 0.0
re4000foam_1Display.Diffuse = 1.0
re4000foam_1Display.EdgeColor = [0.0, 0.0, 0.5]
re4000foam_1Display.BackfaceRepresentation = 'Follow Frontface'
re4000foam_1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
re4000foam_1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
re4000foam_1Display.BackfaceOpacity = 1.0
re4000foam_1Display.Position = [0.0, 0.0, 0.0]
re4000foam_1Display.Scale = [1.0, 1.0, 1.0]
re4000foam_1Display.Orientation = [0.0, 0.0, 0.0]
re4000foam_1Display.Origin = [0.0, 0.0, 0.0]
re4000foam_1Display.Pickable = 1
re4000foam_1Display.Texture = None
re4000foam_1Display.Triangulate = 0
re4000foam_1Display.UseShaderReplacements = 0
re4000foam_1Display.ShaderReplacements = ''
re4000foam_1Display.NonlinearSubdivisionLevel = 1
re4000foam_1Display.UseDataPartitions = 0
re4000foam_1Display.OSPRayUseScaleArray = 0
re4000foam_1Display.OSPRayScaleArray = ''
re4000foam_1Display.OSPRayScaleFunction = 'PiecewiseFunction'
re4000foam_1Display.OSPRayMaterial = 'None'
re4000foam_1Display.Orient = 0
re4000foam_1Display.OrientationMode = 'Direction'
re4000foam_1Display.SelectOrientationVectors = 'None'
re4000foam_1Display.Scaling = 0
re4000foam_1Display.ScaleMode = 'No Data Scaling Off'
re4000foam_1Display.ScaleFactor = 0.015999999642372132
re4000foam_1Display.SelectScaleArray = 'None'
re4000foam_1Display.GlyphType = 'Arrow'
re4000foam_1Display.UseGlyphTable = 0
re4000foam_1Display.GlyphTableIndexArray = 'None'
re4000foam_1Display.UseCompositeGlyphTable = 0
re4000foam_1Display.UseGlyphCullingAndLOD = 0
re4000foam_1Display.LODValues = []
re4000foam_1Display.ColorByLODIndex = 0
re4000foam_1Display.GaussianRadius = 0.0007999999821186066
re4000foam_1Display.ShaderPreset = 'Sphere'
re4000foam_1Display.CustomTriangleScale = 3
re4000foam_1Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
re4000foam_1Display.Emissive = 0
re4000foam_1Display.ScaleByArray = 0
re4000foam_1Display.SetScaleArray = [None, '']
re4000foam_1Display.ScaleArrayComponent = 0
re4000foam_1Display.UseScaleFunction = 1
re4000foam_1Display.ScaleTransferFunction = 'PiecewiseFunction'
re4000foam_1Display.OpacityByArray = 0
re4000foam_1Display.OpacityArray = [None, '']
re4000foam_1Display.OpacityArrayComponent = 0
re4000foam_1Display.OpacityTransferFunction = 'PiecewiseFunction'
re4000foam_1Display.DataAxesGrid = 'GridAxesRepresentation'
re4000foam_1Display.SelectionCellLabelBold = 0
re4000foam_1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
re4000foam_1Display.SelectionCellLabelFontFamily = 'Arial'
re4000foam_1Display.SelectionCellLabelFontFile = ''
re4000foam_1Display.SelectionCellLabelFontSize = 18
re4000foam_1Display.SelectionCellLabelItalic = 0
re4000foam_1Display.SelectionCellLabelJustification = 'Left'
re4000foam_1Display.SelectionCellLabelOpacity = 1.0
re4000foam_1Display.SelectionCellLabelShadow = 0
re4000foam_1Display.SelectionPointLabelBold = 0
re4000foam_1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
re4000foam_1Display.SelectionPointLabelFontFamily = 'Arial'
re4000foam_1Display.SelectionPointLabelFontFile = ''
re4000foam_1Display.SelectionPointLabelFontSize = 18
re4000foam_1Display.SelectionPointLabelItalic = 0
re4000foam_1Display.SelectionPointLabelJustification = 'Left'
re4000foam_1Display.SelectionPointLabelOpacity = 1.0
re4000foam_1Display.SelectionPointLabelShadow = 0
re4000foam_1Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
re4000foam_1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
re4000foam_1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
re4000foam_1Display.GlyphType.TipResolution = 6
re4000foam_1Display.GlyphType.TipRadius = 0.1
re4000foam_1Display.GlyphType.TipLength = 0.35
re4000foam_1Display.GlyphType.ShaftResolution = 6
re4000foam_1Display.GlyphType.ShaftRadius = 0.03
re4000foam_1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
re4000foam_1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
re4000foam_1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
re4000foam_1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
re4000foam_1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
re4000foam_1Display.DataAxesGrid.XTitle = 'X Axis'
re4000foam_1Display.DataAxesGrid.YTitle = 'Y Axis'
re4000foam_1Display.DataAxesGrid.ZTitle = 'Z Axis'
re4000foam_1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
re4000foam_1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
re4000foam_1Display.DataAxesGrid.XTitleFontFile = ''
re4000foam_1Display.DataAxesGrid.XTitleBold = 0
re4000foam_1Display.DataAxesGrid.XTitleItalic = 0
re4000foam_1Display.DataAxesGrid.XTitleFontSize = 12
re4000foam_1Display.DataAxesGrid.XTitleShadow = 0
re4000foam_1Display.DataAxesGrid.XTitleOpacity = 1.0
re4000foam_1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
re4000foam_1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
re4000foam_1Display.DataAxesGrid.YTitleFontFile = ''
re4000foam_1Display.DataAxesGrid.YTitleBold = 0
re4000foam_1Display.DataAxesGrid.YTitleItalic = 0
re4000foam_1Display.DataAxesGrid.YTitleFontSize = 12
re4000foam_1Display.DataAxesGrid.YTitleShadow = 0
re4000foam_1Display.DataAxesGrid.YTitleOpacity = 1.0
re4000foam_1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
re4000foam_1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
re4000foam_1Display.DataAxesGrid.ZTitleFontFile = ''
re4000foam_1Display.DataAxesGrid.ZTitleBold = 0
re4000foam_1Display.DataAxesGrid.ZTitleItalic = 0
re4000foam_1Display.DataAxesGrid.ZTitleFontSize = 12
re4000foam_1Display.DataAxesGrid.ZTitleShadow = 0
re4000foam_1Display.DataAxesGrid.ZTitleOpacity = 1.0
re4000foam_1Display.DataAxesGrid.FacesToRender = 63
re4000foam_1Display.DataAxesGrid.CullBackface = 0
re4000foam_1Display.DataAxesGrid.CullFrontface = 1
re4000foam_1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
re4000foam_1Display.DataAxesGrid.ShowGrid = 0
re4000foam_1Display.DataAxesGrid.ShowEdges = 1
re4000foam_1Display.DataAxesGrid.ShowTicks = 1
re4000foam_1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
re4000foam_1Display.DataAxesGrid.AxesToLabel = 63
re4000foam_1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
re4000foam_1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
re4000foam_1Display.DataAxesGrid.XLabelFontFile = ''
re4000foam_1Display.DataAxesGrid.XLabelBold = 0
re4000foam_1Display.DataAxesGrid.XLabelItalic = 0
re4000foam_1Display.DataAxesGrid.XLabelFontSize = 12
re4000foam_1Display.DataAxesGrid.XLabelShadow = 0
re4000foam_1Display.DataAxesGrid.XLabelOpacity = 1.0
re4000foam_1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
re4000foam_1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
re4000foam_1Display.DataAxesGrid.YLabelFontFile = ''
re4000foam_1Display.DataAxesGrid.YLabelBold = 0
re4000foam_1Display.DataAxesGrid.YLabelItalic = 0
re4000foam_1Display.DataAxesGrid.YLabelFontSize = 12
re4000foam_1Display.DataAxesGrid.YLabelShadow = 0
re4000foam_1Display.DataAxesGrid.YLabelOpacity = 1.0
re4000foam_1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
re4000foam_1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
re4000foam_1Display.DataAxesGrid.ZLabelFontFile = ''
re4000foam_1Display.DataAxesGrid.ZLabelBold = 0
re4000foam_1Display.DataAxesGrid.ZLabelItalic = 0
re4000foam_1Display.DataAxesGrid.ZLabelFontSize = 12
re4000foam_1Display.DataAxesGrid.ZLabelShadow = 0
re4000foam_1Display.DataAxesGrid.ZLabelOpacity = 1.0
re4000foam_1Display.DataAxesGrid.XAxisNotation = 'Mixed'
re4000foam_1Display.DataAxesGrid.XAxisPrecision = 2
re4000foam_1Display.DataAxesGrid.XAxisUseCustomLabels = 0
re4000foam_1Display.DataAxesGrid.XAxisLabels = []
re4000foam_1Display.DataAxesGrid.YAxisNotation = 'Mixed'
re4000foam_1Display.DataAxesGrid.YAxisPrecision = 2
re4000foam_1Display.DataAxesGrid.YAxisUseCustomLabels = 0
re4000foam_1Display.DataAxesGrid.YAxisLabels = []
re4000foam_1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
re4000foam_1Display.DataAxesGrid.ZAxisPrecision = 2
re4000foam_1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
re4000foam_1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
re4000foam_1Display.PolarAxes.Visibility = 0
re4000foam_1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
re4000foam_1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
re4000foam_1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
re4000foam_1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
re4000foam_1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
re4000foam_1Display.PolarAxes.EnableCustomRange = 0
re4000foam_1Display.PolarAxes.CustomRange = [0.0, 1.0]
re4000foam_1Display.PolarAxes.PolarAxisVisibility = 1
re4000foam_1Display.PolarAxes.RadialAxesVisibility = 1
re4000foam_1Display.PolarAxes.DrawRadialGridlines = 1
re4000foam_1Display.PolarAxes.PolarArcsVisibility = 1
re4000foam_1Display.PolarAxes.DrawPolarArcsGridlines = 1
re4000foam_1Display.PolarAxes.NumberOfRadialAxes = 0
re4000foam_1Display.PolarAxes.AutoSubdividePolarAxis = 1
re4000foam_1Display.PolarAxes.NumberOfPolarAxis = 0
re4000foam_1Display.PolarAxes.MinimumRadius = 0.0
re4000foam_1Display.PolarAxes.MinimumAngle = 0.0
re4000foam_1Display.PolarAxes.MaximumAngle = 90.0
re4000foam_1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
re4000foam_1Display.PolarAxes.Ratio = 1.0
re4000foam_1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
re4000foam_1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
re4000foam_1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
re4000foam_1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
re4000foam_1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
re4000foam_1Display.PolarAxes.PolarAxisTitleVisibility = 1
re4000foam_1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
re4000foam_1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
re4000foam_1Display.PolarAxes.PolarLabelVisibility = 1
re4000foam_1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
re4000foam_1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
re4000foam_1Display.PolarAxes.RadialLabelVisibility = 1
re4000foam_1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
re4000foam_1Display.PolarAxes.RadialLabelLocation = 'Bottom'
re4000foam_1Display.PolarAxes.RadialUnitsVisibility = 1
re4000foam_1Display.PolarAxes.ScreenSize = 10.0
re4000foam_1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
re4000foam_1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
re4000foam_1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
re4000foam_1Display.PolarAxes.PolarAxisTitleFontFile = ''
re4000foam_1Display.PolarAxes.PolarAxisTitleBold = 0
re4000foam_1Display.PolarAxes.PolarAxisTitleItalic = 0
re4000foam_1Display.PolarAxes.PolarAxisTitleShadow = 0
re4000foam_1Display.PolarAxes.PolarAxisTitleFontSize = 12
re4000foam_1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
re4000foam_1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
re4000foam_1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
re4000foam_1Display.PolarAxes.PolarAxisLabelFontFile = ''
re4000foam_1Display.PolarAxes.PolarAxisLabelBold = 0
re4000foam_1Display.PolarAxes.PolarAxisLabelItalic = 0
re4000foam_1Display.PolarAxes.PolarAxisLabelShadow = 0
re4000foam_1Display.PolarAxes.PolarAxisLabelFontSize = 12
re4000foam_1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
re4000foam_1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
re4000foam_1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
re4000foam_1Display.PolarAxes.LastRadialAxisTextFontFile = ''
re4000foam_1Display.PolarAxes.LastRadialAxisTextBold = 0
re4000foam_1Display.PolarAxes.LastRadialAxisTextItalic = 0
re4000foam_1Display.PolarAxes.LastRadialAxisTextShadow = 0
re4000foam_1Display.PolarAxes.LastRadialAxisTextFontSize = 12
re4000foam_1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
re4000foam_1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
re4000foam_1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
re4000foam_1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
re4000foam_1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
re4000foam_1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
re4000foam_1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
re4000foam_1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
re4000foam_1Display.PolarAxes.EnableDistanceLOD = 1
re4000foam_1Display.PolarAxes.DistanceLODThreshold = 0.7
re4000foam_1Display.PolarAxes.EnableViewAngleLOD = 1
re4000foam_1Display.PolarAxes.ViewAngleLODThreshold = 0.7
re4000foam_1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
re4000foam_1Display.PolarAxes.PolarTicksVisibility = 1
re4000foam_1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
re4000foam_1Display.PolarAxes.TickLocation = 'Both'
re4000foam_1Display.PolarAxes.AxisTickVisibility = 1
re4000foam_1Display.PolarAxes.AxisMinorTickVisibility = 0
re4000foam_1Display.PolarAxes.ArcTickVisibility = 1
re4000foam_1Display.PolarAxes.ArcMinorTickVisibility = 0
re4000foam_1Display.PolarAxes.DeltaAngleMajor = 10.0
re4000foam_1Display.PolarAxes.DeltaAngleMinor = 5.0
re4000foam_1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
re4000foam_1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
re4000foam_1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
re4000foam_1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
re4000foam_1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
re4000foam_1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
re4000foam_1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
re4000foam_1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
re4000foam_1Display.PolarAxes.ArcMajorTickSize = 0.0
re4000foam_1Display.PolarAxes.ArcTickRatioSize = 0.3
re4000foam_1Display.PolarAxes.ArcMajorTickThickness = 1.0
re4000foam_1Display.PolarAxes.ArcTickRatioThickness = 0.5
re4000foam_1Display.PolarAxes.Use2DMode = 0
re4000foam_1Display.PolarAxes.UseLogAxis = 0

# update the view to ensure updated data information
renderView1.Update()

# Properties modified on re4000foam_1Display
re4000foam_1Display.Opacity = 0.1

# set active source
SetActiveSource(contour1)

# set scalar coloring
ColorBy(contour1Display, ('CELLS', 'vorticity_U_mean', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
contour1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'vorticity_U_mean'
vorticity_U_meanLUT = GetColorTransferFunction('vorticity_U_mean')
vorticity_U_meanLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
vorticity_U_meanLUT.InterpretValuesAsCategories = 0
vorticity_U_meanLUT.AnnotationsInitialized = 0
vorticity_U_meanLUT.ShowCategoricalColorsinDataRangeOnly = 0
vorticity_U_meanLUT.RescaleOnVisibilityChange = 0
vorticity_U_meanLUT.EnableOpacityMapping = 0
vorticity_U_meanLUT.RGBPoints = [0.005553941186018742, 0.231373, 0.298039, 0.752941, 45766.92024828252, 0.865003, 0.865003, 0.865003, 91533.83494262386, 0.705882, 0.0156863, 0.14902]
vorticity_U_meanLUT.UseLogScale = 0
vorticity_U_meanLUT.ColorSpace = 'Diverging'
vorticity_U_meanLUT.UseBelowRangeColor = 0
vorticity_U_meanLUT.BelowRangeColor = [0.0, 0.0, 0.0]
vorticity_U_meanLUT.UseAboveRangeColor = 0
vorticity_U_meanLUT.AboveRangeColor = [0.5, 0.5, 0.5]
vorticity_U_meanLUT.NanColor = [1.0, 1.0, 0.0]
vorticity_U_meanLUT.NanOpacity = 1.0
vorticity_U_meanLUT.Discretize = 1
vorticity_U_meanLUT.NumberOfTableValues = 256
vorticity_U_meanLUT.ScalarRangeInitialized = 1.0
vorticity_U_meanLUT.HSVWrap = 0
vorticity_U_meanLUT.VectorComponent = 0
vorticity_U_meanLUT.VectorMode = 'Magnitude'
vorticity_U_meanLUT.AllowDuplicateScalars = 1
vorticity_U_meanLUT.Annotations = []
vorticity_U_meanLUT.ActiveAnnotatedValues = []
vorticity_U_meanLUT.IndexedColors = []
vorticity_U_meanLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'vorticity_U_mean'
vorticity_U_meanPWF = GetOpacityTransferFunction('vorticity_U_mean')
vorticity_U_meanPWF.Points = [0.005553941186018742, 0.0, 0.5, 0.0, 91533.83494262386, 1.0, 0.5, 0.0]
vorticity_U_meanPWF.AllowDuplicateScalars = 1
vorticity_U_meanPWF.UseLogScale = 0
vorticity_U_meanPWF.ScalarRangeInitialized = 1

# set scalar coloring
ColorBy(contour1Display, ('CELLS', 'vorticity_U_mean', 'X'))

# rescale color and/or opacity maps used to exactly fit the current data range
contour1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(vorticity_U_meanLUT, contour1Display)

# Rescale transfer function
vorticity_U_meanLUT.RescaleTransferFunction(-5000.0, 5000.0)

# Rescale transfer function
vorticity_U_meanPWF.RescaleTransferFunction(-5000.0, 5000.0)

# Rescale transfer function
vorticity_U_meanLUT.RescaleTransferFunction(-1000.0, 1000.0)

# Rescale transfer function
vorticity_U_meanPWF.RescaleTransferFunction(-1000.0, 1000.0)

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# hide color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, False)

# current camera placement for renderView1
renderView1.CameraPosition = [-0.029537595734598812, 0.07830942777224939, 0.07322704937103419]
renderView1.CameraFocalPoint = [0.030611987930544746, -0.012698998594824377, -0.005834750828285593]
renderView1.CameraViewUp = [0.2539738206617428, 0.7245106101512384, -0.6407664739956027]
renderView1.CameraParallelScale = 0.09044335049242341

# save screenshot
SaveScreenshot(dirName+'/Q2_0p3_omegaX_1000.png', renderView1, ImageResolution=[2534, 1835],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

import os
print "Finalizing "+ os.path.basename(__file__) +" " + "@ dir : " + dirName 
import datetime
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print "==============================="
