from data_file import temperature_list_barenfeld_error, temperature_list_barenfeld,\
    source_list_barenfeld_2016, spectral_type_barenfeld, source_list_garrett
from Interpolation import masses_new, masses_new_upper_error, masses_new_lower_error
from Parallaxes import luminosity_106, distances_106, distances_upper_error_106, distances_lower_error_106, \
    lower_new_luminosity_error_log, upper_new_luminosity_error_log

from tabulate import tabulate


def update_luminosity(old_luminosity_list, new_distance):
    return (10**old_luminosity_list) * (new_distance**2) / (145**2)


table = []
luminosity_list_patimo = []


for x in range(len(source_list_barenfeld_2016)):
    table.append([source_list_barenfeld_2016[x], spectral_type_barenfeld[x], str(temperature_list_barenfeld[x]) + '\pm' +
                  str(temperature_list_barenfeld_error[x]), str(round(distances_106[x], 2)) + '(' +
                  str(round(distances_lower_error_106[x], 2)) + ',+' + str(round(distances_upper_error_106[x], 2)) + ')',
                  str(round(luminosity_106[x], 3)) + '(' + str(round(upper_new_luminosity_error_log[x], 3)) + ',-' +
                  str(round(lower_new_luminosity_error_log[x], 3)) + ')', str(round(masses_new[x], 2)) + '(' +
                  str(round(masses_new_upper_error[x], 2)) + ',-'
                  + str(round(masses_new_lower_error[x], 2)) + ')'])

# add updated luminosities and add them to the patimo luminosity list
for index_source_garrett, element_source_garrett in enumerate(source_list_garrett):
    for index_source_barenfeld, element_source_barenfeld in enumerate(source_list_barenfeld_2016):
        if element_source_garrett == element_source_barenfeld:
            luminosity_list_patimo.append(luminosity_106[index_source_barenfeld])
            # luminosity_list_patimo_upper_error.append(upper_error_new_luminosities_106[index_source_barenfeld])
            # luminosity_list_patimo_lower_error.append(lower_error_new_luminosities_106[index_source_barenfeld])

with open('Table 1.txt', 'w') as f:
    f.write(tabulate(table, headers=['Sources', 'SpT', r'$log(T_{\rm{eff}}/\rm{K})$', 'Distance',
                                     'log frac{l_{\star}}{L_{\odot}}', 'Stellar mass (M_{\star})']))

print(tabulate(table, headers=['Sources', 'SpT', 'log(T_{star}/K)', 'Distance', 'log frac{l_{\star}}{L_{\odot}}', 'Stellar mass (M_{\star})']))
table = []
for x in source_list_barenfeld_2016:
    table.append([x])

with open('Sources table.txt', 'w') as f:
    f.write(tabulate(table))
