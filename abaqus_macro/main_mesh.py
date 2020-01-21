# -*- coding: mbcs -*-
# Do not delete the following import lines
import sys
import pickle
import numpy as np
import json
import os
import sys
import shutil
import unicodedata

# working_dir = r'//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/'
working_dir = r'C:/peter_abaqus/Summer-Research-Project/'

sys.path.append(working_dir)
# os.chdir(working_dir)
import helpers
reload(helpers)
from helpers import *

import global_var 
reload(global_var)
from global_var import *

import create_material 
reload(create_material)
from create_material import *


assem_name = 'test_construction'
model = mdb.models[assem_name]
assembly = model.rootAssembly


def import_geo_info():
    global num_crystal
    global a_size
    global b_size
    global theta_x
    global theta_y
    global theta_z
    global loc
    geo_distro_3D = working_dir + 'working_with_meep\geometry.peter'
    with open(geo_distro_3D, 'rb') as f:
        read_out = json.load(f)

        num_crystal = read_out[0]
        a_size = read_out[1]
        b_size = read_out[2]
        for i in range(len(a_size)):
            a_size[i] = float(a_size[i])
        for i in range(len(b_size)):
            b_size[i] = float(b_size[i])
        loc = np.array(read_out[3])
        theta_x = np.array(read_out[4])
        theta_y = np.array(read_out[5])
        theta_z = np.array(read_out[6])


def merge_and_material():
    #generate the mesh

    global pyrite_part
    global calcite_part
    global assem_pyrite_ins
    global assem_calcite_ins

    pyrite_part =[]
    calcite_part =[]
    assem_pyrite_ins =[]
    assem_calcite_ins =[]

    calcite_part = part('calcite', dim=a_size, center=[0,0,0])
    pyrite_part = part('pyrite', dim=b_size, center=[0,0,0])

    a = model.parts['pyrite']
    c_a = a.cells
    b = model.parts['calcite']
    c_b = b.cells

    create_material_section()

    a.SectionAssignment(region=(c_a,), sectionName='quartz', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)
    b.SectionAssignment(region=(c_b,), sectionName='feldspar', offset=0.0, 
        offsetType=MIDDLE_SURFACE, offsetField='', 
        thicknessAssignment=FROM_SECTION)

    a.seedPart(size=0.2, deviationFactor=0.1, minSizeFactor=0.1)
    a.generateMesh()
    b.seedPart(size=0.2, deviationFactor=0.1, minSizeFactor=0.1)
    b.generateMesh()

    for i in range(num_crystal):
        assem_pyrite_ins.append(instance('pyrite-'+str(i), script_part=pyrite_part))

    assem_calcite_ins.append(instance('calcite-1', script_part=calcite_part))

    assem_all_ins = [assem_pyrite_ins[i].part for i in range(len(assem_pyrite_ins))]
    for ins in assem_calcite_ins:
        assem_all_ins.append(ins.part)

    global theta_x
    global theta_y
    global theta_z
    global loc

    for i in range(len(assem_pyrite_ins)):
        assem_pyrite_ins[i].rotate([theta_x[i],theta_y[i], theta_z[i]])
        assem_pyrite_ins[i].translate(loc[i])

    assembly.InstanceFromBooleanMerge(name='merged_mesh', instances= assem_all_ins, mergeNodes=ALL, nodeMergingTolerance=1e-06, domain=MESH, originalInstances=SUPPRESS)

    print(len(assem_pyrite_ins))
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
    # while os.path.isfile(name_job+'.023') or os.path.isfile(name_job+'.lck') == True:
    #     sleep(0.1)
    shutil.copyfile(name_job+'.odb', working_dir+'data_base'+'/'+name_job+'.odb')
    return name_job

def get_output_data(name_job, step, frame, num_intervals, meta_data = None):
    file_path = name_job +'.odb'
    odb = session.openOdb(name=file_path)
    # odb = session.odbs[file_path]
    session.viewports['Viewport: 1'].setValues(displayedObject=odb)
    #getting the output data from the model
    session.Path(name='Path-diagonal', type=POINT_LIST, expression=((0.0299999993294477,0.0299999993294477,0.0),
    (-0.0299999993294477,-0.0299999993294477,0.0)))
    pth_dia = session.paths['Path-diagonal']

    xy_data = [[] for i in range(frame)]
    xy_data_name = ''
    xy_data_name_str = ''


    for i in xrange(frame):
        session.viewports['Viewport: 1'].odbDisplay.setFrame(step=0, frame=i)
        xy_data_name = name_job + 'stress' + str(i)

        if i is not frame-1:
            xy_data_name_str += xy_data_name +','
        else:
            xy_data_name_str += xy_data_name

        session.XYDataFromPath(name=xy_data_name, path=pth_dia, includeIntersections=False,
            projectOntoMesh=False, pathStyle=UNIFORM_SPACING, numIntervals=num_intervals,
            projectionTolerance=0, shape=UNDEFORMED, labelType=TRUE_DISTANCE,
            removeDuplicateXYPairs=True, includeAllElements=False)
        xy_data[i] = session.xyDataObjects[xy_data_name].data

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
    try:
        import_geo_info()

        merge_and_material()
        # mesh_it()
        # boundary('encastre')
        # load()
    except Exception as inst:
        print type(inst)     # the exception instance
        print inst.args
        print inst

    # for i in xrange(num_change_flux):
    #     name_job = run_job(magnitude[i], timePeriod, increment)
    #     meta_data = {
    #         'name': name_job,
    #         'magnitude': magnitude[i],
    #     }
    #     get_output_data(name_job, step, frame, num_intervals, meta_data)

    # run on TeamViewer
    # shutil.copyfile('C:/Users/zivan/abaqusMacros.py', r'C:/peter_abaqus/Summer-Research-Project/macro.py')
    # shutil.copyfile('C:/temp/dflux.inp', r'C:/peter_abaqus/Summer-Research-Project/abaqus_working_space/abaqus_out/dflux.inp')
    # shutil.copyfile('C:/temp/test_ori.inp', r'C:/peter_abaqus/Summer-Research-Project/abaqus_working_space/abaqus_out/test_ori.inp')
    # execfile('C:/peter_abaqus/Summer-Research-Project/main_mesh.py', __main__.__dict__)
    # os.chdir(r"C:\peter_abaqus\Summer-Research-Project\abaqus_working_space\abaqus_out")

    # Run on Citrix
    # shutil.copyfile('C:/Users/dche145/abaqusMacros.py', r'//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/macro.py')
    # execfile('//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/main.py', __main__.__dict__)
