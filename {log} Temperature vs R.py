import matplotlib.pyplot as plt
import numpy as np
from astropy import constants

# all constants in cgs
s_b = constants.sigma_sb.cgs.value

# following values can be changed
flaring = 0.02
L = 1.033 * 10 ** 34
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
        return (flaring * L / (8 * np.pi * R ** 2 * s_b)) ** (1/4)

    y_axis_values.append(T(flaring, L, s_b, R))
    x_axis_values.append(AU)
    AU += steps

plt.ylabel(r'$Temperature [K]$')
plt.xlabel('$R[AU]$')
plt.plot(x_axis_values, y_axis_values, label=(r'${(\frac{\phi L_{\star}}{8\pi R^2\sigma_{SB}})}^{\frac{1}{4}}$'))
plt.title("Temperature vs R")
plt.yscale('log'), plt.xscale('log')
plt.grid(), plt.legend(), plt.show()