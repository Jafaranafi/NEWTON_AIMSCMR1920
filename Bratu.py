"""
solve the boundary value problem:
u1' = u2
u2' = -exp(u1)

u1(0) = 0, u1(1) = 0.
"""

import numpy as np

def fun(x, u):
    return [u[1], -np.exp(u[0])]

def bc(ua, ub):
    return [ua[0], ub[0]]

x = np.linspace(0, 1, 5)

u_a = np.zeros((2, x.size))
u_b = np.zeros((2, x.size))
u_b[0] = 3
#u_b[0] = 12*x*(1-x)

from scipy.integrate import solve_bvp
res_a = solve_bvp(fun, bc, x, u_a)
res_b = solve_bvp(fun, bc, x, u_b)

x_plot = np.linspace(0, 1, 51)
u_plot_a = res_a.sol(x_plot)[0]
u_plot_b = res_b.sol(x_plot)[0]

import matplotlib.pyplot as plt
plt.plot(x_plot, u_plot_a, 'b-', label='u_a')
plt.plot(x_plot, u_plot_b, 'r-', label='u_b')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("$y^{\prime\prime} + \exp(y) = 0$")
plt.grid()
plt.savefig('bratu.pdf')
plt.show()
