from lib_n_cste import *
from speeds import *
from distances import *


def mass_HI(d, FHI):
    """
    Compute the mass of the neutral gaz in the galaxy.

    Parameters
    ----------
    d : float
        The distance of the galaxy in Mpc.
    FHI : float
        Integrated flux of the signal in mJy.km/s.

    Returns
    -------
    mhi : float
        The mass of the neutral gaz in the galaxy in solar mass.
    """
    
    cste = 2.326e5
    
    mhi = cste*(d**2)*FHI
    
    return mhi


def mass_stars(btc, d):
    """
    Compute the mass of the stars inside the galaxy.

    Parameters
    ----------
    btc : float
        Bolometric apparent magnitude of the galaxy in mag.
    d : float
        The distance of the galaxy in Mpc.

    Returns
    -------
    M_star : float
        The mass of the star inside the galaxy in solar mass.

    """
    

    abs_mag = btc - 5*np.log10(d) - 5
    
    L = 10**(0.4*(abs_mag_sun - abs_mag))
    M_star = L*4
    
    return M_star


def mass_tot(Vmax, R):
    """
    Compute the total mass of the galaxy.

    Parameters
    ----------
    Vmax : float
        The maximum of the rotation speed of the galaxy in km/s.
    R : float
        Radius of the galaxy in kpc.
    

    Returns
    -------
    M_tot : float
        The total mass of the galaxy in solar mass.
    """
    
    cste = 2.326e5
    
    M_tot = cste*(Vmax**2)*0.6*R
    
    return M_tot