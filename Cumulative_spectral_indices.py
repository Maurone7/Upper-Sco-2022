from data_file import tazzari_lupus_flux, tazzari_lupus_flux_error, tazzari_lupus_sources, source_ansdell_lupus, \
    flux_ansdell_1_33mm_error_lupus, flux_barenfeld_0_88mm_updated,\
    flux_list_ophiucus_ricci_1mm, source_list_ophiucus_ricci_1mm, ricci_ophiuchi_flux_3_3mm, \
    source_names_ophiucus_ricci_3_3mm, spectral_index_ophiucus, spectral_indices_taurus, tazzari_lupus_spectral_indices,\
    ricci_taurus_fluxes_1mm, flux_ansdell_1_33mm_lupus, radius_dust_updated, luminosity_list_barenfeld_updated
from Histogram_spectral_index import spectral_index_upper_sco
from Table_3 import temperature_list

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest

fig, ax = plt.subplots()

# set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

# avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

def find_flux_1_mm(spectral_index, flux_3_mm):
    return 3**spectral_index * flux_3_mm

flux_lupus_1_mm = []
for index_flux_3_mm, element_flux_3_mm in enumerate(tazzari_lupus_spectral_indices):
    flux_lupus_1_mm.append(find_flux_1_mm(element_flux_3_mm, tazzari_lupus_flux[index_flux_3_mm]))

# capitals are used to indicate which list the elements are from
sources_matching_tazzari_andsell_lupus = []
# ex. when a matching source is found, the flux from Tazzari is added to flux_matching_TAZZARI_andsell
# and the flux from Andsell is added to flux_matching_tazzari_ANDSELL
flux_matching_TAZZARI_andsell_lupus = []
flux_matching_TAZZARI_andsell_error_lupus = []
flux_matching_tazzari_ANDSELL_lupus = []
flux_matching_tazzari_ANDSELL_error_lupus = []
spectral_indices_matching_lupus = []
for index_andsell, element_andsell in enumerate(source_ansdell_lupus):
    for index_tazzari, element_tazzari in enumerate(tazzari_lupus_sources):
        if element_tazzari == element_andsell:
            sources_matching_tazzari_andsell_lupus.append(element_tazzari)
            flux_matching_TAZZARI_andsell_lupus.append(tazzari_lupus_flux[index_tazzari])
            flux_matching_TAZZARI_andsell_error_lupus.append(tazzari_lupus_flux_error[index_tazzari])
            flux_matching_tazzari_ANDSELL_lupus.append(flux_ansdell_1_33mm_lupus[index_andsell])
            flux_matching_tazzari_ANDSELL_error_lupus.append(flux_ansdell_1_33mm_error_lupus[index_andsell])
            spectral_indices_matching_lupus.append(tazzari_lupus_spectral_indices[index_tazzari])


matching_sources_ricci_ophiucus_3mm_1mm = []
matching_fluxes_ricci_ophiucus_3mm_1MM = []
matching_fluxes_ricci_ophiucus_3MM_1mm = []
for index_ricci_1mm, element_ricci_1mm in enumerate(source_list_ophiucus_ricci_1mm):
    for index_ricci_3_3mm, element_ricci_3_3mm in enumerate(source_names_ophiucus_ricci_3_3mm):
        if element_ricci_3_3mm == element_ricci_1mm:
            matching_sources_ricci_ophiucus_3mm_1mm.append(element_ricci_3_3mm)
            matching_fluxes_ricci_ophiucus_3mm_1MM.append(flux_list_ophiucus_ricci_1mm[index_ricci_1mm])
            matching_fluxes_ricci_ophiucus_3MM_1mm.append(ricci_ophiuchi_flux_3_3mm[index_ricci_3_3mm])



count_list_sco = []
steps = (np.max(spectral_index_upper_sco) - np.min(spectral_index_upper_sco)) / 100
minimum = np.min(spectral_index_upper_sco) - 0.3
while minimum < np.max(spectral_index_upper_sco) + 0.3:
    count = 0
    for elements in spectral_index_upper_sco:
        if elements <= minimum:
            count += 1

    count_list_sco.append(count)
    minimum += steps

count_list_sco = [x / len(spectral_index_upper_sco) for x in count_list_sco]

