import numpy as np
# import matplotlib.plot as plt
import pickle
import json
import os
import shutil
shutil.copyfile(r'\\ad.monash.edu\home\User045\dche145\Documents\Abaqus\geometry_shapes\geometry.peter', r'geometry.peter')

file_name = 'geometry.peter'
with open(file_name, 'rb') as f:
    read_out = json.load(f)
    loc = read_out[0]
    Rx = read_out[1]
    Ry = read_out[2]
    Rz = read_out[3]
    theta_x = read_out[4]
    theta_y = read_out[5]
    theta_z = read_out[6]

num_crystal = 10
axis_points_x = [[1, 0, 0] for i in range(num_crystal)]
axis_points_y = [[0, 1, 0] for i in range(num_crystal)]
axis_points_z = [[0, 0, 1] for i in range(num_crystal)]

axis_dir_x = [[-1, 0, 0] for i in range(num_crystal)]
axis_dir_y = [[0, -1, 0] for i in range(num_crystal)]
axis_dir_z = [[0, 0, -1] for i in range(num_crystal)]

for i in range(num_crystal):
    pyrite_parts[i].translate((0, -pyrite_parts[i].dim/2, 0))
    #translate the crystals to the origin

for i in range(num_crystal):
    #rotate the crystals
    assembly.rotate(instanceList=('pyrite'+str(i+1)), axisPoint=axis_points_x[i], 
    axisDirection=axis_dir_x[i], angle=theta_x[i])
    axis_points_x[i] = np.matmul(Rx[i], axis_points_x[i])
    axis_points_y[i] = np.matmul(Rx[i], axis_points_y[i])
    axis_points_z[i] = np.matmul(Rx[i], axis_points_z[i])
    assembly.rotate(instanceList=('pyrite'+str(i+1)), axisPoint=axis_points_y[i], 
    axisDirection=axis_dir_y[i], angle=theta_y[i])
    axis_points_x[i] = np.matmul(Ry[i], axis_points_x[i])
    axis_points_y[i] = np.matmul(Ry[i], axis_points_y[i])
    axis_points_z[i] = np.matmul(Ry[i], axis_points_z[i])
    assembly.rotate(instanceList=('pyrite'+str(i+1)), axisPoint=axis_points_z[i], 
    axisDirection=axis_dir_z[i], angle=theta_z[i])
    axis_points_x[i] = np.matmul(Rz[i], axis_points_x[i])
    axis_points_y[i] = np.matmul(Rz[i], axis_points_y[i])
    axis_points_z[i] = np.matmul(Rz[i], axis_points_z[i])

for i in range(num_crystal):
    #translate the crystals to the desired location
    pyrite_parts[i].translate(loc[i])