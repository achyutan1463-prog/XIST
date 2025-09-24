import numpy as np
import random
import json
import sys
try:
    input_filepath = sys.argv[1]
except IndexError:
    print("Error: You must provide an input file path as a command-line argument.")
    print("Usage: python simulating_params.py <path_to_input_file>")
    sys.exit(1) 

p=[]
with open(input_filepath, "r") as f:
    for line in f:
        # split by comma, strip whitespace, skip empty strings
        numbers = [float(num_str) for num_str in line.strip().split(',') if num_str.strip() != '']
        p.extend(numbers)

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
table = [[None for _ in range(6)] for _ in range(100)]
for set in range (0,100): #loop for each parameter set

 k_of, k_ffr = [1,1]
 k_fo = q[set][0]
 k_frf = q[set][3]
# Regulated OFF-->ON (xXF_A)
 #k1_max, n1, K1, k1_min, k1_delay, k1_off, k1_on = q[set][4:11]

# Regulated ON-->OFF (Activator 2)
 kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = q[set][11:18]

# Regulated OFF-->OFFrepr (Activator 1)
 kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = q[set][18:25]

# Regulated OFFrepr-->OFF (xXF_D)
 #k4_max, n4, K4, k4_min, k4_delay, k4_off, k4_on = q[set][25:32]

 df1 = 1
 df2 = 1
 no_intermediates = 10
 all_allelicstates = []
 j = 0
 while j < 100:
    #normal XX cells
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
        k_prod_eff1 = ((kA1_max-kA1_min) * k_ffr * (K1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 ) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
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

    #XO cells
    #the whole gillespie code
    S1 = [0]    
    A1_1 = [1]  
    A2_1 = [1]  
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
        total_activator1 = (current_A1_1) / df1
        k_prod_eff1 = ((kA1_max-kA1_min) * k_ffr * (K1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 ) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
        #chromosome 1
        a1_1 = k_frf * int(current_S1 == -1) 
        a2_1 = k_prod_eff1 * int(current_S1 == 0) 
        a3_1 = k_fo * int(current_S1 == 0) 
        a4_1 = k_prod_eff2 * int(current_S1 == 1) 
        a5_1 = kA1 * int(current_A1_1==0 and current_S1!=1)
        a6_1 = gamma_A1 * int(current_A1_1==1 and current_S1==1 and current_I1_1 >= no_intermediates)
        a7_1 = kA2 * int(current_A2_1==0 and current_S1!=1) 
        a8_1 = gamma_A2 * int(current_A2_1==1 and current_S1==1 and current_I2_1 >= no_intermediates) 

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
 df1 = 1
 df2 = 1
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
    tend = 51
    
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
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3 ) / df1
        k_prod_eff1 = ((kA1_max-kA1_min) * k_ffr * (K1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 ) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
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
        k_prod_eff1 = ((kA1_max-kA1_min) * k_ffr * (K1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 + current_A2_4) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
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

        #chromosome 4
        a1_4 = k_frf * int(current_S4 == -1) #off repressed to off
        a2_4 = k_prod_eff1 * int(current_S4 == 0) #off to off repressed
        a3_4 = k_fo * int(current_S4 == 0) #off to on
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
 df1 = 2
 df2 = 2 
 j = 0
 while j < 100:
    #tetrploidy
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
        k_prod_eff1 = ((kA1_max-kA1_min) * k_ffr * (K1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 + current_A2_4) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
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

        #chromosome 4
        a1_4 = k_frf * int(current_S4 == -1) #off repressed to off
        a2_4 = k_prod_eff1 * int(current_S4 == 0) #off to off repressed
        a3_4 = k_fo * int(current_S4 == 0) #off to on
        a4_4 = k_prod_eff2 * int(current_S4 == 1) #on to off
        a5_4 = kA1 * int(current_A1_4==0 and current_S4!=1) #activator 1 OFF to ON
        a6_4 = gamma_A1 * int(current_A1_4==1 and current_S4==1 and current_I1_4 >= no_intermediates) #activator 1 ON to OFF
        a7_4 = kA2 * int(current_A2_4==0 and current_S4!=1) #activator2 OFF to ON
        a8_4 = gamma_A2 * int(current_A2_4==1 and current_S4==1 and current_I2_4 >= no_intermediates)  #activator 2  ON to OFFF

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

 table[set][5] = c2
 df1 = 1.5
 df2 = 1.5
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
        total_activator1 = (current_A1_1 + current_A1_2 + current_A1_3 ) / df1
        k_prod_eff1 = ((kA1_max-kA1_min) * k_ffr * (K1**n1) / ((K1**n1) + (total_activator1**n1))) + kA1_min 

        # combined hill function , activator 2
        total_activator2 = (current_A2_1 + current_A2_2 + current_A2_3 ) / df2
        k_prod_eff2 = ((kA2_max-kA2_min) * k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))) + kA2_min 
        
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
 c2_triploid = c2
 c1_triploid = c1
 table[set][4] = [c2,c1]


outputfile = sys.argv[2]
with open(outputfile, 'w') as f:
    # 3. Use json.dump() to write the data to the file
    json.dump(table, f, indent=4)