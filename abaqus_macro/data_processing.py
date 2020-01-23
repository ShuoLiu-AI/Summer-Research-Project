import pickle
import numpy as np

def get_name_job(magnitude):
    name_job = '%.2E' % (magnitude/100)
    name_job = name_job.replace('.', '')
    name_job = 'heatflux' + name_job.replace('+', '')
    return name_job

num_change_flux = 10
magnitude = np.linspace(10e6, 10e10, num_change_flux)

xy_data = []

for i in range(num_change_flux):
    name_job = get_name_job(magnitude[i])
    with open(name_job, 'wb') as f:
        xy_data.append(pickle.load(f))
