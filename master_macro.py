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
        assembly.Instance(name=name, part=part, dependent=ON)
        self.assembly = assembly
        self.name = name
        self.dim = dim
        self.shape = shape

    def translate(self, vec):
        self.assembly.translate(instanceList=(self.name), vector=vec)


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


    #define the geometric shape size and location
    calcite_dim = 2
    pyrite_dim = 0.5

    #this import the calcite into the assembly
    assembly = mdb.models['square-3d-macro'].rootAssembly
    calcite = mdb.models['square-3d-macro'].parts['calcite']
    assembly.Instance(name='calcite-1', part=calcite, dependent=ON)

    pyrite = mdb.models['square-3d-macro'].parts['pyrite']

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
