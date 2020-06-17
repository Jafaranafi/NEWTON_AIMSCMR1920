import numpy as np
from Euler_v2 import Euler 

def fcn(u, t):
    return -3*u + np.sin(2*t)
    
def u_exact(t):
    return (3*np.sin(2*t) - 2*np.cos(2*t) + 2*np.exp(-3*t))/13.

def visualize(u, t):
    import matplotlib.pyplot as plt
    plt.plot(t, u, 'r--o')
    t_fine = np.linspace(t[0], t[-1], 201) # for u_ex
    u_ex = u_exact(t_fine)
    # plt.hold(True)
    plt.plot(t_fine, u_ex, 'b-')
    plt.legend(['numerical','exact'], loc='lower left')
    plt.xlabel('t')
    plt.ylabel('u')
    plt.grid(True)
    dt = t[1] - t[0]
    plt.title('dt=%g' % dt)
    umin = -.4; umax = .4
    plt.axis([t[0], t[-1], umin, umax])
    plt.savefig('tmp2.png'); 
    plt.show()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--I', type=float, default=0)
parser.add_argument('--t0', type=float, default=0)
parser.add_argument('--te', type=float, default=10)
parser.add_argument('--Nt', type=int, default=50)
a = parser.parse_args()
I, t0, te, Nt = a.I, a.t0, a.te, a.Nt

print I,t0,te,Nt

Tspan = [t0,te]

u, t = Euler(fcn, Tspan, I, Nt)
visualize(u, t)
