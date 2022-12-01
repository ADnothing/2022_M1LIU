from lib_n_cste import *
from velocities import *
from distances import *

#=====Flux===========

def std_FHI(w20, rms, R=spectral_R):
    """
    Compute the standart deviation of the integrated flux.

    Parameters
    ----------
    w20 : float
        The width of the signal at 20% maximum in km/s.
    rms : float
        Noise level in mJy.
    R : float, optional
        Spectral resolution in km/s. The default is spectral_R.

    Returns
    -------
    float
        The standart deviation of the integrated flux.

    """
    
    return 2*((1.2*w20/R)**0.5)*R*rms*1e-3

#=====Velocities=====

def std_Optical_speed(w20, w50, FHI, SNR, rms):
    """
    Compute the standart deviation of the optical speed.

    Parameters
    ----------
    w20 : float
        The width of the signal at 20% maximum in km/s.
    w50 : float
        The width of the signal at 50% maximum in km/s.
    FHI : float
        Integrated flux of the signal in Jy.km/s.
    SNR : float
        Signal to noise ratio.
    rms : float
        Noise level in mJy.

    Returns
    -------
    sigma_cz : float
        Standart deviation of the optical speed in km/s.

    """
    
    sigma_cz = 1.5*((w20 - w50)/SNR)
    
    return sigma_cz
