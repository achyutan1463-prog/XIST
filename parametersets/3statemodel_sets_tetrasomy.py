# % of cells graph for 3 state model , tetrploidy (4n,4x)
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import random

p=[3.9662,0.45549,0.0057613,0.028445,1.1345,2.1867,9.142,0.00066475,3.0856,1.0,4.087,0.82579,1.931,0.013838,0.0033453,2.4654,1.0,4.9088,0.0024061,2.5458,0.027539,0.0010367,1.9918,1.0,0.52644,0.013606,2.1676,3.5781,0.0021776,1.7492,1.0,4.5006
,0.4657,0.00011558,0.34966,0.040257,3.5984,2.8752,4.6205,0.001303,2.8396,1.0,2.683,1.5483,2.031,0.01367,0.001516,1.7447,1.0,3.1787,1.9276,2.52,0.022485,0.28649,1.7305,1.0,3.9446,0.063607,1.7519,7.6703,0.050788,1.7987,1.0,4.2222
,0.26043,0.018619,0.019011,0.16643,0.92386,2.8917,5.915,0.0015665,1.809,1.0,1.9842,0.074904,2.2767,0.016703,0.00012735,2.2451,1.0,1.0153,0.3845,2.6677,0.91072,0.014861,2.9652,1.0,4.8184,2.8729,1.5428,0.030658,0.028667,1.3634,1.0,3.7671
,0.0011006,0.00045299,1.8746,0.028242,1.8935,2.4053,1.7769,0.00012827,1.3069,1.0,1.7598,0.2566,2.6562,0.035806,0.00077607,2.2775,1.0,2.9203,3.6012,1.4065,0.13301,0.95128,2.8965,1.0,4.6607,3.4278,1.722,0.024317,0.79711,1.6107,1.0,4.2162
,0.1567,0.00080876,1.9248,0.00014688,3.563,2.3426,0.81843,0.33846,2.4122,1.0,2.9381,0.33902,2.1963,0.027587,0.00046997,3.1499,1.0,1.2334,0.18572,1.0425,1.0332,0.00040402,1.651,1.0,3.9524,0.67236,1.5123,0.028214,0.36013,1.8138,1.0,3.5664
,0.00012096,1.1619,0.058582,3.2814,0.21025,2.3053,4.2614,0.00018465,3.256,1.0,1.9922,2.435,2.901,0.012675,0.0010303,3.4348,1.0,0.63851,0.6149,1.3513,0.82243,0.24358,1.9751,1.0,4.9548,2.3259,1.7085,0.61411,0.96342,1.5513,1.0,2.8447
,0.00038497,0.00012784,0.63202,0.00018284,1.9147,1.8239,2.1805,0.58814,2.6204,1.0,0.74675,0.48136,2.3424,0.024715,0.00085072,2.1861,1.0,3.4195,0.17181,2.3451,0.034995,0.090103,2.8028,1.0,4.4542,0.2344,2.5942,0.05901,0.0065391,1.5233,1.0,1.2694
,0.00019081,3.2707,0.022472,0.063015,0.20681,2.3481,3.1979,0.00086525,3.2949,1.0,2.5781,1.0079,2.6602,0.014242,0.00029472,3.054,1.0,3.2897,0.32022,1.4633,0.022504,0.08367,2.4325,1.0,4.2165,2.7473,1.8032,5.5542,0.024083,2.5615,1.0,3.0471
,0.038755,0.03639,0.0009412,0.0039871,0.2814,1.7493,6.1072,0.00054224,1.4259,1.0,3.6393,0.40173,2.1704,0.062435,0.00024976,2.0202,1.0,4.4693,2.2421,1.2314,0.10486,0.0016767,0.73176,1.0,4.2395,0.041087,2.8321,0.029847,0.00017954,1.335,1.0,4.7389
,1.4554,4.1767,0.00098938,0.00032395,2.0176,2.8144,9.5668,0.00030879,1.8128,1.0,0.92863,0.82238,2.1451,0.022919,0.00014472,3.0864,1.0,1.9407,1.9652,2.9412,6.859,0.069262,2.5399,1.0,3.4663,1.4612,2.0878,1.1618,0.71118,3.3148,1.0,0.48245
,0.0011095,0.075039,0.036922,0.0012645,0.14297,2.713,1.743,0.0011663,1.8071,1.0,3.7358,1.5661,2.485,0.030132,0.0015377,2.5022,1.0,1.8803,0.26681,1.6423,3.5918,0.0016685,0.90098,1.0,2.4902,4.8038,1.1738,0.81439,0.42077,2.853,1.0,4.1461
,4.9782,0.087389,0.34364,0.00035446,2.2249,2.6575,2.4428,0.0090479,1.1496,1.0,3.2289,0.1433,1.7657,0.089919,0.0079895,2.4883,1.0,0.15971,4.6317,2.8214,0.27588,0.03217,2.1103,1.0,2.8283,1.3536,1.6363,0.46717,0.32509,1.7482,1.0,2.5694
,0.00010208,0.19716,0.00557,0.86035,0.069904,2.2144,2.8298,0.0043076,2.7619,1.0,4.299,0.18493,2.3941,0.035509,0.0003485,3.2426,1.0,3.8846,1.9601,2.0578,6.3996,0.62846,1.8199,1.0,3.7231,0.0041171,1.1429,2.2344,0.001291,0.42959,1.0,0.97367
,0.45627,0.75321,0.04566,0.25753,0.3097,2.8861,3.9811,0.00028943,1.4591,1.0,2.4816,0.62577,1.8774,0.056083,0.00057956,3.1182,1.0,4.2225,0.035847,2.8006,0.061623,0.0062411,1.4487,1.0,4.34,0.075413,1.681,9.1899,0.064474,0.48828,1.0,0.34909
,4.436,0.0050257,2.5963,0.0060269,3.0855,1.1221,0.71088,0.21531,3.2355,1.0,0.071051,0.21457,2.3344,0.010279,0.00021249,2.8119,1.0,4.1404,0.70092,2.1377,0.071866,0.39266,1.7742,1.0,2.281,0.089857,2.9766,0.28383,0.043435,1.0069,1.0,2.0278
,0.00039256,0.0024223,4.0812,0.087144,1.8463,2.9173,2.0148,0.17542,1.7001,1.0,2.3817,0.34239,2.3645,0.013453,0.0018311,2.9252,1.0,2.6623,0.48765,1.26,0.56695,0.15969,2.6027,1.0,2.247,3.1523,1.4662,0.043011,0.73399,1.9641,1.0,0.16745
,2.975,0.002887,0.12806,0.00018974,0.54973,2.603,2.652,0.002938,2.9597,1.0,1.3206,0.23174,1.8621,0.028442,0.00022972,2.2756,1.0,3.1012,0.057151,1.3719,0.015409,0.00065012,2.8433,1.0,2.8896,0.86372,2.1689,2.0249,0.36328,3.3514,1.0,4.9452
,0.10731,0.056463,0.33917,0.0001794,0.50105,2.9761,0.11286,0.00031794,2.9238,1.0,1.8884,0.32006,1.7958,0.012172,0.00049354,3.1403,1.0,4.9499,0.0086309,2.5636,0.54254,0.00063468,2.2617,1.0,3.722,1.5105,1.0851,1.2798,0.19247,1.6586,1.0,4.8579
,0.00017144,1.0321,3.2692,0.00019261,4.9982,1.234,0.23321,0.00049121,3.0185,1.0,3.2598,2.1191,2.2786,0.048565,0.0013709,3.2479,1.0,4.6138,0.18704,1.8138,0.86156,0.00013349,0.60458,1.0,1.008,1.502,2.6658,0.052538,0.032409,1.3909,1.0,1.4378
,0.55395,0.00036279,0.96159,0.00049514,2.1954,2.6081,1.3323,0.036285,0.7858,1.0,4.9592,0.46651,1.777,0.06206,0.0007848,1.718,1.0,2.8341,4.1784,1.3944,0.54636,0.066721,0.22689,1.0,1.5109,4.6396,2.4611,6.7149,0.82682,2.612,1.0,3.8661]

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

 k_fo, k_of, k_ffr, k_frf = q[set][0:4]

 #activator 1
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][4:11]

 #activator 2
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]
 df1 = 1
 df2 = 1
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
    
plt.xlabel("parameter sets")
plt.ylabel(" Number of cells")
plt.title("Tetrasomy ( 2n , 4x )")
plt.legend()
#plt.show(block=True)
plt.savefig('/home/madhusud/modeling_gene_expression/parametersets_barplots(Ver)/20_40_plots/tetrasomy_50hrs')
