# trace generated using paraview version 5.6.0-RC2
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

import sys

dirName = sys.argv[1]

# create a new 'OpenFOAMReader'
re4000foam = OpenFOAMReader(FileName=dirName+'/Re4000.foam')
re4000foam.SkipZeroTime = 1
re4000foam.CaseType = 'Reconstructed Case'
re4000foam.LabelSize = '32-bit'
re4000foam.ScalarSize = '64-bit (DP)'
re4000foam.Createcelltopointfiltereddata = 1
re4000foam.Adddimensionalunitstoarraynames = 0
re4000foam.MeshRegions = ['internalMesh']
re4000foam.CellArrays = ['Q', 'T', 'T_mean', 'U', 'U_mean', 'k_mean', 'p', 'reyTensor', 'reyTensor_mean', 'strainRate_U', 'tt_mean', 'vorticity_U', 'vorticity_U_mean']
re4000foam.PointArrays = []
re4000foam.LagrangianArrays = []
re4000foam.Cachemesh = 1
re4000foam.Decomposepolyhedra = 1
re4000foam.ListtimestepsaccordingtocontrolDict = 0
re4000foam.Lagrangianpositionswithoutextradata = 1
re4000foam.Readzones = 0
re4000foam.Copydatatocellzones = 0

# Properties modified on re4000foam
re4000foam.CellArrays = ['vorticity_U_mean']

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1281, 919]

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
re4000foamDisplay.OSPRayScaleArray = 'vorticity_U_mean'
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
re4000foamDisplay.SetScaleArray = ['POINTS', 'vorticity_U_mean']
re4000foamDisplay.ScaleArrayComponent = 'X'
re4000foamDisplay.UseScaleFunction = 1
re4000foamDisplay.ScaleTransferFunction = 'PiecewiseFunction'
re4000foamDisplay.OpacityByArray = 0
re4000foamDisplay.OpacityArray = ['POINTS', 'vorticity_U_mean']
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

# create a new 'Calculator'
calculator1 = Calculator(Input=re4000foam)
calculator1.AttributeType = 'Point Data'
calculator1.CoordinateResults = 0
calculator1.ResultNormals = 0
calculator1.ResultTCoords = 0
calculator1.ResultArrayName = 'Result'
calculator1.Function = ''
calculator1.ReplaceInvalidResults = 1
calculator1.ReplacementValue = 0.0
calculator1.ResultArrayType = 'Double'

# Properties modified on calculator1
calculator1.ResultArrayName = 'omega_x'
calculator1.Function = 'vorticity_U_mean_X'

# show data in view
calculator1Display = Show(calculator1, renderView1)

# get color transfer function/color map for 'omega_x'
omega_xLUT = GetColorTransferFunction('omega_x')
omega_xLUT.AutomaticRescaleRangeMode = "Grow and update on 'Apply'"
omega_xLUT.InterpretValuesAsCategories = 0
omega_xLUT.AnnotationsInitialized = 0
omega_xLUT.ShowCategoricalColorsinDataRangeOnly = 0
omega_xLUT.RescaleOnVisibilityChange = 0
omega_xLUT.EnableOpacityMapping = 0
omega_xLUT.RGBPoints = [-70094.078125, 0.231373, 0.298039, 0.752941, 748.7109375, 0.865003, 0.865003, 0.865003, 71591.5, 0.705882, 0.0156863, 0.14902]
omega_xLUT.UseLogScale = 0
omega_xLUT.ColorSpace = 'Diverging'
omega_xLUT.UseBelowRangeColor = 0
omega_xLUT.BelowRangeColor = [0.0, 0.0, 0.0]
omega_xLUT.UseAboveRangeColor = 0
omega_xLUT.AboveRangeColor = [0.5, 0.5, 0.5]
omega_xLUT.NanColor = [1.0, 1.0, 0.0]
omega_xLUT.NanOpacity = 1.0
omega_xLUT.Discretize = 1
omega_xLUT.NumberOfTableValues = 256
omega_xLUT.ScalarRangeInitialized = 1.0
omega_xLUT.HSVWrap = 0
omega_xLUT.VectorComponent = 0
omega_xLUT.VectorMode = 'Magnitude'
omega_xLUT.AllowDuplicateScalars = 1
omega_xLUT.Annotations = []
omega_xLUT.ActiveAnnotatedValues = []
omega_xLUT.IndexedColors = []
omega_xLUT.IndexedOpacities = []

