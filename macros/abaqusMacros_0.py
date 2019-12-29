# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def Macro1():
    import section
    import regionToolset
    import displayGroupMdbToolset as dgm
    import part
    import material
    import assembly
    import step
    import interaction
    import load
    import mesh
    import optimization
    import job
    import sketch
    import visualization
    import xyPlot
    import displayGroupOdbToolset as dgo
    import connectorBehavior
    a1 = mdb.models['square-3d-macro'].rootAssembly
    p = mdb.models['square-3d-macro'].parts['calcite']
    a1.Instance(name='calcite-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4287, 
        farPlane=17.6642, width=2.43076, height=1.20816, viewOffsetX=1.03412, 
        viewOffsetY=-1.85969)
    a1 = mdb.models['square-3d-macro'].rootAssembly
    p = mdb.models['square-3d-macro'].parts['pyrite']
    a1.Instance(name='pyrite-1', part=p, dependent=ON)
    p1 = a1.instances['pyrite-1']
    p1.translate(vector=(4.34193643569946, 0.0, 0.0))
    session.viewports['Viewport: 1'].view.fitView()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.2883, 
        farPlane=17.9945, width=5.83104, height=2.8982, viewOffsetX=0.972271, 
        viewOffsetY=0.411551)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.2638, 
        farPlane=18.0191, width=5.81837, height=2.89191, viewOffsetX=1.05849, 
        viewOffsetY=-0.829828)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.0656, 
        farPlane=18.2172, width=8.92312, height=4.43505, viewOffsetX=0.70773, 
        viewOffsetY=-1.09563)
    a1 = mdb.models['square-3d-macro'].rootAssembly
    p = mdb.models['square-3d-macro'].parts['pyrite']
    a1.Instance(name='pyrite-2', part=p, dependent=ON)
    p1 = a1.instances['pyrite-2']
    p1.translate(vector=(4.36943643569946, 0.0, 0.0))
    session.viewports['Viewport: 1'].view.fitView()
    a1 = mdb.models['square-3d-macro'].rootAssembly
    p = mdb.models['square-3d-macro'].parts['pyrite']
    a1.Instance(name='pyrite-3', part=p, dependent=ON)
    p1 = a1.instances['pyrite-3']
    p1.translate(vector=(4.39693643569946, 0.0, 0.0))
    session.viewports['Viewport: 1'].view.fitView()
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.471, 
        farPlane=17.9071, width=3.82135, height=1.89933, viewOffsetX=0.992324, 
        viewOffsetY=0.21327)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4545, 
        farPlane=17.9236, width=3.81586, height=1.89659, viewOffsetX=1.19743, 
        viewOffsetY=-0.35123)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.6847, 
        farPlane=17.6934, width=0.81348, height=0.404324, viewOffsetX=1.4625, 
        viewOffsetY=0.484811)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.681, 
        farPlane=17.697, width=0.813227, height=0.404198, viewOffsetX=1.52968, 
        viewOffsetY=0.258138)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4451, 
        farPlane=17.933, width=4.18604, height=2.08059, viewOffsetX=1.29745, 
        viewOffsetY=0.148421)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.4271, 
        farPlane=17.951, width=4.17946, height=2.07732, viewOffsetX=1.30093, 
        viewOffsetY=-0.519423)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=10.7311, 
        farPlane=18.6469, width=14.1852, height=7.05048, viewOffsetX=0.520745, 
        viewOffsetY=-0.840409)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=10.678, 
        farPlane=18.7, width=14.1151, height=7.01561, viewOffsetX=-0.488053, 
        viewOffsetY=0.151337)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.6927, 
        farPlane=17.6854, width=0.619096, height=0.307709, viewOffsetX=1.12384, 
        viewOffsetY=-2.29266)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.6957, 
        farPlane=17.6824, width=0.619252, height=0.307787, viewOffsetX=1.03257, 
        viewOffsetY=-2.20495)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.255, 
        farPlane=18.1231, width=6.85625, height=3.40776, viewOffsetX=0.724349, 
        viewOffsetY=-2.56526)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.2265, 
        farPlane=18.1516, width=6.83889, height=3.39913, viewOffsetX=-0.4015, 
        viewOffsetY=-0.622212)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=10.615, 
        farPlane=18.763, width=15.7032, height=7.80496, viewOffsetX=-1.44967, 
        viewOffsetY=-0.287174)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=10.564, 
        farPlane=18.814, width=15.6278, height=7.76748, viewOffsetX=-3.68115, 
        viewOffsetY=3.38648)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.3522, 
        farPlane=18.0259, width=4.87198, height=2.42152, viewOffsetX=-2.03042, 
        viewOffsetY=2.7248)
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('calcite-1', ), vector=(-4.875, 5.0, -0.125))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.3601, 
        farPlane=15.5629, width=4.87539, height=2.42321, viewOffsetX=-0.73817, 
        viewOffsetY=1.9415)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5693, 
        farPlane=15.3538, width=2.23564, height=1.11118, viewOffsetX=1.68026, 
        viewOffsetY=0.640967)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5594, 
        farPlane=15.3636, width=2.23374, height=1.11023, viewOffsetX=0.895916, 
        viewOffsetY=0.97069)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.2132, 
        farPlane=15.7098, width=7.19925, height=3.57824, viewOffsetX=0.591721, 
        viewOffsetY=1.36182)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.1862, 
        farPlane=15.7369, width=7.18189, height=3.56961, viewOffsetX=-1.74204, 
        viewOffsetY=2.8755)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.6853, 
        farPlane=15.2377, width=0.531207, height=0.264026, 
        viewOffsetX=-1.48946, viewOffsetY=2.54284)
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('pyrite-1', 'pyrite-2', 'pyrite-3'), vector=(
        -4.8775, 0.772752, -0.15))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5051, 
        farPlane=14.8744, width=0.483932, height=0.240529, 
        viewOffsetX=-1.81951, viewOffsetY=3.16631)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5075, 
        farPlane=14.8721, width=0.48401, height=0.240567, viewOffsetX=-1.81341, 
        viewOffsetY=3.12529)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4825, 
        farPlane=14.897, width=0.765794, height=0.380622, viewOffsetX=-1.76874, 
        viewOffsetY=3.19953)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4846, 
        farPlane=14.8893, width=0.765902, height=0.380676, cameraPosition=(
        10.6148, 5.64949, 9.274), cameraUpVector=(-0.528477, 0.596433, 
        -0.604135), cameraTarget=(2.63046, -2.54612, 0.0625582), 
        viewOffsetX=-1.76899, viewOffsetY=3.19998)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4739, 
        farPlane=14.8761, width=0.765335, height=0.380394, cameraPosition=(
        10.7407, 3.55041, 10.0926), cameraUpVector=(-0.44376, 0.706233, 
        -0.551644), cameraTarget=(2.34454, -2.79603, -0.154099), 
        viewOffsetX=-1.76768, viewOffsetY=3.19761)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4823, 
        farPlane=14.8744, width=0.76578, height=0.380615, cameraPosition=(
        8.92705, 4.50787, 11.3787), cameraUpVector=(-0.386975, 0.659304, 
        -0.644646), cameraTarget=(2.4544, -2.67611, 0.321484), 
        viewOffsetX=-1.76871, viewOffsetY=3.19947)
    session.viewports['Viewport: 1'].view.setValues(viewOffsetX=-1.79398, 
        viewOffsetY=3.13981)
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('pyrite-1', ), vector=(-0.075, -0.075, 0.075))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.489, 
        farPlane=14.8677, width=0.636337, height=0.316278, 
        viewOffsetX=-1.79031, viewOffsetY=3.14148)
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('pyrite-2', ), vector=(-0.0825, -0.055, 0.095))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.2319, 
        farPlane=14.9202, width=0.625047, height=0.310667, 
        viewOffsetX=-1.77464, viewOffsetY=3.0845)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.4099, 
        farPlane=14.9097, width=0.632863, height=0.314551, cameraPosition=(
        4.93449, 3.70226, 13.7919), cameraUpVector=(-0.158154, 0.700639, 
        -0.695767), cameraTarget=(2.21366, -2.7475, 0.878198), 
        viewOffsetX=-1.79683, viewOffsetY=3.12307)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5452, 
        farPlane=14.769, width=0.638805, height=0.317505, cameraPosition=(
        1.94779, -3.0178, 14.6066), cameraUpVector=(0.035402, 0.938746, 
        -0.342786), cameraTarget=(1.79867, -3.1596, -0.0809002), 
        viewOffsetX=-1.8137, viewOffsetY=3.15239)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5356, 
        farPlane=14.8452, width=0.638383, height=0.317295, cameraPosition=(
        8.7277, 5.08493, 11.2918), cameraUpVector=(-0.232798, 0.586967, 
        -0.775419), cameraTarget=(1.97246, -2.88896, 0.969573), 
        viewOffsetX=-1.8125, viewOffsetY=3.15031)
    session.viewports['Viewport: 1'].setColor(globalTranslucency=True)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.5746, 
        farPlane=14.8558, width=0.640096, height=0.318147, cameraPosition=(
        13.3596, 7.35953, 0.124015), cameraUpVector=(-0.83869, 0.45322, 
        -0.301978), cameraTarget=(2.54443, -2.52801, -0.892196), 
        viewOffsetX=-1.81736, viewOffsetY=3.15876)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=14.556, 
        farPlane=14.8355, width=0.63928, height=0.317741, cameraPosition=(
        3.697, 6.61664, 13.0996), cameraUpVector=(-0.281775, 0.542279, 
        -0.79154), cameraTarget=(2.69985, -2.08489, 1.30757), 
        viewOffsetX=-1.81504, viewOffsetY=3.15473)
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('pyrite-3', ), vector=(-0.09, -0.105, 0.095))
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.InstanceFromBooleanMerge(name='merged', instances=(
        a1.instances['calcite-1'], a1.instances['pyrite-1'], 
        a1.instances['pyrite-2'], a1.instances['pyrite-3'], ), 
        keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY)
    session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
        engineeringFeatures=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['square-3d-macro'].parts['calcite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].setColor(globalTranslucency=True)
    p = mdb.models['square-3d-macro'].parts['merged']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.331702, 
        farPlane=0.588362, width=0.313171, height=0.155655, cameraPosition=(
        -0.167057, -0.119448, 0.29227), cameraUpVector=(-0.162243, 0.985713, 
        -0.0452361), cameraTarget=(0.0651225, 0.0572553, -0.0598777))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.346394, 
        farPlane=0.570768, width=0.327042, height=0.16255, cameraPosition=(
        -0.0303957, 0.179936, 0.370983), cameraUpVector=(0.190223, 0.818802, 
        -0.541644), cameraTarget=(0.0659288, 0.0590217, -0.0594133))
    session.viewports['Viewport: 1'].view.setValues(nearPlane=0.341741, 
        farPlane=0.574565, width=0.32265, height=0.160366, cameraPosition=(
        -0.0121075, 0.240258, 0.353158), cameraUpVector=(0.10234, 0.73349, 
        -0.671952), cameraTarget=(0.0659792, 0.0591879, -0.0594624))
    p = mdb.models['square-3d-macro'].parts['merged']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#10 ]', ), )
    region = p.Set(cells=cells, name='calcite')
    p = mdb.models['square-3d-macro'].parts['merged']
    p.SectionAssignment(region=region, sectionName='calcite', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['square-3d-macro'].parts['merged']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#f ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['square-3d-macro'].parts['merged']
    p.SectionAssignment(region=region, sectionName='pyrite', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.regenerate()
    a = mdb.models['square-3d-macro'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)


