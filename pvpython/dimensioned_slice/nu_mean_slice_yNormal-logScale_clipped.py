# trace generated using paraview version 5.6.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'OpenFOAMReader'
inlet_0p5foam = OpenFOAMReader(FileName='/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau/inlet_0p5/inlet_0p5.foam')
inlet_0p5foam.SkipZeroTime = 1
inlet_0p5foam.CaseType = 'Reconstructed Case'
inlet_0p5foam.LabelSize = '32-bit'
inlet_0p5foam.ScalarSize = '64-bit (DP)'
inlet_0p5foam.Createcelltopointfiltereddata = 1
inlet_0p5foam.Adddimensionalunitstoarraynames = 0
inlet_0p5foam.MeshRegions = ['internalMesh']
inlet_0p5foam.CellArrays = ['Q', 'T', 'T_mean', 'U', 'U_mean', 'k_mean', 'nu', 'nu_mean', 'p', 'reyTensor', 'reyTensor_mean', 'strainRate_U', 'vorticity_U', 'vorticity_U_mean']
inlet_0p5foam.PointArrays = []
inlet_0p5foam.LagrangianArrays = []
inlet_0p5foam.Cachemesh = 1
inlet_0p5foam.Decomposepolyhedra = 1
inlet_0p5foam.ListtimestepsaccordingtocontrolDict = 0
inlet_0p5foam.Lagrangianpositionswithoutextradata = 1
inlet_0p5foam.Readzones = 0
inlet_0p5foam.Copydatatocellzones = 0

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# Properties modified on inlet_0p5foam
inlet_0p5foam.CellArrays = ['nu_mean']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1267, 919]

# show data in view
inlet_0p5foamDisplay = Show(inlet_0p5foam, renderView1)

