class conversions:
    def SENStoRPM(gearRatio: float, sENS: float):
        sENS*=100
        rpmUnFixed = sENS/2048
        rpmFixed = rpmUnFixed*gearRatio
        return rpmFixed
    
        