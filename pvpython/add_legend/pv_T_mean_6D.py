# trace generated using paraview version 5.6.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
re4000foam = OpenFOAMReader(FileName='/store/8simu_tmp/shape_square/2a_3_T/Newtonian/Re4000/Re4000.foam')
re4000foam.SkipZeroTime = 1
re4000foam.CaseType = 'Reconstructed Case'
re4000foam.LabelSize = '32-bit'
re4000foam.ScalarSize = '64-bit (DP)'
re4000foam.Createcelltopointfiltereddata = 1
re4000foam.Adddimensionalunitstoarraynames = 0
re4000foam.MeshRegions = ['internalMesh']
re4000foam.CellArrays = ['Q', 'T', 'T_mean', 'U', 'U_mean', 'k_mean', 'p', 'reyTensor', 'reyTensor_mean', 'tt_mean', 'vorticity_U_mean']
re4000foam.PointArrays = []
re4000foam.LagrangianArrays = []
re4000foam.Cachemesh = 1
re4000foam.Decomposepolyhedra = 1
re4000foam.ListtimestepsaccordingtocontrolDict = 0
re4000foam.Lagrangianpositionswithoutextradata = 1
re4000foam.Readzones = 0
re4000foam.Copydatatocellzones = 0

# Properties modified on re4000foam
re4000foam.CellArrays = ['T_mean']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1448, 919]

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
re4000foamDisplay.OSPRayScaleArray = 'T_mean'
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
re4000foamDisplay.SetScaleArray = ['POINTS', 'T_mean']
re4000foamDisplay.ScaleArrayComponent = ''
re4000foamDisplay.UseScaleFunction = 1
re4000foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
re4000foamDisplay.OpacityByArray = 0
re4000foamDisplay.OpacityArray = ['POINTS', 'T_mean']
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

