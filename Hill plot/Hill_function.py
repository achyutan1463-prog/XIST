import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np

def hill(total_activator,K,n,kmax,kmin):
 return (kmax - kmin)*(total_activator**n)/(total_activator**n + K**n) + kmin

x = 1
y = np.linspace(0, 10, 100)
total_activator1, total_activator3 = x,y
K31 = 1
n31 = 2
K3p = 1
n3p = 2
K1p = 1
n1p = 2
# 2. Parameters
kp_max = 1
kp_min = 0
a = 1
b = 1
e =  1
c = a / (a + b) 
d = b / (a + b)
f = e / (a + b + e)

#withoutactivator1
rate1 = (kp_max-kp_min)* (a * hill(total_activator3,K3p,n3p,1,0)) + kp_min
# # 3. 1 OR 3
rate2 = (kp_max-kp_min)*(c * hill(total_activator1,K1p,n1p,1,0) + d * hill(total_activator3,K3p,n3p,1,0)) + kp_min

# # 1 OR 3 independently also but also together.

c = a / (a + b + e) 
d = b / (a + b + e)
f = e / (a + b + e)

rate3 =  (kp_max-kp_min)* (c * hill(total_activator1,K1p,n1p,1,0) + d * hill(total_activator3,K3p,n3p,1,0) + f * (hill(total_activator3,K3p,n3p,1,0) * hill(total_activator1,K1p,n1p,1,0)))+ kp_min

# #1 AND 3
models=["AR_simple",'AR_dilution','AR_quadratic']
for i in range(0,len(models)):
 values = [AR,dilution,y_values] #y value ranges(rate1,rate2..)
 index90 = np.abs(values[i]- 0.9*kA1_max).argmin()
 index10 = np.abs(values[i] - 0.1*kA1_max).argmin()
 print(f" EC90/EC10 of {models[i]} = {total_activator1[index90]/ total_activator1[index10]}")
rate4 = (kp_max-kp_min)* e * (hill(total_activator3,K3p,n3p,1,0) * hill(total_activator1,K1p,n1p,1,0)) + kp_min
plt.plot(total_activator3, rate1, label='Single activator')
plt.plot(total_activator3, rate2, label='OR')
plt.plot(total_activator3, rate3, label='cooperative OR')
plt.plot(total_activator3, rate4, label='AND')

plt.xlabel('Activator3 conc')
plt.ylabel('OFF to ON')
plt.legend()
#plt.savefig('/home/madhusud/modeling_gene_expression/modelA_ParameterPlots/Dilution/3regultormodels/without1.png', bbox_inches='tight')
plt.show()
#FFL with OR
c = a / (a + b) 
d = b / (a + b)
# #total_activator1 = hill(total_activator3,K31,n31,1,0)
# #rate =(kp_max-kp_min)*  (c * hill( total_activator1,K1p,n1p,1,0) + d * hill(total_activator3,K3p,n3p,1,0)) + kp_min

## Cascade
# total_activator1 = hill(total_activator3,K31,n31,1,0)
# rate = (kp_max-kp_min) * (hill( total_activator1,K1p,n1p,1,0) + kp_min

# #FFL with AND.
# total_activator1 = hill(total_activator3,K31,n31,1,0)
# rate = (kp_max-kp_min)* (hill( total_activator1,K1p,n1p,1,0) * hill(total_activator3,K3p,n3p,1,0)) + kp_min

# plt.plot(total_activator3,rate)
# plt.xlabel('Activator3 conc')
# plt.ylabel('OFF to ON')
# plt.savefig('/home/madhusud/modeling_gene_expression/modelA_ParameterPlots/Dilution/3regultormodels/without1.png', bbox_inches='tight')
# plt.show()

kA1_max = 2
kA1_min = 0
n1 = 2
K1 = 1
total_activator1 = np.linspace(0, 10, 100)
#Autosomal repressor
finaldose = []
for i in total_activator1:
        
 if i > 1:
            i -= 1
 else:
            i = 0
 finaldose.append(i)
finaldoseAR = np.array(finaldose) 
#print(finaldose)
AR = ((kA1_max-kA1_min) * (finaldoseAR**n1) / ((K1**n1) + (finaldoseAR**n1))) + kA1_min
#dilution factor
finaldose = []
for i in total_activator1:
      i = i/2
      finaldose.append(i)
