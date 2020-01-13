# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def setwd():
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
    import os
    os.chdir(r"C:\peter_abaqus\Summer-Research-Project\abaqus_working_space")


def cut():
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
    a = mdb.models['square-3d-macro-start-origin'].rootAssembly
    a.suppressFeatures(('pyrite-0', 'pyrite-1', 'pyrite-2', 'pyrite-3', 'pyrite-4', 
        'pyrite-5', 'pyrite-6', 'pyrite-7', 'pyrite-8', ))
    a1 = mdb.models['square-3d-macro-start-origin'].rootAssembly
    a1.InstanceFromBooleanCut(name='Part-1', 
        instanceToBeCut=mdb.models['square-3d-macro-start-origin'].rootAssembly.instances['pyrite-9'], 
        cuttingInstances=(a1.instances['calcite-1'], ), 
        originalInstances=DELETE)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=187.547, 
        farPlane=188.806, width=1.72879, height=0.696504, cameraPosition=(
        -131.031, 104.039, 86.3313), cameraTarget=(0.597699, 0.0585417, 
        0.208805))
    a = mdb.models['square-3d-macro-start-origin'].rootAssembly
    a.features['pyrite-8'].resume()


def delete():
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
    a = mdb.models['square-3d-macro-start-origin'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    a = mdb.models['square-3d-macro-start-origin'].rootAssembly
    del a.features['pyrite-6']


