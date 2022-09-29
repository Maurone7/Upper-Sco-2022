import time
t0 = time.time()
import matplotlib.pyplot as plt

f = open('Barenfeld Table 1.txt', 'r')
lines = f.readlines()[22:]
luminosity_log = []
luminosity_error_log = []
mass_log = []
mass_error_log = []
sources_lists = []

for x in lines:
    sources_lists.append(x.split()[1])

for x in lines:
    mass_log.append(float(x.split()[-3]))

for x in lines:
    mass_error_log.append(float(x.split()[-2]))

f.close()
g = open(r'Barenfeld Table 4.txt', 'r')
lines = g.readlines()[22:]
flux = []
flux_error = []
for x in lines:
    flux.append(float(x.split()[2]))

for x in lines:
    flux_error.append(float(x.split()[3]))

g.close()

# FROM GARRETT'S THESIS
source_list_garrett = ['J15530132-2114135', 'J15582981-2310077', 'J15583692-2257153', 'J16001844-2230114', 'J16014086-2258103',
               'J16020757-2257467', 'J16024152-2138245', 'J16035767-2031055', 'J16042165-2130284', 'J16054540-2023088',
               'J16062196-1928445', 'J16072625-2432079', 'J16075796-2040087', 'J16082324-1930009', 'J16090075-1908526',
               'J16111330-2019029', 'J16113134-1838259', 'J16123916-1859284', 'J16135434-2320342', 'J16141107-2305362',
               'J16142029-1906481', 'J16153456-2242421', 'J16154416-1921171', 'J16181904-2028479']

    # the distance is in parsec
distance_list_garrett = [146.35, 147.5, 166.08, 137.67, 108.83, 140.28, 141.8, 143.57, 150.11, 145.1, 145, 142.79, 198.38,
                            138.02, 137.61, 155.3, 127.92, 138.15, 145, 145, 149.96, 139.71, 131.77, 137.92]
    # the masses are M/M_sun
masses_list_garrett = [0.186, 0.294, 1.418, 0.151, 0.188, 0.359, 0.151, 0.984, 1.195, 0.426, 0.702, 0.237, 0.676, 0.563, 0.702,
                       0.294, 0.984, 0.633, 0.151, 1.195, 0.702, 0.702, 0.984, 0.151]
flux_list_2_87mm = [0.603, 0.58, 5.18, 0.36, 0.28, 0.49, 1.08, 0.41, 5.94, 1, 0.62, 1.08, 2.37, 3.1, 3.19, 0.69, 54.1,
                    0.4, 1.25, 0.71, 3.19, 1.26, 2.04, 0.52]
flux_list_0_88mm_garrett = [5.78, 5.86, 174.92, 3.89, 3.45, 5.26, 10.25, 4.30, 218.76, 7.64, 4.08, 13.12, 23.49, 43.19, 47.28,
                            4.88, 903.26, 6.01, 7.53, 4.77, 40.69, 11.75, 26.57, 4.62]
error_mass_garrett = [0.0005, 0.0008, 0.0002, 0.0005, 0.0005, 0.0009, 0.0005, 0.0005, 0.0004, 0.0009, 0.0007, 0.0008, 0.001,
                      0.0009, 0.0007, 0.0008, 0.0005, 0.0008, 0.0005, 0.0004, 0.0007, 0.0007, 0.0005, 0.0005]
i_list = []
errorr_garrett = []

for i in range(len(mass_log)):
    for x in range(len(masses_list_garrett)):
        if sources_lists[i] == source_list_garrett[x]:
            i_list.append(i)

    # print(x, i)

for x in masses_list_garrett:
    errorr_garrett.append(0.2 * x)

i_list.sort(reverse=True)
for i in i_list:
    mass_log.pop(i)
    flux.pop(i)
    mass_error_log.pop(i)

mass = []
mass_error = []

for x in mass_log:
    mass.append(10 ** x)

for x in range(len(mass_error_log)):
    mass_error.append(10 ** (mass_log[x] + mass_error_log[x]) - mass[x])

plt.scatter(masses_list_garrett, flux_list_0_88mm_garrett, c='red')
plt.errorbar(masses_list_garrett, flux_list_0_88mm_garrett, xerr=errorr_garrett, ls='none', c='red')
plt.scatter(mass, flux, c='gray')
plt.errorbar(mass, flux, xerr=mass_error, ls='none', c='gray')
plt.errorbar(mass, flux, xerr=mass_error, ls='none', c='gray')
plt.xlabel(r'$M_{\star}(M_{\odot})$'), plt.ylabel('$F_{0.88mm}(mJy)$')
plt.yscale('log'), plt.xscale('log')
plt.savefig('Fig 1')
plt.show()

t1 = time.time()
total = t1-t0
print(total)