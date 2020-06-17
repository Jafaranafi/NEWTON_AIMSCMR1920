"""
Functions for solving a systems of initial value problems:

      u_t = f( u, t ) on t in [t0,te]

with initial conditions u(t0) = I.

Note: The implementation is for equidistant grids, i.e.
      constant stepsize h.

The following naming convention of variables are used.

===== ==========================================================
Name  Description
===== ==========================================================
fcn   right hand side of the ODE.
I     Initial condition u(t0) = I.
Tspan The time interval for the solution, i.e.  Tspan = [t0,te].
Nt    The total number of mesh cells; mesh points are numbered
      from 0 to Nt.
t     Mesh points in time.
n     Index counter in time.
u     Unknown at current/new time level.
dt    Constant mesh spacing in t.
===== ==========================================================
                                                             
Note: The implementation is for equidistant grids, i.e.
      constant stepsize h.
"""
import numpy as np

def Euler(fcn, Tspan, I, Nt):
   
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    dt = t[1] - t[0]

    f_ = lambda u, t: np.asarray(fcn(u, t))
    if isinstance(I, (float, int)):
        u = np.zeros(Nt+1)  # u[k] is the numerical solution
    else:
        I = np.asarray(I)
        neq = I.size
        u = np.zeros((Nt+1, neq))

    u[0] = I
    for n in xrange(Nt):
        u[n+1] = u[n] + dt*f_( u[n], t[n] )
    return u, t

def Heun(fcn, Tspan, I, Nt):

    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    dt = t[1] - t[0]

    f_ = lambda u, t: np.asarray(fcn(u, t))
    if isinstance(I, (float, int)):
        u = np.zeros(Nt+1)  # u[k] is the numerical solution
    else:
        I = np.asarray(I)
        neq = I.size
        u = np.zeros((Nt+1, neq))

    u[0] = I
    for n in xrange(Nt):
        k1 = dt*f_( u[n], t[n] )
        k2 = dt*f_( u[n]+k1, t[n+1] )
        u[n+1] = u[n] + 0.5 * ( k1 + k2 )
    return u, t


def RK2(fcn, Tspan, I, Nt):

    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    dt = t[1] - t[0]

    f_ = lambda u, t: np.asarray(fcn(u, t))
    if isinstance(I, (float, int)):
        u = np.zeros(Nt+1)  # u[k] is the numerical solution
    else:
        I = np.asarray(I)
        neq = I.size
        u = np.zeros((Nt+1, neq))

    u[0] = I
    for n in xrange(Nt):
        k1 = dt*f_( u[n], t[n] )
        u[n+1] = u[n] + dt*f_( u[n]+0.5*k1, t[n]+0.5*dt )
    return u, t

def RK4(fcn, Tspan, I, Nt):

    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    dt = t[1] - t[0]

    f_ = lambda u, t: np.asarray(fcn(u, t))
    if isinstance(I, (float, int)):
        u = np.zeros(Nt+1)  # u[k] is the numerical solution
    else:
        I = np.asarray(I)
        neq = I.size
        u = np.zeros((Nt+1, neq))
 
    u[0] = I
    for n in xrange(Nt):
        k1 = dt*f_( u[n], t[n] )
        k2 = dt*f_( u[n] + 0.5*k1, t[n] + 0.5*dt )
        k3 = dt*f_( u[n] + 0.5*k2, t[n] + 0.5*dt )
        k4 = dt*f_( u[n] + k3, t[n+1] )
        u[n+1] = u[n] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0
    return u, t

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    def fcn(u, t):
        # return np.stack((u[1], -u[0]))
        return [u[1], -u[0]]

    def exact(t):
        return np.cos(t)
   
    Tspan = [0.,2*np.pi]
    Nt = 50
    I = np.stack((1.,0.))

    for method in [Euler, Heun, RK2, RK4]:
        u, t = method(fcn, Tspan, I, Nt)

        tt = np.linspace(0, 2*np.pi, 101)
        ex = exact(tt)
        plt.plot(t, u[:,0],'o-',   label='numerical')
        plt.plot(tt, ex,'r-', label='exact')
        plt.title(method.__name__+': harmonic oszillator')
        plt.grid(True)
        plt.legend(loc='best')
        plt.show()

