import numpy as np
import matplotlib.pyplot as plt

def Euler(fcn, I, Tspan, Nt):
   
    h = (Tspan[1] - Tspan[0])/float(Nt) 
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)  

    u[0] = I
    for n in range(Nt):
        u[n+1] = u[n] + h*fcn( u[n], t[n] )
    return u, t

def Heun(fcn, I, Tspan, Nt):

    h = (Tspan[1] - Tspan[0])/float(Nt)
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)  

    u[0] = I
    for n in range(Nt):
        k1 = h*fcn( u[n], t[n] )
        k2 = h*fcn( u[n]+k1, t[n+1] )
        u[n+1] = u[n] + 0.5 * ( k1 + k2 )
    return u, t


def RK2(fcn, I, Tspan, Nt):

    h = (Tspan[1] - Tspan[0])/float(Nt)
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)  

    u[0] = I
    for n in range(Nt):
        k1 = h*fcn( u[n], t[n] )
        u[n+1] = u[n] + h*fcn( u[n]+0.5*k1, t[n]+0.5*h ) 
    return u, t

def RK4(fcn, I, Tspan, Nt):

    h = (Tspan[1] - Tspan[0])/float(Nt)
    t = np.linspace(Tspan[0], Tspan[1], Nt+1)
    u = np.zeros(Nt+1)  

    u[0] = I
    for n in range(Nt):
        k1 = h*fcn( u[n], t[n] )
        k2 = h*fcn( u[n]+0.5*k1, t[n]+0.5*h )
        k3 = h*fcn( u[n]+0.5*k2, t[n]+0.5*h )
        k4 = h*fcn( u[n] + k3, t[n+1] )
        u[n+1] = u[n] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0
    return u, t


def fcn(u, t):
    return u

def exact(t, I):
    return I*np.exp(t)
   
Tspan = [0.,5.]
Nt = 150
I = 1.

u, x = RK2(fcn, I, Tspan, Nt)
print u[-1]-exact(5.,I)

xx = np.linspace(0, 5., 101)
ex = exact(xx, I)
plt.plot(x, u,'o-',   label='numerical')
plt.plot(xx, ex,'r-', label='exact')
#plt.legend('numerical solution','exact solution')
plt.title('RK2 method, numerical solution')
plt.grid(True)
plt.legend(loc='best')
plt.show()

