# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def create_model():
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
    mdb.Model(name='test_macro', modelType=STANDARD_EXPLICIT)
    a = mdb.models['test_macro'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    del mdb.models['test_macro']
    a = mdb.models['prism-3d'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    mdb.save()


def merged_mesh():
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
    a = mdb.models['test'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a1 = mdb.models['test'].rootAssembly
    a1.DatumCsysByDefault(CARTESIAN)
    p = mdb.models['test'].parts['calcite']
    a1.Instance(name='calcite-1', part=p, dependent=ON)
    p = mdb.models['test'].parts['pyrite']
    a1.Instance(name='pyrite-1', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['test'].parts['calcite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['test'].parts['calcite']
    p.seedPart(size=0.1, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['test'].parts['calcite']
    p.generateMesh()
    p = mdb.models['test'].parts['pyrite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['test'].parts['pyrite']
    p.seedPart(size=0.01, deviationFactor=0.1, minSizeFactor=0.1)
    p = mdb.models['test'].parts['pyrite']
    p.generateMesh()
    a1 = mdb.models['test'].rootAssembly
    a1.regenerate()
    a = mdb.models['test'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    a1 = mdb.models['test'].rootAssembly
    p = mdb.models['test'].parts['calcite']
    a1.Instance(name='calcite-2', part=p, dependent=ON)
    p = mdb.models['test'].parts['pyrite']
    a1.Instance(name='pyrite-2', part=p, dependent=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)

    p = mdb.models['test'].parts['pyrite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['test'].parts['pyrite']
    n = p.nodes
    nodes = n.getSequenceFromMask(mask=(
        '[#ffffffff:37 #fbffffff #ffffffff:3 #7ffff ]', ), )
    p.Set(nodes=nodes, name='b_nodes')
    p = mdb.models['test'].parts['calcite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['test'].parts['calcite']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#ffffffff:31 #ff ]', ), )
    p.Set(elements=elements, name='a_elements')
    a1 = mdb.models['test'].rootAssembly
    a1.regenerate()
    a = mdb.models['test'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    a1 = mdb.models['test'].rootAssembly
    a1.InstanceFromBooleanMerge(name='merged_mesh', instances=(
        a1.instances['calcite-1'], a1.instances['pyrite-1'], 
        a1.instances['calcite-2'], a1.instances['pyrite-2'], ), mergeNodes=ALL, 
        nodeMergingTolerance=1e-06, domain=MESH, originalInstances=SUPPRESS)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='heat_up')
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=ON)
    p = mdb.models['test'].parts['calcite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    session.viewports['Viewport: 1'].partDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
        referenceRepresentation=OFF)
    p = mdb.models['test'].parts['pyrite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['test'].parts['pyrite']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#ffffffff:31 #ff ]', ), )
    p.Set(elements=elements, name='b_elements')
    a = mdb.models['test'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON, loads=OFF, 
        bcs=OFF, predefinedFields=OFF, connectors=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=OFF)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=OFF)
    a = mdb.models['test'].rootAssembly
    a.resumeFeatures(('calcite-2', 'pyrite-2', ))
    a = mdb.models['test'].rootAssembly
    a.features['merged_mesh-1'].suppress()
    a1 = mdb.models['test'].rootAssembly
    a1.InstanceFromBooleanMerge(name='merged_mesh_2', instances=(
        a1.instances['calcite-2'], a1.instances['pyrite-2'], ), mergeNodes=ALL, 
        nodeMergingTolerance=1e-06, domain=MESH, originalInstances=SUPPRESS)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    a = mdb.models['test'].rootAssembly
    region = a.instances['merged_mesh_2-1'].sets['b_elements']
    mdb.models['test'].loads['dflux'].setValues(region=region, 
        distributionType=UNIFORM)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=2.4843, 
        farPlane=4.71588, width=3.33304, height=1.49317, 
        viewOffsetX=-0.0956355, viewOffsetY=-0.0501579)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Initial')
    
    a = mdb.models['test'].rootAssembly
    n1 = a.instances['merged_mesh_2-1'].nodes
    nodes1 = n1.getSequenceFromMask(mask=(
        '[#f5f75fdf #30fcf7f5 #3b3f0f0f #9e7e1e3d #3dcc661f #c3c3cc3f #beebfbcf', 
        ' #5776febe #1dd55555 #33 #600028cc #1986 #cc500 #ee330000', 
        ' #baaaaaaa #31d555db #23000 #0 #1f0 #f8000000 #0', 
        ' #7c0000 #0 #3e00 #0 #c201f #0 #3f0000', 
        ' #0 #fc0000 #0 #3f00000 #0 #fc00000 #0', 
        ' #3f000000 #31800 #aaaab8cc #555ddbba #cc775555 #30000000 #a3', 
        ' #7c000000 #0 #3e0000 #0 #1f00 #80000000 #f', 
        ' #7c00000 #0 #3e000 #cc5 #0 #f80 #0', 
        ' #3f00 #0 #fc00 #0 #3f000 #0 #fc000', 
        ' #0 #3f0000 #30cc0000 #30000003 #baaaaaee #555555dd #cc775', 
        ' #a330000 #662800 #30cc0000 #c0000003 #aaaabb8c #d7f6eeaa #3dfd7d77', 
        ' #c3c33c3f #dccb3bcf #f0cf0fc #cf0fcf3f #fef3f0f0 #bfafaefa #f ]', ), 
        )
    region = a.Set(nodes=nodes1, name='boundary_nodes')
    mdb.models['test'].boundaryConditions['fixed'].setValues(region=region)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF)
    mdb.Job(name='test_merge_mesh', model='test', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)


def section_ass():
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
    p = mdb.models['test'].parts['pyrite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    p.SectionAssignment(region=region, sectionName='quartz', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['test'].parts['calcite']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    p = mdb.models['test'].parts['calcite']
    c = p.cells
    cells = c.getSequenceFromMask(mask=('[#1 ]', ), )
    region = regionToolset.Region(cells=cells)
    p = mdb.models['test'].parts['calcite']
    p.SectionAssignment(region=region, sectionName='feldspar', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    p = mdb.models['test'].parts['merged_mesh_2']
    session.viewports['Viewport: 1'].setValues(displayedObject=p)
    a = mdb.models['test'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(mesh=ON)
    session.viewports['Viewport: 1'].assemblyDisplay.meshOptions.setValues(
        meshTechnique=ON)
    p = mdb.models['test'].parts['merged_mesh_2']
    e = p.elements
    elements = e.getSequenceFromMask(mask=('[#ffffffff:62 #ffff ]', ), )
    region = regionToolset.Region(elements=elements)
    p = mdb.models['test'].parts['merged_mesh_2']
    p.SectionAssignment(region=region, sectionName='feldspar', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)


