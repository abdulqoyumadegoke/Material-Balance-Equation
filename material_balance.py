from volume_produced import *
from volume_replaced import *
def material_balance(Np, Rp, Rs, Bo, Bg, Wp, Bw, We, Wi, Gi, m, N, Vp, Cf, Swc, Cw, delta_P, Rsi, Boi):
    """
    Np: Cumulative oil production
    Rp: Produced GOR
    Rs: Solution GOR
    Bo: Oil FVF
    Bg: Gas FVF
    Wp: Water produced
    Bw: Water FVF
    We: Water influx from aquifer
    Wi: Initial water in place
    Gi: Initial gas cap volume
    m: Gas cap to oil volume ratio
    N: Oil in place (this will be estimated)
    Vp: Pore volume
    Cf: Formation compressibility
    Swc: Connate water saturation
    Cw: Water compressibility
    delta_P: Pressure difference (Pi - Pf)
    Rsi: Solution gas-oil ratio (initial)
    Boi: Oil FVF at initial conditions
    """
    
    # Volume Produced
    gp = gas_prod(Np, Rp, Rs, Bg)
    op = oil_prod(Np, Bo)
    wp = water_production(Wp, Bw)
    total_volume_produced = gp + op + wp

    #Volume replaced 
    eo = oil_exp(N, Bo, Boi, Rsi, Rs, Bg)
    rc = rc_exp(Vp, Cf, Swc, Cw, delta_P, m, N, Boi)
    ie = ii_exp(m, N, Boi, Bg, Bo)
    aq = aquifer(We, Wi, Bw, Gi, Bg)
    total_volume_replaced = eo + rc + ie + aq

    if total_volume_produced == total_volume_replaced:
        print(f"Material Balance holds, OOIP (N) estimated: {N} RB")
    else:
        print(f"Material Balance not holds, please check your input")
    return total_volume_produced, total_volume_replaced
