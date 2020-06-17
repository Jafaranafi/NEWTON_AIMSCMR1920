import numpy as np
import matplotlib.pyplot as plt

def Euler(fcn, Tspan, I, Nt):
   
    dt = (Tspan[1] - Tspan[0])/float(Nt) 
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)

    f_ = lambda u, t: np.asarray(fcn(u, t))
    if isinstance(I, (float, int)):
        u = np.zeros(Nt+1)  # u[n] is the numerical solution
    else:
        I = np.asarray(I)
        neq = I.size
        u = np.zeros((Nt+1, neq))

    u[0] = I
    for n in xrange(Nt):
        u[n+1] = u[n] + dt*f_( u[n], t[n] )
    return u, t

if __name__ == "__main__":
    def fcn(u, t):
        return np.array([u[1], -u[0]])
        #return np.stack((u[1], -u[0]))
        return [u[1], -u[0]]

    def exact(t):
        return np.cos(t)
   
    Tspan = [0.,4*np.pi]
    Nt = 50
    I = np.stack((1.,0.))

    plt.figure(figsize=(6,3))
    for Nt in [50, 100]:
        u, x = Euler(fcn, Tspan, I, Nt)
        if Nt == 25:
            st = '$\pi/25$'
        else:
            st = '$\pi/50$'
        plt.plot(x, u[:,0],'o-',   label=st)

    xx = np.linspace(0, 4*np.pi, 101)
    ex = exact(xx)

    plt.plot(xx, ex,'r-', label='exact')
    plt.legend(loc='best')
    plt.title('Euler method, simple system of ODEs')
    plt.grid(True)
    plt.show()

