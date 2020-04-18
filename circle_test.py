import numpy as np
from scipy.linalg import norm
from newton import newton
from step import step

def f_circle(n, x):
    fx = np.zeros(n-1)
    fx[0] = x[0]**2 + x[1]**2 - 1.
    return fx

def fp_circle(n, x):
    fpx = np.zeros((n-1, n))

    #fpx[0,0] = 2.0 * x[0]
    #fpx[0,1] = 2.0 * x[1]
    fpx[0,:] = 2.0*x
    return fpx

def circle_test():

    step_max = 35
    step_num = 0
    xy = np.zeros((step_max,2))

    #  A: 
    #  Choose a starting point,
    #  Choose a starting "parameter",
    #  Call Newton to try to get starting point to satisfy implicit function
    #  while holding parameter fixed.

    n = 2
    x0 = np.array([ 0.5, -2.0 ])
    p0 = 0
    tol = 1.0e-05

    fx_norm = norm (f_circle ( n, x0 ), 1)
    print "  %2d  %14.6f  %14.6f  %8.2f"  % ( 0, x0[0], x0[1], fx_norm )

    status, x2 = newton ( n, x0, p0, f_circle, fp_circle, tol )

    step_num = step_num + 1

    xy[0] = x2
    fx_norm = norm ( f_circle ( n, x2 ), 1 )
    print "  %2d  %14.6g  %14.6g  %8.2e"  % ( step_num, x2[0], x2[1], fx_norm )
   
    #  B:
    #  X0 <= X2.
    #  Take a step from the current point X0.
    
    x0 = x2
    t0 = np.zeros(n)
    h = 0.15
 
    for step_num in range(1, step_max):

        status, x2, t2, p2 = step ( n, x0, t0, p0, f_circle, fp_circle, h, tol )

        if status != 0:
            print ' ' 
            print '  STEP failed!\n' 
            break

        xy[step_num] = x2
        fx_norm = norm ( f_circle ( n, x2 ), 1 )
        print('  %2d  %14.6g  %14.6g  %8.2e') % ( step_num, x2[0], x2[1], fx_norm )

        if p0 != p2:
            print ' ' 
            print "  Switching parameters from %d to %3d\n"  % ( p0, p2 )
            p0 = p2

        x0 = x2
        t0 = t2

    #
    #  Plot the points.
    #
    import matplotlib.pylab as plt
    plt.plot( xy[:,0], xy[:,1], 'r.-', markersize=12 )
    plt.grid()
    plt.xlim([-1.20,1.20])
    plt.ylim([-.79,1.1])
    plt.xlabel ( '<--- X --->', fontsize=12 ) 
    plt.ylabel ( '<--- Y --->', fontsize=12 )
    plt.title ('Points on the circle, by the continuation method.', fontsize=16 )
    plt.show()

    filename = 'circle_test.png'
    plt.savefig(filename)
    print '\n' 
    print '  Plot file saved as "%s"\n'  % filename 

    return

if __name__ == "__main__":
    circle_test()
