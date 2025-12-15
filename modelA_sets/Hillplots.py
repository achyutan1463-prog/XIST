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
kp_max = 2
kp_min = 0.0002
a = 1
b = 1
e =  1
c = a / (a + b) 
d = b / (a + b)
f = e / (a + b + e)

# # 3. 1 OR 3
#rate = c * hill(total_activator1,K1p,n1p,kp_max,kp_min) + d * hill(total_activator3,K3p,n3p,kp_max,kp_min)

# # 1 OR 3 independently also but also together.
# a = 1
# b = 1
# c = a / (a + b + e) 
# d = b / (a + b + e)

#rate =  c * hill(total_activator1,K1p,n1p,kp_max,kp_min) + d * hill(total_activator3,K3p,n3p,kp_max,kp_min) + f * (hill(total_activator3,K3p,n3p,kp_max,kp_min) * hill(total_activator1,K1p,n1p,kp_max,kp_min))

# #1 AND 3

# #FFL with OR
#total_activator1 = hill(total_activator3,K31,n31,1,0)
#rate = c * hill( total_activator1,K1p,n1p,kp_max,kp_min) + d * hill(total_activator3,K3p,n3p,kp_max,kp_min)

# #FFL with AND.
#total_activator1 = hill(total_activator3,K31,n31,1,0)
#rate = hill( total_activator1,K1p,n1p,kp_max,kp_min) * hill(total_activator3,K3p,n3p,kp_max,kp_min) 

plt.plot(total_activator3,rate)
plt.xlabel('Activator3 conc')
plt.ylabel('OFF to ON')
plt.show()

