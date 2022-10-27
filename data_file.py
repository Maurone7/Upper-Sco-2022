AU_to_cm = 1.496 * (10 ** 13)

#GARRETT' stuff

source_list_garrett = ['J15530132-2114135', 'J15582981-2310077', 'J15583692-2257153', 'J16001844-2230114', 'J16014086-2258103',
               'J16020757-2257467', 'J16024152-2138245', 'J16035767-2031055', 'J16042165-2130284', 'J16054540-2023088',
               'J16062196-1928445', 'J16072625-2432079', 'J16075796-2040087', 'J16082324-1930009', 'J16090075-1908526',
               'J16111330-2019029', 'J16113134-1838259', 'J16123916-1859284', 'J16135434-2320342', 'J16141107-2305362',
               'J16142029-1906481', 'J16153456-2242421', 'J16154416-1921171', 'J16181904-2028479']

# flux (mJy)
flux_list_2_87mm_garrett = [0.603, 0.58, 5.18, 0.36, 0.28, 0.49, 1.08, 0.41, 5.94, 1, 0.62, 1.08, 2.37, 3.1, 3.19, 0.69,
                            54.1, 0.4, 1.25, 0.71, 3.19, 1.26, 2.04, 0.52]
flux_list_2_87mm_error_garrett = [0.039, 0.029, 0.26, 0.031, 0.034, 0.061, 0.068, 0.034, 0.30, 0.044, 0.42, 0.069, 0.14,
                                  0.18, 0.17, 0.042, 2.71, 0.053, 0.078, 0.044, 0.17, 0.076, 0.11, 0.036]


source_list_barenfeld_2017 = []
radius_dust = []
lines = []
radius_dust_updated = []
lower_bound_radius = []
lower_bound_radius_updated = []
upper_bound_radius = []
upper_bound_radius_updated = []

# sources in paper of 2017 are different, ex. J15521088-2125372 is missing
with open('Table 1 Barenfeld.txt', 'r') as f:
    lines = f.readlines()[1:]
    for x in lines:
        source_list_barenfeld_2017.append(x.split()[1])
        radius_dust.append(int(x.split()[5]))
        lower_bound_radius.append(int((x.split()[6][1:-1])))
        upper_bound_radius.append(int((x.split()[7][1:-1])))
    # Radius is in AU


for x in range(len(source_list_barenfeld_2017)):
    for z in range(len(source_list_garrett)):
        if source_list_barenfeld_2017[x] == source_list_garrett[z]:
            radius_dust_updated.append(radius_dust[x])
            lower_bound_radius_updated.append(lower_bound_radius[x])
            upper_bound_radius_updated.append(upper_bound_radius[x])

radius_dust_updated.insert(2, 65)
lower_bound_radius_updated.insert(2, 0)
upper_bound_radius_updated.insert(2, 0)
radius_dust_updated.insert(8, 65)
lower_bound_radius_updated.insert(8, 0)
upper_bound_radius_updated.insert(8, 0)
radius_dust_updated.insert(16, 65)
lower_bound_radius_updated.insert(16, 0)
upper_bound_radius_updated.insert(16, 0)


luminosity_list_barenfeld = []
luminosity_list_barenfeld_error = []
luminosity_list_barenfeld_updated = []
luminosity_list_barenfeld_error_updated = []
source_list_barenfeld_2016 = []
temperature_list_barenfeld = []
temperature_list_barenfeld_error = []
temperature_list_barenfeld_updated = []
temperature_list_barenfeld_error_updated = []
spectral_type_barenfeld = []

# paper in 2016 has different sources ex. J15521088-2125372 is missing in 2017, but it is present in 2016
# import mass from Barenfeld Table 1 in log
interpolation_function = open('Barenfeld Table 1.txt', 'r')
lines = interpolation_function.readlines()[22:]
for x in lines:
    source_list_barenfeld_2016.append(x.split()[1])
    spectral_type_barenfeld.append(x.split()[2])
    luminosity_list_barenfeld.append(float(x.split()[8]))
    luminosity_list_barenfeld_error.append(float(x.split()[9]))
    temperature_list_barenfeld.append(float(x.split()[6]))
    temperature_list_barenfeld_error.append(float(x.split()[7]))
interpolation_function.close()

