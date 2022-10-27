from astropy import constants
import numpy as np


def update_lum(old_luminosity, old_distance, new_distance):
    return old_luminosity * (new_distance ** 2) / (old_distance ** 2)


def temperature(R, luminosity):
    return (0.02 * luminosity / (8 * np.pi * R**2 * s_b)) ** (1/4)


def Planck_2(wavelength, T):
    return ((2*h*(c**2))/(wavelength**5))*(1/(np.e**(h*c/(wavelength*k_b*T)) -1))


def Mass(flux, distance, opacity, planck, temperature):
    return flux * (distance ** 2) / (opacity * planck * temperature)


def beta(wavelength_1, wavelength_2, T):
    return np.log10((Planck_2(wavelength_1, T))/Planck_2(wavelength_2, T)) / abs(np.log10(wavelength_1/ wavelength_2)) - 2
