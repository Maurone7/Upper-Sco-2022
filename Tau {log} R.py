import matplotlib.pyplot as plt
import numpy as np
from astropy import constants

# all constants in cgs
wavelength_list = [0.088, 0.287]
c = constants.c.cgs.value
h = constants.h.cgs.value
k_b = constants.k_B.cgs.value
s_b = constants.sigma_sb.cgs.value

# following values can be changed
i_list = [0, 30, 60]
# for i in radians from 'x' degrees i = x * np.pi/180
# for i in degrees from 'x' radians i = x * 180/np.pi
flaring = 0.02
L = 1.033 * 10 ** 34
k_v = 2.5
sur_den_0 = 0.0052480746


#1 AU in cm is 1.5.* 10 ** 13
AU = 10
AU_in_cm = 1.5 * 10 ** 13
R_in = AU_in_cm
R = AU_in_cm
R_out = 100 * AU_in_cm

upper_limit = float(input("Upper Limit? "))
steps = float(input("Steps? "))

y_axis_values = []
x_axis_values = []

for wavelengths in wavelength_list:
    wavelength = wavelengths
    f = c / wavelength

    for inclinations in i_list:
        i = inclinations * np.pi / 180
        AU = 10
        while AU <= upper_limit:
            R = AU * AU_in_cm

        # define surface density function
            def sur_den(R):
                return sur_den_0 * ((R / (10 * AU_in_cm)) ** (-1))

        # define tau function
            def tau(sur_den, k_v, i):
                return sur_den(R) * k_v / np.cos(i)

            y_axis_values.append(tau(sur_den, k_v, i))
            x_axis_values.append(AU)
            AU += steps

        if wavelengths == 0.088:
                linestyle = 'dashed'
        else:
                linestyle = '-'

        if inclinations == 60:
                color = 'blue'

        if inclinations == 30:
                color = 'green'

        if inclinations == 0:
                color = 'red'

        plt.plot(x_axis_values, y_axis_values, label=('$\lambda = $' + str(wavelength) + " cm " + str(inclinations)
                                                      + ' degrees'), linestyle=linestyle, color=color)
        y_axis_values = []
        x_axis_values = []

label_1 = (r'$\frac{2{\pi}cosi}{d^2}$')
label_2 = ('$\int_{R_{in}}^{R_{out}}$')
label_3 = (r'$B_\nu[T_i(R)][1-e^{-\tau_{\nu}^{i}(R)}]RdR$')

plt.ylabel(r'$Tau$'), plt.xlabel('$R[AU]$')

plt.title("Tau vs R")
plt.yscale('log')
plt.grid(), plt.legend(), plt.show()