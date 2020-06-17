import numpy as np
from scipy.linalg import solve

def Bvp(fcn, a, b, ua, ub, Nx):
    """ 
    Solution of 1D boundary value problem 
        -u" = fcn(x) for a < x < b
    with boundary conditions
        u(a) = ua,  u(b) = ub.
    on a uniform mesh
    """

    L = b-a                     # length of the domain
    dx = float(L)/float(Nx)     # length of the grid cell
    x = np.linspace(a, b, Nx+1) # the grid
    u = np.zeros(Nx+1)          # solution

    # the matrix setup
    dia = 2.*np.ones(Nx+1) / dx**2
    off = np.ones(Nx) / dx**2
    A = np.diag(dia) - np.diag(off,-1) - np.diag(off,1)  
    A[0,0], A[0,1] = 1., 0.     # left boundary condition
    A[-1,-1], A[-1,-2] = 1., 0. # right boundary condition

    # evaluate right hand side
    rhs = np.zeros(Nx+1)        # right hand side
    for j in range(1,Nx):
        rhs[j] = fcn(x[j])
    rhs[0], rhs[-1] = ua, ub

    # solve the linear system
    u[:] = solve(A, rhs);
    
    # return grid and numerical solution
    return u, x

if __name__ == '__main__':
    Nx = 20 # Nx = number of grid cells, 
            # Nx+1 = number of grid points
    a = -1. # a = left end of the domain
    b = +1. # b = right end of the domain
    ua =-.5 # boundary value left side
    ub = .5 # boundary value right side 

    def fcn(x):
        return 5*x

    def exact(x):
        return x*(-5*x**2 + 8)/6

    import time
    t0 = time.clock()
    u,x = Bvp(fcn, a, b, ua, ub, Nx)
    t1 = time.clock()
    print('cpu time',t1-t0)

    # compute the error norm
    from scipy.linalg import norm
    print('approximation error', abs(norm(u-exact(x))))

    xx = np.linspace(a,b)
    sol = exact(xx)
 
    # generate a plot of the solution
    import matplotlib.pyplot as plt
    plt.plot(x,u,'bo-', linewidth=.8)
    plt.plot(xx,sol,'r-')
    plt.title('numerical solution, $-u^{\prime\prime} = f(x),\; u(-1)=-.5, u(1)=.5$')
    plt.grid()
    plt.legend(['numerical', 'exact'])
    plt.show()
    print('u[1:-1]')

