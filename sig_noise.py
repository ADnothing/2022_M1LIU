from lib_n_cste import *

def S_N(w50, FHI, rms, r=spectral_R):
    """
    Compute the modified signal to noise ratio.

    Parameters
    ----------
    w50 : float
        The width of the signal at 50% maximum in km/s.
    FHI : float
        Integrated flux of the signal in Jy.km/s.
    rms : float
        Noise level in mJy.km/s..
    r : float, optional
        Spectral resolution of the GRT in km/s. The default is spectral_R.

    Returns
    -------
    SNR : float
        Signal to noise ratio.
    """
    
    a = FHI/w50
    b = (w50/(2*r))**0.5
    c = 1/rms
    
    S_R = 1000*a*b*c
    
    return S_R