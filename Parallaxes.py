from data_file import luminosity_list_barenfeld, luminosity_list_barenfeld_error, temperature_list_barenfeld,\
    temperature_list_barenfeld_error, temperature_feiden, mass_feiden, source_list_garrett, source_list_barenfeld_2016

from scipy.interpolate import interp1d
import numpy as np
import matplotlib.pyplot as plt

#import values for all sources into a table
value_single_source = []
trial = []
f = open('GAIA3 archive.json', 'r')
lines = f.readlines()[20:-2]
initial_value = 0
for z in range(len(lines)):
    trial = lines[z][1:]
    x = 0
    for x in range(len(trial)):
        #cut the elements when a ',' is met
        if trial[x] == ',':
            value_single_source.append(trial[initial_value:x])
            initial_value = x+1
f.close()
value_single_source_updated = []

#eliminate bracket from values
for x in value_single_source:
    for z in range(len(x)):
        if x[z] == ']':
            x = x[:z]
    value_single_source_updated.append(x)

# import RUWE values
ruwe_list = []
with open('GAIA 3 Archive RUWE.json') as f:
    lines = f.readlines()[17:-2]
    for x in lines:
        ruwe_list.append(x.split(',')[2])

ruwe_list = [0 if x=='null' else x for x in ruwe_list]
#eliminate empty values in list
#value_single_source_updated = [i for i in value_single_source_updated if i]

#extract parallax values from table
sources_106 = []
parallax_106 = []
parallax_error_106 = []
for i in range(106):
    parallax_106.append(value_single_source_updated[15 * i + 4])
    parallax_error_106.append(value_single_source_updated[15 * i + 5])
    sources_106.append(value_single_source_updated[15 * i + 6][1:-1])

#change 'null' to 1000/145 so that the final distance is 145pc
parallax_106 = ['6.896551724' if item == 'null' else item for item in parallax_106]
parallax_error_106 = ['0.83594566' if item == 'null' else item for item in parallax_error_106]
for index_ruwe, element_ruwe in enumerate(ruwe_list):
    if float(element_ruwe) > 1.6:
        parallax_106[index_ruwe] = '6.896551724'
        parallax_error_106[index_ruwe] = '0.83594566'

#change elements to floats
parallax_106 = [float(x) for x in parallax_106]
parallax_error_106 = [float(x) for x in parallax_error_106]

#turn parallaxes into distances [pc]
distances_106 = []
distances_upper_error_106 = []
distances_lower_error_106 = []
for x in range(len(parallax_106)):
    distances_106.append(1/parallax_106[x] * 1000)
    distances_upper_error_106.append((1 / (parallax_106[x] - parallax_error_106[x])) * 1000 - distances_106[x])
    distances_lower_error_106.append((1 / (parallax_106[x] + parallax_error_106[x])) * 1000 - distances_106[x])

distances_lower_error_106 = [-20.0 if round(x, 2) == -15.68 else x for x in distances_lower_error_106]

#update luminosity and the error
luminosity_106 = []
luminosity_error_106 = []
for x in range(len(distances_106)):
    luminosity_106.append(np.log10((10 ** luminosity_list_barenfeld[x]) * (distances_106[x]**2) / (145**2)))

#interpolate function from points in feiden
f = interp1d(temperature_feiden, mass_feiden)

#calculate masses
masses_106 = []
temperature_list_barenfeld_error_values = []
for index, element in enumerate(temperature_list_barenfeld):
    temperature_list_barenfeld_error_values.append(10**(element + temperature_list_barenfeld_error[index])-10**(element))

temperature_list_barenfeld = [10**x for x in temperature_list_barenfeld]
for x in temperature_list_barenfeld:
    masses_106.append(float(f(x)))

distances_updated_upper_sco = []
for index_source_garrett, element_source_garrett in enumerate(source_list_garrett):
    for index_source_barenfeld, element_source_barenfeld in enumerate(source_list_barenfeld_2016):
        if element_source_garrett == element_source_barenfeld:
            distances_updated_upper_sco.append(distances_106[index_source_barenfeld])


luminosity_upper_error_106 = []
luminosity_lower_error_106 = []
luminosity_106 = [10**x for x in luminosity_106]

# update luminoisity with new distances
def update_luminosity(old_luminosity, new_distance):
    return old_luminosity * (new_distance**2) / (145**2)


