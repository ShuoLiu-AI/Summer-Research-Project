from abaqus import *
from abaqusConstants import *

feldspar_prop = {
    'name': 'feldspar',
    'expansion':(
    (3.6E-06,  25),
    (4.6E-06,  119.85),
    (5.19E-06,  219.85),
    (5.59E-06,  319.85),
    (5.89E-06,  419.85),
    (6.14E-06,  519.85),
    (6.37E-06,  619.85),
    (6.58E-06,  719.85),
    (6.78E-06,  819.85),
    (6.97E-06,  919.85),
    (7.12E-06,  1000)
    ),
    'density': (( 2.703e3, ), ),
    'conductivity':((1.46,),),
    'elastic':(( 87.02e9, 0.29), ),
    'mc_plasticity':((43.53, 46.0), ),
    'mc_harden':((28.4, 0.0), (28.4,0.001),(28.4,0.01),(28.4,1)),
    'mc_tension':((0.0, 0.0), ),
    'specificHeat':(
    (860, 50),
    (945, 200),
    (1054, 400),
    (1090, 500)
    )
}

quartz_prop = {
    'name' : 'quartz',
    'conductivity':(
        (8.0, 1.0), (6.5, 100.0), (5.5, 200.0), (4.5, 300.0), (4.0, 400.0), (3.8,
        500.0), (3.7, 550.0), (3.5, 575.0), (3.5, 580.0), (3.8, 600.0), (3.9,
        700.0), (4.0, 800.0)),
    'elastic':(
        (100e9 ,0.09, 0.0), (95e9, 0.085, 100.0), (90e9, 0.08, 200.0), (85e9,
        0.05, 300.0), (83e9, 0.0, 400.0), (80e9, -0.05, 500.0), (75e9,
        -0.1, 550.0), (60e9, -0.2, 575.0), (80e9, -0.3, 580.0), (95e9,
        0.2, 600.0), (100e9, 0.25, 700.0), (105e9, 0.25, 800.0)),
    'expansion':(
        (1e-05, 1.0), (1.25e-05, 100.0), (1.26e-05, 200.0), (1.27e-05, 300.0), (
        1.28e-05, 400.0), (1.5e-05, 500.0), (1.75e-05, 550.0), (2e-05, 575.0),
        (2.5e-05, 580.0), (2.25e-05, 600.0), (2.1e-05, 700.0), (2e-05, 800.0)),
    'specificHeat':(
        (700.0, 1.0), (810.0, 100.0), (910.0, 200.0), (1005.0, 300.0), (1100.0,
        400.0), (1190.0, 500.0), (1250.0, 550.0), (1400.0, 575.0), (1050.0,
        580.0), (1070.0, 600.0), (1080.0, 700.0), (1090.0, 800.0)),
    'density': (( 2.65E3, ),),
    'mc_plasticity':((43.53, 46.0), ),
    'mc_harden':((28.4, 0.0), (28.4,0.001),(28.4,0.01),(28.4,1)),
    'mc_tension':((0.0, 0.0), )
    # mat_quartz.mohrCoulombPlasticity.TensionCutOff(
    #     temperatureDependency=OFF, dependencies=0, table=((0.0, 0.0), ))
}


def assign_prop(mat, prop, MC=False):
    if len(prop['expansion']) > 1:
        mat.Expansion(temperatureDependency=ON, table=prop['expansion'])
    else:
        mat.Expansion(temperatureDependency=OFF, table=prop['expansion'])
    if len(prop['specificHeat']) > 1:
        mat.SpecificHeat(temperatureDependency=ON, table=prop['specificHeat'])
    else:
        mat.SpecificHeat(temperatureDependency=OFF, table=prop['specificHeat'])
    if len(prop['conductivity']) > 1:
        mat.Conductivity(temperatureDependency=ON, table=prop['conductivity'])
    else:
        mat.Conductivity(temperatureDependency=OFF, table=prop['conductivity'])
    if len(prop['density']) > 1:
        mat.Density(temperatureDependency=ON, table=prop['density'])
    else:
        mat.Density(temperatureDependency=OFF, table=prop['density'])
    if len(prop['elastic']) > 1:
        mat.Elastic(temperatureDependency=ON, table=prop['elastic'])
    else:
        mat.Elastic(temperatureDependency=OFF, table=prop['elastic'])

    if MC:
        mat.MohrCoulombPlasticity(
            table=prop['mc_plasticity'])
        mat.mohrCoulombPlasticity.MohrCoulombHardening(
            table=prop['mc_harden'])
        mat.mohrCoulombPlasticity.TensionCutOff(
            temperatureDependency=OFF, dependencies=0, table=prop['mc_tension'])
