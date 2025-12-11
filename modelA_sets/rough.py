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
#changes in if statements 
#silencing of A3 by x.