finaldoseDil = np.array(finaldose)     
#print(finaldose)
dilution = ((kA1_max-kA1_min) * (finaldoseDil**n1) / ((K1**n1) + (finaldoseDil**n1))) + kA1_min 
plt.subplot(1, 2, 1)  # 1 row, 2 columns, first subplot
plt.plot(finaldose, AR)
plt.xlabel('Total_activator1')
plt.ylabel('OFF to ON')
plt.title('Autosomal repressor (tetraploid)')

# Right subplot
plt.subplot(1, 2, 2)  # 1 row, 2 columns, second subplot
plt.plot(finaldoseDil, dilution)
plt.xlabel('Total_activator1')
plt.ylabel('OFF to ON')
plt.title('Dilution factor of 2(tetraploid)')

plt.tight_layout()
plt.show()
# def sets(p , totalparams): 
#     q = []
#     a = 0
#     b = 32
#     for i in range(len(p)//totalparams):
#         q.append(p[a:b])
#         b += 32
#         a += 32
#     return q

# q = sets(p, 32)
# p1 = []
# p2 = []

# total_activator = np.arange(0, 2, 0.05)

# # iterate through all parameter sets
# for param_set in q:
#     # extract parameters for activator 1
#     k_fo, k_of = [1, 1]
#     k_ffr = param_set[2]
#     k_frf = param_set[3]
    
#     kA1_max, n1, K1, kA1_min, ksA1, gamma_A1, kA1 = param_set[4:11]
    
#     # extract parameters for activator 2
#     kA2_max, n2, K2, kA2_min, ksA2, gamma_A2, kA2 = param_set[11:18]
    
#     # compute k_prod_eff1 and k_prod_eff2 (1D version)
#     k_prod_eff1 = ((kA1_max - kA1_min) * (total_activator ** n1) /
#                    ((K1 ** n1) + (total_activator ** n1))) + kA1_min

#     k_prod_eff2 = ((kA2_max - kA2_min) * (K2 ** n2) /
#                    ((K2 ** n2) + (total_activator ** n2))) + kA2_min

#     # store one curve per parameter set
#     p1.append(k_prod_eff1)
#     p2.append(k_prod_eff2)

# # convert to NumPy arrays (shape: n_sets × n_points)
# p1 = np.array(p1)
# p2 = np.array(p2)
# #print(p1.shape)

# # compute medians and quartiles across all parameter sets
# y1 = np.median(p1, axis=0)
# y2 = np.median(p2, axis=0)
# q1 = np.percentile(p1, 25, axis=0)
# q2 = np.percentile(p1, 75, axis=0)
# q3 = np.percentile(p2, 25, axis=0)
# q4 = np.percentile(p2, 75, axis=0)

# # plot median line with shaded IQR region
# plt.figure(figsize=(10, 5))

# plt.subplot(1, 2, 1)
# plt.plot(total_activator, y1, color='green', label='Median')
# plt.fill_between(total_activator, q1, q2,
#                  color='lightgrey', alpha=0.5, label='25th–75th percentile')
# plt.grid(alpha=0.3)
# plt.xlabel('Zic3', fontsize=12, labelpad=6,weight='bold')
# plt.ylabel('Xist', fontsize=12, labelpad=6,weight='bold')
# plt.yscale('log')

# plt.subplot(1, 2, 2)
# plt.plot(total_activator, y2, color='blue', label='Median')
# plt.fill_between(total_activator, q3, q4,
#                  color='lightgrey', alpha=0.5, label='25th–75th percentile')
# plt.xlabel('Rnf12', fontsize=12, labelpad=6,weight='bold')
# plt.ylabel('Xist', fontsize=12, labelpad=6,weight='bold')
# plt.yscale('log')
# plt.grid(alpha=0.3)

# plt.subplots_adjust(hspace=0.6, wspace=0.5)

# plt.savefig('/home/madhusud/modeling_gene_expression/FinalPlots/Hillfunction_n1-3.png',dpi=600, bbox_inches='tight')
# #plt.show()
# # for i in range(len(p1)):
# #  plt.plot(np.arange(0,10,0.05),np.log10(np.p1[i]))
# # plt.show()
# # for i in range(len(p2)):
# #  plt.plot(np.arange(0,10,0.05),np.log10(p2[i]))
# # plt.show()
        
