import matplotlib.pyplot as plt
import numpy as np
import numdifftools as nd

def hill(total_activator,K,n,kmax,kmin):
 return (kmax - kmin)*(total_activator**n)/(total_activator**n + K**n) + kmin
x = np.linspace(0, 4, 100)
y = np.linspace(0, 4, 100)
total_activator1, total_activator3 = x,y
K31 = 1
n31 = 1
K3p = 1
n3p = 3
K1p = 3
n1p = 1
# 2. Parameters
kp_max = 1
kp_min = 0
a = 1
b = 1
e = 1
c = a / (a + b) 
d = b / (a + b)
#withoutactivator1
rate1 = (kp_max-kp_min) * (hill(total_activator3,K3p,n3p,1,0)) + kp_min
rate8 = (kp_max-kp_min) * (hill(total_activator3/2,K3p,n3p,1,0)) + kp_min
# # 3. 1 OR 3
n1p = 3
n3p = 3
rate2 = (kp_max-kp_min)*(c * hill(total_activator1,K1p,n1p,1,0) + d * hill(total_activator3,K3p,n3p,1,0)) + kp_min

# # 1 OR 3 independently also but also together.
e = 1
c = a / (a + b + e) 
d = b / (a + b + e)
f = e / (a + b + e)
m = 1
rate3 = (kp_max-kp_min)* (c * hill(total_activator1,K1p,n1p,1,0) + d * hill(total_activator3,K3p,n3p,1,0) + f * (hill(total_activator3,K3p,n3p,1,0) * hill(total_activator1,K1p,n1p,1,0)))+ kp_min
#Cooperative OR but with complex.
rate4 = (kp_max-kp_min)* ((c * hill(total_activator1,K1p,n1p,1,0)) + d* hill(total_activator3,K3p,n3p,1,0) +  f*(hill(total_activator3*total_activator1,K3p,m,1,0)))+ kp_min
# #1 AND 3 as a complex.
rate5 =(kp_max-kp_min) * hill(total_activator3*total_activator1,K3p,m,1,0) + kp_min 
# #1 AND 3.
rate6 = (kp_max-kp_min) * (hill(total_activator3,K3p,n3p,1,0) * hill(total_activator1,K1p,n1p,1,0)) + kp_min
#dimer with df.
rate7 =(kp_max-kp_min) * hill((total_activator3)/2 *(total_activator1)/2,K3p,m,1,0) + kp_min 
# # SLOPE
# def hill_scalar(A):
#     #return A**n3p / (K3p**n3p + A**n3p) #one activator
#     #return c * (A**n1p / (K1p**n1p + A**n1p)) + d * (A**n3p / (K3p**n3p + A**n3p)) # 1 OR 3
#     #return c * (A**n1p / (K1p**n1p + A**n1p))  + d * (A**n3p / (K3p**n3p + A**n3p)) + f * (A**n3p / (K3p**n3p + A**n3p)) * (A**n1p / (K1p**n1p + A**n1p))# 1 OR 3 independently but also together.
#     #return c * (A**n1p / (K1p**n1p + A**n1p))  + d * (A**n3p / (K3p**n3p + A**n3p)) + f * ((A*A)**m / (K1p**m+ (A*A)**m)) ##OR + complex
#     return ((A*A)**m / (K1p**m+ (A*A)**m)) #as a dimer
#     #return ((A**n3p / (K3p**n3p + A**n3p)) * (A**n1p / (K1p**n1p + A**n1p))) #AND
# deriv = nd.Derivative(hill_scalar)
# dH_dA = np.array([deriv(a) for a in x])
# print(max(dH_dA))
# SLOPE
def hill_scalar(A):
    # one activator
    Single_activator = A**n3p / (K3p**n3p + A**n3p)

    # 1 OR 3
    OR = 0.5 * (A**n1p / (K1p**n1p + A**n1p)) \
           + 0.5 * (A**n3p / (K3p**n3p + A**n3p))

    # 1 OR 3 independently but also together
    Cooperative_OR = 0.33 * (A**n1p / (K1p**n1p + A**n1p)) \
           + 0.33 * (A**n3p / (K3p**n3p + A**n3p)) \
           + 0.33 * (A**n3p / (K3p**n3p + A**n3p)) * (A**n1p / (K1p**n1p + A**n1p))

    # OR + complex
    OR_Dimer = 0.33 * (A**n1p / (K1p**n1p + A**n1p)) \
               + 0.33 * (A**n3p / (K3p**n3p + A**n3p)) \
               + 0.33 * ((A*A)**m / (K1p**m + (A*A)**m))

    # as a dimer
    Dimer =((A)**(2*m)) / (K1p**(2*m) + (A)**(2*m))

    # AND
    AND = (A**n3p / (K3p**n3p + A**n3p)) * (A**n1p / (K1p**n1p + A**n1p))

    z = [Single_activator, OR, Cooperative_OR, OR_Dimer, Dimer, AND]
    return z

n_outputs = len(hill_scalar(x[0]))

labels = [
    'Single_activator',
    'OR',
    'Cooperative_OR',
    'OR_Dimer',
    'Dimer',
    'AND'
]

for i in range(n_outputs):
    deriv = nd.Derivative(lambda A: hill_scalar(A)[i], method='central', step=1e-6)
    dH_dA = deriv(1)
    print(f'{labels[i]} = {(dH_dA)}')

plt.plot(total_activator3, rate1, label='Single activator',color = 'green')
plt.plot(total_activator3, rate8, label='Single activator with df',color = 'magenta')
# plt.plot(total_activator3, rate2, label='OR',color = 'blue',dashes = [2,2])
# plt.plot(total_activator3, rate3, label='cooperative OR',color = 'red')
# plt.plot(total_activator3, rate4, label='cooperative OR w/ complex',color = 'pink')
plt.plot(total_activator3, rate5, label='Dimer',color = 'orange')
plt.plot(total_activator3, rate7, label='Dimer with DF',color = 'black')
# plt.plot(total_activator3, rate6, label='AND',color = 'black') #overlapping with single activator
plt.xlabel('Activator conc')
plt.ylabel('OFF to ON')
plt.legend()
#plt.savefig('/home/madhusud/modeling_gene_expression/modelA_ParameterPlots/Dilution/3regultormodels/without1.png', bbox_inches='tight')
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
# print(p1.shape)

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
        