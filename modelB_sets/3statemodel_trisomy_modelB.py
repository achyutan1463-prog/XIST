# % of cells graph for 3 state model , trisomy ( #XXX , 2n)
import numpy as np
import matplotlib.pyplot as plt
import random

p=[4.1925,0.14507,0.00014455,0.00053578,0.10547,1.283,0.12301,0.033074,2.7092,1.0,0.33068,0.38819,2.7582,0.20742,0.0051363,2.3129,1.0,3.085,3.7459,2.1186,0.16913,0.48946,3.0088,1.0,0.85446,0.0038295,2.256,1.4807,0.00031943,1.7151,1.0,2.5484
,3.2033,0.073563,0.0017264,0.00035754,0.70188,2.1618,5.5639,0.49072,2.5657,1.0,0.13261,0.25229,1.1139,0.014706,0.0097795,2.9101,1.0,3.7218,4.9294,1.0999,0.030877,0.0027393,2.8527,1.0,0.3347,0.63333,2.7322,0.037694,0.49946,0.34172,1.0,3.4678
,1.3955,0.37839,0.48667,0.00019426,3.4285,1.5007,3.3939,0.041705,2.2023,1.0,3.3804,0.096881,2.0373,0.063372,0.00036323,3.1737,1.0,2.8468,4.9822,1.0505,0.019376,0.14383,2.6491,1.0,2.1015,0.001491,1.4484,0.011814,0.00031586,1.1992,1.0,1.9094
,2.7662,0.00025164,0.02267,0.00040469,4.0371,1.9437,0.9916,0.15715,0.47752,1.0,2.3064,2.4277,2.8623,0.011025,0.00078184,2.5043,1.0,2.2939,1.1767,1.5307,1.952,0.37355,2.7792,1.0,3.1015,1.8544,1.4109,0.55555,0.0063229,3.4145,1.0,0.76804
,0.70304,0.3026,2.5994,0.00017269,0.89501,1.1313,0.91953,0.00075966,0.52039,1.0,1.6381,0.29562,2.5255,0.17473,0.00010456,1.7393,1.0,1.99,2.4785,1.6521,0.022172,0.092982,2.1452,1.0,0.094566,0.21396,1.7376,0.48586,0.09169,2.1007,1.0,3.1381
,3.2068,0.00051638,3.3342,0.00025351,2.627,1.2165,7.4705,0.00015847,2.4344,1.0,0.3317,0.41144,2.988,0.088921,0.00079543,1.4235,1.0,2.7879,3.3392,2.7564,0.22341,0.79301,2.896,1.0,0.16424,0.11623,1.9839,0.010014,0.045596,0.52656,1.0,4.0676
,0.61693,0.025149,4.166,0.00044246,0.57913,1.7357,0.27488,0.41827,1.9925,1.0,1.2043,0.22318,2.0661,0.04538,0.012831,3.4252,1.0,3.0427,2.8288,2.8779,0.48658,0.00034278,1.7803,1.0,2.7036,0.098902,2.0807,0.023481,0.0027137,1.3206,1.0,3.9578
,0.34088,0.00017706,0.013367,0.00089765,0.004227,2.615,0.012768,0.0030863,3.4154,1.0,4.159,0.25147,1.4289,0.03101,0.0092764,1.481,1.0,1.317,3.8616,2.3301,0.011246,0.00057479,3.0224,1.0,1.6392,0.55319,2.4428,0.116,0.15614,1.8252,1.0,4.9242
,0.31003,0.00010208,0.24234,0.00056594,0.0011454,1.6284,3.2122,0.00039133,2.3884,1.0,0.74971,0.23851,2.4766,0.0307,0.00069937,2.0476,1.0,4.4136,0.42987,1.1014,1.0,0.0063234,2.4509,1.0,1.8002,3.3472,2.1291,2.7365,0.025627,2.6024,1.0,2.9897
,3.8152,0.012039,0.095881,0.00017349,0.40684,1.3949,0.24964,0.00013054,3.4514,1.0,1.4843,0.24373,2.3007,0.077571,0.0065723,2.1908,1.0,2.5974,4.8386,1.0737,0.30819,0.0058338,1.4546,1.0,1.3469,1.793,2.8394,0.087069,0.0012613,3.0204,1.0,2.998
,0.10978,0.0069715,0.0063204,0.00051119,0.20086,2.7655,0.23315,0.00053838,2.9303,1.0,1.0652,0.47686,1.4232,0.017582,0.00091232,3.4395,1.0,2.0198,1.5498,2.4227,0.40745,0.00012088,2.9965,1.0,4.249,0.67367,1.2315,1.9438,0.043384,0.54556,1.0,1.673
,2.5472,0.00039295,0.00056781,0.0015791,0.017575,1.3032,0.018449,0.01067,2.798,1.0,2.275,0.56177,1.4654,0.039857,0.00020697,1.7462,1.0,4.0172,4.8039,1.3314,0.040242,0.034989,3.0589,1.0,3.8337,0.69889,2.5646,0.60299,0.36539,1.2471,1.0,2.3697
,0.08289,0.016404,3.764,0.00061151,0.045567,1.6927,0.079792,0.043301,0.4604,1.0,4.066,0.14832,1.2359,0.031933,0.001868,1.3898,1.0,1.6109,3.1835,2.9278,0.32546,0.0004445,2.1217,1.0,2.8392,3.4828,2.2759,3.2107,0.012334,2.4394,1.0,2.0707
,3.4549,0.042647,0.37237,0.0011908,0.041798,2.6438,0.03606,0.041619,0.83912,1.0,0.65842,0.37795,2.7702,0.087376,0.003458,3.3164,1.0,1.8464,2.7913,2.8241,0.46948,0.021498,3.167,1.0,2.4343,0.0046167,2.4941,0.134,0.0035367,2.0081,1.0,2.6453
,1.7388,0.010728,0.0081859,0.00064405,3.0493,2.1866,0.090593,0.0014322,0.50042,1.0,1.0103,0.44052,1.4625,0.022099,0.0059039,3.4929,1.0,2.9583,0.77326,2.1246,0.10175,0.18247,2.7614,1.0,0.17149,0.53468,1.462,0.08526,0.00081043,0.37958,1.0,4.2618
,1.6197,0.020392,0.19648,0.00031024,0.76069,2.9391,0.16734,0.035514,1.867,1.0,0.85811,0.68914,1.8626,0.010407,0.00018733,2.8798,1.0,2.9386,2.4012,2.9342,0.93486,0.00018056,2.2853,1.0,1.8062,0.48325,1.3003,0.052844,0.3267,3.0691,1.0,1.274
,0.1546,0.0032021,0.32886,0.0010653,0.83722,1.2612,1.0337,0.013594,3.3604,1.0,3.3547,1.0275,2.8584,0.018839,0.0030334,3.1968,1.0,2.301,0.48341,2.9982,0.91447,0.00010071,2.0794,1.0,3.1227,2.9485,1.6033,0.33762,0.0070348,1.3197,1.0,4.2641
,0.57464,0.43731,0.00012528,0.0054499,0.018819,1.8084,0.026222,0.0035646,2.8152,1.0,0.76274,0.27273,2.703,0.19949,0.00096916,2.0206,1.0,4.8017,3.4169,2.1918,0.5036,0.0007547,2.0111,1.0,0.47064,0.1608,2.3703,4.6312,0.007163,3.3162,1.0,0.23649
,2.8209,0.43545,0.00019553,0.00011994,2.8528,1.7361,0.53207,0.20258,3.2127,1.0,2.2528,0.28483,2.8648,0.027789,0.00021961,1.6853,1.0,1.2906,1.4154,2.4081,1.0346,0.061898,1.8683,1.0,0.79508,2.8491,2.1097,0.017743,0.21478,2.3766,1.0,1.1924
,1.5662,0.00013496,2.7311,0.0006002,0.0023146,2.4488,4.2419,0.00089389,0.52764,1.0,1.0267,0.27078,1.1205,0.01407,0.00034978,3.3274,1.0,1.5023,2.2292,1.8204,0.97018,0.00016804,2.8932,1.0,3.1819,0.0015483,1.7122,0.028029,0.00030129,3.2963,1.0,2.1587]

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
states_50=states_100=states_150=states_200=states_250=states_300 = []
for set in range (0,2): #loop for each parameter set

 k_fo, k_of, k_ffr, k_frf = q[set][0:4]

 #activator 1
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][4:11]

 #activator 2
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]
 df1 = 1
 df2 = 1
 no_intermediates = 10
 counts_4 = []
 counts_3 = []
 counts_2 = []
 counts_1 = []
 counts_0 = []
 all_allelicstates = []
 j = 0
 while j < 100:
    
    #the whole gillespie code
                                       
    #Initial states
    S1 = [0]    # promoter state chromosome 1
    S2 = [0]    # promoter state chromosome 2
    S3 = [0]    # promoter state chromosome 3 (Added for consistency)
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
    tend = 100
    
    while t[-1] < tend:
        current_S1 = S1[-1]
        current_S2 = S2[-1]
        current_S3 = S3[-1] # Added for consistency
        current_A1_1 = A1_1[-1]
        current_A2_1 = A2_1[-1]
        current_A1_2 = A1_2[-1]
        current_A2_2 = A2_2[-1]
        current_A1_3 = A1_3[-1] # Corrected from A2_1
        current_A2_3 = A2_3[-1] # Corrected from A2_2
        current_I1_1 = I1_1[-1]
        current_I2_1 = I2_1[-1]
        current_I1_2 = I1_2[-1]
        current_I2_2 = I2_2[-1]
        current_I1_3 = I1_3[-1]
        current_I2_3 = I2_3[-1]
        
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
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3 ) / df1
        k_prod_eff1 = ((kA1_max-kA1_min) * k_ffr * (K1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 ) / df2
        k_prod_eff2 = ((kA1_max-kA1_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA1_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_prod_eff1 * int(current_S1 == 0) 
        a3_1 = k_fo * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

        #chromosome 2
        a1_2 = k_frf * int(current_S2 == -1) 
        a2_2 = k_prod_eff1 * int(current_S2 == 0) 
        a3_2 = k_fo * int(current_S2 == 0) 
        a4_2 = k_prod_eff2 * int(current_S2 == 1) 
        a5_2 = kA1 * int(current_A1_2==0 and current_S2!=1) 
        a6_2 = gamma_A1 * int(current_A1_2==1 and current_S2==1 and current_I1_2 >= no_intermediates) 
        a7_2 = kA2 * int(current_A2_2==0 and current_S2!=1) 
        a8_2 = gamma_A2 * int(current_A2_2==1 and current_S2==1 and current_I2_2 >= no_intermediates) 

        #chromosome 3
        a1_3 = k_frf * int(current_S3 == -1) #off repressed to off
        a2_3 = k_prod_eff1 * int(current_S3 == 0) #off to off repressed
        a3_3 = k_fo * int(current_S3 == 0) #off to on
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
        

    allelic_state = []
   
    for i in np.arange(0,101,0.2): # timesteps  - gives a single pair of lists that tell S values at each time step
        index = np.searchsorted(t,i,side = 'right') - 1
        if index >= 0:
            a = S1[index]
            b = S2[index]
            c = S3[index]
            if  a == 1 and b ==1 and c == 1:
                allelic_state.append(3)
            elif (a == 1 and b == 1) or (b == 1 and c == 1) or (a == 1 and c == 1) : 
                allelic_state.append(2)
            elif (a == 1 or b == 1 or c == 1) and not (a == 1 and b == 1 and c == 1):
                allelic_state.append(1)
            else:
                allelic_state.append(0)
        else:
            allelic_state.append(0)

    all_allelicstates.append(allelic_state)
    j += 1

 
 for i in range(len(np.arange(0,101,0.2))): #outside while #same as time
    c3 = c2 = c1 = c0 = 0
    for row in all_allelicstates:
        if i < len(row): # Check to prevent index out of bounds
            if row[i] == 3:
                c3 += 1
            elif row[i] == 2:
                c2 += 1
            elif row[i] == 1:
                c1 += 1
            elif row[i] == 0:
                c0 += 1
    counts_3.append(c3)            
    counts_2.append(c2)
    counts_1.append(c1)
    counts_0.append(c0)

# Plot 
 time = np.arange(0,tend+1,0.2)
# Ensure count lists have the same length as the time axis
 counts_4 = counts_4[:len(time)]
 counts_3 = counts_3[:len(time)]
 counts_2 = counts_2[:len(time)]
 counts_1 = counts_1[:len(time)]
 counts_0 = counts_0[:len(time)]

 #plt.plot(time, counts_4 , label="XiXiXiXi (Tetra-allelic)", color="purple")
 plt.plot(time, counts_3 , label="XaXiXiXi (Triallelic)", color="red")
 plt.plot(time, counts_2 , label="XaXaXiXi (Biallelic)" , color="blue")
 plt.plot(time, counts_1 , label="XaXaXaXi (Monoallelic)", color="green") 
 plt.plot(time, counts_0,  label="XaXaXaXa (Inactive)" , color="orange")

 plt.xlabel("Time")
 plt.ylabel("Number of cells")
 plt.title("Trisomy ( 2n , 3x )")
 plt.legend()
 plt.show()
  #plt.savefig('modelB_'+str(set)