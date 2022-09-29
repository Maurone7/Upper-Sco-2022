# The role of this code is to extract luminosities, radii, g and temperature of certain stars from the models in Feiden's GitHub

import numpy as np
# import all the of files' names to the list named onlyfiles
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(r'all_GS98_p000_p0_y28_mlt1.884_Beq') if isfile(join(r'all_GS98_p000_p0_y28_mlt1.884_Beq', f))]
onlyfiles = sorted(onlyfiles)


age_column_5Myr = []
luminosity_column_5Myr = []
radius_column_5Myr = []
g_column_5Myr = []
temperature_column_5Myr = []
#loop in every file
x = 0
while x < len(onlyfiles):
    #open folder where all the files are saved by adding the name of the files to the path
    with open(r'all_GS98_p000_p0_y28_mlt1.884_Beq/' + str(onlyfiles[x])) as f:
        lines = f.readlines()[14:]
        # loop in every column to find where the age equals 0.005Gyr
        for column in lines:
            if str(float((column.split()[2])))[:5] == '0.005':
                # add age, luminosity, radius, g and temperature to their respective lists
                age_column_5Myr.append((column.split()[2]))
                luminosity_column_5Myr.append(float(column.split()[3]))
                radius_column_5Myr.append(float(column.split()[4]))
                g_column_5Myr.append(float(column.split()[5]))
                temperature_column_5Myr.append(float(column.split()[6]))
                break

        x += 1

# get rid of log scale for the temperatures imported
temperature_column_5Myr = [10 ** x for x in temperature_column_5Myr]

##### repeat same loop
age_column_10Myr = []
luminosity_column_10Myr = []
radius_column_10Myr = []
g_column_10Myr = []
temperature_column_10Myr = []
mass_column_10Myr = []
mass_column = []
# recreate loop for ages equal to 0.01Gyr
x = 0
while x < len(onlyfiles):
    mass_column.append(onlyfiles[x][1:5])
    x += 1

x = 2
mass_column = [z[0:x-1] + '.' + z[x-1:] for z in mass_column]
mass_column = [float(x) for x in mass_column]

x = 0
while x < len(onlyfiles):
    with open(r'all_GS98_p000_p0_y28_mlt1.884_Beq/' + str(onlyfiles[x])) as f:
        lines = f.readlines()[14:]
        for column in lines:
            if str(float((column.split()[2])))[:4] == '0.01':
                age_column_10Myr.append((column.split()[2]))
                luminosity_column_10Myr.append(float(column.split()[3]))
                radius_column_10Myr.append(float(column.split()[4]))
                g_column_10Myr.append(float(column.split()[5]))
                temperature_column_10Myr.append(float(column.split()[6]))
                mass_column_10Myr.append(float(mass_column[x]))

                break

    x += 1

temperature_column_10Myr = [10**x for x in temperature_column_10Myr]

age_column_20Myr = []
luminosity_column_20Myr = []
radius_column_20Myr = []
g_column_20Myr = []
temperature_column_20Myr = []


# recreate loop for ages equal to 0.02Gyr
x = 0
while x < len(onlyfiles):
    with open(r'all_GS98_p000_p0_y28_mlt1.884_Beq/' + str(onlyfiles[x])) as f:
        lines = f.readlines()[14:]
        for column in lines:
            if str(float((column.split()[2])))[:4] == '0.02':
                age_column_20Myr.append((column.split()[2]))
                luminosity_column_20Myr.append(float(column.split()[3]))
                radius_column_20Myr.append(float(column.split()[4]))
                g_column_20Myr.append(float(column.split()[5]))
                temperature_column_20Myr.append(float(column.split()[6]))
                break

        x += 1


temperature_column_20Myr = [10 ** x for x in temperature_column_20Myr]