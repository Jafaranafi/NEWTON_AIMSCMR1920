#!/usr/bin/env python
  
"""A variety of methods to solve first order ordinary differential equations.

Adapted from:
    Jonathan Senning <jonathan.senning@gordon.edu>
    Gordon College
    Based Octave functions written in the spring of 1999
    Python version: March 2008, October 2008
"""

import numpy 

def RKF(f, Tspan, I, tol, hmax, hmin):
    """Runge-Kutta-Fehlberg method to solve u' = f(u,t) with u(t[0]) = I.

    USAGE:
        u, t = RKF(f, Tspan, I, tol, hmax, hmin)
    
    INPUT:
        f     - function equal to du/dt = f(u,t)
        Tspan - initial and endpoint of interval 
        I     - initial u value: I = u(t0)
        tol   - maximum value of local truncation error estimate
        hmax  - maximum step size
        hmin  - minimum step size

    OUTPUT:
        u     - NumPy array of corresponding solution function values
        t     - NumPy array of independent variable values

    NOTES:
        This function implements 4th-5th order Runge-Kutta-Fehlberg Method
        to solve the initial value problem

           du
           -- = f(u,t),     u(te) = I
           dt

        on the interval t in Tspan = [t0,te].

        Based on pseudocode presented in "Numerical Analysis", 6th Edition,
        by Burden and Faires, Brooks-Cole, 1997.
    """

    # Coefficients used to compute the independent variable argument of f

    a2  =   2.500000000000000e-01  #  1/4
    a3  =   3.750000000000000e-01  #  3/8
    a4  =   9.230769230769231e-01  #  12/13
    a5  =   1.000000000000000e+00  #  1
    a6  =   5.000000000000000e-01  #  1/2

    # Coefficients used to compute the dependent variable argument of f

    b21 =   2.500000000000000e-01  #  1/4
    b31 =   9.375000000000000e-02  #  3/32
    b32 =   2.812500000000000e-01  #  9/32
    b41 =   8.793809740555303e-01  #  1932/2197
    b42 =  -3.277196176604461e+00  # -7200/2197
    b43 =   3.320892125625853e+00  #  7296/2197
    b51 =   2.032407407407407e+00  #  439/216
    b52 =  -8.000000000000000e+00  # -8
    b53 =   7.173489278752436e+00  #  3680/513
    b54 =  -2.058966861598441e-01  # -845/4104
    b61 =  -2.962962962962963e-01  # -8/27
    b62 =   2.000000000000000e+00  #  2
    b63 =  -1.381676413255361e+00  # -3544/2565
    b64 =   4.529727095516569e-01  #  1859/4104
    b65 =  -2.750000000000000e-01  # -11/40

    # Coefficients used to compute local truncation error estimate.  These
    # come from subtracting a 4th order RK estimate from a 5th order RK
    # estimate.

    r1  =   2.777777777777778e-03  #  1/360
    r3  =  -2.994152046783626e-02  # -128/4275
    r4  =  -2.919989367357789e-02  # -2197/75240
    r5  =   2.000000000000000e-02  #  1/50
    r6  =   3.636363636363636e-02  #  2/55

    # Coefficients used to compute 4th order RK estimate

    c1  =   1.157407407407407e-01  #  25/216
    c3  =   5.489278752436647e-01  #  1408/2565
    c4  =   5.353313840155945e-01  #  2197/4104
    c5  =  -2.000000000000000e-01  # -1/5

    # Set t and u according to initial condition and assume that h starts
    # with a value that is as large as possible.

    t = Tspan[0]
    b = Tspan[1]
    u = I
    h = hmax

    # Initialize arrays that will be returned

    T = numpy.array( [t] )
    U = numpy.array( [u] )

    while t < b:

        # Adjust step size when we get to last interval

        if t + h > b:
            h = b - t;

        # Compute values needed to compute truncation error estimate and
        # the 4th order RK estimate.

        k1 = h * f( u, t )
        k2 = h * f( u + b21 * k1, t + a2 * h )
        k3 = h * f( u + b31 * k1 + b32 * k2, t + a3 * h )
        k4 = h * f( u + b41 * k1 + b42 * k2 + b43 * k3, t + a4 * h )
        k5 = h * f( u + b51 * k1 + b52 * k2 + b53 * k3 + b54 * k4, t + a5 * h )
        k6 = h * f( u + b61 * k1 + b62 * k2 + b63 * k3 + b64 * k4 + b65 * k5, \
                    t + a6 * h )

        # Compute the estimate of the local truncation error.  If it's small
        # enough then we accept this step and save the 4th order estimate.

        r = abs( r1 * k1 + r3 * k3 + r4 * k4 + r5 * k5 + r6 * k6 ) / h
        if len( numpy.shape( r ) ) > 0:
            r = max( r )
        if r <= tol:
            t = t + h
            u = u + c1 * k1 + c3 * k3 + c4 * k4 + c5 * k5
            T = numpy.append( T, t )
            U = numpy.append( U, [u], 0 )


        # Now compute next step size, and make sure that it is not too big or
        # too small.

        h = h * min( max( 0.84 * ( tol / r )**0.25, 0.1 ), 4.0 )

        if h > hmax:
            h = hmax
        elif h < hmin:
            print "Error: stepsize should be smaller than %e." % hmin
            break

    # endwhile

    return ( U, T )

if __name__ == "__main__":
    from math import pi
    import numpy as np
    import matplotlib.pyplot as plt
    def fcn(u, t):
        return u*np.sin(t)

    def exact(t, I):
        return I*np.exp( 1 - np.cos(t) )

    Tspan = np.array([pi,3*pi])
    Nt = 50
    I = 0.
    tol = 1.e-5

    u, x = RKF(fcn, Tspan, I, tol, 0.5, 0.01)

    xx = np.linspace(0, 10, 101)
    ex = exact(xx, I)
    plt.figure(1)
    plt.plot(x, u,'o-',   label='numerical')
    plt.plot(xx, ex,'r-', label='exact')
    plt.title('RKF method, numerical solution')
    plt.grid(True)
    plt.legend(loc='best')
    plt.show()
    plt.figure(2)
    t = np.linspace(0, 10, len(x))
    plt.plot(t, x,'o-')
    plt.grid(True)
    plt.show()

