from main import *

if __name__ == "__main__":
    
    Vrad =float(input("Vrad km/s : "))
    FHI = float(input("FHI Jy.km/s : "))
    w20 = float(input("w20 km/s : "))
    w50 = float(input("w50 km/s : "))
    incl = float(input("incl rad : "))
    logD25 = float(input("logD25 log(0.1 \") : "))
    rms = float(input("rms mJy : "))
    SNR = float(input("SNR : "))
    btc = float(input("BTC mag : "))
    
    printing(Vrad, FHI, w20, w50, incl, logD25, rms, SNR, btc)
