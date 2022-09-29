from tabulate import tabulate
from astropy import constants
import numpy as np
import Planck

L_sun = constants.L_sun.cgs.value
s_b = constants.sigma_sb.cgs.value

AU_to_cm = 1.5 * 10 ** 13
old_distances_list = [146.35, 147.5, 166.08, 137.67, 108.83, 140.28, 141.8, 143.57, 150.11, 145.1, 145, 142.79, 198.38,
                      138.02, 137.61, 155.3, 127.92, 139.15, 145, 145, 149.96, 139.71, 131.77, 137.92]
source_list = []
source_list_barenfeld = []
distance_new_list = []
distance_new_error_list = []
luminosity_list = []
luminosity_list_updated = []
table = []
radius_dust = []
radius_dust_updated = []
lower_bound_radius = []
lower_bound_radius_updated = []
upper_bound_radius = []
upper_bound_radius_updated = []
temperature_list = []
alpha_planck_list = []
old_lum = []

f = open(r'C:\Users\Owner\Desktop\School\Research\Ricci\Coding project\Table 1 Barenfeld.txt', 'r')
lines = f.readlines()[1:]

for x in lines:
    source_list_barenfeld.append(x.split()[1])
    radius_dust.append(int(x.split()[5]))
    lower_bound_radius.append(int(x.split()[6][1:-1]))
    upper_bound_radius.append(int(x.split()[7][1:-1]))
f.close()


f = open(r'C:\Users\Owner\Desktop\School\Research\Ricci\Coding project\GAIA 3 Parallax.txt', 'r')
lines = f.readlines()[1:]

for x in lines:
    source_list.append(x.split()[0])
    distance_new_list.append(1 / float(x.split()[1]) * 1000)
    distance_new_error_list.append((1 / float(x.split()[1]) * 1000) - 1 / (float(x.split()[1]) + float(x.split()[2])) * 1000)
    luminosity_list.append((10 ** float(x.split()[5])) * L_sun)

f.close()

for x in range(len(source_list)):
    for z in range(len(source_list_barenfeld)):
        if source_list[x] == source_list_barenfeld[z]:
            radius_dust_updated.append(radius_dust[z])
            lower_bound_radius_updated.append(lower_bound_radius[z])
            upper_bound_radius_updated.append(upper_bound_radius[z])


#add values of radius of dust
radius_dust_updated.insert(2, 65)
lower_bound_radius_updated.insert(2, 0)
upper_bound_radius_updated.insert(2, 0)
radius_dust_updated.insert(8, 65)
lower_bound_radius_updated.insert(8,0)
upper_bound_radius_updated.insert(8,0)
radius_dust_updated.insert(16, 66)
lower_bound_radius_updated.insert(16,0)
upper_bound_radius_updated.insert(16,0)

for x in range(len(luminosity_list)):
    luminosity_list_updated.append(np.log10((luminosity_list[x] * (distance_new_list[x] ** 2) / ((old_distances_list[x]) ** 2)) / L_sun))


#formula to find temperature from eq. 3
def temperature(R, luminosity):
    return (0.02 * luminosity / (8 * np.pi * R**2 * s_b)) ** (1/4)


for x in range(len(luminosity_list_updated)):
    temperature_list.append(temperature(radius_dust_updated[x] * AU_to_cm, (10 ** luminosity_list_updated[x]) * L_sun))

for x in temperature_list:
    alpha_planck_list.append(Planck.beta(0.087, 0.3, x))

#add elements to table
for x in range(len(source_list)):
    table.append([source_list[x], distance_new_list[x], distance_new_error_list[x], luminosity_list_updated[x],
                  (str(radius_dust_updated[x]) + '('  + str(lower_bound_radius_updated[x]) + ', +' + str(upper_bound_radius_updated[x]) + ')'),
                  round(temperature_list[x], 2), alpha_planck_list[x]])

#print table on pytohn
# print(tabulate(table, headers=['Sources', 'Distance', 'Parallax Error', 'Luminosity', 'Radius dust', 'Temperature', '$alpha_{Planck}$']))


#create file on notepad called 'Table updated'
with open('Table updpated.txt', 'w') as f:
    f.write(tabulate(table, headers=['Sources', 'Distance', 'Parallax Error', 'Luminosity', 'Radius dust', 'Temperature', '$alpha_{Planck}$']))

f.close()