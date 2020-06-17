from numpy import * 
from numpy.linalg import eig
from scipy.integrate import odeint
""" Robert's problem: stiff IVP """

def func(y, t):
    return [-.04*y[0] + 1.e4*y[1]*y[2],
             .04*y[0] - 1.e4*y[1]*y[2] - 3.e7*y[1]**2,
                                       + 3.e7*y[1]**2
            ]

def jac(y,t):
    return [[-.04, 1.e4*y[2],           1.e4*y[1]],
            [ .04,-1.e4*y[2]-6.e7*y[1],-1.e4*y[1]],
            [  0 ,           6.e7*y[1], 0       ]]

y0 = [1, 0, 0]
t = linspace(0, 40, 101)
sol1 = odeint(func, y0, t,
       rtol=1.e-3, atol=1e-5, full_output=False)
#sol1, infodict = odeint(func, y0, t,
#            rtol=1.e-3, atol=1e-5, full_output=True)

#print 'number of function evaluations', infodict['nfe']

ys = sol1[-1,:]
print 'check mass balance', ys[2]+ys[1]+ys[0]-1.0

import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(t,sol1[:,0], label='y1')
plt.plot(t,sol1[:,1], label='y2')
plt.plot(t,sol1[:,2], label='y3')
plt.legend(loc='best')
plt.grid(True)

#sol2 = odeint(func, y0, t, Dfun=jac,
#            rtol=1.e-3,atol=1e-5)
sol2, infodict = odeint(func, y0, t, Dfun=jac,
            rtol=1.e-3,atol=1e-5, full_output=True)

print 'number of function evaluations', infodict['nfe']
print 'number of Jacobian evaluations', infodict['nje']

ys = sol2[-1,:]
print 'check mass balance', ys[2]+ys[1]+ys[0]-1.0

#A = jac(ys,12)
#w, v = eig(A)
#print 'jac'
#print jac(ys,12)
#print 'eigenvectors and eigenvalues'
#print w; v


plt.figure(2)
plt.plot(t,sol2[:,0], label='y1')
plt.plot(t,sol2[:,1], label='y2')
plt.plot(t,sol2[:,2], label='y3')
plt.legend(loc='best')
plt.grid(True)
plt.savefig('roberts.eps',bbox_inches='tight')
plt.show()
