import numpy as np
from scipy.sparse import spdiags
from scipy.sparse.linalg import spsolve, norm

def Bvp_DD(fcn, a, b, ua, ub, Nx):
    """ 
    Solution of 1D boundary value problem 
        -u" = fcn(x) for a < x < b
    with Dirichlet boundary conditions
        u(a) = ua,  u(b) = ub.
    on a uniform mesh
    """

    L = b-a                      # length of the domain
    dx = float(L)/float(Nx)      # length of the grid cell
    x = np.linspace(a, b, Nx+1)  # the grid
    u = np.zeros(Nx+1)           # the solution

    # The sparse matrix
    dia  = 2*np.ones(Nx-1) / dx**2
    low  = -np.ones(Nx-1) / dx**2
    upp  = -np.ones(Nx-1) / dx**2
    A = spdiags([low,dia,upp],[-1,0,1],Nx-1,Nx-1) 
    # print(A.todense())

    # evaluate right hand side
    rhs = np.zeros(Nx-1)         # the right hand side
    for j in range(Nx-1):
        rhs[j] = fcn(x[j+1])
    rhs[0]  -= low[0]*ua
    rhs[-1] -= upp[-1]*ub

    # solve the linear system
    u[0], u[-1]  = ua, ub
    u[1:-1] = spsolve(A, rhs)
    print(u)
    
    # return the grid and the numerical solution
    return u, x

def Bvp_DN(fcn, a, b, ua, ub, Nx):
    """ 
    Solution of 1D boundary value problem 
        -u" = fcn(x) for a < x < b
    with mixed boundary conditions
        u(a) = ua,  u'(b) = 0.
    on a uniform mesh
    """

    L = b-a                      # length of the domain
    dx = float(L)/float(Nx)      # length of the grid cell
    x = np.linspace(a, b, Nx+1)  # the grid
    u = np.zeros(Nx+1)           # the solution

    # The sparse matrix
    dia  = 2*np.ones(Nx) / dx**2
    low  = -np.ones(Nx) / dx**2
    upp  = -np.ones(Nx) / dx**2
    low[-2] = -2 / dx**2        # correct for left BC
    A = spdiags([low,dia,upp],[-1,0,1],Nx,Nx) 
    # print(A.todense())

    # evaluate right hand side
    rhs = np.zeros(Nx)          # the right hand side
    for j in range(Nx):
        rhs[j] = fcn(x[j+1])
    rhs[0]  -= low[0]*ua        # eliminate left BC

    # solve the linear system
    u[0] = ua                   # set left BC
    u[1:] = spsolve(A, rhs)
    
    # return the grid and the numerical solution
    return u, x

def Bvp_ND(fcn, a, b, ua, ub, Nx):
    """ 
    Solution of 1D boundary value problem 
        -u" = fcn(x) for a < x < b
    with mixed boundary conditions
        u'(a) = 0,  u(b) = 0.
    on a uniform mesh
    """

    L = b-a                      # length of the domain
    dx = float(L)/float(Nx)      # length of the grid cell
    x = np.linspace(a, b, Nx+1)  # the grid
    u = np.zeros(Nx+1)           # the solution

    # The sparse matrix
    dia  = 2*np.ones(Nx) / dx**2
    low  = -np.ones(Nx) / dx**2
    upp  = -np.ones(Nx) / dx**2
    upp[1] = -2 / dx**2        # correct for right BC
    A = spdiags([low,dia,upp],[-1,0,1],Nx,Nx) 
    # print(A.todense())

    # evaluate right hand side
    rhs = np.zeros(Nx)          # the right hand side
    for j in range(Nx):
        rhs[j] = fcn(x[j])
    rhs[-1] -= upp[0]*ub        # eliminate right BC

    # solve the linear system
    u[-1] = ub                  # set right BC
    u[:-1] = spsolve(A, rhs)
    
    # return the grid and the numerical solution
    return u, x

def demo_DD():
    Nx = 10     # Nx = number of grid cells, 
                # Nx+1 = number of grid points
    a = -1.     # a = left end of the domain
    b = +1.     # b = right end of the domain
    ua =-.5     # boundary value left side
    ub = .5     # boundary value right side 

    def fcn(x):
        return 5*x

    def exact(x):
        return x*(-5*x**2 + 8)/6
   
    import time 
    t0 = time.clock()
    u,x = Bvp_DD(fcn, a, b, ua, ub, Nx)
    t1 = time.clock()
    print('cpu time',t1-t0)

    # compute the error norm
    from scipy.linalg import norm
    print('approximation error', abs(norm(u-exact(x))))

    xx = np.linspace(a,b)
    sol = exact(xx)
 
    # generate a plot of the solution
    import matplotlib.pyplot as plt
    plt.plot(x,u,'bo-', linewidth=.5)
    plt.plot(xx,sol,'r-')
    plt.title('numerical solution')
    plt.grid()
    plt.show()

def demo_DN():
    Nx = 20 # Nx = number of grid cells, 
            # Nx+1 = number of grid points
    a = -1. # a = left end of the domain
    b = +1. # b = right end of the domain
    ua = .5 # boundary value left side
    ub = .0 # boundary value right side 

    def fcn(x):
        return 5*x

    def exact(x):
        return (5*x*(3 - x**2) + 13.)/6.

    import time
    t0 = time.clock()
    u,x = Bvp_DN(fcn, a, b, ua, ub, Nx)
    t1 = time.clock()
    print('cpu time',t1-t0)

    # compute the error norm
    from scipy.linalg import norm
    print('approximation error', abs(norm(u-exact(x))))

    xx = np.linspace(a,b)
    sol = exact(xx)
    print('abs point error at x=1:',abs(sol[-1] - u[-1]))
    print(exact(-1))
    print(exact(+1),23/6.)

    # generate a plot of the solution
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8,6))
    line1 = plt.plot(x,u,'--.')
    plt.setp(line1, linewidth=.5, color='blue')
    plt.plot(xx,sol,'r-')
    plt.title('numerical solution: $-u^{\prime\prime} = 5x, u(-1) = .5, u^{\prime}(1) = 0$.')
    plt.grid()
    plt.show()

def demo_ND():
    Nx = 20 # Nx = number of grid cells, 
            # Nx+1 = number of grid points
    a = -1. # a = left end of the domain
    b = +1. # b = right end of the domain
    ua = .0 # boundary value left side
    ub = .5 # boundary value right side 

    def fcn(x):
        return 5*x

    def exact(x):
        return (5*x*(3 - x**2) - 13.)/6. + 1.

    import time
    t0 = time.clock()
    u,x = Bvp_ND(fcn, a, b, ua, ub, Nx)
    t1 = time.clock()
    print('cpu time',t1-t0)

    # compute the error norm
    from scipy.linalg import norm
    print('approximation error', abs(norm(u-exact(x))))

    xx = np.linspace(a,b)
    sol = exact(xx)
    print('abs point error at x=-1:',abs(sol[0] - u[0]))

    # generate a plot of the solution
    import matplotlib.pyplot as plt
    plt.figure(figsize=(8,6))
    line1 = plt.plot(x,u,'--.')
    plt.setp(line1, linewidth=.5, color='blue')
    plt.plot(xx,sol,'r-')
    plt.title('numerical solution: $-u^{\prime\prime} = 5x, u^{\prime}(-1) = 0, u(1) = -.5$')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    demo_DD()
    demo_DN()
    demo_ND()
