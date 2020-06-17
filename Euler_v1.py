import numpy as np

def Euler(fcn, Tspan, I, Nt):
    """
    Solve u' = fcn(u,t) for t in Tspan = [t0,te], 
    u(t0) = I by a simple finite difference method.
    """
    dt = (Tspan[1]-Tspan[0])/float(Nt)
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)

    u[0] = I
    for n in range(Nt):
        dt = t[n+1] - t[n]
        u[n+1] = u[n] + dt*fcn( u[n], t[n] )
    
    return u, t

def visualize(u, t, I):
    import matplotlib.pyplot as plt
    plt.plot(t, u, 'r--o')
    t_fine = np.linspace(0, t[-1], 101) # for u_ex
    u_ex = u_exact(t_fine, I)
    plt.plot(t_fine, u_ex, 'b-')
    plt.legend(['numerical','exact'], loc='upper left')
    plt.xlabel('t')
    plt.ylabel('u')
    plt.grid(True)
    dt = t[1] - t[0]
    plt.title('dt=%g' % dt)
    umin = 1.1*u_ex.min(); umax = 0.5
    plt.axis([t[0], t[-1], umin, umax])
    plt.grid(True)
    plt.savefig('tmp1.eps'); plt.savefig('tmp1.pdf')
    plt.show()

if __name__ == '__main__':
    def fcn(u, t):
        return u*np.sin(t) 

    def u_exact(t, I):
        return I*np.exp( 1 - np.cos(t) )

    I = -1;  Tspan = [0,10]; Nt = 50

    u, t = Euler(fcn, Tspan, I, Nt)
    visualize(u , t , I)
