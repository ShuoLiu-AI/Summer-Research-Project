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
# os.chdir(working_dir)
import helpers
reload(helpers)
from helpers import matmul, matmul_vec, get_rx, get_ry, get_rz, get_name_job


pyrite_part = None
calcite_part = None
pyrite_ins = []
calcite_ins = []
part_name_file = working_dir + 'part_names.peter'
geo_distro_3D = working_dir + 'geometry.peter'
part_name_list = []

class part:
    def __init__(self, name, dim=[0.5, 0.5, 0.5], center=[0, 0, 0], shape='cube', b_create_part=False, assembly=assembly):
        self.assembly = assembly
        self.name = name
        self.dim = dim
        self.center = center
        self.shape = shape
        self.axis = [[self.dim[0], 0, 0], [0, self.dim[0], 0], [0, 0, self.dim[0]]]
        if self.shape == 'cube':
            s = mdb.models['square-3d-macro-start-origin'].ConstrainedSketch(
                name='__profile__', sheetSize=200.0)
            g, v, d, c = s.geometry, s.vertices, s.dimensions, s.constraints
            s.setPrimaryObject(option=STANDALONE)
            two_corner = ((-self.dim[0]/2+self.center[0], self.dim[1]/2+self.center[1]),
                (self.dim[0]/2 + self.center[0], -self.dim[1]/2 + self.center[1]))
            self.center[2] = self.dim[2]/2
            s.rectangle(point1=two_corner[0], point2=two_corner[1])
            p = mdb.models['square-3d-macro-start-origin'].Part(name=self.name,
                dimensionality=THREE_D, type=DEFORMABLE_BODY)
            p.BaseSolidExtrude(sketch=s, depth=self.dim[2])
            self.abq_part=p
            del mdb.models['square-3d-macro-start-origin'].sketches['__profile__']


class instance:
    def __init__(self, name, abq_part = None, script_part = None, center=(0,0,0)):
        self.name=name
        if abq_part is not None:
            self.part = assembly.Instance(name=name, part=abq_part, dependent=ON)
            self.axis = [[0.1, 0, 0], [0, 0.1, 0], [0, 0, 0.1]]
        elif script_part is not None:
            self.part = assembly.Instance(name=name, part=script_part.abq_part, dependent=ON)
            self.axis = script_part.axis
            self.translate((np.array(center) - np.array(script_part.center)).tolist())
        else:
            raise Exception('have to give one of the part')
    def translate(self, vec):
        assembly.translate(instanceList=(self.name,), vector=vec)
    def rotate(self, theta):
        rx = get_rx(theta[0])
        ry = get_ry(theta[1])
        rz = get_rz(theta[2])
        self.axis_temp = [[0,0,1] for i in range(3)]

        assembly.rotate(instanceList=(self.name,), axisPoint=[0,0,0],
        axisDirection=self.axis[0], angle=theta[0]*180/np.pi)
        self.axis_temp[1] = matmul_vec(rx, matmul_vec(ry, self.axis[1]))
        assembly.rotate(instanceList=(self.name,), axisPoint=[0,0,0],
        axisDirection=self.axis_temp[1], angle=theta[1]*180/np.pi)
        self.axis_temp[2] = matmul_vec(rx, matmul_vec(ry, matmul_vec(rz, self.axis[2])))
        assembly.rotate(instanceList=(self.name,), axisPoint=[0,0,0],
        axisDirection=self.axis_temp[2], angle=theta[2]*180/np.pi)

        # for i in range(3):
        #     self.axis_temp[i] = matmul_vec(rx, matmul_vec(ry, matmul_vec(rz, self.axis[i])))
        #     assembly.DatumPointByCoordinate(self.axis_temp[i])
        # if clean_up_geo_test:
        #     del assembly.features['ax_0']
        #     del assembly.features['ax_1']
        #     del assembly.features['ax_2']
        # assembly.features.changeKey(
        #     fromName='Datum pt-1', toName='ax_0')
        # assembly.features.changeKey(
        #     fromName='Datum pt-2', toName='ax_1')
        # assembly.features.changeKey(
        #     fromName='Datum pt-3', toName='ax_2')


