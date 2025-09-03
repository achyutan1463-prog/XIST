#% of cells graph for 3 state model for XO cells
import numpy as np
import matplotlib.pyplot as plt
import random

counts_1 = []
counts_0 = []
all_allelicstates = []
j = 0
while j < 100:
    
    #the whole gillespie code
    S1 = [0]    
    A1_1 = [1]  
    A2_1 = [1]  
    t = [0]     
    I1_1 = [0] 
    I2_1 = [0]
    tend = 100

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
    K1 =  5.2016        #hill function threshsold
    n1 = 2.6442          
    gamma_A1 = 1.0 
    kA1_max = 0.50477
    kA1_min = 0.00040935

    # activator 2
    kA2 = 0.99378     
    K2 = 0.03227        
    n2 =  2.3935          
    gamma_A2 =  1.0
    kA2_max = 4.3102
    kA2_min = 0.0003174 

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
        total_activator1 = current_A1_1
        k_prod_eff1 = k_fo * (total_activator1**n1) / ((K1**n1) + (total_activator1**n1))

        # combined hill function , activator 2
        total_activator2 = current_A2_1
        k_prod_eff2 = k_of * (K2**n2) / ((K2**n2) + (total_activator2**n2))
        
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

    allelic_state = []  
    for i in np.arange(0,101,0.2): # timesteps  - gives a single list that tells S values at each time step
        index = np.searchsorted(t,i,side = 'right') - 1
        if index >= 0:
            a = S1[index]
            if a == 1: 
                allelic_state.append(1)
            else:
                allelic_state.append(0)
        else:
            allelic_state.append(0)

    all_allelicstates.append(allelic_state)
    j += 1

for i in range(len(np.arange(0,101,0.2))): #outside while #same as time
    c1 = c0 = 0
    for row in all_allelicstates:
        if i < len(row):
            if row[i] == 1:
                c1 += 1
            elif row[i] == 0:
                c0 += 1
    counts_1.append(c1)
    counts_0.append(c0)

# Plot all states
time = np.arange(0,101,0.2)
counts_1 = counts_1[:len(time)]
counts_0 = counts_0[:len(time)]

plt.plot(time, counts_1, label="Xa (Active)", color="green")
plt.plot(time, counts_0, label="Xi (Inactive)", color="orange")

plt.xlabel("Time")
plt.ylabel("Number of occurrences")
plt.title("XO cells")
plt.legend()
plt.show(block =True)