# adjust error, it can not be 0.00, so I added 0.01
for x in range(len(temperature_list_barenfeld_error)):
    if temperature_list_barenfeld_error[x] == 0.0:
        temperature_list_barenfeld_error[x] += 0.01

# match all the sources from Barenfeld with the sources from Garrett
for x in range(len(source_list_barenfeld_2016)):
    for z in range(len(source_list_garrett)):
        if source_list_barenfeld_2016[x] == source_list_garrett[z]:
            luminosity_list_barenfeld_updated.append(luminosity_list_barenfeld[x])
            luminosity_list_barenfeld_error_updated.append(luminosity_list_barenfeld_error[x])
            temperature_list_barenfeld_updated.append(temperature_list_barenfeld[x])
            temperature_list_barenfeld_error_updated.append(temperature_list_barenfeld_error[x])



flux_barenfeld_0_88mm = []
flux_barenfeld_0_88_error = []
interpolation_function = open('Barenfeld Table 4.txt', 'r')
lines = interpolation_function.readlines()[32:]
for x in lines:
    flux_barenfeld_0_88mm.append(float(x.split()[2]))
    flux_barenfeld_0_88_error.append(float(x.split()[3]))
interpolation_function.close()

flux_barenfeld_0_88mm_updated = []
flux_barenfeld_0_88_error_updated = []

for x in range(len(source_list_garrett)):
    for z in range(len(source_list_barenfeld_2016)):
        if source_list_garrett[x] == source_list_barenfeld_2016[z]:
            flux_barenfeld_0_88mm_updated.append(flux_barenfeld_0_88mm[z])
            flux_barenfeld_0_88_error_updated.append(flux_barenfeld_0_88_error[z])


# surface density (log)
surface_density_list = [-1.41, -1.58, 0, -1.98, -2.12, -2.17, -1.37, -2.51, 0, -1.72, -2.77, -1.50, -0.64, -1.10, -1.27,
                        -1.69, 0, -2.21, -1.18, -2.28, -1.03, -1.63, -0.88, -1.62]
surface_density_list_lower_bound = [-0.20, -0.14, 0, -0.13, -0.17, -0.31, -0.17, -0.10, 0, -0.08, -0.13, -0.13, -0.22,
                                    -0.15, -0.06, -0.27, 0, -0.10, -0.59, -0.07, -0.12, -0.18, -0.21, -0.18]
surface_density_list_upper_bound = [0.32, 0.21, 0, 0.16, 0.14, 0.53, 0.14, 0.10, 0, 0.07, 0.13, 0.20, 0.13, 0.18, 0.07,
                                    0.15, 0, 0.20, 0.86, 0.12, 0.17, 0.11, 0.25, 0.29]

temperature_feiden = [3060, 3261, 3396, 3517, 3639, 3760, 3888, 4031, 4195, 4397, 4641, 4910, 5214, 5569, 5995, 6618, 7403]
mass_feiden = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7]
log_g_feiden = [4.16, 4.19, 4.20, 4.22, 4.24, 4.26, 4.28, 4.29, 4.30, 4.30, 4.30, 4.28, 4.25, 4.19, 4.06, 3.96, 4.15]

# import info abobut lupus from Ansdell 2018
source_ansdell_lupus = []
spectral_type_ansdell_lupus = []
flux_ansdell_1_33mm_lupus = []
flux_ansdell_1_33mm_error_lupus = []
with open('Ansdell Table 1 1.33mm.txt') as f:
    lines = f.readlines()[47:]
    for x in lines:
        source_ansdell_lupus.append(x[0:17])
        spectral_type_ansdell_lupus.append(x[49:53])
        flux_ansdell_1_33mm_lupus.append(x[66:72])
        flux_ansdell_1_33mm_error_lupus.append(float(x[73:77]))

# remove white spaces at both ends
# ex ' Sz65 ' becomes 'Sz65'
source_ansdell_lupus = [x.strip() for x in source_ansdell_lupus]
flux_ansdell_1_33mm_lupus = [float(x.strip()) for x in flux_ansdell_1_33mm_lupus]

tazzari_lupus_sources = []
tazzari_lupus_flux = []
tazzari_lupus_flux_error = []
tazzari_lupus_spectral_indices = []

with open('Tazzari 2021 2.7mm.txt') as f:
    lines = f.readlines()[12:]
    for x in lines:
        tazzari_lupus_sources.append(x[0:20])
        tazzari_lupus_flux.append(x[79:90])
        tazzari_lupus_flux_error.append(x[90:101])
        tazzari_lupus_spectral_indices.append(x[123:132])


