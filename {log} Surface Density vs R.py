import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from astropy import constants

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
d = 4.32 * 10 ** 20
sur_den_0 = 0.0389045145


#1 AU in cm is 1.5.* 10 ** 13
AU = 1
AU_in_cm = 1.5 * 10 ** 13
R_in = AU * AU_in_cm

# fixed R for the sur_den function
R_out = 100 * AU_in_cm


y_axis_values = []
x_axis_values = []

upper_limit = float(input("Upper Limit? "))
steps = float(input("Steps? "))
mass_g = 0

while AU <= upper_limit:
    R_in_cm = AU * AU_in_cm

# define surface density function
    def sur_den(R_in_cm):
        return sur_den_0 * ((R_in_cm / (10 * AU_in_cm)) ** (-1))

    def mass_graph(R_in_cm, AU_in_cm, sur_den):
        return np.pi * (R_in_cm ** 2 - (R_in_cm - AU_in_cm * steps) ** 2) * sur_den(R_in_cm)

    mass_g += mass_graph(R_in_cm, AU_in_cm, sur_den)



    y_axis_values.append(mass_graph(R_in_cm, AU_in_cm, sur_den) / (5.9722 * 10**27))
    x_axis_values.append(AU)
    AU += steps

print(str(mass_g/ (5.9722 * 10 ** 27)) + r" Earth's masses")
plt.ylabel(r'Surface Density $[\frac{g}{cm^2}]$')
plt.xlabel('$R[AU]$')
plt.plot(x_axis_values, y_axis_values, label=(r'${\sum}_0 (\frac{R}{10 AU})^{-1}$'))
plt.yscale('log'), plt.xscale('log')
plt.title("Surface Density vs R")
plt.grid(), plt.legend(), plt.show()

# sigma(R)= sigma_0 * (R/10) ** (-1)
# log_10 (sigma) = log_10 (sigma_0 * (R/10) ** (-1))
# log_10 (sigma) = log_10(sigma_0) + log_10((R/10) ** (-1))
# log_10 (sigma) = log_10(sigma_0) -1 * (log_10 (R) - log_10(10))
# log_10 (sigma) = log_10(sigma_0) - log_10(R) + log_10(10)
# log_10 (sigma) = log_10(sigma_0) + log_10(10) - log_10(R)
# y = constants - x

