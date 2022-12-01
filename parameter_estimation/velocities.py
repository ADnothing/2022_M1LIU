from lib_n_cste import *


def Optical_speed(Vrad):
    """
    Compute the optical speed of a source given its mean radial velocity.
    
    Parameters
    ----------
    Vrad : float
        The mean radial speed mesured of a source in km/s.

    Returns
    -------
    cz : float
        The optical speed of the source in km/s.
    """
    
    a = 1/Vrad
    b = 1/(c_light)
    
    cz = 1/(a-b)
    
    return cz


def V_max(w20, incl):
    """
    Compute the maximum of the rotation speed of the galaxy.

    Parameters
    ----------
    w20 : float
        The width of the signal at 20% maximum in km/s.
    incl : float
        The inclination of the galaxy in rad.

    Returns
    -------
    Vmax : float
        The maximum of the rotation speed of the galaxy in km/s.
    """
    
    Vmax = w20/(2*np.sin(incl))
    
    return Vmax
