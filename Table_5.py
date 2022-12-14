from Cumulative_spectral_indices import spectral_indices_taurus, spectral_indices_matching_lupus, \
    flux_matching_tazzari_ANDSELL_lupus, sources_matching_tazzari_andsell_lupus,\
    flux_matching_TAZZARI_andsell_lupus, spectral_index_ophiucus, tazzari_lupus_flux

from data_file import source_list_ophiucus_ricci_1mm, flux_list_ophiucus_ricci_1mm, ricci_taurus_sources_1mm,\
    ricci_taurus_fluxes_1mm, tazzari_lupus_spectral_indices

from tabulate import tabulate
import numpy as np


def find_flux_3_mm(spectral_index, flux_1_mm):
    return flux_1_mm/(3**spectral_index)

def find_flux_1_mm(spectral_index, flux_3_mm):
    return 3**spectral_index * flux_3_mm

flux_ophiucus_3_mm = []
for index_flux_1_mm, element_flux_1_mm in enumerate(flux_list_ophiucus_ricci_1mm):
    flux_ophiucus_3_mm.append(find_flux_3_mm(spectral_index_ophiucus[index_flux_1_mm], element_flux_1_mm))

ricci_taurus_fluxes_3mm = []
for index_flux_1_mm, element_flux_1_mm in enumerate(spectral_indices_taurus):
    ricci_taurus_fluxes_3mm.append(find_flux_3_mm(element_flux_1_mm, ricci_taurus_fluxes_1mm[index_flux_1_mm]))


wavelength_upper_sco = 0.87
table_5 = []
for index_spectral_index_lupus, element_spectral_index_lupus in enumerate(spectral_indices_matching_lupus):
    table_5.append(['Lupus', sources_matching_tazzari_andsell_lupus[index_spectral_index_lupus], 1,
                    round(flux_lupus_1_mm[index_spectral_index_lupus], 2), 3,
                    round(flux_matching_TAZZARI_andsell_lupus[index_spectral_index_lupus], 2), round(element_spectral_index_lupus, 2)])

for index_spectraL_index_taurus, element_spectral_index_taurus in enumerate(spectral_indices_taurus):
    table_5.append(['Taurus-Auriga', ricci_taurus_sources_1mm[index_spectraL_index_taurus], 1,
                    ricci_taurus_sources_1mm[index_spectraL_index_taurus],
                    ricci_taurus_fluxes_1mm[index_spectraL_index_taurus],
                   round(ricci_taurus_fluxes_3mm[index_spectraL_index_taurus], 2),
                    round(element_spectral_index_taurus, 2)])

for index_spectraL_index_ophiucus, element_spectral_index_ophiucus in enumerate(spectral_index_ophiucus):
    table_5.append(['Ophiucus', source_list_ophiucus_ricci_1mm[index_spectraL_index_ophiucus], 1,
                    flux_list_ophiucus_ricci_1mm[index_spectraL_index_ophiucus], 3,
                    round(flux_ophiucus_3_mm[index_spectraL_index_ophiucus], 2), round(element_spectral_index_ophiucus, 2)])


# create file on notepad called 'Table 4'
with open('Table 5.txt', 'w') as f:
    f.write(tabulate(table_5,headers=['Region', 'Source', 'Wavelength', r'$Flux_{1mm}$', 'Wavelength', r'$Flux_{3mm}$', r'$\alpha$']))

print(tabulate(table_5, headers=['Region', 'Wavelength', 'Source', 'Flux', 'Wavelength', 'Flux', r'\alpha']))