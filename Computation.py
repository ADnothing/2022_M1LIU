from main import *

if __name__ == "__main__":
    
    Name = input("Name of the galaxy : ")
    Vrad = float(input("Vrad km/s : "))
    FHI = float(input("FHI Jy.km/s : "))
    w20 = float(input("w20 km/s : "))
    w50 = float(input("w50 km/s : "))
    incl = float(input("incl rad : "))
    logD25 = float(input("logD25 log(0.1 \") : "))
    rms = float(input("rms mJy : "))
    SNR = float(input("SNR : "))
    bt = float(input("BT mag : "))
    Av = float(input("AV mag : "))
    gtb = input("HSB or LSB ? : ")
    
    if(gtb == "LSB"):
        r_param = 2.5
    else:
        r_param = 1.6
    
    V, stdV, stdf, d, log_Lb, log_mstar, log_mHI, log_mbar, Vmax, log_mtot, ratio_tot_bar, ratio_DM = calc_all(Vrad, FHI, w20, w50, incl, logD25, rms, SNR, bt, Av, r_param)
   
    writing(Name, rms, SNR, V, stdV, w50, w20, FHI, stdf, d, log_Lb, log_mstar, log_mHI, log_mbar, Vmax, log_mtot, ratio_tot_bar, ratio_DM)