# get opacity transfer function/opacity map for 'omega_x'
omega_xPWF = GetOpacityTransferFunction('omega_x')
omega_xPWF.Points = [-70094.078125, 0.0, 0.5, 0.0, 71591.5, 1.0, 0.5, 0.0]
omega_xPWF.AllowDuplicateScalars = 1
omega_xPWF.UseLogScale = 0
omega_xPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
calculator1Display.Representation = 'Surface'
calculator1Display.AmbientColor = [1.0, 1.0, 1.0]
calculator1Display.ColorArrayName = ['POINTS', 'omega_x']
calculator1Display.DiffuseColor = [1.0, 1.0, 1.0]
calculator1Display.LookupTable = omega_xLUT
calculator1Display.MapScalars = 1
calculator1Display.MultiComponentsMapping = 0
calculator1Display.InterpolateScalarsBeforeMapping = 1
calculator1Display.Opacity = 1.0
calculator1Display.PointSize = 2.0
calculator1Display.LineWidth = 1.0
calculator1Display.RenderLinesAsTubes = 0
calculator1Display.RenderPointsAsSpheres = 0
calculator1Display.Interpolation = 'Gouraud'
calculator1Display.Specular = 0.0
calculator1Display.SpecularColor = [1.0, 1.0, 1.0]
calculator1Display.SpecularPower = 100.0
calculator1Display.Luminosity = 0.0
calculator1Display.Ambient = 0.0
calculator1Display.Diffuse = 1.0
calculator1Display.EdgeColor = [0.0, 0.0, 0.5]
calculator1Display.BackfaceRepresentation = 'Follow Frontface'
calculator1Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
calculator1Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
calculator1Display.BackfaceOpacity = 1.0
calculator1Display.Position = [0.0, 0.0, 0.0]
calculator1Display.Scale = [1.0, 1.0, 1.0]
calculator1Display.Orientation = [0.0, 0.0, 0.0]
calculator1Display.Origin = [0.0, 0.0, 0.0]
calculator1Display.Pickable = 1
calculator1Display.Texture = None
calculator1Display.Triangulate = 0
calculator1Display.UseShaderReplacements = 0
calculator1Display.ShaderReplacements = ''
calculator1Display.NonlinearSubdivisionLevel = 1
calculator1Display.UseDataPartitions = 0
calculator1Display.OSPRayUseScaleArray = 0
calculator1Display.OSPRayScaleArray = 'omega_x'
calculator1Display.OSPRayScaleFunction = 'PiecewiseFunction'
calculator1Display.OSPRayMaterial = 'None'
calculator1Display.Orient = 0
calculator1Display.OrientationMode = 'Direction'
calculator1Display.SelectOrientationVectors = 'None'
calculator1Display.Scaling = 0
calculator1Display.ScaleMode = 'No Data Scaling Off'
calculator1Display.ScaleFactor = 0.015999999642372132
calculator1Display.SelectScaleArray = 'omega_x'
calculator1Display.GlyphType = 'Arrow'
calculator1Display.UseGlyphTable = 0
calculator1Display.GlyphTableIndexArray = 'omega_x'
calculator1Display.UseCompositeGlyphTable = 0
calculator1Display.UseGlyphCullingAndLOD = 0
calculator1Display.LODValues = []
calculator1Display.ColorByLODIndex = 0
calculator1Display.GaussianRadius = 0.0007999999821186066
calculator1Display.ShaderPreset = 'Sphere'
calculator1Display.CustomTriangleScale = 3
calculator1Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
calculator1Display.Emissive = 0
calculator1Display.ScaleByArray = 0
calculator1Display.SetScaleArray = ['POINTS', 'omega_x']
calculator1Display.ScaleArrayComponent = ''
calculator1Display.UseScaleFunction = 1
calculator1Display.ScaleTransferFunction = 'PiecewiseFunction'
calculator1Display.OpacityByArray = 0
calculator1Display.OpacityArray = ['POINTS', 'omega_x']
calculator1Display.OpacityArrayComponent = ''
calculator1Display.OpacityTransferFunction = 'PiecewiseFunction'
calculator1Display.DataAxesGrid = 'GridAxesRepresentation'
calculator1Display.SelectionCellLabelBold = 0
calculator1Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
calculator1Display.SelectionCellLabelFontFamily = 'Arial'
calculator1Display.SelectionCellLabelFontFile = ''
calculator1Display.SelectionCellLabelFontSize = 18
calculator1Display.SelectionCellLabelItalic = 0
calculator1Display.SelectionCellLabelJustification = 'Left'
calculator1Display.SelectionCellLabelOpacity = 1.0
calculator1Display.SelectionCellLabelShadow = 0
calculator1Display.SelectionPointLabelBold = 0
calculator1Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
calculator1Display.SelectionPointLabelFontFamily = 'Arial'
calculator1Display.SelectionPointLabelFontFile = ''
calculator1Display.SelectionPointLabelFontSize = 18
calculator1Display.SelectionPointLabelItalic = 0
calculator1Display.SelectionPointLabelJustification = 'Left'
calculator1Display.SelectionPointLabelOpacity = 1.0
calculator1Display.SelectionPointLabelShadow = 0
calculator1Display.PolarAxes = 'PolarAxesRepresentation'
calculator1Display.ScalarOpacityFunction = omega_xPWF
calculator1Display.ScalarOpacityUnitDistance = 0.0006064726018038802
calculator1Display.SelectMapper = 'Projected tetra'
calculator1Display.SamplingDimensions = [128, 128, 128]
calculator1Display.UseFloatingPointFrameBuffer = 1

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
calculator1Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
calculator1Display.GlyphType.TipResolution = 6
calculator1Display.GlyphType.TipRadius = 0.1
calculator1Display.GlyphType.TipLength = 0.35
calculator1Display.GlyphType.ShaftResolution = 6
calculator1Display.GlyphType.ShaftRadius = 0.03
calculator1Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
calculator1Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
calculator1Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
calculator1Display.DataAxesGrid.XTitle = 'X Axis'
calculator1Display.DataAxesGrid.YTitle = 'Y Axis'
calculator1Display.DataAxesGrid.ZTitle = 'Z Axis'
calculator1Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.XTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XTitleFontFile = ''
calculator1Display.DataAxesGrid.XTitleBold = 0
calculator1Display.DataAxesGrid.XTitleItalic = 0
calculator1Display.DataAxesGrid.XTitleFontSize = 12
calculator1Display.DataAxesGrid.XTitleShadow = 0
calculator1Display.DataAxesGrid.XTitleOpacity = 1.0
calculator1Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.YTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YTitleFontFile = ''
calculator1Display.DataAxesGrid.YTitleBold = 0
calculator1Display.DataAxesGrid.YTitleItalic = 0
calculator1Display.DataAxesGrid.YTitleFontSize = 12
calculator1Display.DataAxesGrid.YTitleShadow = 0
calculator1Display.DataAxesGrid.YTitleOpacity = 1.0
calculator1Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZTitleFontFile = ''
calculator1Display.DataAxesGrid.ZTitleBold = 0
calculator1Display.DataAxesGrid.ZTitleItalic = 0
calculator1Display.DataAxesGrid.ZTitleFontSize = 12
calculator1Display.DataAxesGrid.ZTitleShadow = 0
calculator1Display.DataAxesGrid.ZTitleOpacity = 1.0
calculator1Display.DataAxesGrid.FacesToRender = 63
calculator1Display.DataAxesGrid.CullBackface = 0
calculator1Display.DataAxesGrid.CullFrontface = 1
calculator1Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
calculator1Display.DataAxesGrid.ShowGrid = 0
calculator1Display.DataAxesGrid.ShowEdges = 1
calculator1Display.DataAxesGrid.ShowTicks = 1
calculator1Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
calculator1Display.DataAxesGrid.AxesToLabel = 63
calculator1Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.XLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.XLabelFontFile = ''
calculator1Display.DataAxesGrid.XLabelBold = 0
calculator1Display.DataAxesGrid.XLabelItalic = 0
calculator1Display.DataAxesGrid.XLabelFontSize = 12
calculator1Display.DataAxesGrid.XLabelShadow = 0
calculator1Display.DataAxesGrid.XLabelOpacity = 1.0
calculator1Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.YLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.YLabelFontFile = ''
calculator1Display.DataAxesGrid.YLabelBold = 0
calculator1Display.DataAxesGrid.YLabelItalic = 0
calculator1Display.DataAxesGrid.YLabelFontSize = 12
calculator1Display.DataAxesGrid.YLabelShadow = 0
calculator1Display.DataAxesGrid.YLabelOpacity = 1.0
calculator1Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
calculator1Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
calculator1Display.DataAxesGrid.ZLabelFontFile = ''
calculator1Display.DataAxesGrid.ZLabelBold = 0
calculator1Display.DataAxesGrid.ZLabelItalic = 0
calculator1Display.DataAxesGrid.ZLabelFontSize = 12
calculator1Display.DataAxesGrid.ZLabelShadow = 0
calculator1Display.DataAxesGrid.ZLabelOpacity = 1.0
calculator1Display.DataAxesGrid.XAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.XAxisPrecision = 2
calculator1Display.DataAxesGrid.XAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.XAxisLabels = []
calculator1Display.DataAxesGrid.YAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.YAxisPrecision = 2
calculator1Display.DataAxesGrid.YAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.YAxisLabels = []
calculator1Display.DataAxesGrid.ZAxisNotation = 'Mixed'
calculator1Display.DataAxesGrid.ZAxisPrecision = 2
calculator1Display.DataAxesGrid.ZAxisUseCustomLabels = 0
calculator1Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
calculator1Display.PolarAxes.Visibility = 0
calculator1Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
calculator1Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
calculator1Display.PolarAxes.EnableCustomRange = 0
calculator1Display.PolarAxes.CustomRange = [0.0, 1.0]
calculator1Display.PolarAxes.PolarAxisVisibility = 1
calculator1Display.PolarAxes.RadialAxesVisibility = 1
calculator1Display.PolarAxes.DrawRadialGridlines = 1
calculator1Display.PolarAxes.PolarArcsVisibility = 1
calculator1Display.PolarAxes.DrawPolarArcsGridlines = 1
calculator1Display.PolarAxes.NumberOfRadialAxes = 0
calculator1Display.PolarAxes.AutoSubdividePolarAxis = 1
calculator1Display.PolarAxes.NumberOfPolarAxis = 0
calculator1Display.PolarAxes.MinimumRadius = 0.0
calculator1Display.PolarAxes.MinimumAngle = 0.0
calculator1Display.PolarAxes.MaximumAngle = 90.0
calculator1Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
calculator1Display.PolarAxes.Ratio = 1.0
calculator1Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
calculator1Display.PolarAxes.PolarAxisTitleVisibility = 1
calculator1Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
calculator1Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
calculator1Display.PolarAxes.PolarLabelVisibility = 1
calculator1Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
calculator1Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
calculator1Display.PolarAxes.RadialLabelVisibility = 1
calculator1Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
calculator1Display.PolarAxes.RadialLabelLocation = 'Bottom'
calculator1Display.PolarAxes.RadialUnitsVisibility = 1
calculator1Display.PolarAxes.ScreenSize = 10.0
calculator1Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.PolarAxisTitleOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisTitleFontFile = ''
calculator1Display.PolarAxes.PolarAxisTitleBold = 0
calculator1Display.PolarAxes.PolarAxisTitleItalic = 0
calculator1Display.PolarAxes.PolarAxisTitleShadow = 0
calculator1Display.PolarAxes.PolarAxisTitleFontSize = 12
calculator1Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.PolarAxisLabelOpacity = 1.0
calculator1Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
calculator1Display.PolarAxes.PolarAxisLabelFontFile = ''
calculator1Display.PolarAxes.PolarAxisLabelBold = 0
calculator1Display.PolarAxes.PolarAxisLabelItalic = 0
calculator1Display.PolarAxes.PolarAxisLabelShadow = 0
calculator1Display.PolarAxes.PolarAxisLabelFontSize = 12
calculator1Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
calculator1Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
calculator1Display.PolarAxes.LastRadialAxisTextFontFile = ''
calculator1Display.PolarAxes.LastRadialAxisTextBold = 0
calculator1Display.PolarAxes.LastRadialAxisTextItalic = 0
calculator1Display.PolarAxes.LastRadialAxisTextShadow = 0
calculator1Display.PolarAxes.LastRadialAxisTextFontSize = 12
calculator1Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
calculator1Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
calculator1Display.PolarAxes.SecondaryRadialAxesTextBold = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
calculator1Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
calculator1Display.PolarAxes.EnableDistanceLOD = 1
calculator1Display.PolarAxes.DistanceLODThreshold = 0.7
calculator1Display.PolarAxes.EnableViewAngleLOD = 1
calculator1Display.PolarAxes.ViewAngleLODThreshold = 0.7
calculator1Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
calculator1Display.PolarAxes.PolarTicksVisibility = 1
calculator1Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
calculator1Display.PolarAxes.TickLocation = 'Both'
calculator1Display.PolarAxes.AxisTickVisibility = 1
calculator1Display.PolarAxes.AxisMinorTickVisibility = 0
calculator1Display.PolarAxes.ArcTickVisibility = 1
calculator1Display.PolarAxes.ArcMinorTickVisibility = 0
calculator1Display.PolarAxes.DeltaAngleMajor = 10.0
calculator1Display.PolarAxes.DeltaAngleMinor = 5.0
calculator1Display.PolarAxes.PolarAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.PolarAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
calculator1Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
calculator1Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
calculator1Display.PolarAxes.ArcMajorTickSize = 0.0
calculator1Display.PolarAxes.ArcTickRatioSize = 0.3
calculator1Display.PolarAxes.ArcMajorTickThickness = 1.0
calculator1Display.PolarAxes.ArcTickRatioThickness = 0.5
calculator1Display.PolarAxes.Use2DMode = 0
calculator1Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(re4000foam, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice1 = Slice(Input=calculator1)
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

# show data in view
slice1Display = Show(slice1, renderView1)

# trace defaults for the display properties.
slice1Display.Representation = 'Surface'
slice1Display.AmbientColor = [1.0, 1.0, 1.0]
slice1Display.ColorArrayName = ['POINTS', 'omega_x']
slice1Display.DiffuseColor = [1.0, 1.0, 1.0]
slice1Display.LookupTable = omega_xLUT
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
slice1Display.OSPRayScaleArray = 'omega_x'
slice1Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice1Display.OSPRayMaterial = 'None'
slice1Display.Orient = 0
slice1Display.OrientationMode = 'Direction'
slice1Display.SelectOrientationVectors = 'None'
slice1Display.Scaling = 0
slice1Display.ScaleMode = 'No Data Scaling Off'
slice1Display.ScaleFactor = 0.008399999840185047
slice1Display.SelectScaleArray = 'omega_x'
slice1Display.GlyphType = 'Arrow'
slice1Display.UseGlyphTable = 0
slice1Display.GlyphTableIndexArray = 'omega_x'
slice1Display.UseCompositeGlyphTable = 0
slice1Display.UseGlyphCullingAndLOD = 0
slice1Display.LODValues = []
slice1Display.ColorByLODIndex = 0
slice1Display.GaussianRadius = 0.0004199999920092523
slice1Display.ShaderPreset = 'Sphere'
slice1Display.CustomTriangleScale = 3
slice1Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
slice1Display.Emissive = 0
slice1Display.ScaleByArray = 0
slice1Display.SetScaleArray = ['POINTS', 'omega_x']
slice1Display.ScaleArrayComponent = ''
slice1Display.UseScaleFunction = 1
slice1Display.ScaleTransferFunction = 'PiecewiseFunction'
slice1Display.OpacityByArray = 0
slice1Display.OpacityArray = ['POINTS', 'omega_x']
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
Hide(calculator1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# create a new 'Slice'
slice2 = Slice(Input=slice1)
slice2.SliceType = 'Plane'
slice2.Crinkleslice = 0
slice2.Triangulatetheslice = 1
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [0.0, -0.037999999010935426, 0.0]
slice2.SliceType.Normal = [1.0, 0.0, 0.0]
slice2.SliceType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice2.SliceType)

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.0, -0.0012, 0.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.0, -0.0012, 0.0]
slice2.SliceType.Normal = [0.0, 1.0, 0.0]

