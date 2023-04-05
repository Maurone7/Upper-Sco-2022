import matplotlib.pyplot as plt
import numpy as np

from data_file import van_der_plas_radius, van_der_plas_a, van_der_plas_b

def van_der_pals_temperature(a, b, L):
    return a*(L**b)

def model_func(x, a, k, b):
    return a * np.exp(-k*x) + b

x = np.linspace(0, 200, 100)

def derivation_van_der_pals_a(R):
    # y = 14.175 + (148.7922 - 14.175)/(1 + (x/4.327541)^0.9098155)
    return 14.175 + (148.7922 - 14.175)/(1 + ((R/4.327541)**0.9098155))

def derivation_van_der_pals_b(R):
    # y = 0.1499356 + (0.2328295 - 0.1499356)/(1 + (x/38.81332)^2.522306)
    return 0.1499356 + (0.2328295 - 0.1499356)/(1 + ((R/38.81332)**2.522306))

plt.plot(van_der_plas_radius, van_der_plas_a, 'o', label='a')
plt.plot(van_der_plas_radius, van_der_plas_b, 'o', label='b')
plt.show()