# remove white spaces at both ends
# ex ' Sz 65 ' becomes 'Sz 65'
tazzari_lupus_sources = [x.strip() for x in tazzari_lupus_sources]
tazzari_lupus_flux = [x.strip() for x in tazzari_lupus_flux]
tazzari_lupus_flux.remove('nan')
tazzari_lupus_flux_error = [float(x.strip()) for x in tazzari_lupus_flux_error]
tazzari_lupus_sources.remove('Sz 91')
tazzari_lupus_spectral_indices.remove('      nan')
tazzari_lupus_spectral_indices = [float(x.strip()) for x in tazzari_lupus_spectral_indices]


# one flux for a star is missing, so pop all the data from that line
tazzari_lupus_flux = [float(x) if x != 'nan' else tazzari_lupus_flux.pop(tazzari_lupus_flux.index(x)) for x in tazzari_lupus_flux]


# remove white spaces in the middle of the name
# ex. 'Sz 65' becomes 'Sz65'
tazzari_lupus_sources = [x.replace(" ", "") for x in tazzari_lupus_sources]

sources_name_taurus = []
fluxes_andrews_taurus = []

# add sources names to the list
# since names the table is not very machine-readable a series of trick is performed in order to find the sources names
with open('Andrews Taurus.txt') as f:
    lines = f.readlines()[6:-22]
    for x in lines:
        # this first 'if' is to sort all the long names, if a name in the first column is longer than 4 letters then the whole name is contained in the first column
        if len(x.split()[0]) <= 4:
            # this second 'if' uses the different spectral types names, if we encounter the first (or two) letter
            # to be 'M' or 'K' then the first 2 column contain the name of the source, else we add the third column
            if x.split()[2][0] == 'M' or x.split()[2][0] == 'K' or x.split()[2][0] == '(' or x.split()[2][0:1] == 'B8':
                sources_name_taurus.append(x.split()[0] + ' ' + x.split()[1])
                fluxes_andrews_taurus.append(x.split()[4])
            else:
                sources_name_taurus.append(x.split()[0] + ' ' + x.split()[1] + ' ' + x.split()[2])
                fluxes_andrews_taurus.append(x.split()[5])

        else:
            sources_name_taurus.append(x.split()[0])
            fluxes_andrews_taurus.append(x.split()[3])

source_names_ophiucus_ricci_3_3mm = []
ricci_ophiuchi_flux_3_3mm = []

with open('Ricci Ophiuchi 3.3mm.tex.txt') as f:
    lines = f.readlines()[9:-10]
    for x in lines:
        source_names_ophiucus_ricci_3_3mm.append(x.split('&')[0])
        ricci_ophiuchi_flux_3_3mm.append(x[42:47])

source_names_ophiucus_ricci_3_3mm = [x.strip() for x in source_names_ophiucus_ricci_3_3mm]
ricci_ophiuchi_flux_3_3mm = [x.strip() for x in ricci_ophiuchi_flux_3_3mm]


sources_to_pop = []
fluxes_to_pop = []

for index, element in enumerate(ricci_ophiuchi_flux_3_3mm):
    if element[0] == '<':
        sources_to_pop.append(source_names_ophiucus_ricci_3_3mm[index])
        fluxes_to_pop.append(ricci_ophiuchi_flux_3_3mm[index])

# remove  sources' names that have a flux with '<'
for x in sources_to_pop:
    source_names_ophiucus_ricci_3_3mm.remove(x)

# remove fluxes with '<'
for x in fluxes_to_pop:
    ricci_ophiuchi_flux_3_3mm.remove(x)

# transform values into numbers instead of strings
ricci_ophiuchi_flux_3_3mm = [float(x) for x in ricci_ophiuchi_flux_3_3mm]

ricci_taurus_sources_3mm = []
ricci_taurus_flux_3mm = []
ricci_wavelengths_3mm = []

with open('Ricci Taurus mixed mm.txt') as f:
    lines = f.readlines()[8:-6]
    for x in lines:
        ricci_taurus_flux_3mm.append(x.split('&')[5])
        ricci_taurus_sources_3mm.append(x.split('&')[0])
        ricci_wavelengths_3mm.append(x.split('&')[4])

