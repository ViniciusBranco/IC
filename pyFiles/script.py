__author__ = 'vinicius'
'''
Contribuicao: Carlos Barbosa com >> def wavelength_array(spec) e Maria Luiza com a interpolacao e rebinagem
'''

import pyfits as pf
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as s
import os
import io

def wavelength_array(spec):
    """ Produces array for wavelenght of a given array. """
    w0 = pf.getval(spec, "CRVAL1")
    deltaw = pf.getval(spec, "CD1_1")
    pix0 = pf.getval(spec, "CRPIX1")
    npix = pf.getval(spec, "NAXIS1")
    return w0 + deltaw * (np.arange(npix) + 1 - pix0)


# ======================================================================================================================
""" Leitura dos filtros - 1 por enquanto """
# ======================================================================================================================

jplus_filter = np.loadtxt('Filters/JPLUS/F348_with_ccd_qe.dat') # abre lista de filtros (futuramente: JPASfilterList.txt)

wavelength_filter = jplus_filter[:, 0] # vetor comprimento de onda do filtro
transmission = jplus_filter[:, 1] # vetor transmissao de onda do filtro (sem ccd)

# ======================================================================================================================
""" Leitura dos espectros e rebinagem do filtro sob interpolacao do espectro"""
# ======================================================================================================================

filelist = np.loadtxt('NGClistFits.txt', dtype=str) # abre lista de espectros

for i in filelist:
    flux = pf.getdata(i) # fluxo do espectro
    wavelength_spec = wavelength_array(i) # comprimento de onda do espectro
    f = s.interp1d(wavelength_spec, flux) # interpola os pontos do espectro e retorna a função f
    ''' a fazer '''
    # adaptar wavelength_filter para estar dentro da interpolacao
    # Do contrário, o seguinte erro é esperado:
    # ValueError: A value in x_new is below the interpolation range.
    # Onde 'x_new' é wavelength_filter que é utilizado para se calcular as novas transmissões.
    transmission_new = f(wavelength_filter) # novas transmissões calculadas por f.
    plt.plot(wavelength_spec, flux, 'b-') # plota o espectro
    plt.plot(wavelength_filter, transmission_new, 'r-') # plota a resposta do filtro no dado espectro
    
#plt.savefig("NGCspec.pdf", format='pdf')
plt.show()	

# ======================================================================================================================
""" Rebinagem """
# ======================================================================================================================

""" somente para o filtro 348 do Jplus """



'''
interp_function = s.interp1d(wavelength, transmission)
new_wavelength  = np.linspace(np.ceil(wavelength.min()), np.ceil(wavelength.max()), np.ceil(wavelength.max()-wavelength.min()+1))
new_wavelength  = np.arange(np.ceil(wavelength.min()), np.ceil(wavelength.max()), 1)
new_transmission = np.arange(transmission.min(), transmission.max(), np.ceil(wavelength.max()-wavelength.min()+1))
new_transmission = interp_function(new_wavelength)

transmission_new = np.interp(wavelength_spec, wavelength_filter, transmission)
'''




"""
np.savetxt('JPLUS_F348_with_ccd_qe_NEW.txt', np.column_stack((new_wavelength, new_transmission)), fmt='%s', delimiter='       ')


''' Conferindo filtros rebinados'''
jplus_filter_new = np.loadtxt('JPLUS_F348_with_ccd_qe_NEW.txt')
print wavelength.size
print "----"
print new_wavelength.size
print "----"
print jplus_filter_new.shape
"""

# ======================================================================================================================
""" Convolucao """
# ======================================================================================================================

















# with io.open("name/NGClistFits.txt", newline='\n') as f:
#     for line in f:
#         data = pf.getdata(line)
#         print data
# 	w = wavelength_array(line)
# 	plt.plot(w,data)
	

# plt.savefig("NGCspec.png")
# plt.show()

# plt.savefig('color_e.pdf', format='pdf')













'''
    2. rotina para dat
'''
'''
Abrir o conjunto de filtros
'''
'''
Rebinar os pontos dos filtros para escala de comprimento de onda dos observados
'''
'''
Interpolar os fluxos dos filtros
'''
'''
Convoluir os filtros com os espectros
'''
'''
Gerar arquivo de saida
'''


