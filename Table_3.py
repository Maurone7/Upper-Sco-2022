from astropy import constants
from tabulate import tabulate
from Planck import alpha
import numpy as np
from data_file import radius_dust_updated, AU_to_cm, source_list_garrett, van_der_plas_radius
from Table_1 import luminosity_list_patimo
from Histogram_spectral_index import spectral_index_upper_sco
from Van_der_Pals import derivation_van_der_pals_a, derivation_van_der_pals_b

s_b = constants.sigma_sb.cgs.value
L_sun = constants.L_sun.cgs.value
c = constants.c.cgs.value
k_0 = 10
nu_0 = 10 ** 12
beta_list = []
opacity_list_3mm = []
opacity_list_0_87mm = []
table = []
alpha_planck_list = []
temperature_list_passive_heating = []
temperature_list_van_der_plas = []

def temperature(R, luminosity):
    return (0.02 * luminosity / (8 * np.pi * R**2 * s_b)) ** (1/4)

def van_der_pals_temperature(a, b, L):
    return a*(L**b)

for x in range(len(radius_dust_updated)):
    temperature_list_van_der_plas.append(van_der_pals_temperature(derivation_van_der_pals_a(radius_dust_updated[x]), derivation_van_der_pals_b(radius_dust_updated[x]), 10 ** luminosity_list_patimo[x]))

for x in range(len(luminosity_list_patimo)):
    temperature_list_passive_heating.append(temperature(radius_dust_updated[x] * AU_to_cm, (10 ** luminosity_list_patimo[x]) * L_sun))

for x in temperature_list_van_der_plas:
    alpha_planck_list.append(alpha(0.088, 0.287, x))

for x in range(len(spectral_index_upper_sco)):
    beta_list.append(spectral_index_upper_sco[x] - alpha_planck_list[x])

for x in range(len(beta_list)):
    opacity_list_3mm.append(k_0 * (((c / 0.287) / nu_0) ** beta_list[x]))

for x in range(len(beta_list)):
    opacity_list_0_87mm.append(k_0 * (((c / 0.088) / nu_0) ** beta_list[x]))

for x in range(len(beta_list)):
    table.append([source_list_garrett[x], round(temperature_list_van_der_plas[x], 2), round(alpha_planck_list[x], 2), round(beta_list[x], 2), round(opacity_list_3mm[x], 2), round(opacity_list_0_87mm[x], 2)])

# create file on notepad called 'Table 2'
with open('Table 3.txt', 'w') as f:
    f.write(tabulate(table, headers=['Sources', 'Temperature(K)', r'\alpha_{Planck}', r'\beta', r'\kappa_{3mm}', r'\kappa_{0.88mm}']))

#print(tabulate(table, headers=['Sources', 'Temperature(K)', r'\alpha_{Planck}', r'\beta', r'\kappa_{3mm}', r'\kappa_{0.87mm}']))

import pandas as pd
table_3_pandas = pd.DataFrame(table, columns=['Sources', 'Temperature(K)', r'\alpha_{Planck}', r'\beta', r'\kappa_{3mm}', r'\kappa_{0.88mm}'])
table_3_pandas.to_latex('Table 3 pandas.tex', index=False, longtable=True, escape=False, column_format='lcccccc')