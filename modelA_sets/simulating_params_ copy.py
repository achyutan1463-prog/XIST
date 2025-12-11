import numpy as np
import random
import json
import sys
p = [0.00013351, 0.018789, 0.0039961, 4.5326, 0.3345, 3.9111, 1.9158, 0.0024741, 2.8627, 1.0, 0.057837, 1.8822, 4.2106, 0.24684, 0.0012156, 3.3417, 1.0, 2.7157, 3.5303, 2.6549, 3.6453, 0.25557, 3.4881, 1.0, 0.2376, 3.1555, 1.6035, 0.012652, 0.07372, 1.3138, 1.0, 1.5378, 2.9105, 0.25415, 0.50957, 0.0013434, 2.9622, 1.2311, 0.069404, 0.00043404, 1.7218, 1.0, 1.9853, 0.49704, 4.471, 0.52095, 0.00013051, 3.0138, 1.0, 4.7112, 0.7894, 2.2847, 0.070764, 0.32431, 2.0286, 1.0, 3.498, 0.41562, 1.6528, 0.48311, 0.0093797, 1.4531, 1.0, 1.3185, 0.0027599, 0.12952, 0.0039027, 0.00060065, 0.16978, 3.5806, 2.5763, 0.00076311, 3.3787, 1.0, 1.5894, 1.4172, 3.8718, 0.20141, 0.00031418, 2.9267, 1.0, 0.50415, 0.90963, 2.2053, 0.10112, 0.0016948, 0.58775, 1.0, 4.4544, 0.0061334, 1.6592, 0.012915, 0.00079311, 1.9982, 1.0, 3.5536, 0.37096, 0.0094823, 0.15254, 0.0023745, 0.33637, 1.0277, 0.081749, 0.065474, 3.4596, 1.0, 0.89276, 0.28027, 4.6703, 0.44474, 0.0013736, 3.4882, 1.0, 3.2371, 3.3626, 2.2435, 0.12495, 0.041854, 0.66967, 1.0, 0.61027, 0.49183, 1.5885, 0.0703, 0.29478, 2.8547, 1.0, 0.99773, 0.00018977, 1.6513, 0.46628, 0.00012331, 2.9855, 4.048, 0.87545, 0.45272, 1.687, 1.0, 2.3418, 0.65068, 4.7245, 0.338, 0.00022933, 0.87469, 1.0, 4.6194, 1.8636, 1.5052, 2.1531, 0.31267, 1.1569, 1.0, 3.8098, 0.22979, 1.6049, 4.3147, 0.01672, 1.9392, 1.0, 3.312, 0.1877, 0.00010148, 0.51701, 0.00014776, 0.76229, 2.0005, 1.5131, 0.69589, 3.376, 1.0, 0.25186, 2.2546, 4.8261, 0.21691, 0.00082397, 1.9139, 1.0, 3.9116, 1.7476, 2.6629, 0.21124, 0.090706, 1.1462, 1.0, 0.2276, 0.00084168, 1.9161, 4.6367, 0.00034001, 1.4766, 1.0, 4.843, 0.66826, 0.032701, 0.31526, 0.00032074, 3.3281, 3.8568, 0.53723, 0.0020838, 2.398, 1.0, 0.50903, 2.6129, 4.6867, 0.31492, 0.001206, 2.2336, 1.0, 3.2094, 0.0029129, 1.2385, 0.23562, 0.0020103, 1.7983, 1.0, 1.6797, 1.4733, 2.7727, 1.2969, 0.8752, 3.269, 1.0, 2.034, 0.002249, 2.6738, 0.28536, 0.00018978, 3.0938, 3.1334, 0.57044, 0.13399, 2.0191, 1.0, 0.22459, 3.8797, 4.833, 0.28734, 0.0012598, 0.76885, 1.0, 4.6649, 2.325, 2.9295, 0.20572, 0.00095221, 1.5622, 1.0, 2.4293, 1.9317, 1.2985, 1.1991, 0.48256, 0.27723, 1.0, 3.2837, 0.00089452, 0.5859, 0.91805, 0.00064024, 4.0076, 3.0014, 0.020223, 0.00055839, 1.3576, 1.0, 1.0716, 0.96122, 4.6711, 0.39319, 0.0013806, 1.123, 1.0, 2.1895, 0.87534, 2.0055, 0.64528, 0.8571, 1.5608, 1.0, 3.0788, 0.050494, 2.5764, 0.60534, 0.0017197, 1.4543, 1.0, 2.9004, 0.0080312, 0.00017256, 0.25534, 0.0066975, 3.6608, 2.9142, 1.6132, 0.021951, 1.177, 1.0, 2.672, 3.5748, 3.4135, 0.22066, 0.00017695, 1.0537, 1.0, 1.1465, 1.5935, 1.525, 6.6778, 0.00038452, 1.2369, 1.0, 0.11506, 4.0404, 2.8197, 1.2949, 0.0016282, 2.3275, 1.0, 0.72037, 0.076283, 4.5284, 1.2071, 2.3289, 1.7988, 2.954, 6.0663, 0.00039558, 1.3551, 1.0, 0.38267, 2.1919, 4.0729, 0.22116, 0.0007724, 2.2308, 1.0, 3.84, 0.91877, 2.9163, 0.037932, 0.018348, 0.31259, 1.0, 0.66254, 0.23436, 2.6773, 1.5224, 0.15391, 0.47882, 1.0, 3.5657, 2.1963, 0.00016289, 0.94366, 0.00058242, 4.589, 4.9338, 0.62053, 0.0030993, 0.81548, 1.0, 2.3605, 2.6142, 3.648, 0.1791, 0.0011131, 3.4293, 1.0, 2.3003, 0.80596, 2.3536, 2.4308, 0.0068626, 0.65497, 1.0, 0.1632, 0.097407, 2.5179, 4.425, 0.0083572, 2.0859, 1.0, 3.7871, 0.0059874, 0.19234, 0.054519, 0.00024666, 0.74071, 1.8466, 3.8224, 0.0011063, 2.179, 1.0, 3.624, 3.69, 4.1935, 0.19948, 0.00028783, 2.4224, 1.0, 0.94057, 2.8883, 1.1399, 7.6925, 0.0083927, 1.2949, 1.0, 0.9889, 0.01878, 2.2274, 0.32372, 0.0077021, 0.5125, 1.0, 1.6434, 0.0077423, 0.0054291, 0.10382, 0.0010488, 1.4152, 1.6289, 0.95735, 0.023905, 1.4708, 1.0, 3.254, 4.349, 3.6291, 0.28466, 0.00038306, 0.79027, 1.0, 3.6054, 0.018234, 1.9197, 0.039695, 0.0028786, 2.1476, 1.0, 4.1196, 0.27011, 2.2467, 8.3221, 0.020752, 2.6687, 1.0, 0.14253, 0.00093533, 4.6422, 0.083051, 0.19359, 1.1294, 4.6305, 2.9559, 0.0019458, 2.9551, 1.0, 3.489, 1.6039, 1.6747, 0.05639, 0.00014768, 1.6326, 1.0, 1.6758, 0.70519, 1.8493, 0.060173, 0.36953, 2.4706, 1.0, 2.3713, 0.12774, 1.5717, 0.11808, 0.0064267, 1.5327, 1.0, 4.2052, 1.289, 3.3276, 0.21176, 0.0054621, 1.7929, 4.4639, 0.82843, 0.00079055, 1.3238, 1.0, 4.5128, 0.3161, 4.6357, 0.52632, 0.0028861, 3.2821, 1.0, 1.6365, 0.17747, 2.902, 8.5744, 0.0031248, 1.699, 1.0, 2.6804, 0.20314, 2.2354, 3.4323, 0.20085, 2.5262, 1.0, 4.6385, 0.3197, 0.022366, 0.022827, 0.38534, 0.82934, 4.1168, 3.2014, 0.0003291, 2.7117, 1.0, 1.7331, 4.6415, 3.6022, 0.13004, 0.00091172, 2.4795, 1.0, 3.3287, 1.4719, 1.9684, 0.34577, 0.50454, 1.9424, 1.0, 1.7497, 0.04807, 2.6716, 7.1311, 0.0090063, 2.1206, 1.0, 4.854, 0.00049913, 0.0097038, 0.47138, 0.0022941, 2.6128, 3.1355, 2.0419, 0.013253, 0.88875, 1.0, 2.5073, 1.0933, 3.4197, 0.16831, 0.00011686, 1.2783, 1.0, 2.3198, 0.0057494, 2.9635, 5.0398, 0.0016574, 2.3588, 1.0, 1.3773, 0.36712, 2.7814, 0.40031, 0.0035811, 2.4038, 1.0, 3.9108, 4.3313, 0.00012998, 0.2195, 0.00071515, 0.71412, 4.6021, 0.39615, 0.064621, 2.9759, 1.0, 3.6563, 0.28627, 3.5443, 0.3674, 0.0029219, 2.443, 1.0, 1.5623, 3.479, 2.0841, 0.86111, 0.44589, 2.9562, 1.0, 0.42585, 0.058769, 1.8461, 0.36844, 0.021931, 3.0721, 1.0, 4.9031, 0.026487, 0.0017948, 0.096425, 0.0002306, 0.27038, 2.9226, 1.1397, 0.10144, 0.9407, 1.0, 3.8662, 2.0934, 3.8448, 0.19706, 0.00199, 1.3072, 1.0, 1.3636, 0.53288, 2.8124, 0.10402, 0.010702, 1.6576, 1.0, 0.63888, 0.12587, 1.9571, 0.61533, 0.00068876, 1.4369, 1.0, 1.6058]
no_intermediates = 10
def sets(p , totalparams): 
   q = []
   a = 0
   b = 32
   for i in range (0,len(p)//totalparams):
    q.append(p[a:b])
    b += 32
    a+=32
   return q

q = sets(p,32)
table = [[None for _ in range(9)] for _ in range(100)]
for set in range (0,len(q)): #loop for each parameter set
 k_fo,k_of = [1,1]
 k_ffr = q[set][2]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# Regulated ON-->OFF (Activator 2)
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]
 K3,n3 = q[set][18:20]
 a = 0.5
 b = 0.5
