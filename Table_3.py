from astropy import constants
from tabulate import tabulate
from Planck import alpha
import numpy as np
from data_file import radius_dust_updated, AU_to_cm, source_list_garrett, lower_bound_radius_updated, upper_bound_radius_updated
from Table_1 import luminosity_list_patimo, lower_new_luminosity_error_log, upper_new_luminosity_error_log
from Histogram_spectral_index import spectral_index_upper_sco
from Van_der_Pals import derivation_van_der_pals_a, derivation_van_der_pals_b

print(lower_bound_radius_updated)
s_b = constants.sigma_sb.cgs.value
L_sun = constants.L_sun.cgs.value
c = constants.c.cgs.value
k_0 = 10
nu_0 = 10 ** 12
table = []
temperature_list_passive_heating = []
temperature_list_van_der_plas = []
temperature_list_van_der_plas_upper_error = []
temperature_list_van_der_plas_lower_error = []

def temperature(R, luminosity):
    return (0.02 * luminosity / (8 * np.pi * R**2 * s_b)) ** (1/4)

def van_der_pals_temperature(a, b, L):
    return a*(L**b)

for x in range(len(radius_dust_updated)):
    temperature_list_van_der_plas.append(van_der_pals_temperature(derivation_van_der_pals_a(radius_dust_updated[x]), derivation_van_der_pals_b(radius_dust_updated[x]), 10 ** luminosity_list_patimo[x]))

for x in range(len(radius_dust_updated)):
    temperature_list_van_der_plas_upper_error.append(van_der_pals_temperature(derivation_van_der_pals_a(radius_dust_updated[x] + lower_bound_radius_updated[x]), derivation_van_der_pals_b(radius_dust_updated[x]), 10 ** (luminosity_list_patimo[x] + upper_new_luminosity_error_log[x])))

for x in range(len(radius_dust_updated)):
    temperature_list_van_der_plas_lower_error.append(van_der_pals_temperature(derivation_van_der_pals_a(radius_dust_updated[x] + upper_bound_radius_updated[x]), derivation_van_der_pals_b(radius_dust_updated[x]), 10 ** (luminosity_list_patimo[x] - lower_new_luminosity_error_log[x])))

temperature_list_van_der_plas_upper_error = [temperature_list_van_der_plas_upper_error[x] - temperature_list_van_der_plas[x] for x in range(len(temperature_list_van_der_plas_upper_error))]
temperature_list_van_der_plas_lower_error = [temperature_list_van_der_plas[x] - temperature_list_van_der_plas_lower_error[x] for x in range(len(temperature_list_van_der_plas_lower_error))]

for x in range(len(luminosity_list_patimo)):
    temperature_list_passive_heating.append(temperature(radius_dust_updated[x] * AU_to_cm, (10 ** luminosity_list_patimo[x]) * L_sun))


alpha_planck_list = []
alpha_planck_list_lower_error = []
alpha_planck_list_upper_error = []
for x in range(len(temperature_list_van_der_plas)):
    alpha_planck_list.append(alpha(0.088, 0.287, temperature_list_van_der_plas[x]))
    alpha_planck_list_lower_error.append(alpha(0.088, 0.287, temperature_list_van_der_plas[x] - temperature_list_van_der_plas_lower_error[x]))
    alpha_planck_list_upper_error.append(alpha(0.088, 0.287, temperature_list_van_der_plas[x] + temperature_list_van_der_plas_upper_error[x]))

alpha_planck_list_lower_error = [alpha_planck_list[x] - alpha_planck_list_lower_error[x] for x in range(len(alpha_planck_list_lower_error))]
alpha_planck_list_upper_error = [alpha_planck_list_upper_error[x] - alpha_planck_list[x] for x in range(len(alpha_planck_list_upper_error))]

beta_list = []
beta_list_lower_error = []
beta_list_upper_error = []
for x in range(len(spectral_index_upper_sco)):
    beta_list.append(spectral_index_upper_sco[x] - alpha_planck_list[x])
    beta_list_lower_error.append(spectral_index_upper_sco[x] - (alpha_planck_list[x] + alpha_planck_list_upper_error[x]))
    beta_list_upper_error.append(spectral_index_upper_sco[x] - (alpha_planck_list[x] - alpha_planck_list_lower_error[x]))

