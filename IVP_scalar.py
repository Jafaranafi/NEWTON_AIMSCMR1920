import numpy as np

def Euler(fcn, Tspan, I, Nt):
   
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)  
    dt = t[1] - t[0]

    u[0] = I
    for n in xrange(Nt):
        u[n+1] = u[n] + dt*fcn( u[n], t[n] )
    return u, t

def Heun(fcn, Tspan, I, Nt):

    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)  
    dt = t[1] - t[0]

    u[0] = I
    for n in xrange(Nt):
        k1 = dt*fcn( u[n], t[n] )
        k2 = dt*fcn( u[n]+k1, t[n+1] )
        u[n+1] = u[n] + 0.5 * ( k1 + k2 )
    return u, t


def RK2(fcn, Tspan, I, Nt):

    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)  
    dt = t[1] - t[0]

    u[0] = I
    for n in xrange(Nt):
        k1 = dt*fcn( u[n], t[n] )
        u[n+1] = u[n] + dt*fcn( u[n]+0.5*k1, t[n]+0.5*dt ) 
    return u, t

def RK4(fcn, Tspan, I, Nt):

    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)  
    dt = t[1] - t[0]

    u[0] = I
    for n in xrange(Nt):
        k1 = dt*fcn( u[n], t[n] )
        k2 = dt*fcn( u[n]+0.5*k1, t[n] + 0.5*dt )
        k3 = dt*fcn( u[n]+0.5*k2, t[n] + 0.5*dt )
        k4 = dt*fcn( u[n]+k3, t[n+1] )
        u[n+1] = u[n] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0
    return u, t


if __name__ == '__main__':
    def fcn(u, t):
        return u*np.sin(t)

    def exact(t, I):
        return I*np.exp( 1 - np.cos(t) )
   
    Tspan = [0,10]; Nt = 100; I = -1.

    methods = [Euler, Heun, RK2, RK4]

    import matplotlib.pyplot as plt
    tt = np.linspace(Tspan[0], Tspan[1], 101)
    ex = exact(tt, I)

    import matplotlib.pyplot as plt
    for method in methods:
        u, t = method(fcn, Tspan, I, Nt)

        plt.plot(t, u,'o-',   label='numerical')
        plt.plot(tt, ex,'r-', label='exact')
        plt.title(method.__name__+': numerical solution')
        plt.grid(True)
        plt.legend(loc='best')
        plt.show()
        print method.__name__, 'dt, Error', 10./Nt, u[-1] - exact(Tspan[1],I)

