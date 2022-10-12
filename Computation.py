from main import *

if __name__ == "__main__":
    
    Vrad = input("Vrad km/s")
    FHI = input("FHI Jy.km/s")
    w20 = input("w20 km/s")
    w50 = input("w50 km/s")
    incl = input("incl rad")
    logD25 = input("logD25 log(0.1 \")")
    rms = input("rms mJy")
    SNR = input("SNR")
    
    printing(Vrad, FHI, w20, w50, incl, logD25, rms, SNR)