# create a new 'Slice'
slice1 = Slice(Input=re4000foam)
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
slice1.SliceType.Origin = [0.052, -0.037999999010935426, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.052, -0.037999999010935426, 0.0]

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
slice1Display.OSPRayScaleArray = 'T_mean'
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
slice1Display.SetScaleArray = ['POINTS', 'T_mean']
slice1Display.ScaleArrayComponent = ''
slice1Display.UseScaleFunction = 1
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityByArray = 0
slice1Display.OpacityArray = ['POINTS', 'T_mean']
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
Hide(re4000foam, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'T_mean'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'T_mean'
t_meanLUT = GetColorTransferFunction('T_mean')
t_meanLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
t_meanLUT.InterpretValuesAsCategories = 0
t_meanLUT.AnnotationsInitialized = 0
t_meanLUT.ShowCategoricalColorsinDataRangeOnly = 0
t_meanLUT.RescaleOnVisibilityChange = 0
t_meanLUT.EnableOpacityMapping = 0
t_meanLUT.RGBPoints = [0.10281243920326233, 0.231373, 0.298039, 0.752941, 0.3954866975545883, 0.865003, 0.865003, 0.865003, 0.6881609559059143, 0.705882, 0.0156863, 0.14902]
t_meanLUT.UseLogScale = 0
t_meanLUT.ColorSpace = 'Diverging'
t_meanLUT.UseBelowRangeColor = 0
t_meanLUT.BelowRangeColor = [0.0, 0.0, 0.0]
t_meanLUT.UseAboveRangeColor = 0
t_meanLUT.AboveRangeColor = [0.5, 0.5, 0.5]
t_meanLUT.NanColor = [1.0, 1.0, 0.0]
t_meanLUT.NanOpacity = 1.0
t_meanLUT.Discretize = 1
t_meanLUT.NumberOfTableValues = 256
t_meanLUT.ScalarRangeInitialized = 1.0
t_meanLUT.HSVWrap = 0
t_meanLUT.VectorComponent = 0
t_meanLUT.VectorMode = 'Magnitude'
t_meanLUT.AllowDuplicateScalars = 1
t_meanLUT.Annotations = []
t_meanLUT.ActiveAnnotatedValues = []
t_meanLUT.IndexedColors = []
t_meanLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'T_mean'
t_meanPWF = GetOpacityTransferFunction('T_mean')
t_meanPWF.Points = [0.10281243920326233, 0.0, 0.5, 0.0, 0.6881609559059143, 1.0, 0.5, 0.0]
t_meanPWF.AllowDuplicateScalars = 1
t_meanPWF.UseLogScale = 0
t_meanPWF.ScalarRangeInitialized = 1

# Rescale transfer function
t_meanLUT.RescaleTransferFunction(0.0, 1.0)

# Rescale transfer function
t_meanPWF.RescaleTransferFunction(0.0, 1.0)

# get color legend/bar for t_meanLUT in view renderView1
t_meanLUTColorBar = GetScalarBar(t_meanLUT, renderView1)
t_meanLUTColorBar.AutoOrient = 1
t_meanLUTColorBar.Orientation = 'Vertical'
t_meanLUTColorBar.WindowLocation = 'LowerRightCorner'
t_meanLUTColorBar.Position = [0.89, 0.02]
t_meanLUTColorBar.Title = 'T_mean'
t_meanLUTColorBar.ComponentTitle = ''
t_meanLUTColorBar.TitleJustification = 'Centered'
t_meanLUTColorBar.HorizontalTitle = 0
t_meanLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
t_meanLUTColorBar.TitleOpacity = 1.0
t_meanLUTColorBar.TitleFontFamily = 'Arial'
t_meanLUTColorBar.TitleFontFile = ''
t_meanLUTColorBar.TitleBold = 0
t_meanLUTColorBar.TitleItalic = 0
t_meanLUTColorBar.TitleShadow = 0
t_meanLUTColorBar.TitleFontSize = 16
t_meanLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
t_meanLUTColorBar.LabelOpacity = 1.0
t_meanLUTColorBar.LabelFontFamily = 'Arial'
t_meanLUTColorBar.LabelFontFile = ''
t_meanLUTColorBar.LabelBold = 0
t_meanLUTColorBar.LabelItalic = 0
t_meanLUTColorBar.LabelShadow = 0
t_meanLUTColorBar.LabelFontSize = 16
t_meanLUTColorBar.AutomaticLabelFormat = 1
t_meanLUTColorBar.LabelFormat = '%-#6.3g'
t_meanLUTColorBar.DrawTickMarks = 1
t_meanLUTColorBar.DrawTickLabels = 1
t_meanLUTColorBar.UseCustomLabels = 0
t_meanLUTColorBar.CustomLabels = []
t_meanLUTColorBar.AddRangeLabels = 1
t_meanLUTColorBar.RangeLabelFormat = '%-#6.1e'
t_meanLUTColorBar.DrawAnnotations = 1
t_meanLUTColorBar.AddRangeAnnotations = 0
t_meanLUTColorBar.AutomaticAnnotations = 0
t_meanLUTColorBar.DrawNanAnnotation = 0
t_meanLUTColorBar.NanAnnotation = 'NaN'
t_meanLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
t_meanLUTColorBar.ReverseLegend = 0
t_meanLUTColorBar.ScalarBarThickness = 16
t_meanLUTColorBar.ScalarBarLength = 0.33

# change scalar bar placement
t_meanLUTColorBar.Orientation = 'Horizontal'
t_meanLUTColorBar.WindowLocation = 'AnyLocation'
t_meanLUTColorBar.Position = [0.3336740331491716, 0.05161044613710561]
t_meanLUTColorBar.ScalarBarLength = 0.3299999999999999

# current camera placement for renderView1
renderView1.CameraPosition = [0.07385640857155823, 0.0, 0.0]
renderView1.CameraFocalPoint = [0.052000001072883606, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, 1.0, 2.220446049250313e-16]
renderView1.CameraParallelScale = 0.005656854518178539

## save screenshot
#SaveScreenshot('/store/8simu_tmp/shape_square/2a_3_T/Newtonian/Re4000/slice_6D_T_mean.png', renderView1, ImageResolution=[2896, 1838],
#    FontScaling='Scale fonts proportionally',
#    OverrideColorPalette='',
#    StereoMode='No change',
#    TransparentBackground=0, 
#    # PNG options
#    CompressionLevel='5')

# Properties modified on t_meanLUTColorBar
t_meanLUTColorBar.TitleFontSize = 8
t_meanLUTColorBar.LabelFontSize = 8
t_meanLUTColorBar.ScalarBarThickness = 20
t_meanLUTColorBar.ScalarBarLength = 0.5

# change scalar bar placement
t_meanLUTColorBar.Position = [0.2632320441988954, 0.0559630032644179]
t_meanLUTColorBar.ScalarBarLength = 0.49999999999999994

# current camera placement for renderView1
renderView1.CameraPosition = [0.07385640857155823, 0.0, 0.0]
renderView1.CameraFocalPoint = [0.052000001072883606, 0.0, 0.0]
renderView1.CameraViewUp = [0.0, 1.0, 2.220446049250313e-16]
renderView1.CameraParallelScale = 0.005656854518178539

# save screenshot
SaveScreenshot('/store/8simu_tmp/shape_square/2a_3_T/Newtonian/Re4000/slice_6D_T_mean_2.png', renderView1, ImageResolution=[2896, 1838],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')
