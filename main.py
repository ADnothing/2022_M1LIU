from lib_n_cste import *
from speeds import *
from distances import *
from masses import *
from sig_noise import *
from uncertainties import *

def compu_speeds(Vrad, w20, incl):
    
    cz = Optical_speed(Vrad)
    Vmax = V_max(w20, incl)
    
    return cz, Vmax

def compu_ds(V, logD25):
    
    d = D_Hubble(V)
    R = galaxy_radius(logD25, V)
    
    return d, R

def compu_masses(d, FHI, Vmax, D):
    
    mHI = mass_HI(d, FHI)
    mstars = mass_stars(btc, d)
    mtot = mass_tot(Vmax, D)
    
    return mHI, mstars, mtot

def compu_sigmas(w20, w50, FHI, SNR, rms):
    
    stdf = std_FHI(w20, rms)
    stdV = std_Optical_speed(w20, w50, FHI, SNR, rms)
    
    return stdf, stdV

def printing(Vrad, FHI, w20, w50, incl, logD25, rms, SNR):
    
    V, Vmax = compu_speeds(Vrad, w20, incl)
    print("V = %f km/s\nVmax = %f km/s"%(V, Vmax))
    
    d, D = compu_ds(V, logD25)
    print("d = %f Mpc\nD = %f kpc"%(d, D))
    
    MB = btc - 5*np.log10(d) - 5
    print("MB = %f mag"%(MB))
    
    mHI, mstars, mtot = compu_masses(d, FHI, Vmax, D)
    print("MHI = %f Msun\nMstars = %f Msun\nMtot = %f Msun"%(mHI, mstars, mtot))
    
    S_R = S_N(w50, FHI, rms)
    print("S/N = %f"%(S_R))
    
    stdf, stdV = compu_sigmas(w20, w50, FHI, SNR, rms)
    print("sigma_V = %f km/s\•n sigma_FHI = %f Jy.km/s"%(stdV, stdf))