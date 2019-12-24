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
    
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('calcite-1', ), vector=(-4.875, 5.0, -0.125))
    
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('pyrite-1', 'pyrite-2', 'pyrite-3'), vector=(
        -4.8775, 0.772752, -0.15))
    
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('pyrite-1', ), vector=(-0.075, -0.075, 0.075))
    
    a1 = mdb.models['square-3d-macro'].rootAssembly
    a1.translate(instanceList=('pyrite-2', ), vector=(-0.0825, -0.055, 0.095))
    
    session.viewports['Viewport: 1'].setColor(globalTranslucency=True)
    
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


