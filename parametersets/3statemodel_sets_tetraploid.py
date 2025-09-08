# % of cells graph for 3 state model , tetrploidy (4n,4x)
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import random

p=[0.0034006,0.82941,0.045608,0.19975,0.28022,2.58,3.5419,0.00074566,3.2904,1.0,2.4871,0.94048,2.9386,0.029961,0.00016983,3.2201,1.0,4.2752,2.8675,1.8392,1.0479,0.0012648,2.5819,1.0,4.06,4.996,2.3672,0.07807,0.031208,2.5765,1.0,1.0862
,0.00038566,0.038948,0.96874,0.0022941,4.0339,1.3746,0.80708,0.22018,2.9569,1.0,1.8739,2.925,2.9003,0.054618,0.00019123,2.4832,1.0,4.1802,2.4563,2.3781,0.41115,0.055927,1.1593,1.0,0.76152,1.4668,2.9215,4.8126,0.032447,0.9969,1.0,0.53676
,0.076184,0.66914,0.99516,0.0019673,4.7125,2.915,1.3816,0.00182,0.3292,1.0,1.8873,0.46413,2.9273,0.10517,0.00015908,3.0282,1.0,1.2153,0.07662,2.4736,0.023804,0.017744,0.2698,1.0,3.3137,0.13458,1.6572,9.2765,0.10602,0.34365,1.0,3.7981
,0.0064592,0.00026252,0.52835,0.00029374,4.4898,2.1855,2.9402,0.00019543,2.1407,1.0,4.6131,0.46672,2.0356,0.040103,0.0018612,3.1819,1.0,3.8855,0.003868,1.0622,0.015512,0.0016993,2.4869,1.0,0.34327,0.003778,1.7797,0.032818,0.0013746,2.4486,1.0,2.6645
,0.12854,0.025593,0.99629,0.00010645,4.7723,1.3102,0.12866,0.047328,2.2626,1.0,1.5631,0.45471,1.6262,0.019224,0.002614,3.1851,1.0,2.7976,0.69982,2.5793,3.2112,0.0056397,0.41133,1.0,4.3889,0.23302,1.9781,1.7246,0.066985,2.38,1.0,2.1825
,0.00011282,0.090422,0.001228,0.067874,0.36887,2.9331,4.8301,0.00030314,2.8131,1.0,2.0434,0.29377,1.6248,0.032295,0.00063707,2.2513,1.0,2.2935,0.32821,2.3857,0.011316,0.076359,0.34156,1.0,2.8856,0.10909,2.9851,0.076243,0.0046436,2.4191,1.0,4.94
,0.060521,1.0663,0.042604,0.0092316,2.1354,2.1642,6.0612,0.0023758,2.1696,1.0,4.1204,0.58337,2.185,0.01172,0.0019244,1.8322,1.0,1.5664,0.55013,2.1756,0.41829,0.030792,2.4458,1.0,3.1093,4.0511,1.9885,0.53805,0.022936,1.8566,1.0,4.8593
,0.044351,0.00028367,0.8229,0.0032539,3.4811,2.22,0.021058,0.00034305,1.7014,1.0,2.572,0.74294,2.1273,0.045899,0.0039904,2.4841,1.0,4.9823,0.014024,1.5312,0.19841,0.0016791,2.3923,1.0,3.0679,1.0077,2.0253,0.18352,0.89644,3.3125,1.0,1.6462
,1.2995,0.0023525,0.001995,0.065064,0.54323,2.8083,4.585,0.00033725,1.9608,1.0,1.4942,0.21004,1.9739,0.021214,0.0017034,2.2846,1.0,1.5473,0.36727,1.1223,5.627,0.0036096,2.8629,1.0,4.7655,0.0015197,1.9457,0.74825,0.00090701,3.3519,1.0,4.2693
,0.0084837,0.0011002,0.070644,0.0010214,0.75546,2.4275,1.8668,0.00065488,2.6417,1.0,2.7919,1.76,2.9024,0.035207,0.00066951,3.1674,1.0,1.2179,4.0908,2.0988,0.1721,0.00079095,3.3813,1.0,3.8135,3.8983,1.2739,0.090902,0.00097653,0.44971,1.0,4.0954
,3.9662,0.45549,0.0057613,0.028445,1.1345,2.1867,9.142,0.00066475,3.0856,1.0,4.087,0.82579,1.931,0.013838,0.0033453,2.4654,1.0,4.9088,0.0024061,2.5458,0.027539,0.0010367,1.9918,1.0,0.52644,0.013606,2.1676,3.5781,0.0021776,1.7492,1.0,4.5006
,1.7401,0.0032496,0.39777,0.0001102,1.6065,1.0663,0.92692,0.0019906,2.3176,1.0,1.7801,0.90395,2.7508,0.093695,0.00014049,1.8468,1.0,4.5723,0.0010642,1.4198,0.028686,0.00014327,2.6401,1.0,3.2192,0.031052,1.1347,0.28009,0.0007665,1.2606,1.0,3.1269
,0.019036,0.0029401,0.011261,0.00053047,0.91022,2.6129,4.9743,0.00023017,3.415,1.0,4.2322,0.57284,2.3925,0.010646,0.00087956,3.0655,1.0,3.832,2.8084,1.3209,2.6926,0.44012,1.3741,1.0,4.9609,0.98871,1.8347,0.30955,0.045246,3.409,1.0,4.8033
,0.0044323,0.0015386,0.39179,0.0014347,3.0069,2.2442,0.019318,0.068197,2.9016,1.0,0.15846,0.85482,2.6804,0.013477,0.010762,3.4736,1.0,4.7808,0.0058993,1.3993,0.41896,0.00024853,1.2065,1.0,1.8027,0.91909,2.9239,1.561,0.0022613,0.91241,1.0,3.1725
,0.0021067,0.09341,0.28755,0.0005963,3.2869,1.0743,0.37529,0.0010559,3.2152,1.0,0.53901,0.38137,2.8851,0.28558,0.00010935,3.072,1.0,1.3521,0.011151,2.8129,0.013421,0.005452,2.2101,1.0,4.7637,0.28147,1.8118,1.3975,0.0070999,0.22595,1.0,0.72136
,0.0020217,0.00085826,0.38218,0.0011414,3.0761,1.5586,3.5961,0.27771,2.7154,1.0,3.9306,1.1279,1.8233,0.017655,0.00099994,3.2516,1.0,3.888,0.90239,2.7987,0.9479,0.010316,3.4191,1.0,0.1752,0.034372,1.1362,7.0609,0.0098221,0.95155,1.0,4.1782
,0.26043,0.018619,0.019011,0.16643,0.92386,2.8917,5.915,0.0015665,1.809,1.0,1.9842,0.074904,2.2767,0.016703,0.00012735,2.2451,1.0,1.0153,0.3845,2.6677,0.91072,0.014861,2.9652,1.0,4.8184,2.8729,1.5428,0.030658,0.028667,1.3634,1.0,3.7671
,0.11269,0.013078,0.2719,0.00026263,0.75957,2.5944,1.3769,0.11221,2.7808,1.0,0.95494,0.28939,2.9186,0.12628,0.0012287,3.1098,1.0,2.5779,0.30681,1.4716,2.4552,0.085741,3.1195,1.0,0.34866,3.3027,1.722,0.029809,0.18257,0.8385,1.0,4.5226
,1.7425,0.00062486,0.18762,0.00045907,0.63613,2.8609,0.92297,0.0025066,0.5552,1.0,0.080618,0.29695,2.2656,0.020574,0.0055886,3.0712,1.0,2.1141,0.72137,1.7507,0.29743,0.035256,0.86654,1.0,3.322,4.1548,2.493,0.010502,0.02643,0.53019,1.0,4.3671
,0.053943,0.002721,1.9767,3.8729,2.2163,2.9955,6.3708,0.0011159,1.634,1.0,0.30933,0.37547,1.3063,0.02501,0.0020872,3.4181,1.0,4.8589,1.1747,2.6338,7.2414,0.0042123,0.93933,1.0,1.7007,0.73496,2.0122,7.4747,0.01772,1.7066,1.0,4.2499
]
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
for set in range (0,len(q)): #loop for each parameter set

 k_fo,k_of = [1,1]
 k_ffr = q[set][3]
 k_frf = q[set][4]