# update old error
def update_old_luminosity_error(old_luminosity_error, old_luminosity):
    return np.sqrt((old_luminosity_error**2) - (((2*old_luminosity/145) * 20) ** 2))


# create function for creating error in luminosity
def update_new_luminosity_error(distance_new, new_distance_error, old_luminosity, old_luminosity_error):
    return np.sqrt(((distance_new/145)**2 * old_luminosity_error)**2 + (old_luminosity/(145**2) * (2*distance_new) * new_distance_error)**2)


luminosity_list_barenfeld_error_NOT_log = []
updated_luminosity_list_NOT_log = []
luminosity_updated_old_error_NOT_log = []


# calculate the luminosity NOT in log scale
luminosity_list_barenfeld_NOT_log = [10**x for x in luminosity_list_barenfeld]


for index, element in enumerate(luminosity_list_barenfeld_NOT_log):

    # calculate new Barenfeld luminosity with new distances
    updated_luminosity_list_NOT_log.append(update_luminosity(element, distances_106[index]))

    # calculate Barenfeld luminosity error NOT in log scale
    luminosity_list_barenfeld_error_NOT_log.append(10**(np.log10(element) + luminosity_list_barenfeld_error[index]) - element)
    luminosity_updated_old_error_NOT_log.append(update_old_luminosity_error(luminosity_list_barenfeld_error_NOT_log[index], element))



lower_new_luminosity_error_log = []
upper_new_luminosity_error_log = []
lower_new_luminosity_error_NOT_log = []
upper_new_luminosity_error_NOT_log = []
for index, element in enumerate(luminosity_list_barenfeld_NOT_log):
    lower_new_luminosity_error_NOT_log.append(update_new_luminosity_error(distances_106[index], distances_lower_error_106[index], element, luminosity_updated_old_error_NOT_log[index]))
    upper_new_luminosity_error_NOT_log.append(update_new_luminosity_error(distances_106[index], distances_upper_error_106[index], element, luminosity_updated_old_error_NOT_log[index]))
    lower_new_luminosity_error_log.append(np.log10(lower_new_luminosity_error_NOT_log[index] + luminosity_list_barenfeld_NOT_log[index]) - np.log10(luminosity_list_barenfeld_NOT_log[index]))
    upper_new_luminosity_error_log.append(np.log10(upper_new_luminosity_error_NOT_log[index] + luminosity_list_barenfeld_NOT_log[index]) - np.log10(luminosity_list_barenfeld_NOT_log[index]))


luminosity_106 = [np.log10(x) for x in luminosity_106]

if __name__ == '__main__':
    fig, ax = plt.subplots()

    #set thickness axis
    plt.setp(ax.spines.values(), linewidth=2)

    #avoid axis labels being cut
    plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

    #manipulate trasnparency errobars
    kwargs_errobar = {'alpha': 0.3}

    #create initial and final point for the line
    x = [-2, 1]
    y = [-2, 1]

    plt.scatter(luminosity_list_barenfeld, luminosity_106)
    plt.errorbar(luminosity_list_barenfeld, luminosity_106, xerr=luminosity_list_barenfeld_error, ls='none', c='gray', **kwargs_errobar)
    plt.errorbar(luminosity_list_barenfeld, luminosity_106, yerr=(lower_new_luminosity_error_log, upper_new_luminosity_error_log), ls='none', c='gray', **kwargs_errobar)
    plt.xlabel('$L_{Barenfeld} log(L_{\star}/L_{\odot})$', fontsize=20), plt.ylabel('$L_{new} log(L_{\star}/L_{\odot})$', fontsize=20)
    plt.grid()

    #create straight line with equation y=x
    plt.plot(x,y, c='orange')
    ax.tick_params(which='both', labelsize=15)
    plt.savefig('106 Luminosity updated')
    #plt.show()

    fig, ax = plt.subplots()

    #set thickness axis
    plt.setp(ax.spines.values(), linewidth=2)

    #avoid axis labels being cut
    plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

    #create line limits
    x = np.linspace(np.min(temperature_feiden), np.max(temperature_feiden))

    plt.plot(x,f(x))
    plt.scatter(temperature_list_barenfeld, masses_106)
    plt.xlabel(r'$T_{eff}\rm[K]$', fontsize=20), plt.ylabel(r'$M_{\star}(M_{\odot})$', fontsize=20)
    plt.grid()
    ax.tick_params(which='both', labelsize=15)
    plt.savefig('Mass 106 Feiden')
    #plt.show()