ricci_taurus_sources_3mm = [x.strip() for x in ricci_taurus_sources_3mm]
ricci_taurus_flux_3mm = [x.strip() for x in ricci_taurus_flux_3mm]
ricci_wavelengths_3mm = [x.strip() for x in ricci_wavelengths_3mm]

sources_to_pop = []
fluxes_to_pop = []
wavelengths_to_remove = []

for index, element in enumerate(ricci_taurus_flux_3mm):
    if element[0] == '<':
        sources_to_pop.append(ricci_taurus_sources_3mm[index])
        fluxes_to_pop.append(ricci_taurus_flux_3mm[index])
        wavelengths_to_remove.append(ricci_wavelengths_3mm[index])

# remove  sources' names that have a flux with '<'
for x in sources_to_pop:
    ricci_taurus_sources_3mm.remove(x)

# remove fluxes with '<'
for x in fluxes_to_pop:
    ricci_taurus_flux_3mm.remove(x)

# remove wavelengths from fluxes containing '<'
for x in wavelengths_to_remove:
    ricci_wavelengths_3mm.remove(x)

# transform values into numbers instead of strings
ricci_taurus_flux_3mm = [float(x) for x in ricci_taurus_flux_3mm]
ricci_wavelengths_3mm = [float(x) for x in ricci_wavelengths_3mm]

ricci_luminosity_taurus_1mm_NOT_LOG = []
with open('Ricci_taurus_table2.tex.txt') as f:
    lines = f.readlines()[9:-6]
    for x in lines:
        ricci_luminosity_taurus_1mm_NOT_LOG.append(x.split('&')[3])

ricci_luminosity_taurus_1mm_NOT_LOG = [x.strip() for x in ricci_luminosity_taurus_1mm_NOT_LOG]
ricci_luminosity_taurus_1mm_NOT_LOG = [float(x) for x in ricci_luminosity_taurus_1mm_NOT_LOG]

spectral_indices_taurus = []
ricci_taurus_sources_1mm = []
ricci_taurus_fluxes_1mm = []
with open('Ricci Taurus 1mm.txt') as f:
    lines = f.readlines()[10:-7]
    for x in lines:
        ricci_taurus_sources_1mm.append(x.split('&')[0])
        ricci_taurus_fluxes_1mm.append(x.split('&')[2])
        spectral_indices_taurus.append(x.split('&')[3])

ricci_taurus_fluxes_1mm = [float(x.strip()) for x in ricci_taurus_fluxes_1mm]
ricci_taurus_sources_1mm = [x.strip() for x in ricci_taurus_sources_1mm]
spectral_indices_taurus = [float(x.strip()) for x in spectral_indices_taurus]
ricci_temperature_taurus_1mm = [4060, 4060, 4730, 3488, 3705, 3560, 4060, 3705, 3850, 3850, 4060, 4900, 3850, 3850, 4730, 3850, 3778, 3778, 5080, 5860, 3705]

sources_ophiucus_cox = []
fluxes_ophiucus_cox_0_87mm = []
with open('apjaa97e2t4_ascii.txt') as f:
    lines = f.readlines()[6:-8]
    for x in lines:
        sources_ophiucus_cox.append(x.split('\t')[1])
        fluxes_ophiucus_cox_0_87mm.append(x.split('\t')[7])

fluxes_ophiucus_cox_0_87mm = [x[0:4] if "or" in x else x for x in fluxes_ophiucus_cox_0_87mm]
indices_to_pop = [fluxes_ophiucus_cox_0_87mm.index(x) for x in fluxes_ophiucus_cox_0_87mm if x[0] == '<']


source_list_ophiucus_ricci_1mm = ['SR 4', 'GSS 26', 'EL 20', 'DoAr 25', 'EL 24', 'EL 27', 'SR 21', 'IRS 41', ' YLW 16C', 'IRS 49', 'DoAr 33', 'WSB 52', 'WSB 60', 'DoAr 44', 'RNO 90', 'Wa Oph 60', 'AS 209']
spectral_index_ophiucus = [2.5, 1.9, 2.5, 2.3, 2.2, 2.2, 2.9, 2.1, 2.4, 1.8, 2.2, 1.8, 1.9, 2.2, 2.3, 2.4, 2.4]
flux_list_ophiucus_ricci_1mm = [79, 215, 151, 405, 664, 564, 220, 84, 123, 40, 64, 88, 156, 168, 111, 250, 441]