# show data in view
slice2Display = Show(slice2, renderView1)

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.AmbientColor = [1.0, 1.0, 1.0]
slice2Display.ColorArrayName = ['POINTS', 'omega_x']
slice2Display.DiffuseColor = [1.0, 1.0, 1.0]
slice2Display.LookupTable = omega_xLUT
slice2Display.MapScalars = 1
slice2Display.MultiComponentsMapping = 0
slice2Display.InterpolateScalarsBeforeMapping = 1
slice2Display.Opacity = 1.0
slice2Display.PointSize = 2.0
slice2Display.LineWidth = 1.0
slice2Display.RenderLinesAsTubes = 0
slice2Display.RenderPointsAsSpheres = 0
slice2Display.Interpolation = 'Gouraud'
slice2Display.Specular = 0.0
slice2Display.SpecularColor = [1.0, 1.0, 1.0]
slice2Display.SpecularPower = 100.0
slice2Display.Luminosity = 0.0
slice2Display.Ambient = 0.0
slice2Display.Diffuse = 1.0
slice2Display.EdgeColor = [0.0, 0.0, 0.5]
slice2Display.BackfaceRepresentation = 'Follow Frontface'
slice2Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
slice2Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
slice2Display.BackfaceOpacity = 1.0
slice2Display.Position = [0.0, 0.0, 0.0]
slice2Display.Scale = [1.0, 1.0, 1.0]
slice2Display.Orientation = [0.0, 0.0, 0.0]
slice2Display.Origin = [0.0, 0.0, 0.0]
slice2Display.Pickable = 1
slice2Display.Texture = None
slice2Display.Triangulate = 0
slice2Display.UseShaderReplacements = 0
slice2Display.ShaderReplacements = ''
slice2Display.NonlinearSubdivisionLevel = 1
slice2Display.UseDataPartitions = 0
slice2Display.OSPRayUseScaleArray = 0
slice2Display.OSPRayScaleArray = 'omega_x'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.OSPRayMaterial = 'None'
slice2Display.Orient = 0
slice2Display.OrientationMode = 'Direction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.Scaling = 0
slice2Display.ScaleMode = 'No Data Scaling Off'
slice2Display.ScaleFactor = 0.000800000037997961
slice2Display.SelectScaleArray = 'omega_x'
slice2Display.GlyphType = 'Arrow'
slice2Display.UseGlyphTable = 0
slice2Display.GlyphTableIndexArray = 'omega_x'
slice2Display.UseCompositeGlyphTable = 0
slice2Display.UseGlyphCullingAndLOD = 0
slice2Display.LODValues = []
slice2Display.ColorByLODIndex = 0
slice2Display.GaussianRadius = 4.0000001899898055e-05
slice2Display.ShaderPreset = 'Sphere'
slice2Display.CustomTriangleScale = 3
slice2Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
slice2Display.Emissive = 0
slice2Display.ScaleByArray = 0
slice2Display.SetScaleArray = ['POINTS', 'omega_x']
slice2Display.ScaleArrayComponent = ''
slice2Display.UseScaleFunction = 1
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityByArray = 0
slice2Display.OpacityArray = ['POINTS', 'omega_x']
slice2Display.OpacityArrayComponent = ''
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.SelectionCellLabelBold = 0
slice2Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
slice2Display.SelectionCellLabelFontFamily = 'Arial'
slice2Display.SelectionCellLabelFontFile = ''
slice2Display.SelectionCellLabelFontSize = 18
slice2Display.SelectionCellLabelItalic = 0
slice2Display.SelectionCellLabelJustification = 'Left'
slice2Display.SelectionCellLabelOpacity = 1.0
slice2Display.SelectionCellLabelShadow = 0
slice2Display.SelectionPointLabelBold = 0
slice2Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
slice2Display.SelectionPointLabelFontFamily = 'Arial'
slice2Display.SelectionPointLabelFontFile = ''
slice2Display.SelectionPointLabelFontSize = 18
slice2Display.SelectionPointLabelItalic = 0
slice2Display.SelectionPointLabelJustification = 'Left'
slice2Display.SelectionPointLabelOpacity = 1.0
slice2Display.SelectionPointLabelShadow = 0
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice2Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice2Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
slice2Display.GlyphType.TipResolution = 6
slice2Display.GlyphType.TipRadius = 0.1
slice2Display.GlyphType.TipLength = 0.35
slice2Display.GlyphType.ShaftResolution = 6
slice2Display.GlyphType.ShaftRadius = 0.03
slice2Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice2Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice2Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice2Display.DataAxesGrid.XTitle = 'X Axis'
slice2Display.DataAxesGrid.YTitle = 'Y Axis'
slice2Display.DataAxesGrid.ZTitle = 'Z Axis'
slice2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.XTitleFontFamily = 'Arial'
slice2Display.DataAxesGrid.XTitleFontFile = ''
slice2Display.DataAxesGrid.XTitleBold = 0
slice2Display.DataAxesGrid.XTitleItalic = 0
slice2Display.DataAxesGrid.XTitleFontSize = 12
slice2Display.DataAxesGrid.XTitleShadow = 0
slice2Display.DataAxesGrid.XTitleOpacity = 1.0
slice2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.YTitleFontFamily = 'Arial'
slice2Display.DataAxesGrid.YTitleFontFile = ''
slice2Display.DataAxesGrid.YTitleBold = 0
slice2Display.DataAxesGrid.YTitleItalic = 0
slice2Display.DataAxesGrid.YTitleFontSize = 12
slice2Display.DataAxesGrid.YTitleShadow = 0
slice2Display.DataAxesGrid.YTitleOpacity = 1.0
slice2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
slice2Display.DataAxesGrid.ZTitleFontFile = ''
slice2Display.DataAxesGrid.ZTitleBold = 0
slice2Display.DataAxesGrid.ZTitleItalic = 0
slice2Display.DataAxesGrid.ZTitleFontSize = 12
slice2Display.DataAxesGrid.ZTitleShadow = 0
slice2Display.DataAxesGrid.ZTitleOpacity = 1.0
slice2Display.DataAxesGrid.FacesToRender = 63
slice2Display.DataAxesGrid.CullBackface = 0
slice2Display.DataAxesGrid.CullFrontface = 1
slice2Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
slice2Display.DataAxesGrid.ShowGrid = 0
slice2Display.DataAxesGrid.ShowEdges = 1
slice2Display.DataAxesGrid.ShowTicks = 1
slice2Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
slice2Display.DataAxesGrid.AxesToLabel = 63
slice2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.XLabelFontFamily = 'Arial'
slice2Display.DataAxesGrid.XLabelFontFile = ''
slice2Display.DataAxesGrid.XLabelBold = 0
slice2Display.DataAxesGrid.XLabelItalic = 0
slice2Display.DataAxesGrid.XLabelFontSize = 12
slice2Display.DataAxesGrid.XLabelShadow = 0
slice2Display.DataAxesGrid.XLabelOpacity = 1.0
slice2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.YLabelFontFamily = 'Arial'
slice2Display.DataAxesGrid.YLabelFontFile = ''
slice2Display.DataAxesGrid.YLabelBold = 0
slice2Display.DataAxesGrid.YLabelItalic = 0
slice2Display.DataAxesGrid.YLabelFontSize = 12
slice2Display.DataAxesGrid.YLabelShadow = 0
slice2Display.DataAxesGrid.YLabelOpacity = 1.0
slice2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
slice2Display.DataAxesGrid.ZLabelFontFile = ''
slice2Display.DataAxesGrid.ZLabelBold = 0
slice2Display.DataAxesGrid.ZLabelItalic = 0
slice2Display.DataAxesGrid.ZLabelFontSize = 12
slice2Display.DataAxesGrid.ZLabelShadow = 0
slice2Display.DataAxesGrid.ZLabelOpacity = 1.0
slice2Display.DataAxesGrid.XAxisNotation = 'Mixed'
slice2Display.DataAxesGrid.XAxisPrecision = 2
slice2Display.DataAxesGrid.XAxisUseCustomLabels = 0
slice2Display.DataAxesGrid.XAxisLabels = []
slice2Display.DataAxesGrid.YAxisNotation = 'Mixed'
slice2Display.DataAxesGrid.YAxisPrecision = 2
slice2Display.DataAxesGrid.YAxisUseCustomLabels = 0
slice2Display.DataAxesGrid.YAxisLabels = []
slice2Display.DataAxesGrid.ZAxisNotation = 'Mixed'
slice2Display.DataAxesGrid.ZAxisPrecision = 2
slice2Display.DataAxesGrid.ZAxisUseCustomLabels = 0
slice2Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice2Display.PolarAxes.Visibility = 0
slice2Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
slice2Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
slice2Display.PolarAxes.EnableCustomRange = 0
slice2Display.PolarAxes.CustomRange = [0.0, 1.0]
slice2Display.PolarAxes.PolarAxisVisibility = 1
slice2Display.PolarAxes.RadialAxesVisibility = 1
slice2Display.PolarAxes.DrawRadialGridlines = 1
slice2Display.PolarAxes.PolarArcsVisibility = 1
slice2Display.PolarAxes.DrawPolarArcsGridlines = 1
slice2Display.PolarAxes.NumberOfRadialAxes = 0
slice2Display.PolarAxes.AutoSubdividePolarAxis = 1
slice2Display.PolarAxes.NumberOfPolarAxis = 0
slice2Display.PolarAxes.MinimumRadius = 0.0
slice2Display.PolarAxes.MinimumAngle = 0.0
slice2Display.PolarAxes.MaximumAngle = 90.0
slice2Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
slice2Display.PolarAxes.Ratio = 1.0
slice2Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.PolarAxisTitleVisibility = 1
slice2Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
slice2Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
slice2Display.PolarAxes.PolarLabelVisibility = 1
slice2Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
slice2Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
slice2Display.PolarAxes.RadialLabelVisibility = 1
slice2Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
slice2Display.PolarAxes.RadialLabelLocation = 'Bottom'
slice2Display.PolarAxes.RadialUnitsVisibility = 1
slice2Display.PolarAxes.ScreenSize = 10.0
slice2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.PolarAxisTitleOpacity = 1.0
slice2Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
slice2Display.PolarAxes.PolarAxisTitleFontFile = ''
slice2Display.PolarAxes.PolarAxisTitleBold = 0
slice2Display.PolarAxes.PolarAxisTitleItalic = 0
slice2Display.PolarAxes.PolarAxisTitleShadow = 0
slice2Display.PolarAxes.PolarAxisTitleFontSize = 12
slice2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.PolarAxisLabelOpacity = 1.0
slice2Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
slice2Display.PolarAxes.PolarAxisLabelFontFile = ''
slice2Display.PolarAxes.PolarAxisLabelBold = 0
slice2Display.PolarAxes.PolarAxisLabelItalic = 0
slice2Display.PolarAxes.PolarAxisLabelShadow = 0
slice2Display.PolarAxes.PolarAxisLabelFontSize = 12
slice2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
slice2Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
slice2Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice2Display.PolarAxes.LastRadialAxisTextBold = 0
slice2Display.PolarAxes.LastRadialAxisTextItalic = 0
slice2Display.PolarAxes.LastRadialAxisTextShadow = 0
slice2Display.PolarAxes.LastRadialAxisTextFontSize = 12
slice2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
slice2Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
slice2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
slice2Display.PolarAxes.SecondaryRadialAxesTextBold = 0
slice2Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
slice2Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
slice2Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
slice2Display.PolarAxes.EnableDistanceLOD = 1
slice2Display.PolarAxes.DistanceLODThreshold = 0.7
slice2Display.PolarAxes.EnableViewAngleLOD = 1
slice2Display.PolarAxes.ViewAngleLODThreshold = 0.7
slice2Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
slice2Display.PolarAxes.PolarTicksVisibility = 1
slice2Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
slice2Display.PolarAxes.TickLocation = 'Both'
slice2Display.PolarAxes.AxisTickVisibility = 1
slice2Display.PolarAxes.AxisMinorTickVisibility = 0
slice2Display.PolarAxes.ArcTickVisibility = 1
slice2Display.PolarAxes.ArcMinorTickVisibility = 0
slice2Display.PolarAxes.DeltaAngleMajor = 10.0
slice2Display.PolarAxes.DeltaAngleMinor = 5.0
slice2Display.PolarAxes.PolarAxisMajorTickSize = 0.0
slice2Display.PolarAxes.PolarAxisTickRatioSize = 0.3
slice2Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
slice2Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
slice2Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
slice2Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
slice2Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
slice2Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
slice2Display.PolarAxes.ArcMajorTickSize = 0.0
slice2Display.PolarAxes.ArcTickRatioSize = 0.3
slice2Display.PolarAxes.ArcMajorTickThickness = 1.0
slice2Display.PolarAxes.ArcTickRatioThickness = 0.5
slice2Display.PolarAxes.Use2DMode = 0
slice2Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(slice1, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice1)

