import numpy as np

from data_file import temperature_list_barenfeld, luminosity_list_barenfeld
from Interpolation import f, temperature_feiden
import matplotlib.pyplot as plt

temperature_list_barenfeld = [10 ** x for x in temperature_list_barenfeld]
#luminosity_list_barenfeld = [10 ** x for x in luminosity_list_barenfeld]

x = np.linspace(np.min(temperature_feiden), np.max(temperature_feiden))
plt.plot(x, f(x))
plt.scatter(temperature_list_barenfeld, luminosity_list_barenfeld)
#plt.yscale('log')
plt.xlabel('$T_{eff}(K)$'), plt.ylabel('Luminosity "log"')
#plt.gca().invert_xaxis()
plt.savefig("111.png")
plt.show()