import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

#set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

#avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

from data_file import flux_barenfeld_0_88mm_updated, flux_list_2_87mm_garrett, tazzari_lupus_spectral_indices

spectral_index_upper_sco = []

def spectra_index(flux_1, flux_2, freq1, freq2):
    '''Calculate spectral index with 4 inputs (1 output)
    -2 fluxes
    -2 frequencies'''
    return ((np.log10(flux_1/flux_2))/(np.log10(freq1/freq2)))

for index, element in enumerate(flux_list_2_87mm_garrett):
    spectral_index_upper_sco.append(spectra_index(flux_list_2_87mm_garrett[index], flux_barenfeld_0_88mm_updated[index], 10 ** 11 / 2.87, 10 ** 11 / 0.87))

plt.hist(spectral_index_upper_sco, bins=30, edgecolor='black', linewidth=2)
plt.ylabel('Frequency', fontsize=20), plt.xlabel(r'Spectral index $\alpha_{abs}$', fontsize=20)
#plt.title('Frequency vs Spectral Index', fontsize=20)
ax.tick_params(which='both', labelsize=15)
plt.savefig('Spectral index frequency')
#plt.show()