# hide data in view
Hide(slice2, renderView1)

# show data in view
slice1Display = Show(slice1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# destroy slice2
Delete(slice2)
del slice2

# create a new 'Clip'
clip1 = Clip(Input=slice1)
clip1.ClipType = 'Plane'
clip1.Scalars = ['POINTS', 'omega_x']
clip1.Value = 425.8291015624641
clip1.Invert = 1
clip1.Crinkleclip = 0
clip1.Exact = 0

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.0, -0.037999999010935426, 0.0]
clip1.ClipType.Normal = [1.0, 0.0, 0.0]
clip1.ClipType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=clip1.ClipType)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, -0.0012, 0.0]
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# Properties modified on clip1
clip1.Invert = 0

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, -0.0012, 0.0]
clip1.ClipType.Normal = [0.0, 1.0, 0.0]

# show data in view
clip1Display = Show(clip1, renderView1)

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'
clip1Display.AmbientColor = [1.0, 1.0, 1.0]
clip1Display.ColorArrayName = ['POINTS', 'omega_x']
clip1Display.DiffuseColor = [1.0, 1.0, 1.0]
clip1Display.LookupTable = omega_xLUT
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
clip1Display.OSPRayScaleArray = 'omega_x'
clip1Display.OSPRayScaleFunction = 'PiecewiseFunction'
clip1Display.OSPRayMaterial = 'None'
clip1Display.Orient = 0
clip1Display.OrientationMode = 'Direction'
clip1Display.SelectOrientationVectors = 'None'
clip1Display.Scaling = 0
clip1Display.ScaleMode = 'No Data Scaling Off'
clip1Display.ScaleFactor = 0.000800000037997961
clip1Display.SelectScaleArray = 'omega_x'
clip1Display.GlyphType = 'Arrow'
clip1Display.UseGlyphTable = 0
clip1Display.GlyphTableIndexArray = 'omega_x'
clip1Display.UseCompositeGlyphTable = 0
clip1Display.UseGlyphCullingAndLOD = 0
clip1Display.LODValues = []
clip1Display.ColorByLODIndex = 0
clip1Display.GaussianRadius = 4.0000001899898055e-05
clip1Display.ShaderPreset = 'Sphere'
clip1Display.CustomTriangleScale = 3
clip1Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
clip1Display.Emissive = 0
clip1Display.ScaleByArray = 0
clip1Display.SetScaleArray = ['POINTS', 'omega_x']
clip1Display.ScaleArrayComponent = ''
clip1Display.UseScaleFunction = 1
clip1Display.ScaleTransferFunction = 'PiecewiseFunction'
clip1Display.OpacityByArray = 0
clip1Display.OpacityArray = ['POINTS', 'omega_x']
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
clip1Display.ScalarOpacityFunction = omega_xPWF
clip1Display.ScalarOpacityUnitDistance = 0.0003521818740566494
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
Hide(slice1, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data bounds
renderView1.ResetCamera(-3.85185988877e-34, 3.85185988877e-34, -0.001200000057, 0.00400000018999, -0.00400000018999, 0.00400000018999)

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(slice1)

# show data in view
slice1Display = Show(slice1, renderView1)

# show color bar/color legend
slice1Display.SetScalarBarVisibility(renderView1, True)

# hide data in view
Hide(slice1, renderView1)

# set active source
SetActiveSource(calculator1)

# create a new 'Slice'
slice2 = Slice(Input=calculator1)
slice2.SliceType = 'Plane'
slice2.Crinkleslice = 0
slice2.Triangulatetheslice = 1
slice2.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice2.SliceType.Origin = [0.0, -0.037999999010935426, 0.0]
slice2.SliceType.Normal = [1.0, 0.0, 0.0]
slice2.SliceType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice2.SliceType)

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.0041, -0.037999999010935426, 0.0]

# Properties modified on slice2.SliceType
slice2.SliceType.Origin = [0.0041, -0.037999999010935426, 0.0]

# show data in view
slice2Display = Show(slice2, renderView1)

