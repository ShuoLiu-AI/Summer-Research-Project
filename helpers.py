import numpy as np
from numpy import cos, sin

def get_name_job(magnitude):
    name_job = '%.2E' % (magnitude/100)
    name_job = name_job.replace('.', '')
    name_job = 'heatflux' + name_job.replace('+', '')
    return name_job

def matmul(X, Y):
    result = np.empty((len(X), len(Y[0])))
    for i in range(len(X)):
       # iterate through columns of Y
       for j in range(len(Y[0])):
           # iterate through rows of Y
           for k in range(len(Y)):
               result[i][j] += X[i][k] * Y[k][j]
    return result

def matmul_vec(X, Y):
    result = np.empty((3))
    for i in range(3):
        result[i] = np.sum(np.dot(X[i], Y))
    return result

def get_rx(theta):
    return [[1, 0, 0],
                   [0, cos(theta), -sin(theta)],
                  [0, sin(theta), cos(theta)]]


def get_ry(theta):
    return [[cos(theta), 0, sin(theta)],
                  [0, 1, 0],
                  [-sin(theta), 0, cos(theta)]]


def get_rz(theta):
    return [[cos(theta), -sin(theta), 0],
                 [sin(theta), cos(theta), 0],
                 [0, 0, 1]]

def delete(part_name_list):
    assembly.deleteFeatures(part_name_list)
