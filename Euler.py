import numpy as np
import matplotlib.pyplot as plt

def fcn(u,t):
    return -3*u + np.sin(2*t)

def exact(t):
    return (2*np.exp(3*(np.pi-t)) +  \
            3*np.sin(2*t) - 2*np.cos(2*t))/13
   
t0 = np.pi; te = 3*np.pi
Nt = 20
I = 0.

u = np.zeros(Nt+1)  
t = np.linspace(t0, te, Nt+1)
dt = t[1] - t[0]

u[0] = I
for n in range(Nt):
    u[n+1] = u[n] + dt*fcn( u[n], t[n] )

tt = np.linspace(t0, te, 101)
ex = exact(tt)

#plt.plot(t, u,'o-', tt, ex,'r-')
plt.plot(t, u,'o-')
plt.plot(tt, ex,'r-')
plt.xlabel('t'); plt.ylabel('u')
plt.title('Euler method, numerical solution')
plt.grid(True)
plt.savefig('Euler0.pdf',bbox_inches='tight')
plt.show()
