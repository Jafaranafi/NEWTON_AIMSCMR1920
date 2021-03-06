import numpy as np
from Euler_v1 import Euler 

def fcn(u, t):
    return u*np.sin(t)
    
def u_exact(t, I):
    return I*np.exp( 1 - np.cos(t) )

def visualize(u, t, I):
    import matplotlib.pyplot as plt
    plt.plot(t, u, 'r--o')
    t_fine = np.linspace(t[0], t[-1], 201) # for u_ex
    u_ex = u_exact(t_fine, I)
    # plt.hold(True)
    plt.plot(t_fine, u_ex, 'b-')
    plt.legend(['numerical','exact'], loc='lower left')
    plt.xlabel('t')
    plt.ylabel('u')
    plt.grid(True)
    dt = t[1] - t[0]
    plt.title('dt=%g' % dt)
    # umin = -8; umax = 0.5
    # plt.axis([t[0], t[-1], umin, umax])
    plt.savefig('tmp1.png'); plt.savefig('tmp1.pdf')
    plt.show()

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--I', type=float, default=-1.0)
parser.add_argument('--t0', type=float, default=0)
parser.add_argument('--te', type=float, default=10)
parser.add_argument('--Nt', type=int, default=50)
a = parser.parse_args()
I, t0, te, Nt = a.I, a.t0, a.te, a.Nt

print 'I, t0, te, Nt', I,t0,te,Nt

Tspan = [t0,te]
u, t = Euler(fcn, Tspan, I, Nt)
visualize(u, t, I)