# Regulated OFF-->ON (xXF_A)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1  = q[set][4:11]

# Regulated ON-->OFF (Activator 2)
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 #kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]
 df1 = 4
 df2 = 4
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    
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
    tend = 300
    
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
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 + current_A2_4) / df2
        k_prod_eff2 = ((kA1_max-kA1_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA1_min 
        
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

        # event - chromosome 1
        if rand * rate_sum <= a1_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1:
            S1.append(-1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1:
            S1.append(1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1:
            S1.append(0)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(0)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(0)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        # event - chromosome 2
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2:
            S1.append(current_S1)
            S2.append(-1)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2:
            S1.append(current_S1)
            S2.append(1)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2:
            S1.append(current_S1)
            S2.append(0)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(1)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(0)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(1)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(0)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)
            
         # event - chromosome 3
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(-1)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(1)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(0)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(1)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(0)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(1)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(0)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        # event - chromosome 4
        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(-1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(1)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(0)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(1)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(0)
            A2_4.append(current_A2_4)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4 + a7_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(1)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

        elif rand * rate_sum <= a1_1 + a2_1 + a3_1 + a4_1 + a5_1 + a6_1 + a7_1 + a8_1 + \
             a1_2 + a2_2 + a3_2 + a4_2 + a5_2 + a6_2 + a7_2 + a8_2 + \
             a1_3 + a2_3 + a3_3 + a4_3 + a5_3 + a6_3 + a7_3 + a8_3 + a1_4 + a2_4 + a3_4 + a4_4 + a5_4 + a6_4 + a7_4 + a8_4:
            S1.append(current_S1)
            S2.append(current_S2)
            S3.append(current_S3)
            S4.append(current_S4)
            A1_1.append(current_A1_1)
            A2_1.append(current_A2_1)
            A1_2.append(current_A1_2)
            A2_2.append(current_A2_2)
            A1_3.append(current_A1_3)
            A2_3.append(current_A2_3)
            A1_4.append(current_A1_4)
            A2_4.append(0)
            I1_1.append(current_I1_1)
            I2_1.append(current_I2_1)
            I1_2.append(current_I1_2)
            I2_2.append(current_I2_2)
            I1_3.append(current_I1_3)
            I2_3.append(current_I2_3)
            I1_4.append(current_I1_4)
            I2_4.append(current_I2_4)

                   #intermediates
        elif rand * rate_sum <= sum(rates[:32]) + i1_1:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1 + 1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1 + 1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2 + 1); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2 + 1)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3 + 1); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3 + 1); I1_4.append(current_I1_4); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3 + i1_4:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4 + 1); I2_4.append(current_I2_4)

        elif rand * rate_sum <= sum(rates[:32]) + i1_1 + i2_1 + i1_2 + i2_2 + i1_3 + i2_3 + i1_4 + i2_4:
            S1.append(current_S1); S2.append(current_S2); S3.append(current_S3); S4.append(current_S4)
            A1_1.append(current_A1_1); A2_1.append(current_A2_1); A1_2.append(current_A1_2); A2_2.append(current_A2_2)
            A1_3.append(current_A1_3); A2_3.append(current_A2_3); A1_4.append(current_A1_4); A2_4.append(current_A2_4)
            I1_1.append(current_I1_1); I2_1.append(current_I2_1); I1_2.append(current_I1_2); I2_2.append(current_I2_2)
            I1_3.append(current_I1_3); I2_3.append(current_I2_3); I1_4.append(current_I1_4); I2_4.append(current_I2_4 + 1)
        
    allelic_state = []
   
    for i in np.arange(0,tend+1,0.2): # timesteps  - gives a single pair of lists that tell S values at each time step
        index = np.searchsorted(t,i,side = 'right') - 1
        if index >= 0:
            a = S1[index]
            b = S2[index]
            c = S3[index]
            d = S4[index]
            if a == 1 and b == 1 and c == 1 and d == 1:
                allelic_state.append(4)
            elif (a == 1 and b == 1 and c == 1) or \
                 (a == 1 and b == 1 and d == 1) or \
                 (a == 1 and c == 1 and d == 1) or \
                 (b == 1 and c == 1 and d == 1):
                allelic_state.append(3)
            elif (a == 1 and b == 1) or (a == 1 and c == 1) or (a == 1 and d == 1) or \
                 (b == 1 and c == 1) or (b == 1 and d == 1) or (c == 1 and d == 1):
                allelic_state.append(2)
            elif a == 1 or b == 1 or c == 1 or d == 1:
                allelic_state.append(1)
            else:
                allelic_state.append(0)
        else:
            allelic_state.append(0)

    all_allelicstates.append(allelic_state)  #(after 100 iterations - 100,t)
    j += 1

 
 time = np.arange(0,tend+1,0.2) #outside while 
 i = np.searchsorted(time,50,side = 'right')-1
 c4 = c3 = c2 = c1 = c0 = 0
 for row in all_allelicstates:
            if row[i] == 4:
                c4 += 1
            elif row[i] == 3:
                c3 += 1
            elif row[i] == 2:
                c2 += 1
            elif row[i] == 1:
                c1 += 1
            elif row[i] == 0:
                c0 += 1

 if set == 0:
    plt.bar(str(set), c0, label="XaXaXaXa (Inactive)", color="orange")
    bottom = c0
    plt.bar(str(set), c1, label="XaXaXaXi (Monoallelic)", color="green", bottom=bottom)
    bottom += c1
    plt.bar(str(set), c2, label="XaXaXiXi (Biallelic)", color="blue", bottom=bottom)
    bottom += c2
    plt.bar(str(set), c3, label="XaXiXiXi (Triallelic)", color="red", bottom=bottom)
    bottom += c3
    plt.bar(str(set), c4, label="XiXiXiXi (Tetra-allelic)", color="purple", bottom=bottom)

 else:


    plt.bar(str(set), c0, color="orange")
    bottom = c0
    plt.bar(str(set), c1, color="green", bottom=bottom)
    bottom += c1
    plt.bar(str(set), c2, color="blue", bottom=bottom)
    bottom += c2
    plt.bar(str(set), c3, color="red", bottom=bottom)
    bottom += c3
    plt.bar(str(set), c4, color="purple", bottom=bottom)


# plt.bar(time, counts_2, width=0.2 , label="XaXaXiXi", color="blue")
# plt.bar(time, counts_1, width=0.2 , label="XaXaXaXi", color="green") 
# plt.bar(time, counts_3, width=0.2 , label="XaXiXiXi", color="red")
# plt.bar(time, counts_4, width=0.2 , label="XiXiXiXi", color="purple")
# plt.bar(time, counts_0, width=0.2, label="XaXaXaXa", color="orange")
    
plt.xlabel("Parameter sets")
plt.ylabel("Number of cells")
plt.title("Tetraploid ( 4n , 4X )")
plt.legend()
#plt.show(block=True)
plt.savefig('/home/madhusud/modeling_gene_expression/parametersets_barplots(Ver)/AB_plots/tetraploid_50hrs')