# trace defaults for the display properties.
slice2Display.Representation = 'Surface'
slice2Display.AmbientColor = [1.0, 1.0, 1.0]
slice2Display.ColorArrayName = ['POINTS', 'omega_x']
slice2Display.DiffuseColor = [1.0, 1.0, 1.0]
slice2Display.LookupTable = omega_xLUT
slice2Display.MapScalars = 1
slice2Display.MultiComponentsMapping = 0
slice2Display.InterpolateScalarsBeforeMapping = 1
slice2Display.Opacity = 1.0
slice2Display.PointSize = 2.0
slice2Display.LineWidth = 1.0
slice2Display.RenderLinesAsTubes = 0
slice2Display.RenderPointsAsSpheres = 0
slice2Display.Interpolation = 'Gouraud'
slice2Display.Specular = 0.0
slice2Display.SpecularColor = [1.0, 1.0, 1.0]
slice2Display.SpecularPower = 100.0
slice2Display.Luminosity = 0.0
slice2Display.Ambient = 0.0
slice2Display.Diffuse = 1.0
slice2Display.EdgeColor = [0.0, 0.0, 0.5]
slice2Display.BackfaceRepresentation = 'Follow Frontface'
slice2Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
slice2Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
slice2Display.BackfaceOpacity = 1.0
slice2Display.Position = [0.0, 0.0, 0.0]
slice2Display.Scale = [1.0, 1.0, 1.0]
slice2Display.Orientation = [0.0, 0.0, 0.0]
slice2Display.Origin = [0.0, 0.0, 0.0]
slice2Display.Pickable = 1
slice2Display.Texture = None
slice2Display.Triangulate = 0
slice2Display.UseShaderReplacements = 0
slice2Display.ShaderReplacements = ''
slice2Display.NonlinearSubdivisionLevel = 1
slice2Display.UseDataPartitions = 0
slice2Display.OSPRayUseScaleArray = 0
slice2Display.OSPRayScaleArray = 'omega_x'
slice2Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice2Display.OSPRayMaterial = 'None'
slice2Display.Orient = 0
slice2Display.OrientationMode = 'Direction'
slice2Display.SelectOrientationVectors = 'None'
slice2Display.Scaling = 0
slice2Display.ScaleMode = 'No Data Scaling Off'
slice2Display.ScaleFactor = 0.000800000037997961
slice2Display.SelectScaleArray = 'omega_x'
slice2Display.GlyphType = 'Arrow'
slice2Display.UseGlyphTable = 0
slice2Display.GlyphTableIndexArray = 'omega_x'
slice2Display.UseCompositeGlyphTable = 0
slice2Display.UseGlyphCullingAndLOD = 0
slice2Display.LODValues = []
slice2Display.ColorByLODIndex = 0
slice2Display.GaussianRadius = 4.0000001899898055e-05
slice2Display.ShaderPreset = 'Sphere'
slice2Display.CustomTriangleScale = 3
slice2Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
slice2Display.Emissive = 0
slice2Display.ScaleByArray = 0
slice2Display.SetScaleArray = ['POINTS', 'omega_x']
slice2Display.ScaleArrayComponent = ''
slice2Display.UseScaleFunction = 1
slice2Display.ScaleTransferFunction = 'PiecewiseFunction'
slice2Display.OpacityByArray = 0
slice2Display.OpacityArray = ['POINTS', 'omega_x']
slice2Display.OpacityArrayComponent = ''
slice2Display.OpacityTransferFunction = 'PiecewiseFunction'
slice2Display.DataAxesGrid = 'GridAxesRepresentation'
slice2Display.SelectionCellLabelBold = 0
slice2Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
slice2Display.SelectionCellLabelFontFamily = 'Arial'
slice2Display.SelectionCellLabelFontFile = ''
slice2Display.SelectionCellLabelFontSize = 18
slice2Display.SelectionCellLabelItalic = 0
slice2Display.SelectionCellLabelJustification = 'Left'
slice2Display.SelectionCellLabelOpacity = 1.0
slice2Display.SelectionCellLabelShadow = 0
slice2Display.SelectionPointLabelBold = 0
slice2Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
slice2Display.SelectionPointLabelFontFamily = 'Arial'
slice2Display.SelectionPointLabelFontFile = ''
slice2Display.SelectionPointLabelFontSize = 18
slice2Display.SelectionPointLabelItalic = 0
slice2Display.SelectionPointLabelJustification = 'Left'
slice2Display.SelectionPointLabelOpacity = 1.0
slice2Display.SelectionPointLabelShadow = 0
slice2Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice2Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice2Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
slice2Display.GlyphType.TipResolution = 6
slice2Display.GlyphType.TipRadius = 0.1
slice2Display.GlyphType.TipLength = 0.35
slice2Display.GlyphType.ShaftResolution = 6
slice2Display.GlyphType.ShaftRadius = 0.03
slice2Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice2Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice2Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice2Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice2Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice2Display.DataAxesGrid.XTitle = 'X Axis'
slice2Display.DataAxesGrid.YTitle = 'Y Axis'
slice2Display.DataAxesGrid.ZTitle = 'Z Axis'
slice2Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.XTitleFontFamily = 'Arial'
slice2Display.DataAxesGrid.XTitleFontFile = ''
slice2Display.DataAxesGrid.XTitleBold = 0
slice2Display.DataAxesGrid.XTitleItalic = 0
slice2Display.DataAxesGrid.XTitleFontSize = 12
slice2Display.DataAxesGrid.XTitleShadow = 0
slice2Display.DataAxesGrid.XTitleOpacity = 1.0
slice2Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.YTitleFontFamily = 'Arial'
slice2Display.DataAxesGrid.YTitleFontFile = ''
slice2Display.DataAxesGrid.YTitleBold = 0
slice2Display.DataAxesGrid.YTitleItalic = 0
slice2Display.DataAxesGrid.YTitleFontSize = 12
slice2Display.DataAxesGrid.YTitleShadow = 0
slice2Display.DataAxesGrid.YTitleOpacity = 1.0
slice2Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
slice2Display.DataAxesGrid.ZTitleFontFile = ''
slice2Display.DataAxesGrid.ZTitleBold = 0
slice2Display.DataAxesGrid.ZTitleItalic = 0
slice2Display.DataAxesGrid.ZTitleFontSize = 12
slice2Display.DataAxesGrid.ZTitleShadow = 0
slice2Display.DataAxesGrid.ZTitleOpacity = 1.0
slice2Display.DataAxesGrid.FacesToRender = 63
slice2Display.DataAxesGrid.CullBackface = 0
slice2Display.DataAxesGrid.CullFrontface = 1
slice2Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
slice2Display.DataAxesGrid.ShowGrid = 0
slice2Display.DataAxesGrid.ShowEdges = 1
slice2Display.DataAxesGrid.ShowTicks = 1
slice2Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
slice2Display.DataAxesGrid.AxesToLabel = 63
slice2Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.XLabelFontFamily = 'Arial'
slice2Display.DataAxesGrid.XLabelFontFile = ''
slice2Display.DataAxesGrid.XLabelBold = 0
slice2Display.DataAxesGrid.XLabelItalic = 0
slice2Display.DataAxesGrid.XLabelFontSize = 12
slice2Display.DataAxesGrid.XLabelShadow = 0
slice2Display.DataAxesGrid.XLabelOpacity = 1.0
slice2Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.YLabelFontFamily = 'Arial'
slice2Display.DataAxesGrid.YLabelFontFile = ''
slice2Display.DataAxesGrid.YLabelBold = 0
slice2Display.DataAxesGrid.YLabelItalic = 0
slice2Display.DataAxesGrid.YLabelFontSize = 12
slice2Display.DataAxesGrid.YLabelShadow = 0
slice2Display.DataAxesGrid.YLabelOpacity = 1.0
slice2Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice2Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
slice2Display.DataAxesGrid.ZLabelFontFile = ''
slice2Display.DataAxesGrid.ZLabelBold = 0
slice2Display.DataAxesGrid.ZLabelItalic = 0
slice2Display.DataAxesGrid.ZLabelFontSize = 12
slice2Display.DataAxesGrid.ZLabelShadow = 0
slice2Display.DataAxesGrid.ZLabelOpacity = 1.0
slice2Display.DataAxesGrid.XAxisNotation = 'Mixed'
slice2Display.DataAxesGrid.XAxisPrecision = 2
slice2Display.DataAxesGrid.XAxisUseCustomLabels = 0
slice2Display.DataAxesGrid.XAxisLabels = []
slice2Display.DataAxesGrid.YAxisNotation = 'Mixed'
slice2Display.DataAxesGrid.YAxisPrecision = 2
slice2Display.DataAxesGrid.YAxisUseCustomLabels = 0
slice2Display.DataAxesGrid.YAxisLabels = []
slice2Display.DataAxesGrid.ZAxisNotation = 'Mixed'
slice2Display.DataAxesGrid.ZAxisPrecision = 2
slice2Display.DataAxesGrid.ZAxisUseCustomLabels = 0
slice2Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice2Display.PolarAxes.Visibility = 0
slice2Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
slice2Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
slice2Display.PolarAxes.EnableCustomRange = 0
slice2Display.PolarAxes.CustomRange = [0.0, 1.0]
slice2Display.PolarAxes.PolarAxisVisibility = 1
slice2Display.PolarAxes.RadialAxesVisibility = 1
slice2Display.PolarAxes.DrawRadialGridlines = 1
slice2Display.PolarAxes.PolarArcsVisibility = 1
slice2Display.PolarAxes.DrawPolarArcsGridlines = 1
slice2Display.PolarAxes.NumberOfRadialAxes = 0
slice2Display.PolarAxes.AutoSubdividePolarAxis = 1
slice2Display.PolarAxes.NumberOfPolarAxis = 0
slice2Display.PolarAxes.MinimumRadius = 0.0
slice2Display.PolarAxes.MinimumAngle = 0.0
slice2Display.PolarAxes.MaximumAngle = 90.0
slice2Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
slice2Display.PolarAxes.Ratio = 1.0
slice2Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
slice2Display.PolarAxes.PolarAxisTitleVisibility = 1
slice2Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
slice2Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
slice2Display.PolarAxes.PolarLabelVisibility = 1
slice2Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
slice2Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
slice2Display.PolarAxes.RadialLabelVisibility = 1
slice2Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
slice2Display.PolarAxes.RadialLabelLocation = 'Bottom'
slice2Display.PolarAxes.RadialUnitsVisibility = 1
slice2Display.PolarAxes.ScreenSize = 10.0
slice2Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.PolarAxisTitleOpacity = 1.0
slice2Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
slice2Display.PolarAxes.PolarAxisTitleFontFile = ''
slice2Display.PolarAxes.PolarAxisTitleBold = 0
slice2Display.PolarAxes.PolarAxisTitleItalic = 0
slice2Display.PolarAxes.PolarAxisTitleShadow = 0
slice2Display.PolarAxes.PolarAxisTitleFontSize = 12
slice2Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.PolarAxisLabelOpacity = 1.0
slice2Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
slice2Display.PolarAxes.PolarAxisLabelFontFile = ''
slice2Display.PolarAxes.PolarAxisLabelBold = 0
slice2Display.PolarAxes.PolarAxisLabelItalic = 0
slice2Display.PolarAxes.PolarAxisLabelShadow = 0
slice2Display.PolarAxes.PolarAxisLabelFontSize = 12
slice2Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
slice2Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
slice2Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice2Display.PolarAxes.LastRadialAxisTextBold = 0
slice2Display.PolarAxes.LastRadialAxisTextItalic = 0
slice2Display.PolarAxes.LastRadialAxisTextShadow = 0
slice2Display.PolarAxes.LastRadialAxisTextFontSize = 12
slice2Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
slice2Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
slice2Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
slice2Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
slice2Display.PolarAxes.SecondaryRadialAxesTextBold = 0
slice2Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
slice2Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
slice2Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
slice2Display.PolarAxes.EnableDistanceLOD = 1
slice2Display.PolarAxes.DistanceLODThreshold = 0.7
slice2Display.PolarAxes.EnableViewAngleLOD = 1
slice2Display.PolarAxes.ViewAngleLODThreshold = 0.7
slice2Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
slice2Display.PolarAxes.PolarTicksVisibility = 1
slice2Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
slice2Display.PolarAxes.TickLocation = 'Both'
slice2Display.PolarAxes.AxisTickVisibility = 1
slice2Display.PolarAxes.AxisMinorTickVisibility = 0
slice2Display.PolarAxes.ArcTickVisibility = 1
slice2Display.PolarAxes.ArcMinorTickVisibility = 0
slice2Display.PolarAxes.DeltaAngleMajor = 10.0
slice2Display.PolarAxes.DeltaAngleMinor = 5.0
slice2Display.PolarAxes.PolarAxisMajorTickSize = 0.0
slice2Display.PolarAxes.PolarAxisTickRatioSize = 0.3
slice2Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
slice2Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
slice2Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
slice2Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
slice2Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
slice2Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
slice2Display.PolarAxes.ArcMajorTickSize = 0.0
slice2Display.PolarAxes.ArcTickRatioSize = 0.3
slice2Display.PolarAxes.ArcMajorTickThickness = 1.0
slice2Display.PolarAxes.ArcTickRatioThickness = 0.5
slice2Display.PolarAxes.Use2DMode = 0
slice2Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
slice2Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(calculator1)

