from data_file import source_list_garrett, source_list_barenfeld_2016, temperature_list_barenfeld,\
    ricci_temperature_taurus_1mm, ricci_luminosity_taurus_1mm_NOT_LOG, spectral_indices_taurus
from Parallaxes import luminosity_106, lower_new_luminosity_error_log, upper_new_luminosity_error_log
from Cumulative_spectral_indices import spectral_index_upper_sco
from HR_Diagram import f20, f10, f5

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

x_5Myr = np.linspace(3000, 5280)
x = np.linspace(3000, 5000)

matching_temperatures_barenfeld_garrett = [10 ** x for x in matching_temperatures_barenfeld_garrett]

z = np.polyfit(matching_temperatures_barenfeld_garrett, spectral_index_upper_sco, 3)
p = np.poly1d(z)
plt.plot(x, p(x))
plt.fill_between(x, p(x), p(x)+0.3, **kwargs_errobar)
plt.fill_between(x, p(x), p(x)-0.3, **kwargs_errobar)

#scatter T vs alpha
plt.scatter(matching_temperatures_barenfeld_garrett, spectral_index_upper_sco, c=matching_luminsoities_barenfeld_garrett, cmap='gray', zorder=2, label='Upper-Sco')
#plt.errorbar(matching_temperatures_barenfeld_garrett, matching_luminsoities_barenfeld_garrett, yerr=matching_upper_luminoisty_error_barenfeld_garrett_LOG, ls='none')
#plt.plot(x, f10(x), c='red', label='10Myr', zorder=1)
#plt.plot(x, f20(x), label='20Myr', zorder=1)
#plt.plot(x_5Myr, f5(x_5Myr), c='black', label='5Myr', zorder=1)
plt.gca().invert_xaxis()
plt.legend()
plt.xlabel("$T[K]$", fontsize=20), plt.ylabel('log $L/L_{\odot}$', fontsize=20)
plt.show()

z = np.polyfit(ricci_temperature_taurus_1mm, spectral_indices_taurus, 3)
p_1 = np.poly1d(z)
plt.gca().invert_xaxis()
plt.plot(x, p_1(x))
plt.fill_between(x, p_1(x), p_1(x)+0.3, **kwargs_errobar)
plt.fill_between(x, p_1(x), p_1(x)-0.3, **kwargs_errobar)
plt.scatter(ricci_temperature_taurus_1mm, spectral_indices_taurus, c=ricci_luminosity_taurus_1mm_LOG)
plt.show()

plt.plot(x, p(x))
plt.plot(x, p_1(x))
plt.show()