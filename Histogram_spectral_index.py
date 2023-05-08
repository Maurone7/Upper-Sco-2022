import numpy as np
import matplotlib.pyplot as plt

from astropy import constants

c = constants.c.cgs.value

from data_file import flux_barenfeld_0_88mm_updated, flux_list_2_87mm_garrett, type_barenfeld_updated,\
    flux_barenfeld_0_88_error_updated, flux_list_2_87mm_error_garrett

spectral_index_upper_sco = []
spectral_index_upper_sco_error = []

def spectra_index(flux_1, flux_2, freq1, freq2):
    '''Calculate spectral index with 4 inputs (1 output)
    -2 fluxes
    -2 frequencies'''
    return (np.log10(flux_1/flux_2))/(np.log10(freq1/freq2))

for index, element in enumerate(flux_list_2_87mm_garrett):
    spectral_index_upper_sco.append(spectra_index(flux_list_2_87mm_garrett[index], flux_barenfeld_0_88mm_updated[index], c / 2.87, c / 0.88))
    spectral_index_upper_sco_error.append(spectra_index(flux_list_2_87mm_garrett[index] + flux_list_2_87mm_error_garrett[index], flux_barenfeld_0_88mm_updated[index] + flux_barenfeld_0_88_error_updated[index], c / 2.87, c / 0.88))

spectral_index_upper_sco_error = [spectral_index_upper_sco_error[x] - spectral_index_upper_sco[x] for x in range(len(spectral_index_upper_sco))]
spectral_index_upper_sco_error = [abs(x) for x in spectral_index_upper_sco_error]
spectral_index_upper_sco = [round(x, 2) for x in spectral_index_upper_sco]
spectral_index_upper_sco_error = [round(x, 2) for x in spectral_index_upper_sco_error]


bins = np.array(np.arange(1.5, 3.2, 0.05))

type_transitional_spectra_index = []
type_evolved_spectra_index = []
for index, element in enumerate(type_barenfeld_updated):
    if element =='Transitional':
        type_transitional_spectra_index.append(spectral_index_upper_sco[index])

    if element == 'Evolved':
        type_evolved_spectra_index.append(spectral_index_upper_sco[index])

if __name__ == '__main__':
    fig, ax = plt.subplots()

    # Only show integers on y-axis
    plt.yticks([0, 1, 2, 3])

    # set thickness axis
    plt.setp(ax.spines.values(), linewidth=2)

    # avoid axis labels being cut
    plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

    plt.hist(spectral_index_upper_sco, bins=bins, edgecolor='black', linewidth=2, label='Full')
    plt.hist(type_transitional_spectra_index, bins=bins, edgecolor='orange', linewidth=2, label='Transitional')
    plt.hist(type_evolved_spectra_index, bins=bins, edgecolor='green', linewidth=2, label='Evolved')

    plt.ylabel('Frequency', fontsize=20), plt.xlabel(r'Spectral index $\alpha_{abs}$', fontsize=20)

    #plt.title('Frequency vs Spectral Index', fontsize=20)
    ax.tick_params(which='both', labelsize=15)
    plt.legend()

    plt.savefig('Spectral index frequency')
    plt.show()
