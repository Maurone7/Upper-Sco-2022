from data_file import luminosity_list_barenfeld, luminosity_list_barenfeld_error, source_list_barenfeld_2016
from Parallaxes import distances_106, distances_upper_error_106

from statistics import mean
import matplotlib.pyplot as plt
import numpy as np


def update_luminosity(old_luminosity_list, new_distance):
    return (10**old_luminosity_list) * (new_distance**2) / (145**2)


range_list = []
max_value_list = []

#create function capable to loop over certain values pluggin them in another function
def simulation_patimo_max(function, old_value, old_value_error, updated_parameter, updated_parameter_error):
    for index_old_values, element_old_values in enumerate(old_value):
        max_value_list.append(function(element_old_values + old_value_error[index_old_values], updated_parameter[index_old_values] + updated_parameter_error[index_old_values])
                              - function(element_old_values, updated_parameter[index_old_values]))


# manually calculate all values for luminosity of first barenfeld's source
x_values = []
y_values = []
distance_range_list = np.arange(distances_106[0] - distances_upper_error_106[0], distances_106[0] + distances_upper_error_106[0], distances_upper_error_106[0] / 100)
luminosity_range_list = np.arange(luminosity_list_barenfeld[0] - luminosity_list_barenfeld_error[0], luminosity_list_barenfeld[0] + luminosity_list_barenfeld_error[0], luminosity_list_barenfeld_error[0]/ 100)

source_list_barenfeld_2016_1 = []
average_new_luminosity_106 = []
upper_error_new_luminosities_106 = []
lower_error_new_luminosities_106 = []
for index_distance_106, element_distance_106 in enumerate(distances_106):
    distance_range_list = []
    luminosity_range_list = []
    x_values = []
    y_values = []
    distance_range_list = np.arange(element_distance_106 - distances_upper_error_106[index_distance_106], element_distance_106
                                    + distances_upper_error_106[index_distance_106], distances_upper_error_106[index_distance_106] / 100)
    luminosity_range_list = np.arange(luminosity_list_barenfeld[index_distance_106] - luminosity_list_barenfeld_error[index_distance_106],
                                      luminosity_list_barenfeld[index_distance_106] + luminosity_list_barenfeld_error[index_distance_106],
                                      luminosity_list_barenfeld_error[index_distance_106] / 100)
    for x in range(99):
        for z in range(99):
            y_values.append(update_luminosity(luminosity_range_list[z], distance_range_list[x]))
        x_values.append(distance_range_list[x])

    average_new_luminosity_106.append(np.log10(mean(y_values)))

    upper_error_new_luminosities_106.append(np.log10(max(y_values)) - np.log10(mean(y_values)))
    lower_error_new_luminosities_106.append(np.log10(min(y_values)) - np.log10(mean(y_values)))
    source_list_barenfeld_2016_1.append(source_list_barenfeld_2016[index_distance_106])

print(average_new_luminosity_106)
print(upper_error_new_luminosities_106)
print(lower_error_new_luminosities_106)
plt.xlim(np.log10(min(y_values)), np.log10(max(y_values)))
plt.hist(np.log10(y_values), 200)
plt.show()