# The role of this code is to create H-R diagrams with data from other files (mainly Feiden_automatic)

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

# import updated values (luminosities and temperatures) for all the 106 stars in the sample
from Parallaxes import luminosity_106, temperature_list_barenfeld, lower_new_luminosity_error_log, upper_new_luminosity_error_log, temperature_list_barenfeld_error_values
# import values from Feiden's models
from Feiden_automatic import temperature_column_10Myr, luminosity_column_10Myr, temperature_column_20Myr,\
    luminosity_column_20Myr, temperature_column_5Myr, luminosity_column_5Myr
from data_file import flux_barenfeld_0_88mm_updated, luminosity_list_barenfeld_updated, temperature_list_barenfeld_updated

fig, ax = plt.subplots()

#set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

#avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.17)

#manipulate trasnparency errobars
kwargs_errobar = {'alpha': 0.3}

temperature_list_barenfeld_updated = [10**x for x in temperature_list_barenfeld_updated]
#scatter all points from Feiden
plt.scatter(temperature_list_barenfeld, luminosity_106)
plt.errorbar(temperature_list_barenfeld, luminosity_106, yerr=(upper_new_luminosity_error_log, lower_new_luminosity_error_log), ls='none', c='gray', **kwargs_errobar)
plt.errorbar(temperature_list_barenfeld, luminosity_106, xerr=temperature_list_barenfeld_error_values, ls='none', c='gray', **kwargs_errobar)
plt.scatter(temperature_list_barenfeld_updated, luminosity_list_barenfeld_updated, c='y')

for index, element in enumerate(flux_barenfeld_0_88mm_updated):
    if element < 10:
        plt.scatter(temperature_list_barenfeld_updated[index], luminosity_list_barenfeld_updated[index], c='r')

#interpolate 5Myr
#plt.scatter(temperature_column_5Myr, luminosity_column_5Myr)
f5 = interp1d(temperature_column_5Myr, luminosity_column_5Myr)

#plot line 5Myr
x = np.linspace(min(temperature_column_5Myr), max(temperature_column_5Myr))
plt.plot(x, f5(x), c='black', label='5Myr')


#interpolate 10Myr
#plt.scatter(temperature_column_10Myr, luminosity_column_10Myr)
f10 = interp1d(temperature_column_10Myr, luminosity_column_10Myr)

#plot line 10Myr
x = np.linspace(np.min(temperature_column_10Myr), np.max(temperature_column_10Myr))
plt.plot(x, f10(x), c='red', label='10Myr')


#interpolate 20Myr
#plt.scatter(temperature_column_20Myr, luminosity_column_20Myr)
f20 = interp1d(temperature_column_20Myr, luminosity_column_20Myr)

#plot line 20Myr
x = np.linspace(np.min(temperature_column_20Myr), np.max(temperature_column_20Myr))
plt.plot(x, f20(x), c='blue', label='20Myr')


plt.ylabel('Lum'), plt.xlabel('T')

# invert temperature axis to create H-R diagram
plt.gca().invert_xaxis()
plt.xlabel("$T[K]$", fontsize=20), plt.ylabel('log $L/L_{\odot}$', fontsize=20)
ax.tick_params(which='both', labelsize=15)
plt.legend()
#plt.savefig('H-R diagram')
plt.show()