# create a new 'Slice'
slice3 = Slice(Input=calculator1)
slice3.SliceType = 'Plane'
slice3.Crinkleslice = 0
slice3.Triangulatetheslice = 1
slice3.SliceOffsetValues = [0.0]

# init the 'Plane' selected for 'SliceType'
slice3.SliceType.Origin = [0.0, -0.037999999010935426, 0.0]
slice3.SliceType.Normal = [1.0, 0.0, 0.0]
slice3.SliceType.Offset = 0.0

# toggle 3D widget visibility (only when running from the GUI)
Hide3DWidgets(proxy=slice3.SliceType)

# Properties modified on slice3.SliceType
slice3.SliceType.Origin = [0.008, -0.037999999010935426, 0.0]

# Properties modified on slice3.SliceType
slice3.SliceType.Origin = [0.008, -0.037999999010935426, 0.0]

# show data in view
slice3Display = Show(slice3, renderView1)

# trace defaults for the display properties.
slice3Display.Representation = 'Surface'
slice3Display.AmbientColor = [1.0, 1.0, 1.0]
slice3Display.ColorArrayName = ['POINTS', 'omega_x']
slice3Display.DiffuseColor = [1.0, 1.0, 1.0]
slice3Display.LookupTable = omega_xLUT
slice3Display.MapScalars = 1
slice3Display.MultiComponentsMapping = 0
slice3Display.InterpolateScalarsBeforeMapping = 1
slice3Display.Opacity = 1.0
slice3Display.PointSize = 2.0
slice3Display.LineWidth = 1.0
slice3Display.RenderLinesAsTubes = 0
slice3Display.RenderPointsAsSpheres = 0
slice3Display.Interpolation = 'Gouraud'
slice3Display.Specular = 0.0
slice3Display.SpecularColor = [1.0, 1.0, 1.0]
slice3Display.SpecularPower = 100.0
slice3Display.Luminosity = 0.0
slice3Display.Ambient = 0.0
slice3Display.Diffuse = 1.0
slice3Display.EdgeColor = [0.0, 0.0, 0.5]
slice3Display.BackfaceRepresentation = 'Follow Frontface'
slice3Display.BackfaceAmbientColor = [1.0, 1.0, 1.0]
slice3Display.BackfaceDiffuseColor = [1.0, 1.0, 1.0]
slice3Display.BackfaceOpacity = 1.0
slice3Display.Position = [0.0, 0.0, 0.0]
slice3Display.Scale = [1.0, 1.0, 1.0]
slice3Display.Orientation = [0.0, 0.0, 0.0]
slice3Display.Origin = [0.0, 0.0, 0.0]
slice3Display.Pickable = 1
slice3Display.Texture = None
slice3Display.Triangulate = 0
slice3Display.UseShaderReplacements = 0
slice3Display.ShaderReplacements = ''
slice3Display.NonlinearSubdivisionLevel = 1
slice3Display.UseDataPartitions = 0
slice3Display.OSPRayUseScaleArray = 0
slice3Display.OSPRayScaleArray = 'omega_x'
slice3Display.OSPRayScaleFunction = 'PiecewiseFunction'
slice3Display.OSPRayMaterial = 'None'
slice3Display.Orient = 0
slice3Display.OrientationMode = 'Direction'
slice3Display.SelectOrientationVectors = 'None'
slice3Display.Scaling = 0
slice3Display.ScaleMode = 'No Data Scaling Off'
slice3Display.ScaleFactor = 0.000800000037997961
slice3Display.SelectScaleArray = 'omega_x'
slice3Display.GlyphType = 'Arrow'
slice3Display.UseGlyphTable = 0
slice3Display.GlyphTableIndexArray = 'omega_x'
slice3Display.UseCompositeGlyphTable = 0
slice3Display.UseGlyphCullingAndLOD = 0
slice3Display.LODValues = []
slice3Display.ColorByLODIndex = 0
slice3Display.GaussianRadius = 4.0000001899898055e-05
slice3Display.ShaderPreset = 'Sphere'
slice3Display.CustomTriangleScale = 3
slice3Display.CustomShader = ' // This custom shader code define a gaussian blur\n // Please take a look into vtkSMPointGaussianRepresentation.cxx\n // for other custom shader examples\n //VTK::Color::Impl\n   float dist2 = dot(offsetVCVSOutput.xy,offsetVCVSOutput.xy);\n   float gaussian = exp(-0.5*dist2);\n   opacity = opacity*gaussian;\n'
slice3Display.Emissive = 0
slice3Display.ScaleByArray = 0
slice3Display.SetScaleArray = ['POINTS', 'omega_x']
slice3Display.ScaleArrayComponent = ''
slice3Display.UseScaleFunction = 1
slice3Display.ScaleTransferFunction = 'PiecewiseFunction'
slice3Display.OpacityByArray = 0
slice3Display.OpacityArray = ['POINTS', 'omega_x']
slice3Display.OpacityArrayComponent = ''
slice3Display.OpacityTransferFunction = 'PiecewiseFunction'
slice3Display.DataAxesGrid = 'GridAxesRepresentation'
slice3Display.SelectionCellLabelBold = 0
slice3Display.SelectionCellLabelColor = [0.0, 1.0, 0.0]
slice3Display.SelectionCellLabelFontFamily = 'Arial'
slice3Display.SelectionCellLabelFontFile = ''
slice3Display.SelectionCellLabelFontSize = 18
slice3Display.SelectionCellLabelItalic = 0
slice3Display.SelectionCellLabelJustification = 'Left'
slice3Display.SelectionCellLabelOpacity = 1.0
slice3Display.SelectionCellLabelShadow = 0
slice3Display.SelectionPointLabelBold = 0
slice3Display.SelectionPointLabelColor = [1.0, 1.0, 0.0]
slice3Display.SelectionPointLabelFontFamily = 'Arial'
slice3Display.SelectionPointLabelFontFile = ''
slice3Display.SelectionPointLabelFontSize = 18
slice3Display.SelectionPointLabelItalic = 0
slice3Display.SelectionPointLabelJustification = 'Left'
slice3Display.SelectionPointLabelOpacity = 1.0
slice3Display.SelectionPointLabelShadow = 0
slice3Display.PolarAxes = 'PolarAxesRepresentation'

# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
slice3Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice3Display.OSPRayScaleFunction.UseLogScale = 0

# init the 'Arrow' selected for 'GlyphType'
slice3Display.GlyphType.TipResolution = 6
slice3Display.GlyphType.TipRadius = 0.1
slice3Display.GlyphType.TipLength = 0.35
slice3Display.GlyphType.ShaftResolution = 6
slice3Display.GlyphType.ShaftRadius = 0.03
slice3Display.GlyphType.Invert = 0

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
slice3Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice3Display.ScaleTransferFunction.UseLogScale = 0

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
slice3Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 2.5, 1.0, 0.5, 0.0]
slice3Display.OpacityTransferFunction.UseLogScale = 0

# init the 'GridAxesRepresentation' selected for 'DataAxesGrid'
slice3Display.DataAxesGrid.XTitle = 'X Axis'
slice3Display.DataAxesGrid.YTitle = 'Y Axis'
slice3Display.DataAxesGrid.ZTitle = 'Z Axis'
slice3Display.DataAxesGrid.XTitleColor = [0.0, 0.0, 0.0]
slice3Display.DataAxesGrid.XTitleFontFamily = 'Arial'
slice3Display.DataAxesGrid.XTitleFontFile = ''
slice3Display.DataAxesGrid.XTitleBold = 0
slice3Display.DataAxesGrid.XTitleItalic = 0
slice3Display.DataAxesGrid.XTitleFontSize = 12
slice3Display.DataAxesGrid.XTitleShadow = 0
slice3Display.DataAxesGrid.XTitleOpacity = 1.0
slice3Display.DataAxesGrid.YTitleColor = [0.0, 0.0, 0.0]
slice3Display.DataAxesGrid.YTitleFontFamily = 'Arial'
slice3Display.DataAxesGrid.YTitleFontFile = ''
slice3Display.DataAxesGrid.YTitleBold = 0
slice3Display.DataAxesGrid.YTitleItalic = 0
slice3Display.DataAxesGrid.YTitleFontSize = 12
slice3Display.DataAxesGrid.YTitleShadow = 0
slice3Display.DataAxesGrid.YTitleOpacity = 1.0
slice3Display.DataAxesGrid.ZTitleColor = [0.0, 0.0, 0.0]
slice3Display.DataAxesGrid.ZTitleFontFamily = 'Arial'
slice3Display.DataAxesGrid.ZTitleFontFile = ''
slice3Display.DataAxesGrid.ZTitleBold = 0
slice3Display.DataAxesGrid.ZTitleItalic = 0
slice3Display.DataAxesGrid.ZTitleFontSize = 12
slice3Display.DataAxesGrid.ZTitleShadow = 0
slice3Display.DataAxesGrid.ZTitleOpacity = 1.0
slice3Display.DataAxesGrid.FacesToRender = 63
slice3Display.DataAxesGrid.CullBackface = 0
slice3Display.DataAxesGrid.CullFrontface = 1
slice3Display.DataAxesGrid.GridColor = [1.0, 1.0, 1.0]
slice3Display.DataAxesGrid.ShowGrid = 0
slice3Display.DataAxesGrid.ShowEdges = 1
slice3Display.DataAxesGrid.ShowTicks = 1
slice3Display.DataAxesGrid.LabelUniqueEdgesOnly = 1
slice3Display.DataAxesGrid.AxesToLabel = 63
slice3Display.DataAxesGrid.XLabelColor = [0.0, 0.0, 0.0]
slice3Display.DataAxesGrid.XLabelFontFamily = 'Arial'
slice3Display.DataAxesGrid.XLabelFontFile = ''
slice3Display.DataAxesGrid.XLabelBold = 0
slice3Display.DataAxesGrid.XLabelItalic = 0
slice3Display.DataAxesGrid.XLabelFontSize = 12
slice3Display.DataAxesGrid.XLabelShadow = 0
slice3Display.DataAxesGrid.XLabelOpacity = 1.0
slice3Display.DataAxesGrid.YLabelColor = [0.0, 0.0, 0.0]
slice3Display.DataAxesGrid.YLabelFontFamily = 'Arial'
slice3Display.DataAxesGrid.YLabelFontFile = ''
slice3Display.DataAxesGrid.YLabelBold = 0
slice3Display.DataAxesGrid.YLabelItalic = 0
slice3Display.DataAxesGrid.YLabelFontSize = 12
slice3Display.DataAxesGrid.YLabelShadow = 0
slice3Display.DataAxesGrid.YLabelOpacity = 1.0
slice3Display.DataAxesGrid.ZLabelColor = [0.0, 0.0, 0.0]
slice3Display.DataAxesGrid.ZLabelFontFamily = 'Arial'
slice3Display.DataAxesGrid.ZLabelFontFile = ''
slice3Display.DataAxesGrid.ZLabelBold = 0
slice3Display.DataAxesGrid.ZLabelItalic = 0
slice3Display.DataAxesGrid.ZLabelFontSize = 12
slice3Display.DataAxesGrid.ZLabelShadow = 0
slice3Display.DataAxesGrid.ZLabelOpacity = 1.0
slice3Display.DataAxesGrid.XAxisNotation = 'Mixed'
slice3Display.DataAxesGrid.XAxisPrecision = 2
slice3Display.DataAxesGrid.XAxisUseCustomLabels = 0
slice3Display.DataAxesGrid.XAxisLabels = []
slice3Display.DataAxesGrid.YAxisNotation = 'Mixed'
slice3Display.DataAxesGrid.YAxisPrecision = 2
slice3Display.DataAxesGrid.YAxisUseCustomLabels = 0
slice3Display.DataAxesGrid.YAxisLabels = []
slice3Display.DataAxesGrid.ZAxisNotation = 'Mixed'
slice3Display.DataAxesGrid.ZAxisPrecision = 2
slice3Display.DataAxesGrid.ZAxisUseCustomLabels = 0
slice3Display.DataAxesGrid.ZAxisLabels = []

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
slice3Display.PolarAxes.Visibility = 0
slice3Display.PolarAxes.Translation = [0.0, 0.0, 0.0]
slice3Display.PolarAxes.Scale = [1.0, 1.0, 1.0]
slice3Display.PolarAxes.Orientation = [0.0, 0.0, 0.0]
slice3Display.PolarAxes.EnableCustomBounds = [0, 0, 0]
slice3Display.PolarAxes.CustomBounds = [0.0, 1.0, 0.0, 1.0, 0.0, 1.0]
slice3Display.PolarAxes.EnableCustomRange = 0
slice3Display.PolarAxes.CustomRange = [0.0, 1.0]
slice3Display.PolarAxes.PolarAxisVisibility = 1
slice3Display.PolarAxes.RadialAxesVisibility = 1
slice3Display.PolarAxes.DrawRadialGridlines = 1
slice3Display.PolarAxes.PolarArcsVisibility = 1
slice3Display.PolarAxes.DrawPolarArcsGridlines = 1
slice3Display.PolarAxes.NumberOfRadialAxes = 0
slice3Display.PolarAxes.AutoSubdividePolarAxis = 1
slice3Display.PolarAxes.NumberOfPolarAxis = 0
slice3Display.PolarAxes.MinimumRadius = 0.0
slice3Display.PolarAxes.MinimumAngle = 0.0
slice3Display.PolarAxes.MaximumAngle = 90.0
slice3Display.PolarAxes.RadialAxesOriginToPolarAxis = 1
slice3Display.PolarAxes.Ratio = 1.0
slice3Display.PolarAxes.PolarAxisColor = [1.0, 1.0, 1.0]
slice3Display.PolarAxes.PolarArcsColor = [1.0, 1.0, 1.0]
slice3Display.PolarAxes.LastRadialAxisColor = [1.0, 1.0, 1.0]
slice3Display.PolarAxes.SecondaryPolarArcsColor = [1.0, 1.0, 1.0]
slice3Display.PolarAxes.SecondaryRadialAxesColor = [1.0, 1.0, 1.0]
slice3Display.PolarAxes.PolarAxisTitleVisibility = 1
slice3Display.PolarAxes.PolarAxisTitle = 'Radial Distance'
slice3Display.PolarAxes.PolarAxisTitleLocation = 'Bottom'
slice3Display.PolarAxes.PolarLabelVisibility = 1
slice3Display.PolarAxes.PolarLabelFormat = '%-#6.3g'
slice3Display.PolarAxes.PolarLabelExponentLocation = 'Labels'
slice3Display.PolarAxes.RadialLabelVisibility = 1
slice3Display.PolarAxes.RadialLabelFormat = '%-#3.1f'
slice3Display.PolarAxes.RadialLabelLocation = 'Bottom'
slice3Display.PolarAxes.RadialUnitsVisibility = 1
slice3Display.PolarAxes.ScreenSize = 10.0
slice3Display.PolarAxes.PolarAxisTitleColor = [0.0, 0.0, 0.0]
slice3Display.PolarAxes.PolarAxisTitleOpacity = 1.0
slice3Display.PolarAxes.PolarAxisTitleFontFamily = 'Arial'
slice3Display.PolarAxes.PolarAxisTitleFontFile = ''
slice3Display.PolarAxes.PolarAxisTitleBold = 0
slice3Display.PolarAxes.PolarAxisTitleItalic = 0
slice3Display.PolarAxes.PolarAxisTitleShadow = 0
slice3Display.PolarAxes.PolarAxisTitleFontSize = 12
slice3Display.PolarAxes.PolarAxisLabelColor = [0.0, 0.0, 0.0]
slice3Display.PolarAxes.PolarAxisLabelOpacity = 1.0
slice3Display.PolarAxes.PolarAxisLabelFontFamily = 'Arial'
slice3Display.PolarAxes.PolarAxisLabelFontFile = ''
slice3Display.PolarAxes.PolarAxisLabelBold = 0
slice3Display.PolarAxes.PolarAxisLabelItalic = 0
slice3Display.PolarAxes.PolarAxisLabelShadow = 0
slice3Display.PolarAxes.PolarAxisLabelFontSize = 12
slice3Display.PolarAxes.LastRadialAxisTextColor = [0.0, 0.0, 0.0]
slice3Display.PolarAxes.LastRadialAxisTextOpacity = 1.0
slice3Display.PolarAxes.LastRadialAxisTextFontFamily = 'Arial'
slice3Display.PolarAxes.LastRadialAxisTextFontFile = ''
slice3Display.PolarAxes.LastRadialAxisTextBold = 0
slice3Display.PolarAxes.LastRadialAxisTextItalic = 0
slice3Display.PolarAxes.LastRadialAxisTextShadow = 0
slice3Display.PolarAxes.LastRadialAxisTextFontSize = 12
slice3Display.PolarAxes.SecondaryRadialAxesTextColor = [0.0, 0.0, 0.0]
slice3Display.PolarAxes.SecondaryRadialAxesTextOpacity = 1.0
slice3Display.PolarAxes.SecondaryRadialAxesTextFontFamily = 'Arial'
slice3Display.PolarAxes.SecondaryRadialAxesTextFontFile = ''
slice3Display.PolarAxes.SecondaryRadialAxesTextBold = 0
slice3Display.PolarAxes.SecondaryRadialAxesTextItalic = 0
slice3Display.PolarAxes.SecondaryRadialAxesTextShadow = 0
slice3Display.PolarAxes.SecondaryRadialAxesTextFontSize = 12
slice3Display.PolarAxes.EnableDistanceLOD = 1
slice3Display.PolarAxes.DistanceLODThreshold = 0.7
slice3Display.PolarAxes.EnableViewAngleLOD = 1
slice3Display.PolarAxes.ViewAngleLODThreshold = 0.7
slice3Display.PolarAxes.SmallestVisiblePolarAngle = 0.5
slice3Display.PolarAxes.PolarTicksVisibility = 1
slice3Display.PolarAxes.ArcTicksOriginToPolarAxis = 1
slice3Display.PolarAxes.TickLocation = 'Both'
slice3Display.PolarAxes.AxisTickVisibility = 1
slice3Display.PolarAxes.AxisMinorTickVisibility = 0
slice3Display.PolarAxes.ArcTickVisibility = 1
slice3Display.PolarAxes.ArcMinorTickVisibility = 0
slice3Display.PolarAxes.DeltaAngleMajor = 10.0
slice3Display.PolarAxes.DeltaAngleMinor = 5.0
slice3Display.PolarAxes.PolarAxisMajorTickSize = 0.0
slice3Display.PolarAxes.PolarAxisTickRatioSize = 0.3
slice3Display.PolarAxes.PolarAxisMajorTickThickness = 1.0
slice3Display.PolarAxes.PolarAxisTickRatioThickness = 0.5
slice3Display.PolarAxes.LastRadialAxisMajorTickSize = 0.0
slice3Display.PolarAxes.LastRadialAxisTickRatioSize = 0.3
slice3Display.PolarAxes.LastRadialAxisMajorTickThickness = 1.0
slice3Display.PolarAxes.LastRadialAxisTickRatioThickness = 0.5
slice3Display.PolarAxes.ArcMajorTickSize = 0.0
slice3Display.PolarAxes.ArcTickRatioSize = 0.3
slice3Display.PolarAxes.ArcMajorTickThickness = 1.0
slice3Display.PolarAxes.ArcTickRatioThickness = 0.5
slice3Display.PolarAxes.Use2DMode = 0
slice3Display.PolarAxes.UseLogAxis = 0

