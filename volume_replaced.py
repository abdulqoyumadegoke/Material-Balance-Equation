def oil_exp(N,Bo,Boi,Rsi,Rs,Bg):
    """
    N: Original oil in place
    Bo: Oil FVF
    Boi: Oil FVF at current reservoir cond
    Rsi: Solution GOR
    Rs: Solution GOR at initial reservoir cond
    Bg: Gas FVF
    """
    eo = N*((Bo - Boi) + (Rsi - Rs)*Bg)
    return eo
def rc_exp(Vp,Cf,Swc,Cw,delta_P,m,N,Boi):
    """
    Vp: pore volume
    Cf: formation compresibility
    Swc: connate water saturation
    Cw: water compresibility
    delta_P: Pressure change
    m: gas cap volume to initial oil vol
    """
    rc= N*((1+m)*Boi*((Cf + Swc*Cw)/(1-Swc))*delta_P)
    return rc
def ii_exp(m,N,Boi,Bg,Bo):
    ie= m*N*Boi*((Bg/Boi)-1)
    return ie
def aquifer(We,Wi,Bw,Gi,Bg):
    """
    Aquifer Influx
    We: Water Influx
    Wi: Initial Water
    Bw: Water FVF
    Gi: Initial gas cap volume
    Bg: Gas FVF
    """
    aq= We + (Wi*Bw) + (Gi *Bg)
    return aq