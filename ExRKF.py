#!/usr/bin/env python

"""A variety of methods to solve first order ordinary differential equations.

AUTHOR:
    Jonathan Senning <jonathan.senning@gordon.edu>
    Gordon College
    Based Octave functions written in the spring of 1999
    Python version: March 2008, October 2008
"""

import numpy
from RKF import RKF


if __name__ == "__main__":
    from pylab import *

    def f( u, t ):
        return u * numpy.sin( t )

    Tspan = [0.0, 10.0]
    I = -1.0

    Nt = 50
    t = numpy.linspace( Tspan[0], Tspan[1], Nt+1 )
    h = t[1] - t[0];

    # compute various numerical solutions
    u_rkf, t_rkf = RKF( f, Tspan, I, 1e-6, 1.0, 0.01 ) # unequally spaced t

    # compute true solution values in equal spaced and unequally spaced cases
    u = -numpy.exp( 1.0 - numpy.cos( t ) )
    urkf = -numpy.exp( 1.0 - numpy.cos( t_rkf ) )

#    figure( 1 )
    subplot( 1, 2, 1 )
    plot( t_rkf, u_rkf, 'r-o' )
    xlabel( '$t$' )
    ylabel( '$x$' )
    grid(True)
    title( 'Solutions of $dx/dt = x \sin t$, $x(0)=-1$ ($h = %4.2f$)' % h )
    legend( ( 'Runge-Kutta-Fehlberg' ), loc='lower left' )

#    figure( 2 )
    subplot( 1, 2, 2 )
    plot( t_rkf, u_rkf - urkf, 'r-o' )
    xlabel( '$t$' )
    ylabel( '$x - x^*$' )
    grid(True)
    title( 'Errors in solutions of $dx/dt = x \sin t$, $x(0)=-1$ ($h = %4.2f$)'
           % h )
    legend( ( 'Runge-Kutta-Fehlberg' ), loc='lower left' )
    subplots_adjust(left=0.10, right=0.95, wspace=0.35)

    show()
