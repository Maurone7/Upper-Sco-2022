import matplotlib.pyplot as plt
from astropy import constants

fig, ax = plt.subplots()

#set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

#avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.15)

# all constants in cgs
wavelength = 0.088
c = constants.c.cgs.value
h = constants.h.cgs.value
k_b = constants.k_B.cgs.value
f = c / wavelength
s_b = constants.sigma_sb.cgs.value

# following values can be changed
i = 0
# for i in radians from 'x' degrees i = x * np.pi/180
# for i in degrees from 'x' radians i = x * 180/np.pi
flaring = 0.02
L = 1.033 * 10 ** 34
k_v = 1
M_sun = constants.M_earth.value
d = 4.32 * 10 ** 20
sur_den_0 = 0.0389045145

#1 AU in cm is 1.5.* 10 ** 13
AU = 1
AU_in_cm = 1.5 * 10 ** 13
R_in = AU * AU_in_cm
R_out = 100 * AU_in_cm

y_axis_values = []
x_axis_values = []

upper_limit = 100
steps = 1

while AU <= upper_limit:
    R = AU * AU_in_cm

# define surface density function
    def sur_den(R):
        return sur_den_0 * ((R / (10 * AU_in_cm)) ** (-1))

    y_axis_values.append(sur_den(R))
    x_axis_values.append(AU)
    AU += steps

plt.ylabel(r'Surface Density $[\frac{g}{cm^2}]$', fontsize=20)
plt.xlabel('$R[AU]$', fontsize=20)
plt.plot(x_axis_values, y_axis_values)
plt.grid()
ax.tick_params(which='both', labelsize=15)
plt.savefig('Fig. 7.png')
plt.show()