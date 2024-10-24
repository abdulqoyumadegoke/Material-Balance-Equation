from volume_replaced import *
from volume_produced import *
from material_balance import *

if __name__ == "__main__":
    # Sample values for testing
    Np = 700000  # Cumulative oil produced
    Rp = 3000    # Produced GOR
    Rs = 600     # Solution GOR
    Bo = 1.3     # Oil FVF
    Bg = 0.005   # Gas FVF
    Wp = 100000  # Water produced
    Bw = 1.02    # Water FVF
    We = 50000   # Aquifer water influx
    Wi = 20000   # Initial water in place
    Gi = 100000  # Initial gas cap volume
    m = 0.1      # Gas cap volume to oil volume ratio
    N = 800000   # Original oil in place (guess for now)
    Vp = 150000  # Pore volume
    Cf = 0.00001 # Formation compressibility
    Swc = 0.25   # Connate water saturation
    Cw = 0.00005 # Water compressibility
    delta_P = 500  # Pressure difference
    Rsi = 800     # Initial solution GOR
    Boi = 1.1     # Initial oil FVF
    
    total_volume_produced, total_volume_replaced = material_balance(Np, Rp, Rs, Bo, Bg, Wp, Bw, We, Wi, Gi, m, N, Vp, Cf, Swc, Cw, delta_P, Rsi, Boi)
    print(f"Total Volume Produced: {total_volume_produced} RB")
    print(f"Total Volume Replaced: {total_volume_replaced} RB")