import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

#set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

#avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

from Feiden_automatic import temperature_column_10Myr, mass_column_10Myr
from data_file import temperature_list_barenfeld, temperature_list_barenfeld_error
from scipy.interpolate import interp1d

#calculate error of temperature in number and not log
temperature_list_error = []
for x in range(len(temperature_list_barenfeld)):
    temperature_list_error.append(10**(temperature_list_barenfeld[x] + temperature_list_barenfeld_error[x]) - (10 ** temperature_list_barenfeld[x]))

#change all temperature to numbers and not log
temperature_list_barenfeld = [10 ** x for x in temperature_list_barenfeld]
temperature_list_barenfeld_error = [10 ** x for x in temperature_list_barenfeld_error]
masses_new = []
masses_new_upper_error = []
masses_new_lower_error = []


#interpolate function from points in feiden data on github
f = interp1d(temperature_column_10Myr, mass_column_10Myr)

#calculate error in mass to put in graph
for x in range(len(temperature_list_error)):
    masses_new_upper_error.append(f(temperature_list_barenfeld[x] + temperature_list_error[x]) - f(temperature_list_barenfeld[x]))
    masses_new_lower_error.append(f(temperature_list_barenfeld[x]) - f(temperature_list_barenfeld[x] - temperature_list_error[x]))
    masses_new.append(float(f(temperature_list_barenfeld[x])))

#temperature error has to be calculated based on the initial temperature, as the temperature values are given in log
temperature_error = []
for x in range(len(temperature_list_barenfeld_error)):
    temperature_error.append(10 ** (np.log10(temperature_list_barenfeld[x]) + np.log10(temperature_list_barenfeld_error[x])) - 10 ** np.log10(temperature_list_barenfeld[x]))

#create line limits
x = np.linspace(np.min(temperature_column_10Myr), np.max(temperature_column_10Myr))

#manipulate trasnparency errobars
kwargs_errobar = {'alpha':0.3}

#create points and errorbars with datasets already created
plt.scatter(temperature_column_10Myr, mass_column_10Myr, **kwargs_errobar)

#scatter star on the interpolation line
plt.scatter(temperature_list_barenfeld, f(temperature_list_barenfeld), c='red')
plt.errorbar(temperature_list_barenfeld, f(temperature_list_barenfeld), xerr=temperature_error, ls='none', c='gray', **kwargs_errobar)
plt.errorbar(temperature_list_barenfeld, f(temperature_list_barenfeld), yerr=masses_new_upper_error, ls='none', c='gray', **kwargs_errobar)

#show interpolation line
plt.plot(x, f(x))
plt.grid()
plt.xlabel(r"$T_{eff} \rm\ [K]$", fontsize=20), plt.ylabel('$M_{\star} [M_{\odot}]$', fontsize=20)
ax.tick_params(which='both', labelsize=15)
plt.savefig('Interpolation'), plt.show()