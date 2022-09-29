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
L_sun = constants.L_sun.cgs.value

# following values can be changed
i = 0
# for i in degrees i = x  * 180/np.pi
flaring = 0.02

# J15583692-2257153
L = 0.47

k_v = 1
d = 4.32 * 10 ** 20
sur_den_0 = 0.0052480746


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

while AU <= upper_limit:
    R = AU * AU_in_cm

# define temperature function
    def T(flaring, L, s_b, R):
        return (flaring * 10 ** L * L_sun / (8 * np.pi * R ** 2 * s_b)) ** (1/4)

    y_axis_values.append(T(flaring, L, s_b, R))
    x_axis_values.append(AU)
    AU += steps

plt.ylabel(r'$Temperature [K]$')
plt.xlabel('$R[AU]$')
plt.plot(x_axis_values, y_axis_values, label=(r'$\frac{\phi L_{\star}}{8\pi R^2\sigma_{SB}}$'))
plt.title("Temperature vs R")
plt.grid(), plt.legend(), plt.show()