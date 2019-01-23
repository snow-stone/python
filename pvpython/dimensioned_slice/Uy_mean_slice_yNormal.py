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
re4000foam.CellArrays = ['U_mean']

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
re4000foamDisplay.OSPRayScaleArray = 'U_mean'
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
re4000foamDisplay.SetScaleArray = ['POINTS', 'U_mean']
re4000foamDisplay.ScaleArrayComponent = 'X'
re4000foamDisplay.UseScaleFunction = 1
re4000foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
re4000foamDisplay.OpacityByArray = 0
re4000foamDisplay.OpacityArray = ['POINTS', 'U_mean']
re4000foamDisplay.OpacityArrayComponent = 'X'
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

# create a new 'Clip'
clip1 = Clip(Input=re4000foam)
clip1.ClipType = 'Plane'
clip1.Scalars = [None, '']
clip1.Value = 0.0
clip1.Invert = 1
clip1.Crinkleclip = 0
clip1.Exact = 0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, -0.037999999010935426, 0.0]
clip1.ClipType.Normal = [1.0, 0.0, 0.0]
clip1.ClipType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# toggle 3D widget visibility (only when running from the GUI)
Show3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [-0.008, -0.037999999010935426, 0.0]

# Properties modified on clip1
clip1.Scalars = ['POINTS', '']
clip1.Invert = 0

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [-0.008, -0.037999999010935426, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.AmbientColor = [1.0, 1.0, 1.0]
clip1Display.ColorArrayName = [None, '']
clip1Display.DiffuseColor = [1.0, 1.0, 1.0]
clip1Display.LookupTable = None
clip1Display.MapScalars = 1
clip1Display.MultiComponentsMapping = 0
clip1Display.InterpolateScalarsBeforeMapping = 1
clip1Display.Opacity = 1.0
clip1Display.PointSize = 2.0
clip1Display.LineWidth = 1.0
clip1Display.RenderLinesAsTubes = 0
clip1Display.RenderPointsAsSpheres = 0
clip1Display.Interpolation = 'Gouraud'
clip1Display.Specular = 0.0
clip1Display.SpecularColor = [1.0, 1.0, 1.0]
clip1Display.SpecularPower = 100.0
clip1Display.Luminosity = 0.0
clip1Display.Ambient = 0.0
clip1Display.Diffuse = 1.0
clip1Display.EdgeColor = [0.0, 0.0, 0.5]
clip1Display.BackfaceRepresentation = 'Follow Frontface'
clip1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
clip1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
clip1Display.BackfaceOpacity = 1.0
clip1Display.Position = [0.0, 0.0, 0.0]
clip1Display.Scale = [1.0, 1.0, 1.0]
clip1Display.Orientation = [0.0, 0.0, 0.0]
clip1Display.Origin = [0.0, 0.0, 0.0]
clip1Display.Pickable = 1
clip1Display.Texture = None
clip1Display.Triangulate = 0
clip1Display.UseShaderReplacements = 0
clip1Display.ShaderReplacements = ''
clip1Display.NonlinearSubdivisionLevel = 1
clip1Display.UseDataPartitions = 0
clip1Display.OSPRayUseScaleArray = 0
clip1Display.OSPRayScaleArray = 'U_mean'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.OSPRayMaterial = 'None'
clip1Display.Orient = 0
clip1Display.OrientationMode = 'Direction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.Scaling = 0
clip1Display.ScaleMode = 'No Data Scaling Off'
clip1Display.ScaleFactor = 0.008799999859184027
clip1Display.SelectScaleArray = 'None'
clip1Display.GlyphType = 'Arrow'
clip1Display.UseGlyphTable = 0
clip1Display.GlyphTableIndexArray = 'None'
clip1Display.UseCompositeGlyphTable = 0
clip1Display.UseGlyphCullingAndLOD = 0
clip1Display.LODValues = []
clip1Display.ColorByLODIndex = 0
clip1Display.GaussianRadius = 0.00043999999295920135
clip1Display.ShaderPreset = 'Sphere'
clip1Display.CustomTriangleScale = 3
clip1Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
clip1Display.Emissive = 0
clip1Display.ScaleByArray = 0
clip1Display.SetScaleArray = ['POINTS', 'U_mean']
clip1Display.ScaleArrayComponent = 'X'
clip1Display.UseScaleFunction = 1
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityByArray = 0
clip1Display.OpacityArray = ['POINTS', 'U_mean']
clip1Display.OpacityArrayComponent = 'X'
clip1Display.OpacityTransferFunction = 'PiecewiseFunction'
clip1Display.DataAxesGrid = 'GridAxesRepresentation'
clip1Display.SelectionCellLabelBold = 0
clip1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
clip1Display.SelectionCellLabelFontFamily = 'Arial'
clip1Display.SelectionCellLabelFontFile = ''
clip1Display.SelectionCellLabelFontSize = 18
clip1Display.SelectionCellLabelItalic = 0
clip1Display.SelectionCellLabelJustification = 'Left'
clip1Display.SelectionCellLabelOpacity = 1.0
clip1Display.SelectionCellLabelShadow = 0
clip1Display.SelectionPointLabelBold = 0
clip1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
clip1Display.SelectionPointLabelFontFamily = 'Arial'
clip1Display.SelectionPointLabelFontFile = ''
clip1Display.SelectionPointLabelFontSize = 18
clip1Display.SelectionPointLabelItalic = 0
clip1Display.SelectionPointLabelJustification = 'Left'
clip1Display.SelectionPointLabelOpacity = 1.0
clip1Display.SelectionPointLabelShadow = 0
clip1Display.PolarAxes = 'PolarAxesRepresentation'
clip1Display.ScalarOpacityFunction = None
clip1Display.ScalarOpacityUnitDistance = 0.00043755798744096627
clip1Display.SelectMapper = 'Projected tetra'
clip1Display.SamplingDimensions = [128, 128, 128]
clip1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
clip1Display.GlyphType.TipResolution = 6
clip1Display.GlyphType.TipRadius = 0.1
clip1Display.GlyphType.TipLength = 0.35
clip1Display.GlyphType.ShaftResolution = 6
clip1Display.GlyphType.ShaftRadius = 0.03
clip1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip1Display.DataAxesGrid.XTitle = 'X Axis'
clip1Display.DataAxesGrid.YTitle = 'Y Axis'
clip1Display.DataAxesGrid.ZTitle = 'Z Axis'
clip1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.XTitleFontFile = ''
clip1Display.DataAxesGrid.XTitleBold = 0
clip1Display.DataAxesGrid.XTitleItalic = 0
clip1Display.DataAxesGrid.XTitleFontSize = 12
clip1Display.DataAxesGrid.XTitleShadow = 0
clip1Display.DataAxesGrid.XTitleOpacity = 1.0
clip1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.YTitleFontFile = ''
clip1Display.DataAxesGrid.YTitleBold = 0
clip1Display.DataAxesGrid.YTitleItalic = 0
clip1Display.DataAxesGrid.YTitleFontSize = 12
clip1Display.DataAxesGrid.YTitleShadow = 0
clip1Display.DataAxesGrid.YTitleOpacity = 1.0
clip1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
clip1Display.DataAxesGrid.ZTitleFontFile = ''
clip1Display.DataAxesGrid.ZTitleBold = 0
clip1Display.DataAxesGrid.ZTitleItalic = 0
clip1Display.DataAxesGrid.ZTitleFontSize = 12
clip1Display.DataAxesGrid.ZTitleShadow = 0
clip1Display.DataAxesGrid.ZTitleOpacity = 1.0
clip1Display.DataAxesGrid.FacesToRender = 63
clip1Display.DataAxesGrid.CullBackface = 0
clip1Display.DataAxesGrid.CullFrontface = 1
clip1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
clip1Display.DataAxesGrid.ShowGrid = 0
clip1Display.DataAxesGrid.ShowEdges = 1
clip1Display.DataAxesGrid.ShowTicks = 1
clip1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
clip1Display.DataAxesGrid.AxesToLabel = 63
clip1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.XLabelFontFile = ''
clip1Display.DataAxesGrid.XLabelBold = 0
clip1Display.DataAxesGrid.XLabelItalic = 0
clip1Display.DataAxesGrid.XLabelFontSize = 12
clip1Display.DataAxesGrid.XLabelShadow = 0
clip1Display.DataAxesGrid.XLabelOpacity = 1.0
clip1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.YLabelFontFile = ''
clip1Display.DataAxesGrid.YLabelBold = 0
clip1Display.DataAxesGrid.YLabelItalic = 0
clip1Display.DataAxesGrid.YLabelFontSize = 12
clip1Display.DataAxesGrid.YLabelShadow = 0
clip1Display.DataAxesGrid.YLabelOpacity = 1.0
clip1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
clip1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
clip1Display.DataAxesGrid.ZLabelFontFile = ''
clip1Display.DataAxesGrid.ZLabelBold = 0
clip1Display.DataAxesGrid.ZLabelItalic = 0
clip1Display.DataAxesGrid.ZLabelFontSize = 12
clip1Display.DataAxesGrid.ZLabelShadow = 0
clip1Display.DataAxesGrid.ZLabelOpacity = 1.0
clip1Display.DataAxesGrid.XAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.XAxisPrecision = 2
clip1Display.DataAxesGrid.XAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.XAxisLabels = []
clip1Display.DataAxesGrid.YAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.YAxisPrecision = 2
clip1Display.DataAxesGrid.YAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.YAxisLabels = []
clip1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
clip1Display.DataAxesGrid.ZAxisPrecision = 2
clip1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
clip1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip1Display.PolarAxes.Visibility = 0
clip1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
clip1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
clip1Display.PolarAxes.EnableCustomRange = 0
clip1Display.PolarAxes.CustomRange = [0.0, 1.0]
clip1Display.PolarAxes.PolarAxisVisibility = 1
clip1Display.PolarAxes.RadialAxesVisibility = 1
clip1Display.PolarAxes.DrawRadialGridlines = 1
clip1Display.PolarAxes.PolarArcsVisibility = 1
clip1Display.PolarAxes.DrawPolarArcsGridlines = 1
clip1Display.PolarAxes.NumberOfRadialAxes = 0
clip1Display.PolarAxes.AutoSubdividePolarAxis = 1
clip1Display.PolarAxes.NumberOfPolarAxis = 0
clip1Display.PolarAxes.MinimumRadius = 0.0
clip1Display.PolarAxes.MinimumAngle = 0.0
clip1Display.PolarAxes.MaximumAngle = 90.0
clip1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
clip1Display.PolarAxes.Ratio = 1.0
clip1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
clip1Display.PolarAxes.PolarAxisTitleVisibility = 1
clip1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
clip1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
clip1Display.PolarAxes.PolarLabelVisibility = 1
clip1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
clip1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
clip1Display.PolarAxes.RadialLabelVisibility = 1
clip1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
clip1Display.PolarAxes.RadialLabelLocation = 'Bottom'
clip1Display.PolarAxes.RadialUnitsVisibility = 1
clip1Display.PolarAxes.ScreenSize = 10.0
clip1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
clip1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
clip1Display.PolarAxes.PolarAxisTitleFontFile = ''
clip1Display.PolarAxes.PolarAxisTitleBold = 0
clip1Display.PolarAxes.PolarAxisTitleItalic = 0
clip1Display.PolarAxes.PolarAxisTitleShadow = 0
clip1Display.PolarAxes.PolarAxisTitleFontSize = 12
clip1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
clip1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
clip1Display.PolarAxes.PolarAxisLabelFontFile = ''
clip1Display.PolarAxes.PolarAxisLabelBold = 0
clip1Display.PolarAxes.PolarAxisLabelItalic = 0
clip1Display.PolarAxes.PolarAxisLabelShadow = 0
clip1Display.PolarAxes.PolarAxisLabelFontSize = 12
clip1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
clip1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
clip1Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip1Display.PolarAxes.LastRadialAxisTextBold = 0
clip1Display.PolarAxes.LastRadialAxisTextItalic = 0
clip1Display.PolarAxes.LastRadialAxisTextShadow = 0
clip1Display.PolarAxes.LastRadialAxisTextFontSize = 12
clip1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
clip1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
clip1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
clip1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
clip1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
clip1Display.PolarAxes.EnableDistanceLOD = 1
clip1Display.PolarAxes.DistanceLODThreshold = 0.7
clip1Display.PolarAxes.EnableViewAngleLOD = 1
clip1Display.PolarAxes.ViewAngleLODThreshold = 0.7
clip1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
clip1Display.PolarAxes.PolarTicksVisibility = 1
clip1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
clip1Display.PolarAxes.TickLocation = 'Both'
clip1Display.PolarAxes.AxisTickVisibility = 1
clip1Display.PolarAxes.AxisMinorTickVisibility = 0
clip1Display.PolarAxes.ArcTickVisibility = 1
clip1Display.PolarAxes.ArcMinorTickVisibility = 0
clip1Display.PolarAxes.DeltaAngleMajor = 10.0
clip1Display.PolarAxes.DeltaAngleMinor = 5.0
clip1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
clip1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
clip1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
clip1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
clip1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
clip1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
clip1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
clip1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
clip1Display.PolarAxes.ArcMajorTickSize = 0.0
clip1Display.PolarAxes.ArcTickRatioSize = 0.3
clip1Display.PolarAxes.ArcMajorTickThickness = 1.0
clip1Display.PolarAxes.ArcTickRatioThickness = 0.5
clip1Display.PolarAxes.Use2DMode = 0
clip1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(re4000foam, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(Input=clip1)
clip2.ClipType = 'Plane'
clip2.Scalars = [None, '']
clip2.Value = 0.0
clip2.Invert = 1
clip2.Crinkleclip = 0
clip2.Exact = 0

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.03599999891594052, -0.037999999010935426, 0.0]
clip2.ClipType.Normal = [1.0, 0.0, 0.0]
clip2.ClipType.Offset = 0.0

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.03599999891594052, -0.008, 0.0]
clip2.ClipType.Normal = [0.0, 1.0, 0.0]