def import_3D_geo_shape(num):
    if clean_up_geo_test:
        with open(part_name_file) as f:
            part_name_list_read = json.load(f)
            for i in range(len(part_name_list_read)):
                part_name_list_read[i] = unicodedata.normalize(
                'NFKD', part_name_list_read[i]).encode('ascii','ignore')
        assembly.deleteFeatures(part_name_list_read)
    #define the geometric shape size and location
    calcite_dim = [2.4, 2.4, 2.4]
    pyrite_dim = [0.2, 0.2, 0.2]

    global pyrite_part
    global calcite_part
    global pyrite_ins
    global calcite_ins
    calcite_part = part('calcite', dim=calcite_dim, center=[0,0,0])
    pyrite_part = part('pyrite', dim=pyrite_dim, center=[0,0,0])

    for i in range(num):
        pyrite_ins.append(instance('pyrite-'+str(i), script_part=pyrite_part))
        part_name_list.append('pyrite-'+str(i))
    calcite_ins.append(instance('calcite-1', script_part=calcite_part))
    part_name_list.append('calcite-1')
    with open(part_name_file, 'w') as f:
        json.dump(part_name_list, f)

def create_3D_distro(num_crystal):
    #copy .\geometry.peter \\ad.monash.edu\home\User045\dche145\Documents\Abaqus\microwave-break-rocks\geometry.peter
    geo_distro_3D = 'geometry.peter'
    with open(geo_distro_3D, 'rb') as f:
        read_out = json.load(f)
        loc = np.array(read_out[0])
        Rx = np.array(read_out[1])
        Ry = np.array(read_out[2])
        Rz = np.array(read_out[3])
        theta_x = np.array(read_out[4])
        theta_y = np.array(read_out[5])
        theta_z = np.array(read_out[6])


    for i in range(num_crystal):
        pyrite_ins[i].rotate([theta_x[i],theta_y[i], theta_z[i]])
        pyrite_ins[i].translate(loc[i])
        pass

def merge_and_material():
    all_parts = []
    for i in range(num_crystal):
        all_parts.append(pyrite_ins[i].part)
    all_parts.append(calcite_ins[0].part)

    assembly.InstanceFromBooleanMerge(name='merged-1', instances=all_parts,
        keepIntersections=ON, originalInstances=SUPPRESS, domain=GEOMETRY)
    with open(part_name_file, 'r') as f:
        part_name_list_read = json.load(f)
        part_name_list_read.append('merged-1')
    with open(part_name_file, 'w') as f:
        json.dump(part_name_list_read, f)
    merged_part = mdb.models[assem_name].parts['merged-1']
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

def get_output_data(name_job, step, frame, meta_data = None):
    file_path = name_job +'.odb'
    odb = session.openOdb(name=file_path)
    # odb = session.odbs[file_path]
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
#getting the output data from the model
    session.Path(name='Path-diagonal', type=POINT_LIST, expression=((0.0299999993294477,0.0299999993294477,0.0),
    (-0.0299999993294477,-0.0299999993294477,0.0)))
    session.Path(name='Path-horizontal', type=POINT_LIST, expression=((0.0299999993294477,0.0299999993294477,0.0),
    (-0.0299999993294477,-0.0299999993294477,0.0)))
    pth_dia = session.paths['Path-diagonal']
    pth_hor = session.paths['Path-horizontal']

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

            num_intervals = 150
            session.XYDataFromPath(name=xy_data_name, path=pth_dia, includeIntersections=False,
                projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=num_intervals,
                projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE,
                removeDuplicateXYPairs=True, includeAllElements=False)
            xy_data[i].append(session.xyDataObjects[xy_data_name].data)

    meta_data['step'] = step
    meta_data['frame'] = frame
    meta_data['num_intervals'] = num_intervals

    global new_session

    if new_session:
        new_session=False
        mode = 'wb'
    else:
        mode = 'ab'

    with open(working_dir + 'saved_data', mode) as f:
        pickle.dump(meta_data, f)
        pickle.dump(xy_data, f)



if __name__== "__main__":
    # assem_name = 'square-3d-macro-start-origin'
    assem_name = 'square-3d'

    assembly = mdb.models[assem_name].rootAssembly
    num_change_flux = 25
    magnitude = np.linspace(10e6, 10e10, num_change_flux)
    timePeriod=10.0
    increment=0.2
    step = 1
    frame = int(np.ceil(timePeriod/increment))
    num_crystal = 10
    new_session = True
    clean_up_geo_test = False
    # import_3D_geo_shape(num_crystal)
    # create_3D_distro(num_crystal)
    # merge_and_material()


    for i in xrange(num_change_flux):
        timePeriod -= 6.0/num_change_flux
        name_job = run_job(magnitude[i], timePeriod, increment)
        meta_data = {
            'name': name_job,
            'magnitude': magnitude[i],
        }
        get_output_data(name_job, step, frame, meta_data)

    # How to copy Macro
    # shutil.copyfile('C:/Users/dche145/abaqusMacros.py', r'//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/macro.py')
    # execfile('//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/master_macro.py', __main__.__dict__)
