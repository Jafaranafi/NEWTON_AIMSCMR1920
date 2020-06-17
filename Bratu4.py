"""
solve the boundary value problem:
u1' = u2
u2' = -lam*exp(u1)

u1(0) = 0, u1(1) = 0.
"""

import numpy as np

lam = 2.0;

def fun(x, u):
    return [u[1], -lam*np.exp(u[0])]

def bc(ua, ub):
    return [ua[0], ub[0]]

x = np.linspace(0, 1, 5)

u_a = np.zeros((2, x.size))
u_b = np.zeros((2, x.size))
u_a[0] = 1/lam*np.sin(np.pi*x)
u_b[0] = lam*np.sin(np.pi*x)

from scipy.integrate import solve_bvp
res_a = solve_bvp(fun, bc, x, u_a)
res_b = solve_bvp(fun, bc, x, u_b)

x_plot = np.linspace(0, 1, 51)
u_plot_a = res_a.sol(x_plot)[0]
u_plot_b = res_b.sol(x_plot)[0]
print(u_plot_b)
print(u_plot_a)
import matplotlib.pyplot as plt
plt.plot(x_plot, u_plot_a, 'b-', label='u_a')
plt.plot(x_plot, u_plot_b, 'r-', label='u_b')
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Bratu: $u^{\prime\prime} + \lambda \exp(u) = 0,\; u(0)=u(1)=0,\;\lambda=2$")
plt.grid()
plt.savefig('bratu.pdf')
plt.show()
