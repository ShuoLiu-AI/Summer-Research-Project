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
import numpy as np
import json
import os
import sys
import shutil
import unicodedata

working_dir = r'//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/'
sys.path.append(working_dir)
os.chdir(working_dir)
from helpers import matmul, get_rx, get_ry, get_rz, get_name_job


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
        self.assembly.translate(instanceList=(self.name,), vector=vec)
    def rotate(self):
        raise Exception('not implemented')

assem_name = 'square-3d-macro-start-origin'
assembly = mdb.models[assem_name].rootAssembly
pyrite_parts = []
calcite_parts = []
part_name_file = 'part_names.peter'
part_name_list = []

def import_3D_geo_shape(num):
    clean_up = True
    if clean_up:
        with open(part_name_file) as f:
            part_name_list_read = json.load(f)
            for i in range(len(part_name_list_read)):
                part_name_list_read[i] = unicodedata.normalize(
                'NFKD', part_name_list_read[i]).encode('ascii','ignore')
        assembly.deleteFeatures(part_name_list_read)
    #define the geometric shape size and location
    calcite_dim = 2
    pyrite_dim = 0.5
    #this import the calcite into the assembly
    calcite = mdb.models[assem_name].parts['calcite']
    pyrite = mdb.models[assem_name].parts['pyrite']
    global pyrite_parts
    global calcite_parts
    for i in range(num):
        pyrite_parts.append(parts('pyrite-'+str(i), pyrite, assembly, 0.5, 'cube'))
        part_name_list.append('pyrite-'+str(i))
    calcite_parts.append(parts('calcite-1', calcite, assembly, 2, 'cube'))
    part_name_list.append('calcite-1')
    with open(part_name_file, 'w') as f:
        json.dump(part_name_list, f)

def create_3D_distro(num_crystal):
    #copy .\geometry.peter \\ad.monash.edu\home\User045\dche145\Documents\Abaqus\microwave-break-rocks\geometry.peter
    file_name = 'geometry.peter'
    with open(file_name, 'rb') as f:
        read_out = json.load(f)
        loc = np.array(read_out[0])
        Rx = np.array(read_out[1])
        Ry = np.array(read_out[2])
        Rz = np.array(read_out[3])
        theta_x = np.array(read_out[4])
        theta_y = np.array(read_out[5])
        theta_z = np.array(read_out[6])


    axis_dir_x = [[1, 0, 0] for i in range(num_crystal)]
    axis_dir_y = [[0, 1, 0] for i in range(num_crystal)]
    axis_dir_z = [[0, 0, 1] for i in range(num_crystal)]

    for i in range(num_crystal):
        pyrite_parts[i].translate([0, 0, -pyrite_parts[i].dim/2])
        #translate the crystals to the origin
    calcite_parts[0].translate([0, 0, -calcite_parts[0].dim/2])

    for i in range(num_crystal):
        #rotate the crystals
        rx = get_rx(theta_x[i])
        ry = get_ry(theta_y[i])
        rz = get_rz(theta_z[i])
        assembly.rotate(instanceList=('pyrite-'+str(i),), axisPoint=[0,0,0],
        axisDirection=axis_dir_x[i], angle=theta_x[i]*180/np.pi)
        axis_dir_x[i] = matmul(rx, axis_dir_x[i])
        axis_dir_y[i] = matmul(rx, axis_dir_y[i])
        axis_dir_z[i] = matmul(rx, axis_dir_z[i])
        assembly.rotate(instanceList=('pyrite-'+str(i),), axisPoint=[0,0,0],
        axisDirection=axis_dir_y[i], angle=theta_y[i]*180/np.pi)
        axis_dir_x[i] = matmul(ry, axis_dir_x[i])
        axis_dir_y[i] = matmul(ry, axis_dir_y[i])
        axis_dir_z[i] = matmul(ry, axis_dir_z[i])
        assembly.rotate(instanceList=('pyrite-'+str(i),), axisPoint=[0,0,0],
        axisDirection=axis_dir_z[i], angle=theta_z[i]*180/np.pi)
        axis_dir_x[i] = matmul(rz, axis_dir_x[i])
        axis_dir_y[i] = matmul(rz, axis_dir_y[i])
        axis_dir_z[i] = matmul(rz, axis_dir_z[i])

    for i in range(num_crystal):
        #translate the crystals to the desired location
        pyrite_parts[i].translate(loc[i])


def merge_and_material():
    all_parts = []
    for i in range(num_crystal):
        all_parts.append(pyrite_parts[i].part)
    all_parts.append(calcite_parts[0].part)

    assembly.InstanceFromBooleanMerge(name='merged', instances=all_parts,
        keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY)

    merged_part = mdb.models[assem_name].parts['merged']
    calcite_cell = merged_part.cells.findAt(((0, 0, 0),))
    region = regionToolset.Region(cells = calcite_cell)

    merged_part.SectionAssignment(region=region, sectionName='calcite', offset=0.0,
        offsetType=MIDDLE_SURFACE, offsetField='',
        thicknessAssignment=FROM_SECTION)

    session.viewports['Viewport: 1'].setValues(displayedObject=assembly)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
        predefinedFields=ON, connectors=ON)
    assembly.regenerate()

def run_job(magnitude=10e8, timePeriod=5, increment=0.3):
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

def get_output_data(name_job, step, frame):
    file_path = name_job +'.odb'
    odb = session.openOdb(name=file_path)
    # odb = session.odbs[file_path]
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
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
    num_crystal = 10

    import_3D_geo_shape(num_crystal)
    create_3D_distro(num_crystal)
    merge_and_material()

    # for i in xrange(num_change_flux):
    #     name_job = run_job(magnitude[i], timePeriod, increment)
    #     get_output_data(name_job, step, frame)
    #
    # How to copy Macro
    # shutil.copyfile('C:/Users/dche145/abaqusMacros.py', r'//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/macro.py')
    # execfile('//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/master_macro.py', __main__.__dict__)
