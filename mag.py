from lib_n_cste import *
from distances import *

def mag_btc(bt, Av):
    """
    Compute the apparent magnitute of the galaxy in the blue band
    corrected of the Milky-Way absorption.

    Parameters
    ----------
    bt : float
        Total magnitude in blue band in mag.
    Av : float
        Absorption of the Milky Way in V band in mag.

    Returns
    -------
    btc : float
        The corrected blue apparent blue magnitude of the galaxy.

    """
    
    btc = bt - 1.32*Av
    
    return btc

def MB(btc, d):
    """
    Compute the absolute magnitude of the galaxy in the blue band.

    Parameters
    ----------
    btc : float
        The corrected blue apparent blue magnitude of the galaxy.
    d : float
        The distance of the galaxy in Mpc.

    Returns
    -------
    Lb : float
        Absolute magnitude of the galaxy in the blue band in mag.

    """
    
    Lb = btc - 5*np.log10(d*1000000) + 5
    
    return Lb