# -*- coding: mbcs -*-
# Do not delete the following import lines


from abaqus import *
from abaqusConstants import *
import __main__
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
from decimal import Decimal
import sys
import pickle
sys.path.insert(15,
    r'c:/SIMULIA/CAE/2019/win_b64/code/python2.7/lib/abaqus_plugins/excelUtilities')
import abq_ExcelUtilities.excelUtilities as abq_exc
import numpy as np


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


def Creating_3D_geo_shape():
    assem_name = 'square-3d-macro'

    #define the geometric shape size and location
    calcite_dim = 2
    pyrite_dim = 0.5

    #this import the calcite into the assembly
    assembly = mdb.models[assem_name].rootAssembly
    calcite = mdb.models[assem_name].parts['calcite']
    pyrite = mdb.models[assem_name].parts['pyrite']
    pyrite1 = parts('pyrite-1', pyrite, assembly, 0.5, 'cube')
    pyrite2 = parts('pyrite-2', pyrite, assembly, 0.5, 'cube')
    pyrite3 = parts('pyrite-3', pyrite, assembly, 0.5, 'cube')
    calcite1 = parts('calcite-1', calcite, assembly, 2, 'cube')

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

def get_name_job(magnitude):
    name_job = '%.2E' % (magnitude/100)
    name_job = name_job.replace('.', '')
    name_job = 'heatflux' + name_job.replace('+', '')
    return name_job

def get_time_step_data(magnitude=10e8, timePeriod=5, increment=0.3):
#setup different simulation jobs
    name_job = get_name_job(magnitude)
    pre_fix = 'M'+name_job

    mdb.models['square-3d'].loads['Load-1'].setValues(magnitude=magnitude)
    mdb.models['square-3d'].steps['heat_up'].setValues(timePeriod=timePeriod,
        initialInc=increment)
    mdb.Job(name=name_job, model='square-3d', description='', type=ANALYSIS,
        atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90,
        memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True,
        explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF,
        modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='',
        scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1,
        numGPUs=0)
    job = mdb.jobs[name_job]
    job.submit(consistencyChecking=OFF)
    job.waitForCompletion()
    while os.path.isfile(name_job+'.023') or os.path.isfile(name_job+'.lck') == True:
        sleep(0.1)
    return name_job

def get_to_session(name_job):
    file_path = name_job +'.odb'
    odb = session.openOdb(name=file_path)
    # odb = session.odbs[file_path]
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)

def get_output_data(name_job, step, frame):
#getting the output data from the model
    session.Path(name='Path-1', type=POINT_LIST, expression=((4.875,
        -4.98750019073486, 0.125), (4.995, -4.98750019073486, 0.125)))
    pth = session.paths['Path-1']

    xy_data = [[] for i in range(step)]
    xy_data_name = ''
    xy_data_name_str = ''

    for i in xrange(step):
        for j in xrange(frame):
            session.viewports['Viewport: 1'].odbDisplay.setFrame(step=i, frame=j)
            xy_data_name = name_job + 'stress'+str(i)+'_'+str(j)

            if i is not step-1 or j is not frame-1:
                xy_data_name_str += xy_data_name +','
            else:
                xy_data_name_str += xy_data_name

            session.XYDataFromPath(name=xy_data_name, path=pth, includeIntersections=False,
                projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=60,
                projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE,
                removeDuplicateXYPairs=True, includeAllElements=False)
            xy_data[i].append(session.xyDataObjects[xy_data_name].data)

    with open(r'\\ad.monash.edu\home\User045\dche145\Documents\Abaqus\macros\saved_data'+name_job, 'wb') as f:
        pickle.dump(xy_data, f)


if __name__== "__main__":
    num_change_flux = 10
    magnitude = np.linspace(10e6, 10e10, num_change_flux)
    timePeriod=5
    increment=0.3
    step = 1
    frame = int(np.ceil(timePeriod/increment))


    for i in xrange(num_change_flux):
        name_job = get_time_step_data(magnitude[i], timePeriod, increment)
        get_to_session(name_job)
        get_output_data(name_job, step, frame)

    # execfile('//ad.monash.edu/home/User045/dche145/Documents/Abaqus/macros/master_macro.py', __main__.__dict__)
