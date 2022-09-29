from tabulate import tabulate
from data_file import flux_list_2_87mm_error_garrett, flux_barenfeld_0_88mm_updated, \
    flux_barenfeld_0_88_error_updated, flux_list_2_87mm_garrett, radius_dust_updated,\
    lower_bound_radius_updated, upper_bound_radius_updated, surface_density_list, surface_density_list_lower_bound,\
    surface_density_list_upper_bound, source_list_garrett

from Histogram_spectral_index import spectral_index_upper_sco

table = []


for x in range(len(source_list_garrett)):
    table.append([source_list_garrett[x], str(flux_barenfeld_0_88mm_updated[x]) + '\pm' + str(flux_barenfeld_0_88_error_updated[x]),
                  str(flux_list_2_87mm_garrett[x]) + '\pm' + str(flux_list_2_87mm_error_garrett[x]),
                  str(spectral_index_upper_sco[x]),
                  str(radius_dust_updated[x]) + '(' + str(lower_bound_radius_updated[x]) + ',' +
                  str(upper_bound_radius_updated[x]) + ')', str(surface_density_list[x]) + '(' +
                  str(surface_density_list_lower_bound[x]) + ',' + str(surface_density_list_upper_bound[x]) + ')'])



#create file on notepad called 'Table 2'
with open('Table 2.txt', 'w') as f:
    f.write(tabulate(table, headers=['Sources', 'F_{0.88mm}(mJy)', 'F_{2.87mm}(mJy)', r'\alpha',
                                     'Radius disk (AU)', r'log \frac{\sum_{0}}{gcm^{-2}}])']))

f.close()

#print(tabulate(table, headers=['Sources', 'F_{0.88mm}(mJy)', 'F_{2.87mm}(mJy)', r'\alpha', 'Radius disk (AU)',
#                               r'log \frac{\sum_{0}}{gcm^{-2}}']))