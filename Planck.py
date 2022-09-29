from astropy import constants
import numpy as np

k_b = constants.k_B.cgs.value
c = constants.c.cgs.value
h = constants.h.cgs.value

def planck_function_wavelength(wavelength, T):
    '''Calculate Planck function
    It requires 2 inputs:
    -1 wavelength [cm]
    -1 Temperature [K]'''
    return ((2*h*(c**2))/(wavelength**5))*(1/(np.e**(h*c/(wavelength*k_b*T)) - 1))

def planck_function_frequency(frequency, T):
    '''Calculate Planck function
    It requires 2 inputs:
    -1 frequency [Hz]
    11 Temperature [K]'''
    return ((2*h*(frequency**3))/(c**2) * 1/(np.e**((h*frequency)/(k_b*T)) - 1))

def alpha(wavelength_1, wavelength_2, T):
    '''Calculate spectral index( (alpha) with Planck functions at two different wavelengths
    It takes advantage of another function defined in the same file (planck_function_wavelength)
    It requires 3 inputs:
    -2 wavelengths, one per planck's function
    -1 Temperature, both planck's functions use the same temperature'''
    return np.log(planck_function_wavelength(wavelength_1, T) / planck_function_wavelength(wavelength_2, T)) / \
           np.log(wavelength_2 / wavelength_1) - 2


def beta(wavelength_1, wavelength_2, T):
    '''Calculate alpha_{Planck}
    It requires 3 inputs:
    -2 Wavelengths [cm]
    -1 Temperature [K]'''
    return np.log10((planck_function_wavelength(wavelength_1, T)) / planck_function_wavelength(wavelength_2, T)) / \
           (np.log10(wavelength_1 / wavelength_2))
