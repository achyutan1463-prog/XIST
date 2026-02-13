import numpy as np
import matplotlib.pyplot as plt
import numdifftools as nd
#Cascade ,FFL
def hill(s, K, n,max,min):
    return ((max-min)*((s**n) / (K**n + s**n))) + min

K1 = 1
n = 1
K2 = 1
m = 1
gamma_A2 = 0.1
Vmax1 = 1
Vmin1 = 0
Vmax2 = 1
Vmin2 = 0
A1= np.linspace(0,10,100)
A2 =  hill(A1,K1,n,1,0)/ gamma_A2
hill_A2 = hill(A2,K2,m,1,0)#cascade

#FFL OR
a=1
b=1

c = a / (a + b) 
d = b / (a + b)

hill_A3 = c * hill(A2,K2,m,1,0) + d * hill(A1,K1,m,1,0)
hill_A4 = hill(A2,K2,m,1,0) * hill(A1,K1,m,1,0)
#slope
def hill_scalar(A):
 cascade= hill(hill(A,K1,n,1,0)/ gamma_A2,K2,m,1,0)
 FFL_OR=  c * hill(hill(A,K1,n,1,0)/ gamma_A2,K2,m,1,0) + d * hill(A,K1,m,1,0)
 FFL_AND = hill(hill(A,K1,n,1,0)/ gamma_A2,K2,m,1,0) * hill(A,K1,m,1,0)
 Single = hill(A,K1,n,1,0)
 x=[cascade,FFL_OR,FFL_AND,Single] 
 return x
n_outputs = len(hill_scalar(A1[0]))
x=['cascade','FFL_OR','FFL_AND','Single'] 
for i in range(n_outputs) : 
    deriv = nd.Derivative(lambda A: hill_scalar(A)[i]) 
    dH_dA = deriv(K2) 
    print(f'{x[i]} = {(dH_dA)}')

plt.plot(A1,hill_A2,label='Cascade')
plt.plot(A1,hill(A1,K1,n,1,0),label='Single Activator')
plt.plot(A1,hill_A3,label='FFL OR')
plt.plot(A1,hill_A4,label='FFL AND')
#plt.title(f'Cascades Multiply Sensitivity\nSlope: {slope_single:.2f} -> {slope_cascade:.2f}')
plt.xlabel('Input Concentration')
plt.ylabel('Final Output')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


