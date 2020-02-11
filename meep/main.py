from meep_funcs import *
import sys

np.random.seed(15)

def b_voronoi(n_towers = 20):
    towers = np.random.rand(n_towers, 3)

    bounding_box = np.array([0., 1., 0., 1., 0., 1.]) # [x_min, x_max, y_min, y_max]
    vor = bounded_voronoi.voronoi(towers, bounding_box)

    points = []
    hull = []

    for i in range(len(vor.regions)):
        points.append(vor.vertices[vor.regions[i]])

    hull = convex_hull.get_conv_hull(points, 'polygon1.csv', 'polygon1-hull.csv')

    convex_hull.plot_hull(vor.vertices, hull)
    # convex_hull.plot_hull(points, hull)
    print('created ' + str(len(vor.regions)) + ' polygons')

def create_sim():
    size_cell = [2, 2, 2]
    size_solid = [0.5, 0.5, 0.5]
    size_crystal_base = [0.1, 0.1, 0.1]
    num_crystal = 200
    pml_layers = [mp.PML(0.3)]

    dist = float(sys.argv[1])

    solid_region1 = mp.Block(size_solid, 
                        center = mp.Vector3(dist/2. + 0.25, 0., 0.),
                        material=mp.Medium(epsilon=7.69, D_conductivity=2*math.pi*0.42*2.787/3.4))

    solid_region2 = mp.Block(size_solid, 
                        center = mp.Vector3(-dist/2 - 0.25,  0., 0.),
                        material=mp.Medium(epsilon=7.69, D_conductivity=2*math.pi*0.42*2.787/3.4))

    geometry = [solid_region1, solid_region2]

    source_pad = 0.25
    source = [mp.Source(mp.ContinuousSource(wavelength=2*(11**0.5), width=20),
                    component= mp.Ez,
                    center=mp.Vector3(0.55, 0, 0),
                    size=mp.Vector3(0, 0.1, 0.1))]

    # sim = mp.Simulation(resolution=int(50),
    #         cell_size=size_cell,
    #         boundary_layers=pml_layers,
    #         sources = source,
    #         epsilon_func = my_eps)
            
    # gen_polygon_data()

    sim_diff_dist = mp.Simulation(resolution=30,
                    cell_size=size_cell,
                    boundary_layers=pml_layers,
                    sources = source,
                    geometry=geometry,
                    default_material=mp.Medium(epsilon=7.1))
    # vis(sim_diff_dist)
    return sim_diff_dist


b_voronoi(20)

# get_sim_output(str(sys.argv[2]), create_sim(), length_t = 40, out_every=0.6, get_3_field=False)
# out_num_geo('checker_geo.bin', my_checker_geo, range_geo=[1.0,1.0,1.0], range_index=[100,100,100])
