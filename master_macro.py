# -*- coding: mbcs -*-
# Do not delete the following import lines


from abaqus import *
from abaqusConstants import *
import __main__
 
class parts:
    dim = 2
    shape = 'cube'
    name = ''
    assembly = ''

    def __init__(self, name, part, assembly,  dim, shape):
        self.part = assembly.Instance(name=name, part=part, dependent=ON)
        self.assembly = assembly
        self.name = name
        self.dim = dim
        self.shape = shape

    def translate(self, vec):
        self.assembly.translate(instanceList=(self.name), vector=vec)
    def part(self):
        return self.part


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


    assem_name = 'square-3d-macro'

    #define the geometric shape size and location
    calcite_dim = 2
    pyrite_dim = 0.5

    #this import the calcite into the assembly
    assembly = mdb.models[assem_name].rootAssembly
    calcite = mdb.models[assem_name].parts['calcite']
    assembly.Instance(name='calcite-1', part=calcite, dependent=ON)

    pyrite = mdb.models[assem_name].parts['pyrite']

    parts pyrite1('pyrite-1', pyrite, assembly, 0.5, 'cube')
    parts pyrite2('pyrite-2', pyrite, assembly, 0.5, 'cube')
    parts pyrite3('pyrite-3', pyrite, assembly, 0.5, 'cube')

    pyrite1.translate((0, 0, 1))
    pyrite1.translate((-0.5, 0.2, 0.5))
    pyrite1.translate((-0.5, -0.5, 1))
    
    assembly.InstanceFromBooleanMerge(name='merged', instances=(
        assembly.instances['calcite-1'], assembly.instances['pyrite-1'], 
        assembly.instances['pyrite-2'], assembly.instances['pyrite-3'], ), 
        keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY)


    merged_part = mdb.models[assem_name].parts['merged']
    calcite_cell = merged.cells.findAt(((0, 0, 0),))
    region = regionToolset.Region(cells = calcite_cell)

    merged_part.SectionAssignment(region=region, sectionName='calcite', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    
    session.viewports['Viewport: 1'].setValues(displayedObject=assembly)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)