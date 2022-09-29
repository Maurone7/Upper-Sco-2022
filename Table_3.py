from astropy import constants
from tabulate import tabulate
from Planck  import alpha
import numpy as np
from data_file import radius_dust_updated, AU_to_cm, source_list_garrett
from Table_1 import luminosity_list_patimo
from Histogram_spectral_index import spectral_index_upper_sco

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
temperature_list = []

def temperature(R, luminosity):
    return (0.02 * luminosity / (8 * np.pi * R**2 * s_b)) ** (1/4)


for x in range(len(luminosity_list_patimo)):
    temperature_list.append(temperature(radius_dust_updated[x] * AU_to_cm, (10 ** luminosity_list_patimo[x]) * L_sun))

for x in temperature_list:
    alpha_planck_list.append(alpha(0.088, 0.287, x))

for x in range(len(spectral_index_upper_sco)):
    beta_list.append(spectral_index_upper_sco[x] - alpha_planck_list[x])

for x in range(len(beta_list)):
    opacity_list_3mm.append(k_0 * (((c / 0.287) / nu_0) ** beta_list[x]))

for x in range(len(beta_list)):
    opacity_list_0_87mm.append(k_0 * (((c / 0.088) / nu_0) ** beta_list[x]))

for x in range(len(beta_list)):
    table.append([source_list_garrett[x], round(temperature_list[x], 2), round(alpha_planck_list[x], 2), round(beta_list[x], 2), round(opacity_list_3mm[x], 2), round(opacity_list_0_87mm[x], 2)])

# create file on notepad called 'Table 2'
with open('Table 3.txt', 'w') as f:
    f.write(tabulate(table, headers=['Sources', 'Temperature(K)', r'\alpha_{Planck}', r'\beta', r'\kappa_{3mm}', r'\kappa_{0.87mm}']))

#print(tabulate(table, headers=['Sources', 'Temperature(K)', r'\alpha_{Planck}', r'\beta', r'\kappa_{3mm}', r'\kappa_{0.87mm}']))