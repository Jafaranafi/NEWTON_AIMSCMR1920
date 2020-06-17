import numpy as np

def Euler(fcn, Tspan, I, Nt):
    """
    Solve u' = fcn(u,t) for t in Tspan = [t0,te], 
    u(t0) = I by a simple finite difference method.
    """
    dt = (Tspan[1]-Tspan[0])/float(Nt)
    u = np.zeros(Nt+1)
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)

    u[0] = I
    for n in range(Nt):
        u[n+1] = u[n] + dt*fcn( u[n], t[n] )
    return u, t

def test_four_steps():
    def fcn(u, t):
        return u*np.sin(t)

    def u_exact(t, I):
        return I*np.exp( 1 - np.cos(t) )

    I = -1.; Nt = 5; Tspan = [0,1]
    u_by_hand = np.array([-1.0000000000000000 ,
                          -1.0000000000000000 ,
                          -1.0397338661590123 ,
                          -1.1207121538793736 ])
    u , t = Euler(fcn, Tspan, I , Nt)
    diff = np.abs(u_by_hand - u[:4]).max()
    tol = 1E-15
    assert diff < tol

if __name__ == '__main__':
    test_four_steps()
