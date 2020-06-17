from math import pi 
import matplotlib.pyplot as plt
from Euler_sys import Euler

def demo_osszillator():
    """Test case oszillator model."""
    def fcn(u, t):
        u1, u2 = u
        return [ u2, -u1 ]

    dt = pi/10          # stepsize 
    Nt = int(5*pi/dt)   # number of steps
    Tspan = [0.,dt*Nt]  # Time range
    U0 = [1, 0]
    u, t = Euler(fcn, Tspan, U0, Nt)

    u1 = u[:,0]
    u2 = u[:,1]
    fig = plt.figure()
    plt.plot(t, u1, 'ro-', label='$u$')
    plt.plot(t, u2, 'bo-', label='$u^{\prime}$')
    plt.legend(loc='upper left')
    plt.xlabel('t')
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    demo_osszillator()
