from lib_n_cste import *
from velocities import *
from distances import *
from masses import *
from uncertainties import *
from mag import *

def compu_speeds(Vrad, w20, incl):
    
    cz = Optical_speed(Vrad)
    Vmax = V_max(w20, incl)
    
    return cz, Vmax

def compu_ds(V, logD25):
    
    d = D_Hubble(V)
    R = galaxy_diameter(logD25, V)
    
    return d, R

def compu_mag(bt, Av, d):
    
    btc = mag_btc(bt, Av)
    Lb = MB(btc, d)
    
    return Lb

def compu_masses(d, FHI, Vmax, D, Lb, r_param):
    
    mHI = mass_HI(d, FHI)
    mstars = mass_stars(Lb, d)
    mtot = mass_tot(Vmax, D, r_param)
    mbar = mass_barr(mHI, mstars)
    
    return mHI, mstars, mtot, mbar

def compu_sigmas(w20, w50, FHI, SNR, rms):
    
    stdf = std_FHI(w20, rms)
    stdV = std_Optical_speed(w20, w50, FHI, SNR, rms)
    
    return stdf, stdV

def calc_all(Vrad, FHI, w20, w50, incl, logD25, rms, SNR, bt, Av, r_param):
    
    V, Vmax = compu_speeds(Vrad, w20, incl) 
    d, D = compu_ds(V, logD25)
    Lb = compu_mag(bt, Av, d)
    mHI, mstars, mtot, mbar = compu_masses(d, FHI, Vmax, D, Lb, r_param)
    stdf, stdV = compu_sigmas(w20, w50, FHI, SNR, rms)
    
    log_Lb = np.log10(Lb)
    log_mHI = np.log10(mHI)
    log_mstars = np.log10(mstars)
    log_mtot = np.log10(mtot)
    log_mbar = np.log10(mbar)
    ratio_tot_bar = mtot/mbar
    ratio_DM = (mtot-mbar)/mtot
    
    return V, stdV, stdf, d, log_Lb, log_mstar, log_mHI, log_mbar, Vmax, log_mtot, ratio_tot_bar, ratio_DM
    

def writing(Name, rms, SNR, V, stdV, w50, w20, FHI, stdf, d, log_Lb, log_mstar, log_mHI, log_mbar, Vmax, log_mtot, ratio_tot_bar, ratio_DM, file="./results.csv"):

        f = open(file, '+')
        writer = csv.writer(f)
        writer.writerow([Name, rms, SNR, V, stdV, w50, w20, FHI, stdf, d, log_Lb, log_mstar, log_mHI, log_mbar, Vmax, log_mtot, ratio_tot_bar, ratio_DM])
        f.close()
        
