# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def output_report():
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
    pth = session.paths['Path-1']
    session.XYDataFromPath(name='XYData-1', path=pth, includeIntersections=False,
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=10,
        projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE,
        removeDuplicateXYPairs=True, includeAllElements=False)
x0 = session.xyDataObjects['XYData-1']
    session.writeXYReport(fileName='abaqus.rpt', xyData=(x0, ))
