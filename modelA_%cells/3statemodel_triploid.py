# % of cells graph for 3 state model , trisploid (3n3x)
import numpy as np
import matplotlib.pyplot as plt
import random

#silencing delays
ksA1 = 3.0713
ksA2 = 2.7175
no_intermediates = 10

#promoter switching rates
k_frf = 0.014989
k_ffr = 0.00012063
k_fo = 1.0
k_of = 1.0

# activator 1
kA1 = 0.67419
K1 = 5.2016  #hill function threshsold
n1 = 2.6442
gamma_A1 = 1.0
kA1_max = 0.50477
kA1_min = 0.00040935
df1 = 3  #dilution factor for activator 1

# activator 2
kA2 = 0.99378
K2 = 0.03227  #hill function threshsold
n2 = 2.3935
gamma_A2 = 1.0
kA2_max = 4.3102
kA2_min = 0.0003174
df2 = 3  #dilution factor for activator 2

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
    tend = 100
    
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
        k_prod_eff1 = ((kA1_max-kA1_min) * k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3)  / df2
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
time = np.arange(0,101,0.2)
# Ensure count lists have the same length as the time axis
counts_3 = counts_3[:len(time)]
counts_2 = counts_2[:len(time)]
counts_1 = counts_1[:len(time)]
counts_0 = counts_0[:len(time)]

#stacking
bottom_0 = np.array(counts_0)
bottom_1 = bottom_0 + np.array(counts_1)
bottom_2 = bottom_1 + np.array(counts_2)

plt.plot(time, counts_3 , label="XiXiXi (Triallelic)", color="red")
plt.plot(time, counts_2 , label="XaXiXi (Biallelic)" , color="blue")
plt.plot(time, counts_1 , label="XaXaXi (Monoallelic)", color="green") 
plt.plot(time, counts_0,  label="XaXaXa (Inactive)" , color="orange")

# plt.bar(time, counts_2, width=0.2 , label="XaXiXi", color="blue")
# plt.bar(time, counts_1, width=0.2 , label="XaXaXi", color="green") 
# plt.bar(time, counts_3, width=0.2 , label="XiXiXi", color="red")
#plt.bar(time, counts_0, width=0.2, label="XaXaXa", color="orange")
    
plt.xlabel("Time")
plt.ylabel("Number of occurrences")
plt.title("Triploid ( 3n , 3x)")
plt.legend()
plt.show(block=True)