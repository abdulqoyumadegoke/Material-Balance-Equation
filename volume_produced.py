#material balance equation 
def gas_prod(Np,Rp,Rs,Bg):
    """
    Np: Cumulative Oil production
    Rp: Cumulative produced GOR
    Rs: Solution GOR at reservoir condition
    Bg: Gas FVF
    """
    gp=Np*((Rp-Rs)*Bg)
    return gp
def oil_prod(Np,Bo):
    """
    Np: Cumulative oil produced
    Bo: oil FVF
    """
    op= (Np*Bo)
    return op
def water_production(Wp,Bw):
    """
    Wp: Water Produced
    Bw: water FVF
    """
    wp= (Wp*Bw)
    return wp
