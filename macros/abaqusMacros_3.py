# -*- coding: mbcs -*-
# Do not delete the following import lines
from abaqus import *
from abaqusConstants import *
import __main__

def create_path():
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
    session.Path(name='Path-1', type=POINT_LIST, expression=((4.875, 
        -4.98750019073486, 0.125), (4.995, -4.98750019073486, 0.125)))


def run_macro():
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
    execfile(
        '//ad.monash.edu/home/User045/dche145/Documents/Abaqus/macros/master_macro.py', 
        __main__.__dict__)


def get_to_session():
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
    session.mdbData.summary()
    session.viewports['Viewport: 1'].setValues(
        displayedObject=session.odbs['C:/Users/dche145/AppData/Local/Temp/17/heatflux_108.odb'])
    odb = session.odbs['C:/Users/dche145/AppData/Local/Temp/17/heatflux_108.odb']
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    xyp = session.XYPlot('XYPlot-1')
    chartName = xyp.charts.keys()[0]
    chart = xyp.charts[chartName]
    pth = session.paths['Path-1']
    xy1 = xyPlot.XYDataFromPath(path=pth, includeIntersections=False, 
        projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=10, 
        projectionTolerance=0, shape=DEFORMED, labelType=TRUE_DISTANCE, 
        removeDuplicateXYPairs=True, includeAllElements=False)
    c1 = session.Curve(xyData=xy1)
    chart.setValues(curvesToPlot=(c1, ), )
    session.viewports['Viewport: 1'].setValues(displayedObject=xyp)


def open_database():
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
    o1 = session.openOdb(
        name='C:/Users/dche145/AppData/Local/Temp/17/heatflux1E06.odb')
    session.viewports['Viewport: 1'].setValues(displayedObject=o1)


