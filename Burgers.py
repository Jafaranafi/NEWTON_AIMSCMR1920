from numpy import *
from scipy.integrate import solve_bvp

""" Traveling wave for viscous Burgers equation """

nu = 0.05
L = 2.0
uL = 1.0
uR = 0.0
uM = .5*(uL+uR)
du = .5*(uL-uR)

def fun(t, u, p):
    return [ u[1], (u[0]-p)*u[1]/nu ]

def bc1(ua, ub, p):
    return [ua[0]-uL, ub[0]-uM, p-uM]

def bc2(ua, ub, p):
    return [ua[0]-uM, ub[0]-uR, p-uM]

x = linspace(-L, 0, 76)
u = zeros((2, x.size))
u[0] = uM

res1 = solve_bvp(fun, bc1, x, u, p=[.4])
x1 = linspace(-L, 0, 21)
u1 = res1.sol(x1)[0]

x = linspace(0, L, 76)
u[0] = uM

res2 = solve_bvp(fun, bc2, x, u, p=[.4])
x2 = linspace(0, L, 21)
u2 = res2.sol(x2)[0]

def exact(x):
    return uM - du*tanh(x/(4*nu))

xe = linspace(-L, L, 101)
ue = exact(xe)

import matplotlib.pyplot as plt
plt.plot(x1, u1, 'bo-', linewidth=1)
plt.plot(x2, u2, 'bo-', linewidth=1)
plt.plot(xe, ue, 'r-', linewidth=1,  label='exact')
plt.legend()
plt.title('Traveling wave solution for Burgers equation')
plt.xlabel("x")
plt.ylabel("y")
plt.grid()
plt.show()