count_list_taurus = []
steps = (np.max(spectral_indices_taurus) - np.min(spectral_indices_taurus))/100
minimum = np.min(spectral_indices_taurus) - 0.3
while minimum < np.max(spectral_indices_taurus) + 0.3:
    count = 0
    for elements in spectral_indices_taurus:
        if elements <= minimum:
            count += 1

    count_list_taurus.append(count)
    minimum += steps

count_list_taurus = [x / 11 for x in count_list_taurus]

count_list_lupus = []
steps = (np.max(tazzari_lupus_spectral_indices) - np.min(tazzari_lupus_spectral_indices))/100
minimum = np.min(tazzari_lupus_spectral_indices) - 0.3
while minimum < np.max(tazzari_lupus_spectral_indices) + 0.3:
    count = 0
    for elements in tazzari_lupus_spectral_indices:
        if elements <= minimum:
            count += 1

    count_list_lupus.append(count)
    minimum += steps

count_list_lupus = [x /len(tazzari_lupus_spectral_indices) for x in count_list_lupus]


count_list_ophiucus = []
steps = (np.max(spectral_index_ophiucus) - np.min(spectral_index_ophiucus)) / 100
minimum = np.min(spectral_index_ophiucus) - 0.3
while minimum < np.max(spectral_index_ophiucus) + 0.3:
    count = 0
    for elements in spectral_index_ophiucus:
        if elements <= minimum:
            count += 1

    count_list_ophiucus.append(count)
    minimum += steps

count_list_ophiucus = [x / len(spectral_index_ophiucus) for x in count_list_ophiucus]

plt.scatter(flux_list_ophiucus_ricci_1mm, spectral_index_ophiucus, label='Ophiucus',)
plt.scatter(flux_lupus_1_mm, tazzari_lupus_spectral_indices, label='Lupus', marker='^', color='black')
plt.scatter(ricci_taurus_fluxes_1mm, spectral_indices_taurus, label='Taurus', marker='s')
plt.scatter(flux_barenfeld_0_88mm_updated, spectral_index_upper_sco, label='Upper Sco', color='red')
plt.xticks(np.array(np.arange(1.4, 3.1, 0.1)))
plt.xlabel('$Flux_{1mm}$', fontsize=20), plt.ylabel(r'$\alpha$', fontsize=20)
plt.xscale('log')
plt.legend()
ax.tick_params(which='both', labelsize=15)
plt.savefig('Spectral index vs flux_1mm')
plt.show()

x_ophiucus = np.linspace(np.min(spectral_index_ophiucus) - 0.3, np.max(spectral_index_ophiucus) + 0.3, len(count_list_ophiucus))
x_lupus = np.linspace(np.min(tazzari_lupus_spectral_indices) - 0.3, np.max(tazzari_lupus_spectral_indices) + 0.3, len(count_list_lupus))
x_taurus = np.linspace(np.min(spectral_indices_taurus) - 0.3, np.max(spectral_indices_taurus) + 0.3, len(count_list_taurus))
x_sco = np.linspace(np.min(spectral_index_upper_sco) - 0.3, np.max(spectral_index_upper_sco) + 0.3, len(count_list_sco))

fig, ax = plt.subplots()

# set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

# avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

# create step diagram
plt.step(x_ophiucus, count_list_ophiucus, label='Ophiucus')
plt.step(x_taurus, count_list_taurus, label='Taurus-Auriga')
plt.step(x_lupus, count_list_lupus, label='Lupus')
plt.step(x_sco, count_list_sco, label='Upper Sco')


plt.ylim(0,1)
plt.legend()
plt.xlabel(r'$\alpha$', fontsize=20), plt.ylabel('Cumulative fraction', fontsize=20)
ax.tick_params(which='both', labelsize=15)
plt.savefig('Cumulative Spectra Indices')
plt.show()


print("Upper_sco, Ophiucus", kstest(spectral_index_upper_sco, spectral_index_ophiucus))
print("Upper_sco, Taurus", kstest(spectral_index_upper_sco, spectral_indices_taurus))
print("Upper_sco, Lupus", kstest(spectral_index_upper_sco, tazzari_lupus_spectral_indices))
print("Upper_sco, Together", kstest(spectral_index_upper_sco, spectral_index_ophiucus + spectral_indices_taurus +
                                 tazzari_lupus_spectral_indices))

x_axis = []
luminosity_list_barenfeld_updated = [10**x for x in luminosity_list_barenfeld_updated]
for index, element in enumerate(radius_dust_updated):
    x_axis.append((luminosity_list_barenfeld_updated[index]/(element**2)) ** (1/4))
