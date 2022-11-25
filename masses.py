from lib_n_cste import *
from velocities import *
from distances import *
from mag import *


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


def mass_stars(log_Lb, d):
    """
    Compute the mass of the stars inside the galaxy.

    Parameters
    ----------
    log_Lb : float
        log10 of the luminance of the galaxy in the blue band in mag.
    d : float
        The distance of the galaxy in Mpc.

    Returns
    -------
    M_star : float
        The mass of the star inside the galaxy in solar mass.

    """
    
    L = 10**log_Lb
    M_star = 1.4*L
    
    return M_star


def mass_tot(Vmax, D, r_param):
    """
    Compute the total mass of the galaxy.

    Parameters
    ----------
    Vmax : float
        The maximum of the rotation speed of the galaxy in km/s.
    D : float
        Diameter of the galaxy in kpc.
    r_param
        Proportion of the radius taken into account (HSB or LSB galaxy)
    

    Returns
    -------
    M_tot : float
        The total mass of the galaxy in solar mass.
    """
    
    cste = 2.326e5
    
    M_tot = cste*(Vmax**2)*r_param*(D/2)
    
    return M_tot


def mass_barr(mhi, M_star):
    """
    Compute the baryonic mass of the galaxy
    considering no contribution from dusts and molecular gas

    Parameters
    ----------
    mhi : float
        The mass of the neutral gaz in the galaxy in solar mass.
    M_star : float
        The mass of the star inside the galaxy in solar mass.

    Returns
    -------
    M_bar : float
        Baryonic mass of the galaxy.

    """
    
    M_gas = 1.4*mhi
    M_bar = M_gas + M_star
    
    return M_bar