beta_list_lower_error = [beta_list[x] - beta_list_lower_error[x] for x in range(len(beta_list_lower_error))]
beta_list_upper_error = [beta_list_upper_error[x] - beta_list[x] for x in range(len(beta_list_upper_error))]

opacity_list_3mm = []
opacity_list_3mm_lower_error = []
opacity_list_3mm_upper_error = []
for x in range(len(beta_list)):
    opacity_list_3mm.append(k_0 * (((c / 0.287) / nu_0) ** beta_list[x]))
    opacity_list_3mm_upper_error.append(k_0 * (((c / 0.287) / nu_0) ** (beta_list[x] - beta_list_lower_error[x])))
    opacity_list_3mm_lower_error.append(k_0 * (((c / 0.287) / nu_0) ** (beta_list[x] + beta_list_upper_error[x])))

opacity_list_3mm_lower_error = [opacity_list_3mm[x] - opacity_list_3mm_lower_error[x] for x in range(len(opacity_list_3mm_lower_error))]
opacity_list_3mm_upper_error = [opacity_list_3mm_upper_error[x] - opacity_list_3mm[x] for x in range(len(opacity_list_3mm_upper_error))]

opacity_list_0_87mm = []
opacity_list_0_87mm_lower_error = []
opacity_list_0_87mm_upper_error = []
for x in range(len(beta_list)):
    opacity_list_0_87mm.append(k_0 * (((c / 0.088) / nu_0) ** beta_list[x]))
    opacity_list_0_87mm_lower_error.append(k_0 * (((c / 0.088) / nu_0) ** (beta_list[x] - beta_list_lower_error[x])))
    opacity_list_0_87mm_upper_error.append(k_0 * (((c / 0.088) / nu_0) ** (beta_list[x] + beta_list_upper_error[x])))

opacity_list_0_87mm_lower_error = [opacity_list_0_87mm_lower_error[x] - opacity_list_0_87mm[x] for x in range(len(opacity_list_0_87mm_lower_error))]
opacity_list_0_87mm_upper_error = [opacity_list_0_87mm[x] - opacity_list_0_87mm_upper_error[x] for x in range(len(opacity_list_0_87mm_upper_error))]

for x in range(len(beta_list)):
    table.append([source_list_garrett[x], str(round(temperature_list_van_der_plas[x], 2)) + '(' + str(round(temperature_list_van_der_plas_upper_error[x], 2)) + ',-' + str(round(temperature_list_van_der_plas_lower_error[x], 2)) + ')',
                  str(round(alpha_planck_list[x], 2)) + '(' + str(round(alpha_planck_list_upper_error[x], 2)) + ',-' + str(round(alpha_planck_list_lower_error[x], 2)) + ')',
                  str(round(beta_list[x], 2)) + '(' + str(round(beta_list_upper_error[x], 2)) + ',-' + str(round(beta_list_lower_error[x], 2)) + ')',
                  str(round(opacity_list_3mm[x], 2)) + '(' + str(round(opacity_list_3mm_upper_error[x], 2)) + ",-" + str(round(opacity_list_3mm_lower_error[x], 2)) + ')',
                  str(round(opacity_list_0_87mm[x], 2)) + "(" + str(round(opacity_list_0_87mm_upper_error[x], 2)) + ",-" + str(round(opacity_list_0_87mm_lower_error[x], 2)) + ')'])

# create file on notepad called 'Table 2'
with open('Table 3.txt', 'w') as f:
    f.write(tabulate(table, headers=['Sources', 'Temperature(K)', r'\alpha_{Planck}', r'\beta', r'\kappa_{3mm}', r'\kappa_{0.88mm}']))

#print(tabulate(table, headers=['Sources', 'Temperature(K)', r'\alpha_{Planck}', r'\beta', r'\kappa_{3mm}', r'\kappa_{0.87mm}']))

import pandas as pd
table_3_pandas = pd.DataFrame(table, columns=['Sources', 'Temperature(K)', r'\alpha_{Planck}', r'\beta', r'\kappa_{2.87mm}', r'\kappa_{0.88mm}'])
table_3_pandas.to_latex('Table 3 pandas.tex', index=False, longtable=True, escape=False, column_format='lcccccc')
