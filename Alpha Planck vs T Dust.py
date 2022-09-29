import numpy as np
from astropy import constants
from Planck import beta
import matplotlib.pyplot as plt
fig, ax = plt.subplots()

#set thickness axis
plt.setp(ax.spines.values(), linewidth=2)

#avoid axis labels being cut
plt.gcf().subplots_adjust(bottom=0.15, left=0.13)

#import constants' values in cgs
h = constants.h.cgs.value
c = constants.c.cgs.value
T = np.linspace(3.5, 200, 200)
plt.plot(T, beta(0.087, 0.287, T))
plt.grid()
plt.xlabel(r'$T_{eff}\rm[K]$', fontsize=20), plt.ylabel(r'$\alpha_{Planck}$', fontsize=20)
ax.tick_params(which='both', labelsize=15)
plt.savefig('Planck vs T')
plt.show()