from data_file import source_list_garrett, flux_list_2_87mm_garrett, flux_barenfeld_0_88_error_updated,\
    radius_dust_updated, surface_density_list, surface_density_list_lower_bound, surface_density_list_upper_bound, AU_to_cm
from Table_3 import opacity_list_3mm, opacity_list_3mm_lower_error, opacity_list_3mm_upper_error, opacity_list_0_87mm, temperature_list_van_der_plas
from Planck import planck_function_frequency
from Parallaxes import distances_updated_upper_sco

from astropy import constants
from tabulate import tabulate
import numpy as np
from scipy.integrate import quad

# Constants and data import
k_0 = 10
nu_0 = 10 ** 12
pc_to_cm = 3.1 * 10 ** 18
M_earth = constants.M_earth.cgs.value
table = []
distance_updated_upper_sco_in_cm = [x * pc_to_cm for x in distances_updated_upper_sco]

# Define the function for mass calculation
def Mass(flux, distance, opacity, planck):
    return flux * (distance ** 2) / (opacity * planck)

# Define the integrand function for the dust mass calculation
def integrand(R, surface_density_list):
    return 2 * np.pi * 10 ** surface_density_list * (R / (10 * AU_to_cm)) ** (-1) * R

# Calculate masses for 3 mm observations
mass_list_3mm = []
mass_list_3mm_lower_limit = []
mass_list_3mm_upper_limit = []
for x in range(len(flux_list_2_87mm_garrett)):
    mass_list_3mm.append(Mass(flux_list_2_87mm_garrett[x] * 10 ** (-26), distance_updated_upper_sco_in_cm[x],
                              opacity_list_3mm[x], planck_function_frequency((3*(10**10)) / 0.287, temperature_list_van_der_plas[x])))
    mass_list_3mm_upper_limit.append(Mass(flux_list_2_87mm_garrett[x] * 10 ** (-26), distance_updated_upper_sco_in_cm[x],
                                          opacity_list_3mm[x] - opacity_list_3mm_lower_error[x], planck_function_frequency((3*(10**10)) / 0.287, temperature_list_van_der_plas[x])))
    mass_list_3mm_lower_limit.append(Mass(flux_list_2_87mm_garrett[x] * 10 ** (-26), distance_updated_upper_sco_in_cm[x],
                                            opacity_list_3mm[x] + opacity_list_3mm_upper_error[x], planck_function_frequency((3*(10**10)) / 0.287, temperature_list_van_der_plas[x])))

# Calculate the upper and lower uncertainties of 3mm masses
mass_list_3mm_upper_limit = [mass_list_3mm_upper_limit[x] - mass_list_3mm[x] for x in range(len(mass_list_3mm))]
mass_list_3mm_lower_limit = [mass_list_3mm[x] - mass_list_3mm_lower_limit[x] for x in range(len(mass_list_3mm))]

# Calculate masses for 0.88 mm observations
mass_list_0_88mm = []
mass_list_0_88mm_lower_limit = []
mass_list_0_88mm_upper_limit = []

for x in range(len(flux_list_2_87mm_garrett)):
    mass_list_0_88mm.append(Mass(flux_barenfeld_0_88_error_updated[x] * 10 ** (-26), distance_updated_upper_sco_in_cm[x],
                                 opacity_list_0_87mm[x], planck_function_frequency((3*(10**10)) / 0.088, temperature_list_van_der_plas[x])))
    mass_list_0_88mm_upper_limit.append(Mass(flux_barenfeld_0_88_error_updated[x] * 10 ** (-26), distance_updated_upper_sco_in_cm[x],
                                                opacity_list_0_87mm[x] - opacity_list_3mm_lower_error[x], planck_function_frequency((3*(10**10)) / 0.088, temperature_list_van_der_plas[x])))
    mass_list_0_88mm_lower_limit.append(Mass(flux_barenfeld_0_88_error_updated[x] * 10 ** (-26), distance_updated_upper_sco_in_cm[x],
                                                opacity_list_0_87mm[x] + opacity_list_3mm_upper_error[x], planck_function_frequency((3*(10**10)) / 0.088, temperature_list_van_der_plas[x])))

# Calculate the upper and lower uncertainties of 3mm masses
mass_list_0_88mm_upper_limit = [mass_list_0_88mm_upper_limit[x] - mass_list_0_88mm[x] for x in range(len(mass_list_3mm))]
mass_list_0_88mm_lower_limit = [mass_list_0_88mm[x] - mass_list_0_88mm_lower_limit[x] for x in range(len(mass_list_3mm))]

mass_list_integral = []
mass_list_integral_upper_limit = []
mass_list_integral_lower_limit = []
for x in range(len(source_list_garrett)):
    mass_list_integral.append(quad(integrand, 0.1 * AU_to_cm, radius_dust_updated[x] * AU_to_cm, args=(surface_density_list[x]))[0])
    mass_list_integral_upper_limit.append(quad(integrand, 0.1 * AU_to_cm, radius_dust_updated[x] * AU_to_cm, args=(surface_density_list[x] + surface_density_list_upper_bound[x]))[0])
    mass_list_integral_lower_limit.append(quad(integrand, 0.1 * AU_to_cm, radius_dust_updated[x] * AU_to_cm, args=(surface_density_list[x] + surface_density_list_lower_bound[x]))[0])

mass_list_integral_upper_limit = [mass_list_integral_upper_limit[x] - mass_list_integral[x] for x in range(len(mass_list_integral))]
mass_list_integral_lower_limit = [mass_list_integral[x] - mass_list_integral_lower_limit[x] for x in range(len(mass_list_integral))]

for x in range(len(source_list_garrett)):
    table.append([source_list_garrett[x],
                  str(round(mass_list_3mm[x] / M_earth, 4)) + '(' + str(round(mass_list_3mm_upper_limit[x]/M_earth, 4)) + ",-" + str(round(mass_list_3mm_lower_limit[x]/M_earth, 4)) + ")",
                  str(round(mass_list_0_88mm[x] / M_earth, 4)) + "(" + str(round(mass_list_0_88mm_upper_limit[x]/M_earth, 4)) + ",-" + str(round(mass_list_0_88mm_lower_limit[x]/M_earth, 4)) + ")",
                  str(round(mass_list_integral[x] / M_earth, 2)) + "(" + str(round(mass_list_integral_upper_limit[x]/M_earth, 2)) + ",-" + str(round(mass_list_integral_lower_limit[x]/M_earth, 2)) + ")"])

# create file on notepad called 'Table 4'
with open('Table 4.txt', 'w') as f:
    f.write(tabulate(table, headers=['Sources', 'M_{3mm}(M_{\quad})', 'M_{0.88mm}(M_{\quad})', 'Mass Integral']))


#print(tabulate(table, headers=['Sources', 'M_{3mm}(M_{\quad})', 'M_{0.88mm}(M_{\quad})', 'Mass Integral']))
import pandas as pd
table_4_pandas = pd.DataFrame(table, columns=['Sources', 'M_{3mm}(M_{\oplus})', 'M_{0.88mm}(M_{\oplus})', 'Mass Integral'])
table_4_pandas.to_latex('Table 4 pandas.tex', index=False, escape=False, longtable=True, column_format='lccc')

if __name__ == '__main__':
    print(tabulate(table, headers=['Sources', 'M_{3mm}(M_{\quad})', 'M_{0.88mm}(M_{\quad})', 'Mass Integral']))