# hide data in view
Hide(calculator1, renderView1)

# show color bar/color legend
slice3Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(clip1)

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, -0.012, 0.0]

# Properties modified on clip1.ClipType
clip1.ClipType.Origin = [0.0, -0.012, 0.0]

# update the view to ensure updated data information
renderView1.Update()

# set active source
SetActiveSource(slice1)

# set active source
SetActiveSource(clip1)

# set active source
SetActiveSource(slice3)

# set active source
SetActiveSource(slice2)

# Rescale transfer function
omega_xLUT.RescaleTransferFunction(-1000.0, 1000.0)

# Rescale transfer function
omega_xPWF.RescaleTransferFunction(-1000.0, 1000.0)

# set active source
SetActiveSource(slice3)

# reset view to fit data bounds
renderView1.ResetCamera(0.00800000037998, 0.00800000037998, -0.00400000018999, 0.00400000018999, -0.00400000018999, 0.00400000018999)

# reset view to fit data bounds
renderView1.ResetCamera(0.00800000037998, 0.00800000037998, -0.00400000018999, 0.00400000018999, -0.00400000018999, 0.00400000018999)

# reset view to fit data
renderView1.ResetCamera()

# get color legend/bar for omega_xLUT in view renderView1
omega_xLUTColorBar = GetScalarBar(omega_xLUT, renderView1)
omega_xLUTColorBar.AutoOrient = 1
omega_xLUTColorBar.Orientation = 'Vertical'
omega_xLUTColorBar.WindowLocation = 'LowerRightCorner'
omega_xLUTColorBar.Position = [0.89, 0.02]
omega_xLUTColorBar.Title = 'omega_x'
omega_xLUTColorBar.ComponentTitle = ''
omega_xLUTColorBar.TitleJustification = 'Centered'
omega_xLUTColorBar.HorizontalTitle = 0
omega_xLUTColorBar.TitleColor = [0.0, 0.0, 0.0]
omega_xLUTColorBar.TitleOpacity = 1.0
omega_xLUTColorBar.TitleFontFamily = 'Arial'
omega_xLUTColorBar.TitleFontFile = ''
omega_xLUTColorBar.TitleBold = 0
omega_xLUTColorBar.TitleItalic = 0
omega_xLUTColorBar.TitleShadow = 0
omega_xLUTColorBar.TitleFontSize = 16
omega_xLUTColorBar.LabelColor = [0.0, 0.0, 0.0]
omega_xLUTColorBar.LabelOpacity = 1.0
omega_xLUTColorBar.LabelFontFamily = 'Arial'
omega_xLUTColorBar.LabelFontFile = ''
omega_xLUTColorBar.LabelBold = 0
omega_xLUTColorBar.LabelItalic = 0
omega_xLUTColorBar.LabelShadow = 0
omega_xLUTColorBar.LabelFontSize = 16
omega_xLUTColorBar.AutomaticLabelFormat = 1
omega_xLUTColorBar.LabelFormat = '%-#6.3g'
omega_xLUTColorBar.DrawTickMarks = 1
omega_xLUTColorBar.DrawTickLabels = 1
omega_xLUTColorBar.UseCustomLabels = 0
omega_xLUTColorBar.CustomLabels = []
omega_xLUTColorBar.AddRangeLabels = 1
omega_xLUTColorBar.RangeLabelFormat = '%-#6.1e'
omega_xLUTColorBar.DrawAnnotations = 1
omega_xLUTColorBar.AddRangeAnnotations = 0
omega_xLUTColorBar.AutomaticAnnotations = 0
omega_xLUTColorBar.DrawNanAnnotation = 0
omega_xLUTColorBar.NanAnnotation = 'NaN'
omega_xLUTColorBar.TextPosition = 'Ticks right/top, annotations left/bottom'
omega_xLUTColorBar.ReverseLegend = 0
omega_xLUTColorBar.ScalarBarThickness = 16
omega_xLUTColorBar.ScalarBarLength = 0.33

# change scalar bar placement
omega_xLUTColorBar.Orientation = 'Vertical'
omega_xLUTColorBar.WindowLocation = 'AnyLocation'
omega_xLUTColorBar.Position = [0.785768930523029, 0.3252557127312298]
omega_xLUTColorBar.ScalarBarLength = 0.3299999999999996

omega_xLUTColorBar.TitleFontSize = 4
omega_xLUTColorBar.LabelFontSize = 4
omega_xLUTColorBar.ScalarBarThickness = 5
omega_xLUTColorBar.ScalarBarLength = 0.5

# current camera placement for renderView1
renderView1.CameraPosition = [0.023120297672353244, -0.005511351954040058, 0.03263797833751225]
renderView1.CameraFocalPoint = [0.004000000189989805, -0.003999999957159162, 0.0]
renderView1.CameraViewUp = [0.013846228886864613, 0.99917582883037, 0.038156847704651144]
renderView1.CameraParallelScale = 0.009797959246405369

# save screenshot
SaveScreenshot(dirName+'/hluo_kidneyVortices_decked.png', renderView1, ImageResolution=[2562, 1838],
    FontScaling='Scale fonts proportionally',
    OverrideColorPalette='',
    StereoMode='No change',
    TransparentBackground=0, 
    # PNG options
    CompressionLevel='5')

print "Finalizing keydneyVortices_decked.py " + "@ dir : " + dirName 
import datetime
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
print "==============================="