# trace defaults for the display properties.
inlet_0p5foamDisplay.Representation = 'Surface'
inlet_0p5foamDisplay.AmbientColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.ColorArrayName = [None, '']
inlet_0p5foamDisplay.DiffuseColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.LookupTable = None
inlet_0p5foamDisplay.MapScalars = 1
inlet_0p5foamDisplay.MultiComponentsMapping = 0
inlet_0p5foamDisplay.InterpolateScalarsBeforeMapping = 1
inlet_0p5foamDisplay.Opacity = 1.0
inlet_0p5foamDisplay.PointSize = 2.0
inlet_0p5foamDisplay.LineWidth = 1.0
inlet_0p5foamDisplay.RenderLinesAsTubes = 0
inlet_0p5foamDisplay.RenderPointsAsSpheres = 0
inlet_0p5foamDisplay.Interpolation = 'Gouraud'
inlet_0p5foamDisplay.Specular = 0.0
inlet_0p5foamDisplay.SpecularColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.SpecularPower = 100.0
inlet_0p5foamDisplay.Luminosity = 0.0
inlet_0p5foamDisplay.Ambient = 0.0
inlet_0p5foamDisplay.Diffuse = 1.0
inlet_0p5foamDisplay.EdgeColor = [0.0, 0.0, 0.5]
inlet_0p5foamDisplay.BackfaceRepresentation = 'Follow Frontface'
inlet_0p5foamDisplay.BackfaceAmbientColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.BackfaceOpacity = 1.0
inlet_0p5foamDisplay.Position = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.Scale = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.Orientation = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.Origin = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.Pickable = 1
inlet_0p5foamDisplay.Texture = None
inlet_0p5foamDisplay.Triangulate = 0
inlet_0p5foamDisplay.UseShaderReplacements = 0
inlet_0p5foamDisplay.ShaderReplacements = ''
inlet_0p5foamDisplay.NonlinearSubdivisionLevel = 1
inlet_0p5foamDisplay.UseDataPartitions = 0
inlet_0p5foamDisplay.OSPRayUseScaleArray = 0
inlet_0p5foamDisplay.OSPRayScaleArray = 'nu_mean'
inlet_0p5foamDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
inlet_0p5foamDisplay.OSPRayMaterial = 'None'
inlet_0p5foamDisplay.Orient = 0
inlet_0p5foamDisplay.OrientationMode = 'Direction'
inlet_0p5foamDisplay.SelectOrientationVectors = 'None'
inlet_0p5foamDisplay.Scaling = 0
inlet_0p5foamDisplay.ScaleMode = 'No Data Scaling Off'
inlet_0p5foamDisplay.ScaleFactor = 0.015999999642372132
inlet_0p5foamDisplay.SelectScaleArray = 'None'
inlet_0p5foamDisplay.GlyphType = 'Arrow'
inlet_0p5foamDisplay.UseGlyphTable = 0
inlet_0p5foamDisplay.GlyphTableIndexArray = 'None'
inlet_0p5foamDisplay.UseCompositeGlyphTable = 0
inlet_0p5foamDisplay.UseGlyphCullingAndLOD = 0
inlet_0p5foamDisplay.LODValues = []
inlet_0p5foamDisplay.ColorByLODIndex = 0
inlet_0p5foamDisplay.GaussianRadius = 0.0007999999821186066
inlet_0p5foamDisplay.ShaderPreset = 'Sphere'
inlet_0p5foamDisplay.CustomTriangleScale = 3
inlet_0p5foamDisplay.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
inlet_0p5foamDisplay.Emissive = 0
inlet_0p5foamDisplay.ScaleByArray = 0
inlet_0p5foamDisplay.SetScaleArray = ['POINTS', 'nu_mean']
inlet_0p5foamDisplay.ScaleArrayComponent = ''
inlet_0p5foamDisplay.UseScaleFunction = 1
inlet_0p5foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
inlet_0p5foamDisplay.OpacityByArray = 0
inlet_0p5foamDisplay.OpacityArray = ['POINTS', 'nu_mean']
inlet_0p5foamDisplay.OpacityArrayComponent = ''
inlet_0p5foamDisplay.OpacityTransferFunction = 'PiecewiseFunction'
inlet_0p5foamDisplay.DataAxesGrid = 'GridAxesRepresentation'
inlet_0p5foamDisplay.SelectionCellLabelBold = 0
inlet_0p5foamDisplay.SelectionCellLabelColor = [0.0, 1.0, 0.0]
inlet_0p5foamDisplay.SelectionCellLabelFontFamily = 'Arial'
inlet_0p5foamDisplay.SelectionCellLabelFontFile = ''
inlet_0p5foamDisplay.SelectionCellLabelFontSize = 18
inlet_0p5foamDisplay.SelectionCellLabelItalic = 0
inlet_0p5foamDisplay.SelectionCellLabelJustification = 'Left'
inlet_0p5foamDisplay.SelectionCellLabelOpacity = 1.0
inlet_0p5foamDisplay.SelectionCellLabelShadow = 0
inlet_0p5foamDisplay.SelectionPointLabelBold = 0
inlet_0p5foamDisplay.SelectionPointLabelColor = [1.0, 1.0, 0.0]
inlet_0p5foamDisplay.SelectionPointLabelFontFamily = 'Arial'
inlet_0p5foamDisplay.SelectionPointLabelFontFile = ''
inlet_0p5foamDisplay.SelectionPointLabelFontSize = 18
inlet_0p5foamDisplay.SelectionPointLabelItalic = 0
inlet_0p5foamDisplay.SelectionPointLabelJustification = 'Left'
inlet_0p5foamDisplay.SelectionPointLabelOpacity = 1.0
inlet_0p5foamDisplay.SelectionPointLabelShadow = 0
inlet_0p5foamDisplay.PolarAxes = 'PolarAxesRepresentation'
inlet_0p5foamDisplay.ScalarOpacityFunction = None
inlet_0p5foamDisplay.ScalarOpacityUnitDistance = 0.0006064726018038802
inlet_0p5foamDisplay.SelectMapper = 'Projected tetra'
inlet_0p5foamDisplay.SamplingDimensions = [128, 128, 128]
inlet_0p5foamDisplay.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
inlet_0p5foamDisplay.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
inlet_0p5foamDisplay.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
inlet_0p5foamDisplay.GlyphType.TipResolution = 6
inlet_0p5foamDisplay.GlyphType.TipRadius = 0.1
inlet_0p5foamDisplay.GlyphType.TipLength = 0.35
inlet_0p5foamDisplay.GlyphType.ShaftResolution = 6
inlet_0p5foamDisplay.GlyphType.ShaftRadius = 0.03
inlet_0p5foamDisplay.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
inlet_0p5foamDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
inlet_0p5foamDisplay.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
inlet_0p5foamDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
inlet_0p5foamDisplay.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
inlet_0p5foamDisplay.DataAxesGrid.XTitle = 'X Axis'
inlet_0p5foamDisplay.DataAxesGrid.YTitle = 'Y Axis'
inlet_0p5foamDisplay.DataAxesGrid.ZTitle = 'Z Axis'
inlet_0p5foamDisplay.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.DataAxesGrid.XTitleFontFamily = 'Arial'
inlet_0p5foamDisplay.DataAxesGrid.XTitleFontFile = ''
inlet_0p5foamDisplay.DataAxesGrid.XTitleBold = 0
inlet_0p5foamDisplay.DataAxesGrid.XTitleItalic = 0
inlet_0p5foamDisplay.DataAxesGrid.XTitleFontSize = 12
inlet_0p5foamDisplay.DataAxesGrid.XTitleShadow = 0
inlet_0p5foamDisplay.DataAxesGrid.XTitleOpacity = 1.0
inlet_0p5foamDisplay.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.DataAxesGrid.YTitleFontFamily = 'Arial'
inlet_0p5foamDisplay.DataAxesGrid.YTitleFontFile = ''
inlet_0p5foamDisplay.DataAxesGrid.YTitleBold = 0
inlet_0p5foamDisplay.DataAxesGrid.YTitleItalic = 0
inlet_0p5foamDisplay.DataAxesGrid.YTitleFontSize = 12
inlet_0p5foamDisplay.DataAxesGrid.YTitleShadow = 0
inlet_0p5foamDisplay.DataAxesGrid.YTitleOpacity = 1.0
inlet_0p5foamDisplay.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.DataAxesGrid.ZTitleFontFamily = 'Arial'
inlet_0p5foamDisplay.DataAxesGrid.ZTitleFontFile = ''
inlet_0p5foamDisplay.DataAxesGrid.ZTitleBold = 0
inlet_0p5foamDisplay.DataAxesGrid.ZTitleItalic = 0
inlet_0p5foamDisplay.DataAxesGrid.ZTitleFontSize = 12
inlet_0p5foamDisplay.DataAxesGrid.ZTitleShadow = 0
inlet_0p5foamDisplay.DataAxesGrid.ZTitleOpacity = 1.0
inlet_0p5foamDisplay.DataAxesGrid.FacesToRender = 63
inlet_0p5foamDisplay.DataAxesGrid.CullBackface = 0
inlet_0p5foamDisplay.DataAxesGrid.CullFrontface = 1
inlet_0p5foamDisplay.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.DataAxesGrid.ShowGrid = 0
inlet_0p5foamDisplay.DataAxesGrid.ShowEdges = 1
inlet_0p5foamDisplay.DataAxesGrid.ShowTicks = 1
inlet_0p5foamDisplay.DataAxesGrid.LabelUniqueEdgesOnly = 1
inlet_0p5foamDisplay.DataAxesGrid.AxesToLabel = 63
inlet_0p5foamDisplay.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.DataAxesGrid.XLabelFontFamily = 'Arial'
inlet_0p5foamDisplay.DataAxesGrid.XLabelFontFile = ''
inlet_0p5foamDisplay.DataAxesGrid.XLabelBold = 0
inlet_0p5foamDisplay.DataAxesGrid.XLabelItalic = 0
inlet_0p5foamDisplay.DataAxesGrid.XLabelFontSize = 12
inlet_0p5foamDisplay.DataAxesGrid.XLabelShadow = 0
inlet_0p5foamDisplay.DataAxesGrid.XLabelOpacity = 1.0
inlet_0p5foamDisplay.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.DataAxesGrid.YLabelFontFamily = 'Arial'
inlet_0p5foamDisplay.DataAxesGrid.YLabelFontFile = ''
inlet_0p5foamDisplay.DataAxesGrid.YLabelBold = 0
inlet_0p5foamDisplay.DataAxesGrid.YLabelItalic = 0
inlet_0p5foamDisplay.DataAxesGrid.YLabelFontSize = 12
inlet_0p5foamDisplay.DataAxesGrid.YLabelShadow = 0
inlet_0p5foamDisplay.DataAxesGrid.YLabelOpacity = 1.0
inlet_0p5foamDisplay.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.DataAxesGrid.ZLabelFontFamily = 'Arial'
inlet_0p5foamDisplay.DataAxesGrid.ZLabelFontFile = ''
inlet_0p5foamDisplay.DataAxesGrid.ZLabelBold = 0
inlet_0p5foamDisplay.DataAxesGrid.ZLabelItalic = 0
inlet_0p5foamDisplay.DataAxesGrid.ZLabelFontSize = 12
inlet_0p5foamDisplay.DataAxesGrid.ZLabelShadow = 0
inlet_0p5foamDisplay.DataAxesGrid.ZLabelOpacity = 1.0
inlet_0p5foamDisplay.DataAxesGrid.XAxisNotation = 'Mixed'
inlet_0p5foamDisplay.DataAxesGrid.XAxisPrecision = 2
inlet_0p5foamDisplay.DataAxesGrid.XAxisUseCustomLabels = 0
inlet_0p5foamDisplay.DataAxesGrid.XAxisLabels = []
inlet_0p5foamDisplay.DataAxesGrid.YAxisNotation = 'Mixed'
inlet_0p5foamDisplay.DataAxesGrid.YAxisPrecision = 2
inlet_0p5foamDisplay.DataAxesGrid.YAxisUseCustomLabels = 0
inlet_0p5foamDisplay.DataAxesGrid.YAxisLabels = []
inlet_0p5foamDisplay.DataAxesGrid.ZAxisNotation = 'Mixed'
inlet_0p5foamDisplay.DataAxesGrid.ZAxisPrecision = 2
inlet_0p5foamDisplay.DataAxesGrid.ZAxisUseCustomLabels = 0
inlet_0p5foamDisplay.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
inlet_0p5foamDisplay.PolarAxes.Visibility = 0
inlet_0p5foamDisplay.PolarAxes.Translation = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.PolarAxes.Scale = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.PolarAxes.Orientation = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.PolarAxes.EnableCustomBounds = [0, 0, 0]
inlet_0p5foamDisplay.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
inlet_0p5foamDisplay.PolarAxes.EnableCustomRange = 0
inlet_0p5foamDisplay.PolarAxes.CustomRange = [0.0, 1.0]
inlet_0p5foamDisplay.PolarAxes.PolarAxisVisibility = 1
inlet_0p5foamDisplay.PolarAxes.RadialAxesVisibility = 1
inlet_0p5foamDisplay.PolarAxes.DrawRadialGridlines = 1
inlet_0p5foamDisplay.PolarAxes.PolarArcsVisibility = 1
inlet_0p5foamDisplay.PolarAxes.DrawPolarArcsGridlines = 1
inlet_0p5foamDisplay.PolarAxes.NumberOfRadialAxes = 0
inlet_0p5foamDisplay.PolarAxes.AutoSubdividePolarAxis = 1
inlet_0p5foamDisplay.PolarAxes.NumberOfPolarAxis = 0
inlet_0p5foamDisplay.PolarAxes.MinimumRadius = 0.0
inlet_0p5foamDisplay.PolarAxes.MinimumAngle = 0.0
inlet_0p5foamDisplay.PolarAxes.MaximumAngle = 90.0
inlet_0p5foamDisplay.PolarAxes.RadialAxesOriginToPolarAxis = 1
inlet_0p5foamDisplay.PolarAxes.Ratio = 1.0
inlet_0p5foamDisplay.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleVisibility = 1
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitle = 'Radial Distance'
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleLocation = 'Bottom'
inlet_0p5foamDisplay.PolarAxes.PolarLabelVisibility = 1
inlet_0p5foamDisplay.PolarAxes.PolarLabelFormat = '%-#6.3g'
inlet_0p5foamDisplay.PolarAxes.PolarLabelExponentLocation = 'Labels'
inlet_0p5foamDisplay.PolarAxes.RadialLabelVisibility = 1
inlet_0p5foamDisplay.PolarAxes.RadialLabelFormat = '%-#3.1f'
inlet_0p5foamDisplay.PolarAxes.RadialLabelLocation = 'Bottom'
inlet_0p5foamDisplay.PolarAxes.RadialUnitsVisibility = 1
inlet_0p5foamDisplay.PolarAxes.ScreenSize = 10.0
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleOpacity = 1.0
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleFontFile = ''
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleBold = 0
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleItalic = 0
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleShadow = 0
inlet_0p5foamDisplay.PolarAxes.PolarAxisTitleFontSize = 12
inlet_0p5foamDisplay.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.PolarAxes.PolarAxisLabelOpacity = 1.0
inlet_0p5foamDisplay.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
inlet_0p5foamDisplay.PolarAxes.PolarAxisLabelFontFile = ''
inlet_0p5foamDisplay.PolarAxes.PolarAxisLabelBold = 0
inlet_0p5foamDisplay.PolarAxes.PolarAxisLabelItalic = 0
inlet_0p5foamDisplay.PolarAxes.PolarAxisLabelShadow = 0
inlet_0p5foamDisplay.PolarAxes.PolarAxisLabelFontSize = 12
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTextOpacity = 1.0
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTextFontFile = ''
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTextBold = 0
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTextItalic = 0
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTextShadow = 0
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTextFontSize = 12
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesTextFontFile = ''
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesTextBold = 0
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesTextItalic = 0
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesTextShadow = 0
inlet_0p5foamDisplay.PolarAxes.SecondaryRadialAxesTextFontSize = 12
inlet_0p5foamDisplay.PolarAxes.EnableDistanceLOD = 1
inlet_0p5foamDisplay.PolarAxes.DistanceLODThreshold = 0.7
inlet_0p5foamDisplay.PolarAxes.EnableViewAngleLOD = 1
inlet_0p5foamDisplay.PolarAxes.ViewAngleLODThreshold = 0.7
inlet_0p5foamDisplay.PolarAxes.SmallestVisiblePolarAngle = 0.5
inlet_0p5foamDisplay.PolarAxes.PolarTicksVisibility = 1
inlet_0p5foamDisplay.PolarAxes.ArcTicksOriginToPolarAxis = 1
inlet_0p5foamDisplay.PolarAxes.TickLocation = 'Both'
inlet_0p5foamDisplay.PolarAxes.AxisTickVisibility = 1
inlet_0p5foamDisplay.PolarAxes.AxisMinorTickVisibility = 0
inlet_0p5foamDisplay.PolarAxes.ArcTickVisibility = 1
inlet_0p5foamDisplay.PolarAxes.ArcMinorTickVisibility = 0
inlet_0p5foamDisplay.PolarAxes.DeltaAngleMajor = 10.0
inlet_0p5foamDisplay.PolarAxes.DeltaAngleMinor = 5.0
inlet_0p5foamDisplay.PolarAxes.PolarAxisMajorTickSize = 0.0
inlet_0p5foamDisplay.PolarAxes.PolarAxisTickRatioSize = 0.3
inlet_0p5foamDisplay.PolarAxes.PolarAxisMajorTickThickness = 1.0
inlet_0p5foamDisplay.PolarAxes.PolarAxisTickRatioThickness = 0.5
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisMajorTickSize = 0.0
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTickRatioSize = 0.3
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
inlet_0p5foamDisplay.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
inlet_0p5foamDisplay.PolarAxes.ArcMajorTickSize = 0.0
inlet_0p5foamDisplay.PolarAxes.ArcTickRatioSize = 0.3
inlet_0p5foamDisplay.PolarAxes.ArcMajorTickThickness = 1.0
inlet_0p5foamDisplay.PolarAxes.ArcTickRatioThickness = 0.5
inlet_0p5foamDisplay.PolarAxes.Use2DMode = 0
inlet_0p5foamDisplay.PolarAxes.UseLogAxis = 0

