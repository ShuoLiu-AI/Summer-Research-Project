# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def heat_flux():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='heat_up')
    a = mdb.models['square-3d-macro-start-origin'].rootAssembly
    c1 = a.instances['merged-2'].cells
    cells1 = c1.getSequenceFromMask(mask=('[#1000 ]', ), )
    region = regionToolset.Region(cells=cells1)
    mdb.models['square-3d-macro-start-origin'].BodyHeatFlux(name='Load-2', 
        createStepName='heat_up', region=region, magnitude=10.0, 
        distributionType=USER_DEFINED)


