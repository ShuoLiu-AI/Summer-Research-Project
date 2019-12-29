# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def get_time_step_data():
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
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=0)
    pth = session.paths['Path-1']
    session.XYDataFromPath(name='heat_up_0', path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=60, 
        projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=1)
    pth = session.paths['Path-1']
    session.XYDataFromPath(name='heatup_1', path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=60, 
        projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)
    session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=2)
    pth = session.paths['Path-1']
    session.XYDataFromPath(name='heatup_2', path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=60, 
        projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)
    xyp = session.xyPlots['XYPlot-1']
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    pth = session.paths['Path-1']
    xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=60, 
        projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)
    c1 = session.Curve(xyData=xy1)
    chart.setValues(curvesToPlot=(c1, ), )
    import sys
    sys.path.insert(15, 
        r'c:/SIMULIA/CAE/2019/win_b64/code/python2.7/lib/abaqus_plugins/excelUtilities')
    import abq_ExcelUtilities.excelUtilities
    abq_ExcelUtilities.excelUtilities.XYtoExcel(
        xyDataNames='heat_up_0,heatup_1,heatup_2', 
        trueName='From Current XY Plot')


def setup_diff_sim_jobs():
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
    a = mdb.models['square-3d'].rootAssembly
    session.viewports['Viewport: 1'].setValues(displayedObject=a)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
        predefinedFields=ON, connectors=ON)
    session.viewports['Viewport: 1'].view.setValues(nearPlane=11.5808, 
        farPlane=17.5121, width=0.529726, height=0.206748, viewOffsetX=1.19544, 
        viewOffsetY=-2.38187)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='heat_up')
    mdb.models['square-3d'].loads['Load-1'].setValues(magnitude=100000000.0)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
        predefinedFields=OFF, connectors=OFF, adaptiveMeshConstraints=ON)
    del mdb.models['square-3d'].steps['cool_down']
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=OFF)
    mdb.Job(name='heatflux_108', model='square-3d', description='', type=ANALYSIS, 
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
        numGPUs=0)
    mdb.jobs['heatflux_108'].submit(consistencyChecking=OFF)


def change_step_time():
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
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(
        adaptiveMeshConstraints=ON)
    mdb.models['square-3d'].steps['heat_up'].setValues(timePeriod=6.0, 
        initialInc=0.3)


