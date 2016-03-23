#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'vinicius'
'''
Contribuicao: Maria Luiza Linhares Dantas)
'''

# ======================================================================================================================


import numpy as np
import scipy.interpolate as s
import os

# ======================================================================================================================



jplus_filter = np.loadtxt('Filters/JPLUS/F348_with_ccd_qe.dat')

wavelength = jplus_filter[:, 0]
transmission = jplus_filter[:, 1]

interp_function = s.interp1d(wavelength, transmission)
new_wavelength  = np.linspace(np.ceil(wavelength.min()), np.ceil(wavelength.max()), np.ceil(wavelength.max()-wavelength.min()+1))
new_wavelength  = np.arange(np.ceil(wavelength.min()), np.ceil(wavelength.max()), 1)
new_transmission = np.arange(transmission.min(), transmission.max(), np.ceil(wavelength.max()-wavelength.min()+1))
new_transmission = interp_function(new_wavelength)

np.savetxt('jplus_filter_response_1angstrom.txt', np.column_stack((new_wavelength, new_transmission)),
       fmt='%s', delimiter='       ')


''' Conferindo '''
jplus_filter_new = np.loadtxt('jplus_filter_response_1angstrom.txt')
print wavelength.size
print "----"
print new_wavelength.size
print "----"
print jplus_filter_new.shape


"""


# Main thread ----------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    
    fuv_response = np.loadtxt('FUV_filter_response.txt')
    nuv_response = np.loadtxt('NUV_filter_response.txt')

    wavelength      = fuv_response[:, 0]
    transmission = fuv_response[:, 1]
    
    wavelength_nuv      = nuv_response[:, 0]
    filter_response_nuv = nuv_response[:, 1]
    
    # For the FUV band:
    
    interp_function_fuv = s.interp1d(wavelength, transmission)
    new_wavelength  = np.linspace(np.ceil(wavelength.min()), np.ceil(wavelength.max()), np.ceil(wavelength.max()-wavelength.min()+1))
    new_wavelength  = np.arange(np.ceil(wavelength.min()), np.ceil(wavelength.max()), 1)
    new_transmission = np.arange(transmission.min(), transmission.max(), np.ceil(wavelength.max()-wavelength.min()+1))
    new_transmission = interp_function_fuv(new_wavelength)

    np.savetxt('fuv_filter_response_1angstrom.txt', np.column_stack((new_wavelength, new_transmission)),
               fmt='%s', delimiter='       ', header='wavelength   response', comments='#')
    
    # For the NUV band:
    interp_function_nuv = s.interp1d(wavelength_nuv, filter_response_nuv)
    new_wavelength_nuv  = np.linspace(np.ceil(wavelength_nuv.min()), np.ceil(wavelength_nuv.max()), np.ceil(wavelength_nuv.max()-wavelength_nuv.min()+1))
    new_wavelength_nuv  = np.arange(np.ceil(wavelength_nuv.min()), np.ceil(wavelength_nuv.max()), 1)
    new_filter_response_nuv = np.arange(filter_response_nuv.min(), filter_response_nuv.max(), np.ceil(wavelength_nuv.max()-wavelength_nuv.min()+1))
    new_filter_response_nuv = interp_function_nuv(new_wavelength_nuv)

    np.savetxt('nuv_filter_response_1angstrom.txt', np.column_stack((new_wavelength_nuv, new_filter_response_nuv)),
              fmt='%s', delimiter='       ', header='wavelength   response', comments='#')
"""


