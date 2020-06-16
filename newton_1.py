import numpy as np
from numpy.linalg import norm, solve

def newton(fcn, dfcn, x0):
    """ Sample implementation of Newton method """ 
    tol = 1.e-7
    itmax = 400

    x = x0
    for it in range(itmax):
        f = fcn(x)
        if norm(f,2) < tol:
            break

        df = dfcn(x)
        delx = solve(df, -f)
        if norm(f,2) < tol:
            break
        x = x + delx
    if it == itmax-1:
        print('Newton method fails to converge')
    return x 
    #Noted that 
#    x_1(0.5)=x1
#    x_1(0)=x_1
#    x_2(0)=x_2
#    x_2(0.5)=x2

if __name__ == "__main__":
    def fcn(z1):
        x1,x2= z1
        x_1=1
        x_2=1
        T=1

        return np.array([x1-x_1-0.5/2*(x_2+x2),x2-x_2-0.5/2*(-T*np.exp(x_1)-T*np.exp(x1))])

    def dfcn(z1):
        x1,x2=z1
        x_1=1
        x_2=1
        T=1
        J = np.array([[1,-0.5/2],[0.5/2*T*np.exp(x1),1]])
        return J
#   x0 = np.array([0,1.8])
    x0 = np.array([0,0])

    # execute Newton method for the extended system
    print('Newton method')
    print('initial guess',x0)
    
    x = newton(fcn, dfcn, x0)

    print('')
    print('The solution', x)
    print('')
    print('The function', fcn(x))