# Properties modified on clip2
clip2.Scalars = ['POINTS', '']
clip2.Invert = 0

# Properties modified on clip2.ClipType
clip2.ClipType.Origin = [0.03599999891594052, -0.008, 0.0]
clip2.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip2Display = Show(clip2, renderView1)

# trace defaults for the display properties.
clip2Display.Representation = 'Surface'
clip2Display.AmbientColor = [1.0, 1.0, 1.0]
clip2Display.ColorArrayName = [None, '']
clip2Display.DiffuseColor = [1.0, 1.0, 1.0]
clip2Display.LookupTable = None
clip2Display.MapScalars = 1
clip2Display.MultiComponentsMapping = 0
clip2Display.InterpolateScalarsBeforeMapping = 1
clip2Display.Opacity = 1.0
clip2Display.PointSize = 2.0
clip2Display.LineWidth = 1.0
clip2Display.RenderLinesAsTubes = 0
clip2Display.RenderPointsAsSpheres = 0
clip2Display.Interpolation = 'Gouraud'
clip2Display.Specular = 0.0
clip2Display.SpecularColor = [1.0, 1.0, 1.0]
clip2Display.SpecularPower = 100.0
clip2Display.Luminosity = 0.0
clip2Display.Ambient = 0.0
clip2Display.Diffuse = 1.0
clip2Display.EdgeColor = [0.0, 0.0, 0.5]
clip2Display.BackfaceRepresentation = 'Follow Frontface'
clip2Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
clip2Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
clip2Display.BackfaceOpacity = 1.0
clip2Display.Position = [0.0, 0.0, 0.0]
clip2Display.Scale = [1.0, 1.0, 1.0]
clip2Display.Orientation = [0.0, 0.0, 0.0]
clip2Display.Origin = [0.0, 0.0, 0.0]
clip2Display.Pickable = 1
clip2Display.Texture = None
clip2Display.Triangulate = 0
clip2Display.UseShaderReplacements = 0
clip2Display.ShaderReplacements = ''
clip2Display.NonlinearSubdivisionLevel = 1
clip2Display.UseDataPartitions = 0
clip2Display.OSPRayUseScaleArray = 0
clip2Display.OSPRayScaleArray = 'U_mean'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.OSPRayMaterial = 'None'
clip2Display.Orient = 0
clip2Display.OrientationMode = 'Direction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.Scaling = 0
clip2Display.ScaleMode = 'No Data Scaling Off'
clip2Display.ScaleFactor = 0.008799999859184027
clip2Display.SelectScaleArray = 'None'
clip2Display.GlyphType = 'Arrow'
clip2Display.UseGlyphTable = 0
clip2Display.GlyphTableIndexArray = 'None'
clip2Display.UseCompositeGlyphTable = 0
clip2Display.UseGlyphCullingAndLOD = 0
clip2Display.LODValues = []
clip2Display.ColorByLODIndex = 0
clip2Display.GaussianRadius = 0.00043999999295920135
clip2Display.ShaderPreset = 'Sphere'
clip2Display.CustomTriangleScale = 3
clip2Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
clip2Display.Emissive = 0
clip2Display.ScaleByArray = 0
clip2Display.SetScaleArray = ['POINTS', 'U_mean']
clip2Display.ScaleArrayComponent = 'X'
clip2Display.UseScaleFunction = 1
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityByArray = 0
clip2Display.OpacityArray = ['POINTS', 'U_mean']
clip2Display.OpacityArrayComponent = 'X'
clip2Display.OpacityTransferFunction = 'PiecewiseFunction'
clip2Display.DataAxesGrid = 'GridAxesRepresentation'
clip2Display.SelectionCellLabelBold = 0
clip2Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
clip2Display.SelectionCellLabelFontFamily = 'Arial'
clip2Display.SelectionCellLabelFontFile = ''
clip2Display.SelectionCellLabelFontSize = 18
clip2Display.SelectionCellLabelItalic = 0
clip2Display.SelectionCellLabelJustification = 'Left'
clip2Display.SelectionCellLabelOpacity = 1.0
clip2Display.SelectionCellLabelShadow = 0
clip2Display.SelectionPointLabelBold = 0
clip2Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
clip2Display.SelectionPointLabelFontFamily = 'Arial'
clip2Display.SelectionPointLabelFontFile = ''
clip2Display.SelectionPointLabelFontSize = 18
clip2Display.SelectionPointLabelItalic = 0
clip2Display.SelectionPointLabelJustification = 'Left'
clip2Display.SelectionPointLabelOpacity = 1.0
clip2Display.SelectionPointLabelShadow = 0
clip2Display.PolarAxes = 'PolarAxesRepresentation'
clip2Display.ScalarOpacityFunction = None
clip2Display.ScalarOpacityUnitDistance = 0.0003486563235674366
clip2Display.SelectMapper = 'Projected tetra'
clip2Display.SamplingDimensions = [128, 128, 128]
clip2Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip2Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip2Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
clip2Display.GlyphType.TipResolution = 6
clip2Display.GlyphType.TipRadius = 0.1
clip2Display.GlyphType.TipLength = 0.35
clip2Display.GlyphType.ShaftResolution = 6
clip2Display.GlyphType.ShaftRadius = 0.03
clip2Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip2Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip2Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip2Display.DataAxesGrid.XTitle = 'X Axis'
clip2Display.DataAxesGrid.YTitle = 'Y Axis'
clip2Display.DataAxesGrid.ZTitle = 'Z Axis'
clip2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.XTitleFontFamily = 'Arial'
clip2Display.DataAxesGrid.XTitleFontFile = ''
clip2Display.DataAxesGrid.XTitleBold = 0
clip2Display.DataAxesGrid.XTitleItalic = 0
clip2Display.DataAxesGrid.XTitleFontSize = 12
clip2Display.DataAxesGrid.XTitleShadow = 0
clip2Display.DataAxesGrid.XTitleOpacity = 1.0
clip2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.YTitleFontFamily = 'Arial'
clip2Display.DataAxesGrid.YTitleFontFile = ''
clip2Display.DataAxesGrid.YTitleBold = 0
clip2Display.DataAxesGrid.YTitleItalic = 0
clip2Display.DataAxesGrid.YTitleFontSize = 12
clip2Display.DataAxesGrid.YTitleShadow = 0
clip2Display.DataAxesGrid.YTitleOpacity = 1.0
clip2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
clip2Display.DataAxesGrid.ZTitleFontFile = ''
clip2Display.DataAxesGrid.ZTitleBold = 0
clip2Display.DataAxesGrid.ZTitleItalic = 0
clip2Display.DataAxesGrid.ZTitleFontSize = 12
clip2Display.DataAxesGrid.ZTitleShadow = 0
clip2Display.DataAxesGrid.ZTitleOpacity = 1.0
clip2Display.DataAxesGrid.FacesToRender = 63
clip2Display.DataAxesGrid.CullBackface = 0
clip2Display.DataAxesGrid.CullFrontface = 1
clip2Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
clip2Display.DataAxesGrid.ShowGrid = 0
clip2Display.DataAxesGrid.ShowEdges = 1
clip2Display.DataAxesGrid.ShowTicks = 1
clip2Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
clip2Display.DataAxesGrid.AxesToLabel = 63
clip2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.XLabelFontFamily = 'Arial'
clip2Display.DataAxesGrid.XLabelFontFile = ''
clip2Display.DataAxesGrid.XLabelBold = 0
clip2Display.DataAxesGrid.XLabelItalic = 0
clip2Display.DataAxesGrid.XLabelFontSize = 12
clip2Display.DataAxesGrid.XLabelShadow = 0
clip2Display.DataAxesGrid.XLabelOpacity = 1.0
clip2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.YLabelFontFamily = 'Arial'
clip2Display.DataAxesGrid.YLabelFontFile = ''
clip2Display.DataAxesGrid.YLabelBold = 0
clip2Display.DataAxesGrid.YLabelItalic = 0
clip2Display.DataAxesGrid.YLabelFontSize = 12
clip2Display.DataAxesGrid.YLabelShadow = 0
clip2Display.DataAxesGrid.YLabelOpacity = 1.0
clip2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
clip2Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
clip2Display.DataAxesGrid.ZLabelFontFile = ''
clip2Display.DataAxesGrid.ZLabelBold = 0
clip2Display.DataAxesGrid.ZLabelItalic = 0
clip2Display.DataAxesGrid.ZLabelFontSize = 12
clip2Display.DataAxesGrid.ZLabelShadow = 0
clip2Display.DataAxesGrid.ZLabelOpacity = 1.0
clip2Display.DataAxesGrid.XAxisNotation = 'Mixed'
clip2Display.DataAxesGrid.XAxisPrecision = 2
clip2Display.DataAxesGrid.XAxisUseCustomLabels = 0
clip2Display.DataAxesGrid.XAxisLabels = []
clip2Display.DataAxesGrid.YAxisNotation = 'Mixed'
clip2Display.DataAxesGrid.YAxisPrecision = 2
clip2Display.DataAxesGrid.YAxisUseCustomLabels = 0
clip2Display.DataAxesGrid.YAxisLabels = []
clip2Display.DataAxesGrid.ZAxisNotation = 'Mixed'
clip2Display.DataAxesGrid.ZAxisPrecision = 2
clip2Display.DataAxesGrid.ZAxisUseCustomLabels = 0
clip2Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip2Display.PolarAxes.Visibility = 0
clip2Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
clip2Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
clip2Display.PolarAxes.EnableCustomRange = 0
clip2Display.PolarAxes.CustomRange = [0.0, 1.0]
clip2Display.PolarAxes.PolarAxisVisibility = 1
clip2Display.PolarAxes.RadialAxesVisibility = 1
clip2Display.PolarAxes.DrawRadialGridlines = 1
clip2Display.PolarAxes.PolarArcsVisibility = 1
clip2Display.PolarAxes.DrawPolarArcsGridlines = 1
clip2Display.PolarAxes.NumberOfRadialAxes = 0
clip2Display.PolarAxes.AutoSubdividePolarAxis = 1
clip2Display.PolarAxes.NumberOfPolarAxis = 0
clip2Display.PolarAxes.MinimumRadius = 0.0
clip2Display.PolarAxes.MinimumAngle = 0.0
clip2Display.PolarAxes.MaximumAngle = 90.0
clip2Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
clip2Display.PolarAxes.Ratio = 1.0
clip2Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
clip2Display.PolarAxes.PolarAxisTitleVisibility = 1
clip2Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
clip2Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
clip2Display.PolarAxes.PolarLabelVisibility = 1
clip2Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
clip2Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
clip2Display.PolarAxes.RadialLabelVisibility = 1
clip2Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
clip2Display.PolarAxes.RadialLabelLocation = 'Bottom'
clip2Display.PolarAxes.RadialUnitsVisibility = 1
clip2Display.PolarAxes.ScreenSize = 10.0
clip2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.PolarAxisTitleOpacity = 1.0
clip2Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
clip2Display.PolarAxes.PolarAxisTitleFontFile = ''
clip2Display.PolarAxes.PolarAxisTitleBold = 0
clip2Display.PolarAxes.PolarAxisTitleItalic = 0
clip2Display.PolarAxes.PolarAxisTitleShadow = 0
clip2Display.PolarAxes.PolarAxisTitleFontSize = 12
clip2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.PolarAxisLabelOpacity = 1.0
clip2Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
clip2Display.PolarAxes.PolarAxisLabelFontFile = ''
clip2Display.PolarAxes.PolarAxisLabelBold = 0
clip2Display.PolarAxes.PolarAxisLabelItalic = 0
clip2Display.PolarAxes.PolarAxisLabelShadow = 0
clip2Display.PolarAxes.PolarAxisLabelFontSize = 12
clip2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
clip2Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
clip2Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip2Display.PolarAxes.LastRadialAxisTextBold = 0
clip2Display.PolarAxes.LastRadialAxisTextItalic = 0
clip2Display.PolarAxes.LastRadialAxisTextShadow = 0
clip2Display.PolarAxes.LastRadialAxisTextFontSize = 12
clip2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
clip2Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
clip2Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
clip2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
clip2Display.PolarAxes.SecondaryRadialAxesTextBold = 0
clip2Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
clip2Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
clip2Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
clip2Display.PolarAxes.EnableDistanceLOD = 1
clip2Display.PolarAxes.DistanceLODThreshold = 0.7
clip2Display.PolarAxes.EnableViewAngleLOD = 1
clip2Display.PolarAxes.ViewAngleLODThreshold = 0.7
clip2Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
clip2Display.PolarAxes.PolarTicksVisibility = 1
clip2Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
clip2Display.PolarAxes.TickLocation = 'Both'
clip2Display.PolarAxes.AxisTickVisibility = 1
clip2Display.PolarAxes.AxisMinorTickVisibility = 0
clip2Display.PolarAxes.ArcTickVisibility = 1
clip2Display.PolarAxes.ArcMinorTickVisibility = 0
clip2Display.PolarAxes.DeltaAngleMajor = 10.0
clip2Display.PolarAxes.DeltaAngleMinor = 5.0
clip2Display.PolarAxes.PolarAxisMajorTickSize = 0.0
clip2Display.PolarAxes.PolarAxisTickRatioSize = 0.3
clip2Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
clip2Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
clip2Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
clip2Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
clip2Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
clip2Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
clip2Display.PolarAxes.ArcMajorTickSize = 0.0
clip2Display.PolarAxes.ArcTickRatioSize = 0.3
clip2Display.PolarAxes.ArcMajorTickThickness = 1.0
clip2Display.PolarAxes.ArcTickRatioThickness = 0.5
clip2Display.PolarAxes.Use2DMode = 0
clip2Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(clip1, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip3 = Clip(Input=clip2)
clip3.ClipType = 'Plane'
clip3.Scalars = [None, '']
clip3.Value = 0.0
clip3.Invert = 1
clip3.Crinkleclip = 0
clip3.Exact = 0

# init the 'Plane' selected for 'ClipType'
clip3.ClipType.Origin = [0.03599999891594052, -0.0020000000949949026, 0.0]
clip3.ClipType.Normal = [1.0, 0.0, 0.0]
clip3.ClipType.Offset = 0.0

# Properties modified on clip3
clip3.Scalars = ['POINTS', '']

# show data in view
clip3Display = Show(clip3, renderView1)

# trace defaults for the display properties.
clip3Display.Representation = 'Surface'
clip3Display.AmbientColor = [1.0, 1.0, 1.0]
clip3Display.ColorArrayName = [None, '']
clip3Display.DiffuseColor = [1.0, 1.0, 1.0]
clip3Display.LookupTable = None
clip3Display.MapScalars = 1
clip3Display.MultiComponentsMapping = 0
clip3Display.InterpolateScalarsBeforeMapping = 1
clip3Display.Opacity = 1.0
clip3Display.PointSize = 2.0
clip3Display.LineWidth = 1.0
clip3Display.RenderLinesAsTubes = 0
clip3Display.RenderPointsAsSpheres = 0
clip3Display.Interpolation = 'Gouraud'
clip3Display.Specular = 0.0
clip3Display.SpecularColor = [1.0, 1.0, 1.0]
clip3Display.SpecularPower = 100.0
clip3Display.Luminosity = 0.0
clip3Display.Ambient = 0.0
clip3Display.Diffuse = 1.0
clip3Display.EdgeColor = [0.0, 0.0, 0.5]
clip3Display.BackfaceRepresentation = 'Follow Frontface'
clip3Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
clip3Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
clip3Display.BackfaceOpacity = 1.0
clip3Display.Position = [0.0, 0.0, 0.0]
clip3Display.Scale = [1.0, 1.0, 1.0]
clip3Display.Orientation = [0.0, 0.0, 0.0]
clip3Display.Origin = [0.0, 0.0, 0.0]
clip3Display.Pickable = 1
clip3Display.Texture = None
clip3Display.Triangulate = 0
clip3Display.UseShaderReplacements = 0
clip3Display.ShaderReplacements = ''
clip3Display.NonlinearSubdivisionLevel = 1
clip3Display.UseDataPartitions = 0
clip3Display.OSPRayUseScaleArray = 0
clip3Display.OSPRayScaleArray = 'U_mean'
clip3Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip3Display.OSPRayMaterial = 'None'
clip3Display.Orient = 0
clip3Display.OrientationMode = 'Direction'
clip3Display.SelectOrientationVectors = 'None'
clip3Display.Scaling = 0
clip3Display.ScaleMode = 'No Data Scaling Off'
clip3Display.ScaleFactor = 0.004399999883025885
clip3Display.SelectScaleArray = 'None'
clip3Display.GlyphType = 'Arrow'
clip3Display.UseGlyphTable = 0
clip3Display.GlyphTableIndexArray = 'None'
clip3Display.UseCompositeGlyphTable = 0
clip3Display.UseGlyphCullingAndLOD = 0
clip3Display.LODValues = []
clip3Display.ColorByLODIndex = 0
clip3Display.GaussianRadius = 0.00021999999415129424
clip3Display.ShaderPreset = 'Sphere'
clip3Display.CustomTriangleScale = 3
clip3Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
clip3Display.Emissive = 0
clip3Display.ScaleByArray = 0
clip3Display.SetScaleArray = ['POINTS', 'U_mean']
clip3Display.ScaleArrayComponent = 'X'
clip3Display.UseScaleFunction = 1
clip3Display.ScaleTransferFunction = 'PiecewiseFunction'
clip3Display.OpacityByArray = 0
clip3Display.OpacityArray = ['POINTS', 'U_mean']
clip3Display.OpacityArrayComponent = 'X'
clip3Display.OpacityTransferFunction = 'PiecewiseFunction'
clip3Display.DataAxesGrid = 'GridAxesRepresentation'
clip3Display.SelectionCellLabelBold = 0
clip3Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
clip3Display.SelectionCellLabelFontFamily = 'Arial'
clip3Display.SelectionCellLabelFontFile = ''
clip3Display.SelectionCellLabelFontSize = 18
clip3Display.SelectionCellLabelItalic = 0
clip3Display.SelectionCellLabelJustification = 'Left'
clip3Display.SelectionCellLabelOpacity = 1.0
clip3Display.SelectionCellLabelShadow = 0
clip3Display.SelectionPointLabelBold = 0
clip3Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
clip3Display.SelectionPointLabelFontFamily = 'Arial'
clip3Display.SelectionPointLabelFontFile = ''
clip3Display.SelectionPointLabelFontSize = 18
clip3Display.SelectionPointLabelItalic = 0
clip3Display.SelectionPointLabelJustification = 'Left'
clip3Display.SelectionPointLabelOpacity = 1.0
clip3Display.SelectionPointLabelShadow = 0
clip3Display.PolarAxes = 'PolarAxesRepresentation'
clip3Display.ScalarOpacityFunction = None
clip3Display.ScalarOpacityUnitDistance = 0.00018660674480972287
clip3Display.SelectMapper = 'Projected tetra'
clip3Display.SamplingDimensions = [128, 128, 128]
clip3Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
clip3Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip3Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
clip3Display.GlyphType.TipResolution = 6
clip3Display.GlyphType.TipRadius = 0.1
clip3Display.GlyphType.TipLength = 0.35
clip3Display.GlyphType.ShaftResolution = 6
clip3Display.GlyphType.ShaftRadius = 0.03
clip3Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
clip3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip3Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
clip3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
clip3Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
clip3Display.DataAxesGrid.XTitle = 'X Axis'
clip3Display.DataAxesGrid.YTitle = 'Y Axis'
clip3Display.DataAxesGrid.ZTitle = 'Z Axis'
clip3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.XTitleFontFamily = 'Arial'
clip3Display.DataAxesGrid.XTitleFontFile = ''
clip3Display.DataAxesGrid.XTitleBold = 0
clip3Display.DataAxesGrid.XTitleItalic = 0
clip3Display.DataAxesGrid.XTitleFontSize = 12
clip3Display.DataAxesGrid.XTitleShadow = 0
clip3Display.DataAxesGrid.XTitleOpacity = 1.0
clip3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.YTitleFontFamily = 'Arial'
clip3Display.DataAxesGrid.YTitleFontFile = ''
clip3Display.DataAxesGrid.YTitleBold = 0
clip3Display.DataAxesGrid.YTitleItalic = 0
clip3Display.DataAxesGrid.YTitleFontSize = 12
clip3Display.DataAxesGrid.YTitleShadow = 0
clip3Display.DataAxesGrid.YTitleOpacity = 1.0
clip3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
clip3Display.DataAxesGrid.ZTitleFontFile = ''
clip3Display.DataAxesGrid.ZTitleBold = 0
clip3Display.DataAxesGrid.ZTitleItalic = 0
clip3Display.DataAxesGrid.ZTitleFontSize = 12
clip3Display.DataAxesGrid.ZTitleShadow = 0
clip3Display.DataAxesGrid.ZTitleOpacity = 1.0
clip3Display.DataAxesGrid.FacesToRender = 63
clip3Display.DataAxesGrid.CullBackface = 0
clip3Display.DataAxesGrid.CullFrontface = 1
clip3Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
clip3Display.DataAxesGrid.ShowGrid = 0
clip3Display.DataAxesGrid.ShowEdges = 1
clip3Display.DataAxesGrid.ShowTicks = 1
clip3Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
clip3Display.DataAxesGrid.AxesToLabel = 63
clip3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.XLabelFontFamily = 'Arial'
clip3Display.DataAxesGrid.XLabelFontFile = ''
clip3Display.DataAxesGrid.XLabelBold = 0
clip3Display.DataAxesGrid.XLabelItalic = 0
clip3Display.DataAxesGrid.XLabelFontSize = 12
clip3Display.DataAxesGrid.XLabelShadow = 0
clip3Display.DataAxesGrid.XLabelOpacity = 1.0
clip3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.YLabelFontFamily = 'Arial'
clip3Display.DataAxesGrid.YLabelFontFile = ''
clip3Display.DataAxesGrid.YLabelBold = 0
clip3Display.DataAxesGrid.YLabelItalic = 0
clip3Display.DataAxesGrid.YLabelFontSize = 12
clip3Display.DataAxesGrid.YLabelShadow = 0
clip3Display.DataAxesGrid.YLabelOpacity = 1.0
clip3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
clip3Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
clip3Display.DataAxesGrid.ZLabelFontFile = ''
clip3Display.DataAxesGrid.ZLabelBold = 0
clip3Display.DataAxesGrid.ZLabelItalic = 0
clip3Display.DataAxesGrid.ZLabelFontSize = 12
clip3Display.DataAxesGrid.ZLabelShadow = 0
clip3Display.DataAxesGrid.ZLabelOpacity = 1.0
clip3Display.DataAxesGrid.XAxisNotation = 'Mixed'
clip3Display.DataAxesGrid.XAxisPrecision = 2
clip3Display.DataAxesGrid.XAxisUseCustomLabels = 0
clip3Display.DataAxesGrid.XAxisLabels = []
clip3Display.DataAxesGrid.YAxisNotation = 'Mixed'
clip3Display.DataAxesGrid.YAxisPrecision = 2
clip3Display.DataAxesGrid.YAxisUseCustomLabels = 0
clip3Display.DataAxesGrid.YAxisLabels = []
clip3Display.DataAxesGrid.ZAxisNotation = 'Mixed'
clip3Display.DataAxesGrid.ZAxisPrecision = 2
clip3Display.DataAxesGrid.ZAxisUseCustomLabels = 0
clip3Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
clip3Display.PolarAxes.Visibility = 0
clip3Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
clip3Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
clip3Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
clip3Display.PolarAxes.EnableCustomRange = 0
clip3Display.PolarAxes.CustomRange = [0.0, 1.0]
clip3Display.PolarAxes.PolarAxisVisibility = 1
clip3Display.PolarAxes.RadialAxesVisibility = 1
clip3Display.PolarAxes.DrawRadialGridlines = 1
clip3Display.PolarAxes.PolarArcsVisibility = 1
clip3Display.PolarAxes.DrawPolarArcsGridlines = 1
clip3Display.PolarAxes.NumberOfRadialAxes = 0
clip3Display.PolarAxes.AutoSubdividePolarAxis = 1
clip3Display.PolarAxes.NumberOfPolarAxis = 0
clip3Display.PolarAxes.MinimumRadius = 0.0
clip3Display.PolarAxes.MinimumAngle = 0.0
clip3Display.PolarAxes.MaximumAngle = 90.0
clip3Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
clip3Display.PolarAxes.Ratio = 1.0
clip3Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
clip3Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
clip3Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
clip3Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
clip3Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
clip3Display.PolarAxes.PolarAxisTitleVisibility = 1
clip3Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
clip3Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
clip3Display.PolarAxes.PolarLabelVisibility = 1
clip3Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
clip3Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
clip3Display.PolarAxes.RadialLabelVisibility = 1
clip3Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
clip3Display.PolarAxes.RadialLabelLocation = 'Bottom'
clip3Display.PolarAxes.RadialUnitsVisibility = 1
clip3Display.PolarAxes.ScreenSize = 10.0
clip3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.PolarAxisTitleOpacity = 1.0
clip3Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
clip3Display.PolarAxes.PolarAxisTitleFontFile = ''
clip3Display.PolarAxes.PolarAxisTitleBold = 0
clip3Display.PolarAxes.PolarAxisTitleItalic = 0
clip3Display.PolarAxes.PolarAxisTitleShadow = 0
clip3Display.PolarAxes.PolarAxisTitleFontSize = 12
clip3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.PolarAxisLabelOpacity = 1.0
clip3Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
clip3Display.PolarAxes.PolarAxisLabelFontFile = ''
clip3Display.PolarAxes.PolarAxisLabelBold = 0
clip3Display.PolarAxes.PolarAxisLabelItalic = 0
clip3Display.PolarAxes.PolarAxisLabelShadow = 0
clip3Display.PolarAxes.PolarAxisLabelFontSize = 12
clip3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
clip3Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
clip3Display.PolarAxes.LastRadialAxisTextFontFile = ''
clip3Display.PolarAxes.LastRadialAxisTextBold = 0
clip3Display.PolarAxes.LastRadialAxisTextItalic = 0
clip3Display.PolarAxes.LastRadialAxisTextShadow = 0
clip3Display.PolarAxes.LastRadialAxisTextFontSize = 12
clip3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
clip3Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
clip3Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
clip3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
clip3Display.PolarAxes.SecondaryRadialAxesTextBold = 0
clip3Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
clip3Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
clip3Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
clip3Display.PolarAxes.EnableDistanceLOD = 1
clip3Display.PolarAxes.DistanceLODThreshold = 0.7
clip3Display.PolarAxes.EnableViewAngleLOD = 1
clip3Display.PolarAxes.ViewAngleLODThreshold = 0.7
clip3Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
clip3Display.PolarAxes.PolarTicksVisibility = 1
clip3Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
clip3Display.PolarAxes.TickLocation = 'Both'
clip3Display.PolarAxes.AxisTickVisibility = 1
clip3Display.PolarAxes.AxisMinorTickVisibility = 0
clip3Display.PolarAxes.ArcTickVisibility = 1
clip3Display.PolarAxes.ArcMinorTickVisibility = 0
clip3Display.PolarAxes.DeltaAngleMajor = 10.0
clip3Display.PolarAxes.DeltaAngleMinor = 5.0
clip3Display.PolarAxes.PolarAxisMajorTickSize = 0.0
clip3Display.PolarAxes.PolarAxisTickRatioSize = 0.3
clip3Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
clip3Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
clip3Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
clip3Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
clip3Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
clip3Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
clip3Display.PolarAxes.ArcMajorTickSize = 0.0
clip3Display.PolarAxes.ArcTickRatioSize = 0.3
clip3Display.PolarAxes.ArcMajorTickThickness = 1.0
clip3Display.PolarAxes.ArcTickRatioThickness = 0.5
clip3Display.PolarAxes.Use2DMode = 0
clip3Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(clip2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=clip3)
slice1.SliceType = 'Plane'
slice1.Crinkleslice = 0
slice1.Triangulatetheslice = 1
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.013999999035149813, -0.0020000000949949026, 0.0]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]
slice1.SliceType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.013999999035149813, -0.003, 0.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.013999999035149813, -0.003, 0.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

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
slice1Display.OSPRayScaleArray = 'U_mean'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.OSPRayMaterial = 'None'
slice1Display.Orient = 0
slice1Display.OrientationMode = 'Direction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.Scaling = 0
slice1Display.ScaleMode = 'No Data Scaling Off'
slice1Display.ScaleFactor = 0.004399999883025885
slice1Display.SelectScaleArray = 'None'
slice1Display.GlyphType = 'Arrow'
slice1Display.UseGlyphTable = 0
slice1Display.GlyphTableIndexArray = 'None'
slice1Display.UseCompositeGlyphTable = 0
slice1Display.UseGlyphCullingAndLOD = 0
slice1Display.LODValues = []
slice1Display.ColorByLODIndex = 0
slice1Display.GaussianRadius = 0.00021999999415129424
slice1Display.ShaderPreset = 'Sphere'
slice1Display.CustomTriangleScale = 3
slice1Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
slice1Display.Emissive = 0
slice1Display.ScaleByArray = 0
slice1Display.SetScaleArray = ['POINTS', 'U_mean']
slice1Display.ScaleArrayComponent = 'X'
slice1Display.UseScaleFunction = 1
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityByArray = 0
slice1Display.OpacityArray = ['POINTS', 'U_mean']
slice1Display.OpacityArrayComponent = 'X'
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
Hide(clip3, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U_mean', 'Magnitude'))

# rescale color and/or opacity maps used to include current data range
slice1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'U_mean'
u_meanLUT = GetColorTransferFunction('U_mean')
u_meanLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
u_meanLUT.InterpretValuesAsCategories = 0
u_meanLUT.AnnotationsInitialized = 0
u_meanLUT.ShowCategoricalColorsinDataRangeOnly = 0
u_meanLUT.RescaleOnVisibilityChange = 0
u_meanLUT.EnableOpacityMapping = 0
u_meanLUT.RGBPoints = [0.0, 0.231373, 0.298039, 0.752941, 0.8624250905416253, 0.865003, 0.865003, 0.865003, 1.7248501810832506, 0.705882, 0.0156863, 0.14902]
u_meanLUT.UseLogScale = 0
u_meanLUT.ColorSpace = 'Diverging'
u_meanLUT.UseBelowRangeColor = 0
u_meanLUT.BelowRangeColor = [0.0, 0.0, 0.0]
u_meanLUT.UseAboveRangeColor = 0
u_meanLUT.AboveRangeColor = [0.5, 0.5, 0.5]
u_meanLUT.NanColor = [1.0, 1.0, 0.0]
u_meanLUT.NanOpacity = 1.0
u_meanLUT.Discretize = 1
u_meanLUT.NumberOfTableValues = 256
u_meanLUT.ScalarRangeInitialized = 1.0
u_meanLUT.HSVWrap = 0
u_meanLUT.VectorComponent = 0
u_meanLUT.VectorMode = 'Magnitude'
u_meanLUT.AllowDuplicateScalars = 1
u_meanLUT.Annotations = []
u_meanLUT.ActiveAnnotatedValues = []
u_meanLUT.IndexedColors = []
u_meanLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'U_mean'
u_meanPWF = GetOpacityTransferFunction('U_mean')
u_meanPWF.Points = [0.0, 0.0, 0.5, 0.0, 1.7248501810832506, 1.0, 0.5, 0.0]
u_meanPWF.AllowDuplicateScalars = 1
u_meanPWF.UseLogScale = 0
u_meanPWF.ScalarRangeInitialized = 1

# set scalar coloring
ColorBy(slice1Display, ('POINTS', 'U_mean', 'Y'))

# rescale color and/or opacity maps used to exactly fit the current data range
slice1Display.RescaleTransferFunctionToDataRange(False, False)

# Update a scalar bar component title.
UpdateScalarBarsComponentTitle(u_meanLUT, slice1Display)

# get color legend/bar for u_meanLUT in view renderView1
u_meanLUTColorBar = GetScalarBar(u_meanLUT, renderView1)
u_meanLUTColorBar.AutoOrient = 1
u_meanLUTColorBar.Orientation = 'Vertical'
u_meanLUTColorBar.WindowLocation = 'LowerRightCorner'
u_meanLUTColorBar.Position = [0.89, 0.02]
u_meanLUTColorBar.Title = 'U_mean'
u_meanLUTColorBar.ComponentTitle = 'Y'
u_meanLUTColorBar.TitleJustification = 'Centered'
u_meanLUTColorBar.HorizontalTitle = 0
u_meanLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
u_meanLUTColorBar.TitleOpacity = 1.0
u_meanLUTColorBar.TitleFontFamily = 'Arial'
u_meanLUTColorBar.TitleFontFile = ''
u_meanLUTColorBar.TitleBold = 0
u_meanLUTColorBar.TitleItalic = 0
u_meanLUTColorBar.TitleShadow = 0
u_meanLUTColorBar.TitleFontSize = 16
u_meanLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
u_meanLUTColorBar.LabelOpacity = 1.0
u_meanLUTColorBar.LabelFontFamily = 'Arial'
u_meanLUTColorBar.LabelFontFile = ''
u_meanLUTColorBar.LabelBold = 0
u_meanLUTColorBar.LabelItalic = 0
u_meanLUTColorBar.LabelShadow = 0
u_meanLUTColorBar.LabelFontSize = 16
u_meanLUTColorBar.AutomaticLabelFormat = 1
u_meanLUTColorBar.LabelFormat = '%-#6.3g'
u_meanLUTColorBar.DrawTickMarks = 1
u_meanLUTColorBar.DrawTickLabels = 1
u_meanLUTColorBar.UseCustomLabels = 0
u_meanLUTColorBar.CustomLabels = []
u_meanLUTColorBar.AddRangeLabels = 1
u_meanLUTColorBar.RangeLabelFormat = '%-#6.1e'
u_meanLUTColorBar.DrawAnnotations = 1
u_meanLUTColorBar.AddRangeAnnotations = 0
u_meanLUTColorBar.AutomaticAnnotations = 0
u_meanLUTColorBar.DrawNanAnnotation = 0
u_meanLUTColorBar.NanAnnotation = 'NaN'
u_meanLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
u_meanLUTColorBar.ReverseLegend = 0
u_meanLUTColorBar.ScalarBarThickness = 16
u_meanLUTColorBar.ScalarBarLength = 0.33

# change scalar bar placement
u_meanLUTColorBar.Orientation = 'Horizontal'
u_meanLUTColorBar.WindowLocation = 'AnyLocation'
u_meanLUTColorBar.Position = [0.3032872928176798, 0.1888139281828075]
u_meanLUTColorBar.ScalarBarLength = 0.32999999999999935

# Properties modified on t_meanLUTColorBar
u_meanLUTColorBar.TitleFontSize = 4
u_meanLUTColorBar.LabelFontSize = 4
u_meanLUTColorBar.ScalarBarThickness = 5
u_meanLUTColorBar.ScalarBarLength = 0.5

# current camera placement for renderView1
renderView1.CameraPosition = [0.013999999035149813, -0.0893950302862747, 0.0]
renderView1.CameraFocalPoint = [0.013999999035149813, -0.003000000026077032, 0.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.022360679233547745

# save screenshot
SaveScreenshot('/store/8simu_tmp/shape_square/2a_3_T/Newtonian/Re4000/Uy_mean_slice_yNomal_y_Eq_neg3mm_test.png', renderView1, ImageResolution=[2896, 1834],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')
