import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
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
d = 4.32 * 10 ** 20
sur_den_0 = 0.0052480746


#1 AU in cm is 1.5.* 10 ** 13
AU = 10
AU_in_cm = 1.5 * 10 ** 13
R_in = AU_in_cm
R = AU_in_cm

# fixed R for the sur_den function
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
            R_out = AU * AU_in_cm

        # define temperature function
            def T(flaring, L, s_b, R):
                return (flaring * L / (8 * np.pi * R ** 2 * s_b)) ** (1/4)

        # define surface density function
            def sur_den(R):
                return sur_den_0 * ((R / (10 * AU_in_cm)) ** (-1))

        # define tau function
            def tau(sur_den, k_v, i):
                return sur_den(R) * k_v / np.cos(i)

        # define planck's function
            def planck_function(h, f, c, k_b, T):
                return 2 * h * (f ** 3) / ((c ** 2) * (np.e**(h * f / (k_b * T(flaring, L, s_b, R))) - 1))

        # define part of the function 2.1 to be integrated
            def fun(R, h, f, c, k_b, T, tau):
                return planck_function(h,f,c,k_b,T) * (1 - np.e ** (-tau)) *R

        # define integration
            def int(fun, h, f, c, k_b, T, tau):
                return quad(fun,
                            R_in, R_out, args=(h, f, c, k_b, T, tau(sur_den, k_v, i)))

            def final(fun, h, f, c, k_b, T, tau):
                return 2 * np.pi * np.cos(i) / d ** 2 * int(fun, h, f, c, k_b, T, tau)[0]



            y_axis_values.append(10 ** 26 * final(fun, h, f, c, k_b, T, tau))
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
                                                      + ' degrees'), color=color)
        y_axis_values = []
        x_axis_values = []

label_1 = (r'$\frac{2{\pi}cosi}{d^2}$')
label_2 = ('$\int_{R_{in}}^{R_{out}}$')
label_3 = (r'$B_\nu[T_i(R)][1-e^{-\tau_{\nu}^{i}(R)}]RdR$')

plt.ylabel(r'$F_\nu[mJy]$'), plt.xlabel('$R_{out}[AU]$')

plt.title("Flux vs $R_{out}$")
plt.grid(), plt.legend(), plt.show()