# reset view to fit data
renderView1.ResetCamera()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip1 = Clip(Input=inlet_0p5foam)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'nu_mean']
clip1.Value = 0.0001377613546083012
clip1.Invert = 1
clip1.Crinkleclip = 0
clip1.Exact = 0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, -0.037999999010935426, 0.0]
clip1.ClipType.Normal = [1.0, 0.0, 0.0]
clip1.ClipType.Offset = 0.0

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [-0.008, -0.037999999010935426, 0.0]

# Properties modified on clip1
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
clip1Display.OSPRayScaleArray = 'nu_mean'
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
clip1Display.SetScaleArray = ['POINTS', 'nu_mean']
clip1Display.ScaleArrayComponent = ''
clip1Display.UseScaleFunction = 1
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityByArray = 0
clip1Display.OpacityArray = ['POINTS', 'nu_mean']
clip1Display.OpacityArrayComponent = ''
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
Hide(inlet_0p5foam, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Clip'
clip2 = Clip(Input=clip1)
clip2.ClipType = 'Plane'
clip2.Scalars = ['POINTS', 'nu_mean']
clip2.Value = 0.0001377613546083012
clip2.Invert = 1
clip2.Crinkleclip = 0
clip2.Exact = 0

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.03599999891594052, -0.037999999010935426, 0.0]
clip2.ClipType.Normal = [1.0, 0.0, 0.0]
clip2.ClipType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip2.ClipType)

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
clip2Display.OSPRayScaleArray = 'nu_mean'
clip2Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip2Display.OSPRayMaterial = 'None'
clip2Display.Orient = 0
clip2Display.OrientationMode = 'Direction'
clip2Display.SelectOrientationVectors = 'None'
clip2Display.Scaling = 0
clip2Display.ScaleMode = 'No Data Scaling Off'
clip2Display.ScaleFactor = 0.008399999840185047
clip2Display.SelectScaleArray = 'None'
clip2Display.GlyphType = 'Arrow'
clip2Display.UseGlyphTable = 0
clip2Display.GlyphTableIndexArray = 'None'
clip2Display.UseCompositeGlyphTable = 0
clip2Display.UseGlyphCullingAndLOD = 0
clip2Display.LODValues = []
clip2Display.ColorByLODIndex = 0
clip2Display.GaussianRadius = 0.0004199999920092523
clip2Display.ShaderPreset = 'Sphere'
clip2Display.CustomTriangleScale = 3
clip2Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
clip2Display.Emissive = 0
clip2Display.ScaleByArray = 0
clip2Display.SetScaleArray = ['POINTS', 'nu_mean']
clip2Display.ScaleArrayComponent = ''
clip2Display.UseScaleFunction = 1
clip2Display.ScaleTransferFunction = 'PiecewiseFunction'
clip2Display.OpacityByArray = 0
clip2Display.OpacityArray = ['POINTS', 'nu_mean']
clip2Display.OpacityArrayComponent = ''
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
clip2Display.ScalarOpacityUnitDistance = 0.00034954614837155165
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

