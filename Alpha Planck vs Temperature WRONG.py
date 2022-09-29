from astropy import constants
import numpy as np
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

#set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

c = constants.c.cgs.value
h = constants.h.cgs.value
k_b = constants.k_B.cgs.value
x = np.linspace(4,200, num=1000)

def Planck_nu(wavelength, T):
    nu = c / wavelength
    return (2*h*(nu**3)/(c**2))*(1/(np.e**(h*nu/(k_b*T)) -1 ))

def function(wavelength_1, wavelength_2, T):
    return (np.log(Planck_nu(wavelength_1, T) / Planck_nu(wavelength_2, T)))/(np.log(wavelength_2/wavelength_1))

plt.plot(x, function(0.3, 0.087, x))
plt.xlabel('$T_{eff}[K]$', fontsize=20), plt.ylabel(r'$\alpha_{Planck}$', fontsize=20)
plt.grid()
plt.show()