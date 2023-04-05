from data_file import source_list_garrett, flux_list_2_87mm_garrett, flux_barenfeld_0_88_error_updated,\
    radius_dust_updated, surface_density_list, AU_to_cm
from Table_3 import opacity_list_3mm, opacity_list_0_87mm, temperature_list_van_der_plas
from Planck import planck_function_frequency
from Parallaxes import distances_updated_upper_sco

from astropy import constants
from tabulate import tabulate
import numpy as np
from scipy.integrate import quad

k_0 = 10
nu_0 = 10 ** 12
pc_to_cm = 3.1 * 10 ** 18
M_earth = constants.M_earth.cgs.value
table = []
mass_list_3mm = []
mass_list_0_88mm = []
mass_list_integral = []
distance_updaeted_upper_sco_in_cm = [x * pc_to_cm for x in distances_updated_upper_sco]

def Mass(flux, distance, opacity, planck, temperature):
    return flux * (distance ** 2) / (opacity * planck * temperature)


def integrand(R, surface_density_list):
    return 2 * np.pi * 10 ** surface_density_list * (R / (10 * AU_to_cm)) ** (-1) * R


for x in range(len(flux_list_2_87mm_garrett)):
    mass_list_3mm.append(Mass(flux_list_2_87mm_garrett[x] * 10 ** (-26), distance_updaeted_upper_sco_in_cm[x],
                              opacity_list_3mm[x], planck_function_frequency((3*(10**10)) / 0.287, temperature_list_van_der_plas[x]), temperature_list_van_der_plas[x]))

for x in range(len(flux_list_2_87mm_garrett)):
    mass_list_0_88mm.append(Mass(flux_barenfeld_0_88_error_updated[x] * 10 ** (-26), distance_updaeted_upper_sco_in_cm[x],
                                 opacity_list_0_87mm[x], planck_function_frequency((3*(10**10)) / 0.088, temperature_list_van_der_plas[x]), temperature_list_van_der_plas[x]))

for x in range(len(source_list_garrett)):
    mass_list_integral.append(quad(integrand, 0.1 * AU_to_cm, radius_dust_updated[x] * AU_to_cm, args=(surface_density_list[x]))[0])

for x in range(len(source_list_garrett)):
    table.append([source_list_garrett[x], round(mass_list_3mm[x] / M_earth, 4), round(mass_list_0_88mm[x] / M_earth, 4), round(mass_list_integral[x] / M_earth, 2)])

# create file on notepad called 'Table 4'
with open('Table 4.txt', 'w') as f:
    f.write(tabulate(table, headers=['Sources', 'M_{3mm}(M_{\quad})', 'M_{0.88mm}(M_{\quad})', 'Mass Integral']))


#print(tabulate(table, headers=['Sources', 'M_{3mm}(M_{\quad})', 'M_{0.88mm}(M_{\quad})', 'Mass Integral']))
import pandas as pd
table_4_pandas = pd.DataFrame(table, columns=['Sources', 'M_{3mm}(M_{\quad})', 'M_{0.88mm}(M_{\quad})', 'Mass Integral'])
table_4_pandas.to_latex('Table 4 pandas.tex', index=False, escape=False, longtable=True, column_format='lccc')