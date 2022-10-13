from lib_n_cste import *

def D_Hubble(V, h=H0):
    """
    Compute the distance of a galaxy by the Hubble law.

    Parameters
    ----------
    V : float
        The speed of the galaxy in km/s.
    h : float, optional
        Hubble constant in s/km/Mpc. The default is H0.

    Returns
    -------
    d : float
        The distance of the galaxy in Mpc.

    """
    
    d = V/h
    
    return d


#def Tully_fisher():


def galaxy_radius(logD25, V):
    """
    Compute the radius of a galaxy.

    Parameters
    ----------
    logD25 : float
        Apparent radius of the galaxy in log(0.1["]).
    Vrad : float
        The speed of the galaxy in km/s.

    Returns
    -------
    D : float
        The diameter of the galaxy in kpc.

    """
    
    D25 = 10**(logR25 + 1)      #arcsec
    D25_rad = D25*np.pi/648000  #rad
    
    D = D_Hubble(V)
    
    D = D25*D*1e3
    
    
    return D