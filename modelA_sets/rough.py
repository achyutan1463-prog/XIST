    A3_1 = [1]  
    A3_2 = [1]
    current_A3_1 = A3_1[-1]
    current_A3_2 = A3_2[-1]
    K3,n3 = q[set][18:20]
    total_activator3 = (current_A3_1 + current_A3_2) / df1
    k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 
        a9_1 = gamma_A3 * int(current_A3_1==1 and current_S1==1 and current_I3_1 >= no_intermediates) 
        a9_2 = gamma_A3 * int(current_A3_2==1 and current_S1==1 and current_I3_2 >= no_intermediates) 
        a9_3 = gamma_A3 * int(current_A3_3==1 and current_S1==1 and current_I3_3 >= no_intermediates) 
        a9_4 = gamma_A3 * int(current_A3_4==1 and current_S1==1 and current_I3_4 >= no_intermediates) 
       
        # for I1_1
        if I1_1[-1] < no_intermediates:
            i1_1 = ksA1 * int(current_S1 == 1)
        else:
            i1_1 = 0

        # for I2_1
        if I2_1[-1] < no_intermediates:
            i2_1 = ksA2 * int(current_S1 == 1)
        else:
            i2_1 = 0
        # for I3_1
        if I3_1[-1] < no_intermediates:
            i3_1 = ksA3 * int(current_S1 == 1)
        else:
            i3_1 = 0
            
        # for I1_2
        if I1_2[-1] < no_intermediates:
            i1_2 = ksA1 * int(current_S2 == 1)
        else:
            i1_2 = 0

        #  for I2_2
        if I2_2[-1] < no_intermediates:
            i2_2 = ksA2 * int(current_S2 == 1)
        else:
            i2_2 = 0   

        # for I3_2
        if I3_2[-1] < no_intermediates:
            i3_2 = ksA3 * int(current_S2 == 1)
        else:
            i3_2 = 0

       # for I1_3
        if I1_3[-1] < no_intermediates:
            i1_3 = ksA1 * int(current_S3 == 1)
        else:
            i1_3 = 0

        #  for I2_3
        if I2_3[-1] < no_intermediates:
            i2_3 = ksA2 * int(current_S3 == 1)
        else:
            i2_3 = 0

        # for I3_3
        if I3_3[-1] < no_intermediates:
            i3_3 = ksA3 * int(current_S3 == 1)
        else:
            i3_3 = 0

        # for I1_4
        if I1_4[-1] < no_intermediates:
            i1_4 = ksA1 * int(current_S4 == 1)
        else:
            i1_4 = 0
            
        #  for I2_4
        if I2_4[-1] < no_intermediates:
            i2_4 = ksA2 * int(current_S4 == 1)
        else:
            i2_4 = 0
        # for I3_4
        if I3_4[-1] < no_intermediates:
            i3_4 = ksA3 * int(current_S4 == 1)
        else:
            i3_4 = 0

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,a9_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,a9_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,a9_3,
                 a1_4, a2_4, a3_4, a4_4, a5_4, a6_4, a7_4, a8_4,a9_4,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3, i1_4, i2_4,]
#changes in if statements 
#silencing of A3 by x.
import numpy as np
import matplotlib.pyplot as plt

def hill(x, K, n):
    return x**n / (K**n + x**n)

# Parameters
K_A, n_A = 1.0, 2
K_B, n_B = 1.0, 2
k_min, k_max = 0.1, 1.0

# Activator A kinetics
kA_min = 0.0
kA_max = 2.0
delta_A = 1.0

# Inputs
kA_prod = np.linspace(0, 5, 500)  # x-axis now
B_const = 1.0

# A steady state
A_ss = (kA_min + kA_prod) / delta_A

# Hill terms
H_A = hill(A_ss, K_A, n_A)
H_B = hill(B_const, K_B, n_B)

# OR logic
H_OR = 1 - (1 - H_A) * (1 - H_B)

# Production rate
rate = k_min + (k_max - k_min) * H_OR

# Plot
plt.plot(kA_prod, rate, label="OR (with activator degradation)")
plt.xlabel("Activator A production rate")
plt.ylabel("Reaction rate")
plt.legend()
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Hill function with kmax and kmin
def hill(A, K, n, kmin=0, kmax=1):
    """
    Hill activation function with min and max levels.
    A: activator concentration
    K: Hill constant
    n: Hill coefficient
    kmin: minimum activation (basal)
    kmax: maximum activation
    """
    return kmin + (kmax - kmin) * (A**n / (K**n + A**n))

# Parameters
Kx = 1.0      # X -> Z Hill constant
Ky = 1.0      # Y -> Z Hill constant
Kxy = 1.0     # X -> Y Hill constant
n = 2         # Hill coefficient
kmin = 0.1    # minimum activation
kmax = 0.9    # maximum activation

# Activator concentration
X = np.linspace(0, 10, 500)

# Y is activated by X
Y = hill(X, Kxy, n, kmin=0, kmax=1)  # Y min=0, max=1 for simplicity

# Z activation via OR logic with kmin/kmax
fX = hill(X, Kx, n, kmin=kmin, kmax=kmax)
fY = hill(Y, Ky, n, kmin=kmin, kmax=kmax)
Z = 1 - (1 - fX)*(1 - fY)  # OR logic

# Plot
plt.figure(figsize=(6,4))
plt.plot(X, Z, label='Z activation (OR FFL with kmin/kmax)')
plt.xlabel('Activator X concentration')
plt.ylabel('Z activation rate')
plt.title('Feedforward Loop (X->Y->Z) - OR logic')
plt.legend()
plt.grid(True)
plt.show()



