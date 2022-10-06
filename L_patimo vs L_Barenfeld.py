#this file creates an image comparing the stellar luminosity calculated by Barenfeld and me. If they are located on the line their ages can be approximated to be about 10Myr
# NOTE: THIS ONLY TAKES IN CONSIDERATION THE 24 DISKS IN THE SAMPLE

from data_file import luminosity_list_barenfeld_updated, luminosity_list_barenfeld_error_updated
from Table_1 import luminosity_list_patimo, lower_new_luminosity_error_log, upper_new_luminosity_error_log

import matplotlib. pyplot as plt
fig, ax = plt.subplots()

# set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

# avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.17)

# create initial and final point for the line
x = [-2, 1]
y = [-2, 1]

# create straight line with equation y=x
plt.plot(x,y, c='orange')

# manipulate trasnparency errobars
kwargs_errobar = {'alpha':0.3}


# create plots
plt.scatter(luminosity_list_barenfeld_updated, luminosity_list_patimo)
plt.errorbar(luminosity_list_barenfeld_updated, luminosity_list_patimo, xerr=luminosity_list_barenfeld_error_updated, ls='none', **kwargs_errobar)
#plt.errorbar(luminosity_list_barenfeld_updated, luminosity_list_patimo, yerr=(lower_new_luminosity_error_log, upper_new_luminosity_error_log), ls='none', c='gray', **kwargs_errobar)
plt.xlabel('$L_{Barenfeld} log(L_{\star}/L_{\odot})$', fontsize=20), plt.ylabel('$L_{new} log(L_{\star}/L_{\odot})$', fontsize=20)
plt.grid()
ax.tick_params(which='both', labelsize=15)
# plt.savefig('L_patimo vs L_Barenfeld')
plt.show()