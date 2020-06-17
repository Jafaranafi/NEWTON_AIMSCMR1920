import numpy as np

I = -1; T = 10.; Nt = 40

dt = T/float(Nt)
t = np.linspace(0, T, Nt+1)
u = np.zeros(Nt+1)

u[0] = I
for n in range(Nt):
    u[n+1] = u[n]*( 1 + dt*np.sin(t[n]) )
    
import matplotlib.pyplot as plt
plt.figure()
plt.plot(t, u, 'r--o')
t_fine = np.linspace(0, t[-1], 101) # for u_ex
u_ex = I*np.exp( 1 - np.cos(t_fine) )
plt.xlabel('t')
plt.ylabel('u')
plt.plot(t_fine, u_ex, 'b-')
plt.legend(['numerical','exact'], loc='upper left')
dt = t[1] - t[0]
plt.title('dt=%g' % dt)
umin = 1.1*u_ex.min(); umax = 0.5
plt.axis([t[0], t[-1], umin, umax])
plt.grid(True)
plt.show()