# Regulated OFF-->OFFrepr (Activator 1)
 #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]

 all_allelicstates = []
 j = 0
 while j < 100:

    #XX
    #the whole gillespie code
    df1 = 1
    df2 = 1
    S1 = [0]    
    S2 = [0]    
    A1_1 = [1]  
    A2_1 = [1]  
    A1_2 = [1]  
    A2_2 = [1]  
    t = [0]     
    I1_1 = [0] 
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    A3_1 = [1]  
    A3_2 = [1]
    tend = 52

    while t[-1] < tend:
        current_A1_1 = A1_1[-1]
        current_A1_2 = A1_2[-1]
        current_S2 = S2[-1]
        current_S1 = S1[-1]
        current_A2_1 = A2_1[-1]
        current_A2_2 = A2_2[-1]
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_A3_1 = A3_1[-1]
        current_A3_2 = A3_2[-1]
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

        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2) / df1
        total_activator3 = (current_A3_1 + current_A3_2) / df1
        k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_2 + current_A2_1) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0) * int(current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1) * int(current_S1==1) * int(current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int (current_A2_1==0) * int(current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1) * int(current_S1==1) * int(current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int (current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0) * int(current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2) * int(current_S2==1) * int(current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0) * int(current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1) * int(current_S2==1) * int(current_I2_2 >= no_intermediates) 

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2 , i1_1 , i2_1, i1_2 , i2_2]

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf')
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        t.append(t[-1] + tau)

        rand = random.uniform(0, 1)
        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        # event - chromosome 2
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
            S1.append(current_S1)
            S2.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
            S1.append(current_S1)
            S2.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
            S1.append(current_S1)
            S2.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
            S1.append(current_S1)
            S2.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        # intermediates
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2 + 1)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2 + i2_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2 + 1)

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    if a == 1 and b == 1: 
            all_allelicstates.append(2)
    elif (a == 1 or b == 1) and not (a == 1 and b == 1):
            all_allelicstates.append(1)
    else:
            all_allelicstates.append(0)
    j += 1
 c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1

 
 table[set][1] = c1
 all_allelicstates = []
 j = 0
 while j < 100:
   #XO
    #the whole gillespie code 
    S1 = [0]    
    A1_1 = [1]  
    A2_1 = [1]  
    A3_1 = [1] 
    t = [0]     
    I1_1 = [0] 
    I2_1 = [0]
    tend = 52
    df1 = 1
    df2 = 1
    while t[-1] < tend:

        current_A1_1 = A1_1[-1]
        current_S1 = S1[-1]
        current_A2_1 = A2_1[-1]
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_A3_1 = A3_1[-1]



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

        # combined hill function , activator 1
        total_activator1 = current_A1_1
        total_activator3 = (current_A3_1) / df1
        k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 

        # combined hill function , activator 2
        total_activator2 = current_A2_1
        k_prod_eff2 = (kA2_max - kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2)) + kA2_min
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0) * int(current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1) * int(current_S1==1) * int(current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int (current_A2_1==0) * int(current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1) * int(current_S1==1) * int(current_I2_1 >= no_intermediates) 

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1, i1_1 , i2_1]

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf')
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        t.append(t[-1] + tau)

        rand = random.uniform(0, 1)
        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)

        # intermediates
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + i1_1:
            S1.append(current_S1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + i1_1 + i2_1:
            S1.append(current_S1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    if a == 1 : 
            all_allelicstates.append(1)
    else:
            all_allelicstates.append(0)
    j += 1
 c1 = c0 = 0
 for row in all_allelicstates:
            if row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1

 table[set][0] = c0
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    # Trisomy
    #the whole gillespie code
                                      
    #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3 
    A1_1 = [1]  # activator1 from chromosome 1
    A2_1 = [1]  # activator2 from chromosome 1
    A1_2 = [1]  # activator1 from chromosome 2
    A2_2 = [1]  # activator2 from chromosome 2
    A1_3 = [1]  # activator1 from chromosome 3
    A2_3 = [1]  # activator2 from chromosome 3
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    A3_1 = [1]  
    A3_2 = [1]
    A3_3 = [1]
    tend = 51
    df1 = 1
    df2 = 1
    while t[-1] < tend:
        current_S1 = S1[-1]
        current_S2 = S2[-1]
        current_S3 = S3[-1] 
        current_A1_1 = A1_1[-1]
        current_A2_1 = A2_1[-1]
        current_A1_2 = A1_2[-1]
        current_A2_2 = A2_2[-1]
        current_A1_3 = A1_3[-1] 
        current_A2_3 = A2_3[-1] 
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        current_A3_3 = A3_3[-1]
        current_A3_1 = A3_1[-1]
        current_A3_2 = A3_2[-1]

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
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3)  /  df1
        total_activator3 = (current_A3_1 + current_A3_2 +current_A3_3) / df1
        k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3)  / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3]
 

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf') # No more reactions possible
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        
        t.append(t[-1] + tau)
        rand = random.uniform(0, 1)

        # Create cumulative sum of rates for event selection
        cumulative_rates = np.cumsum(rates)

        # event - chromosome 1
        if rand * rate_sum <= cumulative_rates[0]:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[1]:
            S1.append(-1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[2]:
            S1.append(1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[3]:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[4]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[5]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[6]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[7]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        # event - chromosome 2
        elif rand * rate_sum <= cumulative_rates[8]:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[9]:
            S1.append(current_S1)
            S2.append(-1)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[10]:
            S1.append(current_S1)
            S2.append(1)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[11]:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[12]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[13]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[14]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[15]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
         # event - chromosome 3
        elif rand * rate_sum <= cumulative_rates[16]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[17]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[18]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[19]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[20]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(1)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[21]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(0)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[22]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[23]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)   

                   #intermediates

        elif rand * rate_sum <= cumulative_rates[24]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[25]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[26]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2 + 1)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[27]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[28]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[29]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3 + 1)
    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    if  a == 1 and b ==1 and c == 1:
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (b == 1 and c == 1) or (a == 1 and c == 1) : 
                all_allelicstates.append(2)
    elif (a == 1 or b == 1 or c == 1) and not (a == 1 and b == 1 and c == 1):
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1

 c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 3:
                c3 += 1
            elif row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1
 c2_trisomy = c2
 table[set][2] = c2
 all_allelicstates = []
 df1 = 1
 df2 = 1 
 j = 0
 while j < 100:
    #tetrasomy
    #the whole gillespie code
                                       
    #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3
    S4 = [0]    # promoter state chromosome 4
    A1_1 = [1]  # activator1 from chromosome 1
    A2_1 = [1]  # activator2 from chromosome 1
    A1_2 = [1]  # activator1 from chromosome 2
    A2_2 = [1]  # activator2 from chromosome 2
    A1_3 = [1]  # activator1 from chromosome 3
    A2_3 = [1]  # activator2 from chromosome 3
    A1_4 = [1]  # activator1 from chromosome 4
    A2_4 = [1]  # activator2 from chromosome 4
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    I1_4 = [0]
    I2_4 = [0]
    tend = 52
    A3_1 = [1]  
    A3_2 = [1]
    A3_3 = [1]  
    A3_4 = [1]

    while t[-1] < tend:
        current_S1 = S1[-1]
        current_S2 = S2[-1]
        current_S3 = S3[-1]
        current_S4 = S4[-1]
        current_A1_1 = A1_1[-1]
        current_A2_1 = A2_1[-1]
        current_A1_2 = A1_2[-1]
        current_A2_2 = A2_2[-1]
        current_A1_3 = A1_3[-1]
        current_A2_3 = A2_3[-1]
        current_A1_4 = A1_4[-1]
        current_A2_4 = A2_4[-1]
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        current_I1_4 = I1_4[-1]
        current_I2_4 = I2_4[-1]
        current_A3_1 = A3_1[-1]
        current_A3_2 = A3_2[-1]
        current_A3_3 = A3_3[-1]
        current_A3_4 = A3_4[-1]  
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
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3 + current_A1_4) / df1
        total_activator3 = (current_A3_1 + current_A3_2+ current_A3_3+ current_A3_4) / df1
        k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min   

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 + current_A2_4) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

        #chromosome 4
        a1_4 = k_frf * int(current_S4 == -1) #off repressed to off
        a2_4 = k_ffr * int(current_S4 == 0) #off to off repressed
        a3_4 = k_prod_eff1 * int(current_S4 == 0) #off to on
        a4_4 = k_prod_eff2 * int(current_S4 == 1) #on to off
        a5_4 = kA1 * int(current_A1_4==0 and current_S4!=1) #activator 1 OFF to ON
        a6_4 = gamma_A1 * int(current_A1_4==1 and current_S4==1 and current_I1_4 >= no_intermediates) #activator 1 ON to OFF
        a7_4 = kA2 * int(current_A2_4==0 and current_S4!=1) #activator2 OFF to ON
        a8_4 = gamma_A2 * int(current_A2_4==1 and current_S4==1 and current_I2_4 >= no_intermediates)  #activator 2  ON to OFF

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
                 a1_4, a2_4, a3_4, a4_4, a5_4, a6_4, a7_4, a8_4,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3, i1_4, i2_4]
 

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf') # No more reactions possible
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        
        t.append(t[-1] + tau)
        rand = random.uniform(0, 1)

        cumulative_rates = np.cumsum(rates)

        # event - chromosome 1
        if rand * rate_sum <= cumulative_rates[0]:
            S1.append(0); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[1]:
            S1.append(-1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[2]:
            S1.append(1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[3]:
            S1.append(0); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[4]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[5]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(0); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[6]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[7]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(0); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        # event - chromosome 2
        elif rand * rate_sum <= cumulative_rates[8]:
            S1.append(current_S1); S2.append(0); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[9]:
            S1.append(current_S1); S2.append(-1); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[10]:
            S1.append(current_S1); S2.append(1); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[11]:
            S1.append(current_S1); S2.append(0); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[12]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(1); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[13]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(0); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[14]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(1)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[15]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(0)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            
        # event - chromosome 3
        elif rand * rate_sum <= cumulative_rates[16]:
            S1.append(current_S1); S2.append(current_S2); S3.append(0); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[17]:
            S1.append(current_S1); S2.append(current_S2); S3.append(-1); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[18]:
            S1.append(current_S1); S2.append(current_S2); S3.append(1); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[19]:
            S1.append(current_S1); S2.append(current_S2); S3.append(0); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[20]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(1); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[21]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(0); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[22]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(1); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[23]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(0); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        # event - chromosome 4
        elif rand * rate_sum <= cumulative_rates[24]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(0)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[25]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(-1)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[26]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(1)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[27]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(0)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[28]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(1); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[29]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(0); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[30]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(1)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[31]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(0)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        #intermediates
        elif rand * rate_sum <= cumulative_rates[32]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1 + 1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[33]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1 + 1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[34]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2 + 1); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[35]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[36]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            
        elif rand * rate_sum <= cumulative_rates[37]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3 + 1); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            
        elif rand * rate_sum <= cumulative_rates[38]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4 + 1); I2_4.append(current_I2_4)
            
        elif rand * rate_sum <= cumulative_rates[39]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4 + 1)

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    d = S4[index]
    if a == 1 and b == 1 and c == 1 and d == 1:
                all_allelicstates.append(4)
    elif (a == 1 and b == 1 and c == 1) or \
                 (a == 1 and b == 1 and d == 1) or \
                 (a == 1 and c == 1 and d == 1) or \
                 (b == 1 and c == 1 and d == 1):
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (a == 1 and c == 1) or (a == 1 and d == 1) or \
                 (b == 1 and c == 1) or (b == 1 and d == 1) or (c == 1 and d == 1):
                all_allelicstates.append(2)
    elif a == 1 or b == 1 or c == 1 or d == 1:
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1

 c4 = c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 4:
                c4 += 1
            elif row == 3:
                c3 += 1
            elif row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1
 c3_tetrasomy = c3
 table[set][3] = c3
 all_allelicstates = []
 j = 0
 while j < 100:
    #tetraploid
    #the whole gillespie code
                                       
    #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3
    S4 = [0]    # promoter state chromosome 4
    A1_1 = [1]  # activator1 from chromosome 1
    A2_1 = [1]  # activator2 from chromosome 1
    A1_2 = [1]  # activator1 from chromosome 2
    A2_2 = [1]  # activator2 from chromosome 2
    A1_3 = [1]  # activator1 from chromosome 3
    A2_3 = [1]  # activator2 from chromosome 3
    A1_4 = [1]  # activator1 from chromosome 4
    A2_4 = [1]  # activator2 from chromosome 4
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    I1_4 = [0]
    I2_4 = [0]
    tend = 52
    df1 = 2
    df2 = 2 
    A3_1 = [1]  
    A3_2 = [1]
    A3_3 = [1]  
    A3_4 = [1]
    while t[-1] < tend:
        current_S1 = S1[-1]
        current_S2 = S2[-1]
        current_S3 = S3[-1]
        current_S4 = S4[-1]
        current_A1_1 = A1_1[-1]
        current_A2_1 = A2_1[-1]
        current_A1_2 = A1_2[-1]
        current_A2_2 = A2_2[-1]
        current_A1_3 = A1_3[-1]
        current_A2_3 = A2_3[-1]
        current_A1_4 = A1_4[-1]
        current_A2_4 = A2_4[-1]
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        current_I1_4 = I1_4[-1]
        current_I2_4 = I2_4[-1]
        current_A3_1 = A3_1[-1]
        current_A3_2 = A3_2[-1]
        current_A3_3 = A3_3[-1]
        current_A3_4 = A3_4[-1]
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
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3 + current_A1_4) / df1
        total_activator3 = (current_A3_1 + current_A3_2+ current_A3_3+ current_A3_4) / df1
        k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 + current_A2_4) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 
        a9_1 = gamma_A3 * int(current_A3_1==1 and current_S1==1 and current_I3_1 >= no_intermediates) 
        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 
        a9_2 = gamma_A3 * int(current_A3_2==1 and current_S1==1 and current_I3_2 >= no_intermediates) 
        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF
        a9_3 = gamma_A3 * int(current_A3_3==1 and current_S1==1 and current_I3_3 >= no_intermediates) 
        #chromosome 4
        a1_4 = k_frf * int(current_S4 == -1) #off repressed to off
        a2_4 = k_ffr * int(current_S4 == 0) #off to off repressed
        a3_4 = k_prod_eff1 * int(current_S4 == 0) #off to on
        a4_4 = k_prod_eff2 * int(current_S4 == 1) #on to off
        a5_4 = kA1 * int(current_A1_4==0 and current_S4!=1) #activator 1 OFF to ON
        a6_4 = gamma_A1 * int(current_A1_4==1 and current_S4==1 and current_I1_4 >= no_intermediates) #activator 1 ON to OFF
        a7_4 = kA2 * int(current_A2_4==0 and current_S4!=1) #activator2 OFF to ON
        a8_4 = gamma_A2 * int(current_A2_4==1 and current_S4==1 and current_I2_4 >= no_intermediates)  #activator 2  ON to OFF
        a9_4 = gamma_A3 * int(current_A3_4==1 and current_S1==1 and current_I3_4 >= no_intermediates) 

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,a9_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,a9_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,a9_3,
                 a1_4, a2_4, a3_4, a4_4, a5_4, a6_4, a7_4, a8_4,a9_4,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3, i1_4, i2_4,]
 

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf') # No more reactions possible
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        
        t.append(t[-1] + tau)
        rand = random.uniform(0, 1)

        cumulative_rates = np.cumsum(rates)

        # event - chromosome 1
        if rand * rate_sum <= cumulative_rates[0]:
            S1.append(0); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[1]:
            S1.append(-1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[2]:
            S1.append(1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[3]:
            S1.append(0); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[4]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[5]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(0); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[6]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[7]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(0); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        # event - chromosome 2
        elif rand * rate_sum <= cumulative_rates[8]:
            S1.append(current_S1); S2.append(0); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[9]:
            S1.append(current_S1); S2.append(-1); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[10]:
            S1.append(current_S1); S2.append(1); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[11]:
            S1.append(current_S1); S2.append(0); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[12]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(1); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[13]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(0); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[14]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(1)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[15]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(0)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            
        # event - chromosome 3
        elif rand * rate_sum <= cumulative_rates[16]:
            S1.append(current_S1); S2.append(current_S2); S3.append(0); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[17]:
            S1.append(current_S1); S2.append(current_S2); S3.append(-1); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[18]:
            S1.append(current_S1); S2.append(current_S2); S3.append(1); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[19]:
            S1.append(current_S1); S2.append(current_S2); S3.append(0); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[20]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(1); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[21]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(0); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[22]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(1); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[23]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(0); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        # event - chromosome 4
        elif rand * rate_sum <= cumulative_rates[24]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(0)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[25]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(-1)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[26]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(1)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[27]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(0)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[28]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(1); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[29]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(0); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[30]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(1)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[31]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(0)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        #intermediates
        elif rand * rate_sum <= cumulative_rates[32]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1 + 1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[33]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1 + 1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[34]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2 + 1); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[35]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= cumulative_rates[36]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            
        elif rand * rate_sum <= cumulative_rates[37]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3 + 1); I1_4.append(current_I1_4); I2_4.append(current_I2_4)
            
        elif rand * rate_sum <= cumulative_rates[38]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4 + 1); I2_4.append(current_I2_4)
            
        elif rand * rate_sum <= cumulative_rates[39]:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4 + 1)

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    d = S4[index]
    if a == 1 and b == 1 and c == 1 and d == 1:
                all_allelicstates.append(4)
    elif (a == 1 and b == 1 and c == 1) or \
                 (a == 1 and b == 1 and d == 1) or \
                 (a == 1 and c == 1 and d == 1) or \
                 (b == 1 and c == 1 and d == 1):
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (a == 1 and c == 1) or (a == 1 and d == 1) or \
                 (b == 1 and c == 1) or (b == 1 and d == 1) or (c == 1 and d == 1):
                all_allelicstates.append(2)
    elif a == 1 or b == 1 or c == 1 or d == 1:
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1

 c4 = c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 4:
                c4 += 1
            elif row == 3:
                c3 += 1
            elif row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1

 table[set][5] = c2
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    # Triploid
    #the whole gillespie code
                                      
    #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3 
    A1_1 = [1]  # activator1 from chromosome 1
    A2_1 = [1]  # activator2 from chromosome 1
    A1_2 = [1]  # activator1 from chromosome 2
    A2_2 = [1]  # activator2 from chromosome 2
    A1_3 = [1]  # activator1 from chromosome 3
    A2_3 = [1]  # activator2 from chromosome 3
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    tend = 51
    df1 = 1.5
    df2 = 1.5
    A3_1 = [1]  
    A3_2 = [1]
    A3_3 = [1]  
    A3_4 = [1]
    while t[-1] < tend:
        current_S1 = S1[-1]
        current_S2 = S2[-1]
        current_S3 = S3[-1] 
        current_A1_1 = A1_1[-1]
        current_A2_1 = A2_1[-1]
        current_A1_2 = A1_2[-1]
        current_A2_2 = A2_2[-1]
        current_A1_3 = A1_3[-1] 
        current_A2_3 = A2_3[-1] 
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        current_A3_1 = A3_1[-1]
        current_A3_2 = A3_2[-1]
        current_A3_3 = A3_3[-1]
        current_A3_4 = A3_4[-1]
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
            
        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3)  /  df1
        total_activator3 = (current_A3_1 + current_A3_2+ current_A3_3) / df1
        k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3)  / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
        a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
        a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
        a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
        a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
        a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
        a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
                 a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
                 a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
                 i1_1, i2_1, i1_2, i2_2, i1_3, i2_3]
 

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf') # No more reactions possible
            t.append(t[-1] + tau)
            break
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        
        t.append(t[-1] + tau)
        rand = random.uniform(0, 1)

        # Create cumulative sum of rates for event selection
        cumulative_rates = np.cumsum(rates)

        # event - chromosome 1
        if rand * rate_sum <= cumulative_rates[0]:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[1]:
            S1.append(-1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[2]:
            S1.append(1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[3]:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[4]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[5]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[6]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[7]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        # event - chromosome 2
        elif rand * rate_sum <= cumulative_rates[8]:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[9]:
            S1.append(current_S1)
            S2.append(-1)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[10]:
            S1.append(current_S1)
            S2.append(1)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[11]:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[12]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[13]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[14]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[15]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
         # event - chromosome 3
        elif rand * rate_sum <= cumulative_rates[16]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[17]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[18]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[19]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[20]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(1)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[21]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(0)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[22]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[23]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)   

                   #intermediates

        elif rand * rate_sum <= cumulative_rates[24]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[25]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[26]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2 + 1)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[27]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[28]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1)
            I2_3.append(current_I2_3)

        elif rand * rate_sum <= cumulative_rates[29]:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3 + 1)
    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    if  a == 1 and b ==1 and c == 1:
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (b == 1 and c == 1) or (a == 1 and c == 1) : 
                all_allelicstates.append(2)
    elif (a == 1 or b == 1 or c == 1) and not (a == 1 and b == 1 and c == 1):
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1

 c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 3:
                c3 += 1
            elif row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1
 table[set][4] = [c2,c1]

                  #XXY triploid
 df1 = 1.5
 df2 = 1.5
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    
    #the whole gillespie code
    S1 = [0]    
    S2 = [0]    
    A1_1 = [1]  
    A2_1 = [1]  
    A1_2 = [1]  
    A2_2 = [1]  
    t = [0]     
    I1_1 = [0] 
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    tend = 52
    A3_1 = [1]  
    A3_2 = [1]

    while t[-1] < tend:
        current_A1_1 = A1_1[-1]
        current_A1_2 = A1_2[-1]
        current_S2 = S2[-1]
        current_S1 = S1[-1]
        current_A2_1 = A2_1[-1]
        current_A2_2 = A2_2[-1]
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_A3_1 = A3_1[-1]
        current_A3_2 = A3_2[-1]
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

        # combined hill function , activator 1
        total_activator1 = (current_A1_1 + current_A1_2) / df1
        total_activator3 = (current_A3_1 + current_A3_2) / df1
        k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_2 + current_A2_1) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_ffr * int(current_S1 == 0) 
        a3_1 = k_prod_eff1 * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0) * int(current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1) * int(current_S1==1) * int(current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int (current_A2_1==0) * int(current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1) * int(current_S1==1) * int(current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int (current_S2 == -1) 
        a2_2 = k_ffr * int(current_S2 == 0) 
        a3_2 = k_prod_eff1 * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0) * int(current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2) * int(current_S2==1) * int(current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0) * int(current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1) * int(current_S2==1) * int(current_I2_2 >= no_intermediates) 

        rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2 , i1_1 , i2_1, i1_2 , i2_2]

        rate_sum = sum(rates)

        # time update
        if rate_sum == 0:
            tau = float('inf')
        else:
            tau = np.random.exponential(scale=1 / rate_sum)
        t.append(t[-1] + tau)

        rand = random.uniform(0, 1)
        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        # event - chromosome 2
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
            S1.append(current_S1)
            S2.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
            S1.append(current_S1)
            S2.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
            S1.append(current_S1)
            S2.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
            S1.append(current_S1)
            S2.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        # intermediates
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1 + 1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1 + 1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2 + 1)
            I2_2.append(current_I2_2)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2 + i2_2:
            S1.append(current_S1)
            S2.append(current_S2)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2 + 1)

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    if a == 1 and b == 1: 
            all_allelicstates.append(2)
    elif (a == 1 or b == 1) and not (a == 1 and b == 1):
            all_allelicstates.append(1)
    else:
            all_allelicstates.append(0)
    j += 1
 c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row == 2:
                c2 += 1
            elif row == 1:
                c1 += 1
            elif row == 0:
                c0 += 1
 table[set][6] = c1
                            ###XXXY tetraploid
 df1 = 2
 df2 = 2
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
        
        #the whole gillespie code
                                        
        #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3 
    A1_1 = [1]  # activator1 from chromosome 1
    A2_1 = [1]  # activator2 from chromosome 1
    A1_2 = [1]  # activator1 from chromosome 2
    A2_2 = [1]  # activator2 from chromosome 2
    A1_3 = [1]  # activator1 from chromosome 3
    A2_3 = [1]  # activator2 from chromosome 3
    t = [0]     # time
    I1_1 = [0] # intermediate levels
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    I1_3 = [0]
    I2_3 = [0]
    tend = 51
    A3_1 = [1]  
    A3_2 = [1]
    A3_3 = [1]
    while t[-1] < tend:
            current_S1 = S1[-1]
            current_S2 = S2[-1]
            current_S3 = S3[-1] 
            current_A1_1 = A1_1[-1]
            current_A2_1 = A2_1[-1]
            current_A1_2 = A1_2[-1]
            current_A2_2 = A2_2[-1]
            current_A1_3 = A1_3[-1] 
            current_A2_3 = A2_3[-1] 
            current_I1_1 = I1_1[-1]
            current_I2_1 = I2_1[-1]
            current_I1_2 = I1_2[-1]
            current_I2_2 = I2_2[-1]
            current_I1_3 = I1_3[-1]
            current_I2_3 = I2_3[-1]
            current_A3_1 = A3_1[-1]
            current_A3_2 = A3_2[-1]     
            current_A3_3 = A3_3[-1]    
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
                
            # combined hill function , activator 1
            total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3)  /  df1
            total_activator3 = (current_A3_1 + current_A3_2+ current_A3_3) / df1
            k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 

            # combined hill function , activator 2
            total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3)  / df2
            k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min
            
            #chromosome 1
            a1_1 = k_frf * int(current_S1 == -1) 
            a2_1 = k_ffr * int(current_S1 == 0) 
            a3_1 = k_prod_eff1 * int(current_S1 == 0) 
            a4_1 = k_prod_eff2 * int(current_S1 == 1) 
            a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
            a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
            a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
            a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

            #chromosome 2
            a1_2 = k_frf * int(current_S2 == -1) 
            a2_2 = k_ffr * int(current_S2 == 0) 
            a3_2 = k_prod_eff1 * int(current_S2 == 0) 
            a4_2 = k_prod_eff2 * int(current_S2 == 1) 
            a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
            a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
            a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
            a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

            #chromosome 3
            a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
            a2_3 = k_ffr * int(current_S3 == 0) #off to off repressed
            a3_3 = k_prod_eff1 * int(current_S3 == 0) #off to on
            a4_3 = k_prod_eff2 * int(current_S3 == 1) #on to off
            a5_3 = kA1 * int(current_A1_3==0 and current_S3!=1) #activator 1 OFF to ON
            a6_3 = gamma_A1 * int(current_A1_3==1 and current_S3==1 and current_I1_3 >= no_intermediates) #activator 1 ON to OFF
            a7_3 = kA2 * int(current_A2_3==0 and current_S3!=1) #activator2 OFF to ON
            a8_3 = gamma_A2 * int(current_A2_3==1 and current_S3==1 and current_I2_3 >= no_intermediates)  #activator 2  ON to OFF

            rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,
                    a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2,
                    a1_3, a2_3, a3_3, a4_3, a5_3, a6_3, a7_3, a8_3,
                    i1_1, i2_1, i1_2, i2_2, i1_3, i2_3]
    

            rate_sum = sum(rates)

            # time update
            if rate_sum == 0:
                tau = float('inf') # No more reactions possible
                t.append(t[-1] + tau)
                break
            else:
                tau = np.random.exponential(scale=1 / rate_sum)
            
            t.append(t[-1] + tau)
            rand = random.uniform(0, 1)

            # event - chromosome 1
            if rand * rate_sum <= a1_1:
                S1.append(0)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1:
                S1.append(-1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
                S1.append(1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
                S1.append(0)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(0)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(0)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            # event - chromosome 2
            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
                S1.append(current_S1)
                S2.append(0)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
                S1.append(current_S1)
                S2.append(-1)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
                S1.append(current_S1)
                S2.append(1)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
                S1.append(current_S1)
                S2.append(0)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(1)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(0)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(1)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(0)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)
            # event - chromosome 3
            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(0)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(-1)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(1)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(0)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(1)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(0)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(1)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(0)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)   

                    #intermediates

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
                a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1 + 1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
                a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1 + 1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
                a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2 + 1)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
                a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2 + 1)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
                a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2 + i1_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3 + 1)
                I2_3.append(current_I2_3)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
                a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
                a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3:
                S1.append(current_S1)
                S2.append(current_S2)
                S3.append(current_S3)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                A1_3.append(current_A1_3)
                A2_3.append(current_A2_3)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)
                I1_3.append(current_I1_3)
                I2_3.append(current_I2_3 + 1)
            

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    c = S3[index]
    if  a == 1 and b ==1 and c == 1:
                all_allelicstates.append(3)
    elif (a == 1 and b == 1) or (b == 1 and c == 1) or (a == 1 and c == 1) : 
                    all_allelicstates.append(2)
    elif (a == 1 or b == 1 or c == 1) and not (a == 1 and b == 1 and c == 1):
                    all_allelicstates.append(1)
    else:
                    all_allelicstates.append(0)
    j += 1

 c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
                if row == 3:
                    c3 += 1
                elif row == 2:
                    c2 += 1
                elif row == 1:
                    c1 += 1
                elif row == 0:
                    c0 += 1
 table[set][7] = c1
    
        ###XXYY tetraploid

 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
        
        #the whole gillespie code
    S1 = [0]    
    S2 = [0]    
    A1_1 = [1]  
    A2_1 = [1]  
    A1_2 = [1]  
    A2_2 = [1]  
    t = [0]     
    I1_1 = [0] 
    I2_1 = [0]
    I1_2 = [0]
    I2_2 = [0]
    tend = 52
    df1 = 2
    df2 = 2
    A3_1 = [1]  
    A3_2 = [1]
    while t[-1] < tend:
            current_A1_1 = A1_1[-1]
            current_A1_2 = A1_2[-1]
            current_S2 = S2[-1]
            current_S1 = S1[-1]
            current_A2_1 = A2_1[-1]
            current_A2_2 = A2_2[-1]
            current_I1_1 = I1_1[-1]
            current_I2_1 = I2_1[-1]
            current_I1_2 = I1_2[-1]
            current_I2_2 = I2_2[-1]
            current_A3_1 = A3_1[-1]
            current_A3_2 = A3_2[-1]
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

            # combined hill function , activator 1
            total_activator1 = (current_A1_1 + current_A1_2) / df1
            total_activator3 = (current_A3_1 + current_A3_2) / df1
            k_prod_eff1 = (kA1_max-kA1_min) * (a*(total_activator1**n1 / ((K1**n1) + (total_activator1**n1))) + b * (total_activator3**n3) / (K3**n3 + total_activator3**n3))  + kA1_min 

            # combined hill function , activator 2
            total_activator2 = (current_A2_2 + current_A2_1) / df2
            k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
            
            #chromosome 1
            a1_1 = k_frf * int(current_S1 == -1) 
            a2_1 = k_ffr * int(current_S1 == 0) 
            a3_1 = k_prod_eff1 * int(current_S1 == 0) 
            a4_1 = k_prod_eff2 * int(current_S1 == 1) 
            a5_1 = kA1 * int(current_A1_1==0) * int(current_S1!=1)
            a6_1 = gamma_A1 * int(current_A1_1==1) * int(current_S1==1) * int(current_I1_1 >= no_intermediates)
            a7_1 = kA2 * int (current_A2_1==0) * int(current_S1!=1) 
            a8_1 = gamma_A2 * int(current_A2_1==1) * int(current_S1==1) * int(current_I2_1 >= no_intermediates) 

            #chromosome 2
            a1_2 = k_frf * int (current_S2 == -1) 
            a2_2 = k_ffr * int(current_S2 == 0) 
            a3_2 = k_prod_eff1 * int(current_S2 == 0) 
            a4_2 = k_prod_eff2 * int(current_S2 == 1) 
            a5_2 = kA1 * int(current_A1_2==0) * int(current_S2!=1) 
            a6_2 = gamma_A1 * int(current_A1_2) * int(current_S2==1) * int(current_I1_2 >= no_intermediates) 
            a7_2 = kA2 * int(current_A2_2==0) * int(current_S2!=1) 
            a8_2 = gamma_A2 * int(current_A2_2==1) * int(current_S2==1) * int(current_I2_2 >= no_intermediates) 

            rates = [a1_1, a2_1, a3_1, a4_1, a5_1, a6_1, a7_1, a8_1,a1_2, a2_2, a3_2, a4_2, a5_2, a6_2, a7_2, a8_2 , i1_1 , i2_1, i1_2 , i2_2]

            rate_sum = sum(rates)

            # time update
            if rate_sum == 0:
                tau = float('inf')
            else:
                tau = np.random.exponential(scale=1 / rate_sum)
            t.append(t[-1] + tau)

            rand = random.uniform(0, 1)
            # event - chromosome 1
            if rand * rate_sum <= a1_1:
                S1.append(0)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1:
                S1.append(-1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
                S1.append(1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
                S1.append(0)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(0)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(0)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            # event - chromosome 2
            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
                S1.append(current_S1)
                S2.append(0)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
                S1.append(current_S1)
                S2.append(-1)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
                S1.append(current_S1)
                S2.append(1)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
                S1.append(current_S1)
                S2.append(0)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(1)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(0)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(1)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(0)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            # intermediates
            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1 + 1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1 + 1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2 + 1)
                I2_2.append(current_I2_2)

            elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + i1_1 + i2_1 + i1_2 + i2_2:
                S1.append(current_S1)
                S2.append(current_S2)
                A1_1.append(current_A1_1)
                A2_1.append(current_A2_1)
                A1_2.append(current_A1_2)
                A2_2.append(current_A2_2)
                I1_1.append(current_I1_1)
                I2_1.append(current_I2_1)
                I1_2.append(current_I1_2)
                I2_2.append(current_I2_2 + 1)

    index = np.searchsorted(t,50,side = 'right') - 1
    a = S1[index]
    b = S2[index]
    if a == 1 and b == 1: 
                all_allelicstates.append(2)
    elif (a == 1 or b == 1) and not (a == 1 and b == 1):
                all_allelicstates.append(1)
    else:
                all_allelicstates.append(0)
    j += 1
 c2 = c1 = c0 = 0
 for row in all_allelicstates:
                if row == 2:
                    c2 += 1
                elif row == 1:
                    c1 += 1
                elif row == 0:
                    c0 += 1
 table[set][8] = c0

    
print(table)