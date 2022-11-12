import scipy.stats

from data_file import source_list_garrett, source_list_barenfeld_2016, temperature_list_barenfeld,\
    ricci_temperature_taurus_1mm, ricci_luminosity_taurus_1mm_NOT_LOG, spectral_indices_taurus,\
    luminosity_list_barenfeld_updated
from Parallaxes import luminosity_106, lower_new_luminosity_error_log, upper_new_luminosity_error_log
from Cumulative_spectral_indices import spectral_index_upper_sco

import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

#set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

#avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

# find matching sorces between Barenfeld and Garrett
matching_sources_barenfeld_garrett = []
matching_luminsoities_barenfeld_garrett = []
matching_spectral_indices_barenfeld_garrett = []
matching_temperatures_barenfeld_garrett = []
matching_lower_luminoisty_error_barenfeld_garrett_LOG = []
matching_upper_luminoisty_error_barenfeld_garrett_LOG = []


for index_barenfeld, element_barenfeld in enumerate(source_list_barenfeld_2016):
    for index_garrett, element_garrett in enumerate(source_list_garrett):
        if element_garrett == element_barenfeld:
            matching_sources_barenfeld_garrett.append(element_garrett)
            matching_luminsoities_barenfeld_garrett.append(luminosity_106[index_barenfeld])
            matching_spectral_indices_barenfeld_garrett.append(spectral_index_upper_sco[index_garrett])
            matching_temperatures_barenfeld_garrett.append(temperature_list_barenfeld[index_barenfeld])
            matching_lower_luminoisty_error_barenfeld_garrett_LOG.append(lower_new_luminosity_error_log[index_barenfeld])
            matching_upper_luminoisty_error_barenfeld_garrett_LOG.append(upper_new_luminosity_error_log[index_barenfeld])

ricci_luminosity_taurus_1mm_LOG = [np.log10(x) for x in ricci_luminosity_taurus_1mm_NOT_LOG]

# manipulate trasnparency errobars
kwargs_errobar = {'alpha':0.3}

x = np.linspace(-1.5, 1)

matching_temperatures_barenfeld_garrett = [10 ** x for x in matching_temperatures_barenfeld_garrett]

#scatter L vs alpha
plt.scatter(luminosity_list_barenfeld_updated, spectral_index_upper_sco, c=matching_temperatures_barenfeld_garrett, cmap='gray', zorder=2, label='Upper-Sco')
plt.gca().invert_xaxis()
plt.legend()
plt.xlabel(r"$L [L_{\odot}]$")
#plt.xlabel(r"$T[\rm K]$", fontsize=20)
plt.ylabel(r'$\alpha$', fontsize=20)
plt.show()

import seaborn as sns
sns.regplot(x = )

plt.gca().invert_xaxis()
plt.scatter(ricci_luminosity_taurus_1mm_LOG, spectral_indices_taurus, c=ricci_temperature_taurus_1mm)
plt.xlabel(r"$L [L_{\odot}]$", fontsize=20), plt.ylabel(r'$\alpha$', fontsize=20)
plt.show()
