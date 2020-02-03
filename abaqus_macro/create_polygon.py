from abaqus import *
from abaqusConstants import *
import numpy as np
import os
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
import pickle

def isCollinear(p0, p1, p2):
    p0 = np.array(p0)
    p1 = np.array(p1)
    p2 = np.array(p2)
    e1 = p0 - p1
    e2 = p2 - p1
    x = np.cross(e1, e2)
    if sum(abs(x)) < 1e-5:
        return True
    else:
        return False

data = []
convexHull = []

with open(r'C:\peter_abaqus\Summer-Research-Project\meep\polygon1.csv', 'rb') as f:
	data = pickle.load(f)
with open(r'C:\peter_abaqus\Summer-Research-Project\meep\polygon1-hull.csv', 'rb') as f:
	convexHull = pickle.load(f)

for i in range(len(data)):
	# create coordinate reference and supress
	part_name = 'Part-'+str(i)
	p = mdb.models['Model-1'].Part(name=part_name, dimensionality=THREE_D, type=DEFORMABLE_BODY)
	p.ReferencePoint(point=(0.0, 0.0, 0.0))	
	p.features['RP'].suppress()

	for item in data[i]:
		p.DatumPointByCoordinate(coords=(item[0], item[1], item[2]))
		
	d1 = p.datums

	# join datum for edges
	for hull in convexHull[i]:
		p.WirePolyLine(points=((d1[int(hull[0])+1], d1[int(hull[1])+1]),), mergeType=IMPRINT, meshable=ON)
		p.WirePolyLine(points=((d1[int(hull[1])+1], d1[int(hull[2])+1]),), mergeType=IMPRINT, meshable=ON)
		p.WirePolyLine(points=((d1[int(hull[2])+1], d1[int(hull[0])+1]),), mergeType=IMPRINT, meshable=ON)
		
	eg = p.edges


	# create faces
	for p in convexHull[i]:
		seq = []
		wireSet = []
		for edge in eg:
			point = edge.pointOn[0]
			if isCollinear(point, d1[int(p[0])+1].pointOn,d1[int(p[1])+1].pointOn):	
				if 1 in wireSet:
					continue
				else:
					seq.append(edge)
					wireSet.append(1)
			if isCollinear(point, d1[int(p[1])+1].pointOn,d1[int(p[2])+1].pointOn):
				if 2 in wireSet:
					continue
				else:
					seq.append(edge)
					wireSet.append(2)
			if isCollinear(point, d1[int(p[2])+1].pointOn,d1[int(p[0])+1].pointOn):
				if 3 in wireSet:
					continue
				else:
					seq.append(edge)
					wireSet.append(3)
			if len(seq) == 3:
				p = mdb.models['Model-1'].parts[part_name]
				p.CoverEdges(edgeList = seq, tryAnalytical=True)
				break


	p = mdb.models['Model-1'].parts[part_name]
	f = p.faces
	p.AddCells(faceList = f)

# execfile('C:/peter_abaqus/Summer-Research-Project/abaqus_macro/create_polygon.py', __main__.__dict__)