# create a new 'Slice'
slice1 = Slice(Input=clip2)
slice1.SliceType = 'Plane'
slice1.Crinkleslice = 0
slice1.Triangulatetheslice = 1
slice1.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.013999999035149813, -0.037999999010935426, 0.0]
slice1.SliceType.Normal = [1.0, 0.0, 0.0]
slice1.SliceType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice1.SliceType)

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.013999999035149813, 0.0, 0.0]
slice1.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice1.SliceType
slice1.SliceType.Origin = [0.013999999035149813, 0.0, 0.0]
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
slice1Display.OSPRayScaleArray = 'nu_mean'
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
Hide(clip2, renderView1)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data
renderView1.ResetCamera()

# reset view to fit data
renderView1.ResetCamera()

# set scalar coloring
ColorBy(slice1Display, ('CELLS', 'nu_mean'))

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
nu_meanLUT.RGBPoints = [2.4401779228355736e-06, 0.231373, 0.298039, 0.752941, 7.711203761573415e-05, 0.865003, 0.865003, 0.865003, 0.00015178389730863273, 0.705882, 0.0156863, 0.14902]
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
nu_meanPWF.Points = [2.4401779228355736e-06, 0.0, 0.5, 0.0, 0.00015178389730863273, 1.0, 0.5, 0.0]
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
nu_meanLUTColorBar.Position = [0.300426203630624, 0.7306093579978237]
nu_meanLUTColorBar.ScalarBarLength = 0.32999999999999996

# reset view to fit data bounds
renderView1.ResetCamera(-0.00800000037998, 0.0359999984503, -1.54074395551e-33, 0.0, -0.00400000018999, 0.00400000018999)

# current camera placement for renderView1
renderView1.CameraPosition = [0.013999999035149813, -0.08639503026019767, 0.0]
renderView1.CameraFocalPoint = [0.013999999035149813, -7.703719777548943e-34, 0.0]
renderView1.CameraViewUp = [0.0, 0.0, 1.0]
renderView1.CameraParallelScale = 0.022360679233547745

# save screenshot
SaveScreenshot('/store/8simu_tmp/shape_square/2a_3_T/BirdCarreau/inlet_0p5/nu_mean_slice_yNormal_y_Eq_0mm.png', renderView1, ImageResolution=[2534, 1835],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')
