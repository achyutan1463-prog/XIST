import matplotlib.pyplot as plt
import numpy as np
R=1
Rtotal = R
n1p = 2
K1p = 1
x = np.linspace(0, 1000, 100000)
y = np.linspace(0, 1000, 100000)
total_activator1, total_activator3 = x,y

K=[0.1,0.5,0.9,10]
R=[0.25,0.5,0.75,1]
c=["magenta","green","black","blue"]
for i in range(len(c)):
 freeA1=(total_activator1-K[i]-Rtotal + ((total_activator1-K[i]-Rtotal)**2 + 4*K[i]* total_activator1)**0.5)/2
 AR =  (freeA1**n1p) / ((K1p**n1p) + (freeA1**n1p))
 plt.plot(total_activator1, AR, label=str(K[i]),color = c[i])

plt.xlabel('Activator conc')
plt.ylabel('OFF to ON')
plt.xlim(0, 5) # Adjust the 10 to whatever looks best!
plt.legend()
plt.show()