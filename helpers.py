import numpy as np
from numpy import cos, sin

def get_name_job(magnitude):
    name_job = '%.2E' % (magnitude/100)
    name_job = name_job.replace('.', '')
    name_job = 'heatflux' + name_job.replace('+', '')
    return name_job

def matmul(X, Y):
    result = np.empty((3))
    for i in xrange(3):
        result[i] = np.sum(np.dot(X[i], Y))
    return result

def get_rx(theta):
    theta = -theta
    return [[1, 0, 0],
                   [0, cos(theta), -sin(theta)],
                  [0, sin(theta), cos(theta)]]


def get_ry(theta):
    theta = -theta
    return [[cos(theta), 0, sin(theta)],
                  [0, 1, 0],
                  [-sin(theta), 0, cos(theta)]]


def get_rz(theta):
    theta = -theta
    return [[cos(theta), -sin(theta), 0],
                 [sin(theta), cos(theta), 0],
                 [0, 0, 1]]

def delete(part_name_list):
    assembly.deleteFeatures(part_name_list)
