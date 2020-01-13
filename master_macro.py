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

# working_dir = r'//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/'
working_dir = r'C:/peter_abaqus/Summer-Research-Project/'
sys.path.append(working_dir)
# os.chdir(working_dir)
import helpers
from mat_prop import *
from global_var import *
reload(helpers)
from helpers import *

def import_3D_geo_shape(num):
    if clean_up_geo_test:
        with open(part_name_file) as f:
            part_name_list_read = json.load(f)
            for i in range(len(part_name_list_read)):
                part_name_list_read[i] = unicodedata.normalize(
                'NFKD', part_name_list_read[i]).encode('ascii','ignore')
        assembly.deleteFeatures(part_name_list_read)
    #define the geometric shape size and location
    calcite_dim = [1.0, 1.0, 1.0]
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
    geo_distro_3D = working_dir + 'geometry.peter'
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

    #cut so to get rid of external regions
    instance('calcite-for-cut', script_part=calcite_part)
    for i in xrange(num_crystal):
        assembly.InstanceFromBooleanCut(name='pyrite-to-get-rid-'+str(i), 
            instanceToBeCut=assembly.instances['pyrite-'+str(i)], 
            cuttingInstances=(assembly.instances['calcite-for-cut'], ), 
            originalInstances=SUPPRESS)
        assembly.features['pyrite-'+str(i)].resume()
        assembly.features['calcite-for-cut'].resume()

    del assembly.features['calcite-for-cut']

    assembly.InstanceFromBooleanMerge(name='merged', instances=all_parts,
        keepIntersections=ON, originalInstances=DELETE, domain=GEOMETRY)

    assembly.InstanceFromBooleanCut(name='merged', 
        instanceToBeCut=assembly.instances['merged-1'], 
        cuttingInstances=(list(assembly.instances['pyrite-to-get-rid-'+ str(i) + '-1'] for i in xrange(num_crystal))), 
        originalInstances=DELETE)

    for i in xrange(num_crystal):
        del model.parts['pyrite-to-get-rid-'+str(i)]

    with open(part_name_file, 'r') as f:
        part_name_list_read = json.load(f)
        part_name_list_read.append('merged-1')
    with open(part_name_file, 'w') as f:
        json.dump(part_name_list_read, f)

    merged_part = model.parts['merged']
    
    global a_cells
    global b_cells
    for cell in merged_part.cells:
        if(cell.getSize() > pyrite_ins[0].size):
            a_cells.append(cell)
        else:
            b_cells.append(cell)

    merged_part.SectionAssignment(region=a_cells, sectionName='feldspar', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

    merged_part.SectionAssignment(region=b_cells, sectionName='quartz', offset=0.0,
    offsetType=MIDDLE_SURFACE, offsetField='',
    thicknessAssignment=FROM_SECTION)

    session.viewports['Viewport: 1'].setValues(displayedObject=assembly)
    session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON,
        predefinedFields=ON, connectors=ON)
    assembly.regenerate()
    return merged_part

def mesh_it(part):
    # Assign an element type to the part instance.
    region = (part.cells,)
    elemType = mesh.ElemType(elemCode=C3D10MT, elemLibrary=STANDARD)
    myAssembly.setElementType(regions=region, elemTypes=(elemType,))

    # Seed the part instance.

    myAssembly.seedPartInstance(regions=(part,), size=0.06)

    # Mesh the part instance.

    myAssembly.generateMesh(regions=(part,))

    # Display the meshed beam.
    if disp_mesh:
        myViewport.assemblyDisplay.setValues(mesh=ON)
        myViewport.assemblyDisplay.meshOptions.setValues(meshTechnique=ON)
        myViewport.setValues(displayedObject=myAssembly)
        
def load():
    # Find the end face using coordinates.

    endFaceCenter = (-100,0,12.5)
    endFace = myInstance.faces.findAt((endFaceCenter,) )

    # Create a boundary condition that encastres one end
    # of the beam.

    endRegion = (endFace,)
    myModel.EncastreBC(name='Fixed',createStepName='beamLoad',
        region=endRegion)

    # Find the top face using coordinates.

    topFaceCenter = (0,10,12.5)
    topFace = myInstance.faces.findAt((topFaceCenter,) )

    # Create a pressure load on the top face of the beam.

    topSurface = ((topFace, SIDE1), )
    myModel.Pressure(name='Pressure', createStepName='beamLoad',
        region=topSurface, magnitude=0.5)

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
    # assem_name = 'square-3d-macro-start-origin'
    assem_name = 'square-3d-macro-start-origin'
    model = mdb.models[assem_name]
    assembly = model.rootAssembly
    num_change_flux = 25
    magnitude = np.linspace(10, 500, num_change_flux)
    timePeriod=50.0
    increment=0.5
    frame = int(np.ceil(timePeriod/increment))
    num_intervals = 150

    step = 1 
    num_crystal = 10
    new_session = True
    clean_up_geo_test = False

    del assembly.features['merged-2']
    import_3D_geo_shape(num_crystal)
    create_3D_distro(num_crystal)
    merged_part = merge_and_material()
    mesh_it(merged_part)

    # for i in xrange(num_change_flux):
    #     name_job = run_job(magnitude[i], timePeriod, increment)
    #     meta_data = {
    #         'name': name_job,
    #         'magnitude': magnitude[i],
    #     }
    #     get_output_data(name_job, step, frame, num_intervals, meta_data)

    # run on TeamViewer
    # shutil.copyfile('C:/Users/zivan/abaqusMacros.py', r'C:/peter_abaqus/Summer-Research-Project/macro.py')
    # execfile('C:/peter_abaqus/Summer-Research-Project/master_macro.py', __main__.__dict__)
    # os.chdir(r"C:\peter_abaqus\Summer-Research-Project\abaqus_working_space\abaqus_out")

    # Run on Citrix
    # shutil.copyfile('C:/Users/dche145/abaqusMacros.py', r'//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/macro.py')
    # execfile('//ad.monash.edu/home/User045/dche145/Documents/Abaqus/microwave-break-rocks/master_macro.py', __main__.__dict__)