#import numpy as np
#import matplotlib.pyplot as plt
#from IVP import RK2

#def fcn(u,t):
#    return [u[0]*(1-0.5*u[1]),u[1]*( 0.25*u[0]-0.75)]

#Nt = 200
#te = 25
#Tspan = [0,te]

#I1 = [2,2]
#I2 = [2.5,2.0]

#u, t = RK2(fcn, Tspan, I1, Nt)
#v, t = RK2(fcn, Tspan, I2, Nt)

#plt.figure()
#plt.plot(u[:,0],u[:,1],'b-',linewidth=1.)
#plt.plot(v[:,0],v[:,1],'b-',linewidth=1.)
#plt.title('RK2: limit cycle')
#plt.grid(True)
#plt.show()
#import numpy as np
#from scipy.optimize import fsolve

#def myFunction(z):
#   x = z[0]
#   y = z[1]
#   w = z[2]

#   F = np.empty((3))
#   F[0] = x**2+y**2-20
#   F[1] = y - x**2
#   F[2] = w + 5 - x*y
#   return F

#zGuess = np.array([1,1,1])
#z = fsolve(myFunction,zGuess)
#print(z)

#import matplotlib.pyplot as plt
#import numpy as np
#from scipy.optimize import fsolve
#def f(x):
#    y=2.0*x**2+3.0*x-10
#    return y
#x=np.linspace(-5,3)
##print(x)
#plt.plot(x,f(x))
#plt.plot(x,np.zeros(len(x)))
#plt.show()
#x=fsolve(f,1.0)
#print(x)
#x=fsolve(f,-2.0)
#print(x)

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve
#def f2(z):
#    x=z[0]
#    y=z[1]
#    f=np.zeros(z)
#    f[0]=2.0*x**(2.0/3.0)+y**(2.0/3.0)-9.0**(1.0/3.0)
#    f[1]=x**2/4.0+y**(0.5)-1.0
#    return f
#t=np.array([1,1])
#z=fsolve(f2,t)
#print(z)
#print(f2(z))
####def test_Newton_system1():
####	from numpy import cos, sin, pi, exp
####	def F(x):
####		return np.array([x[0]**2 - x[1] + x[0]*cos(pi*x[0]),x[0]*x[1] + exp(-x[1]) - x[0]**(-1.)])
####	def J(x):
####		return np.array([[2*x[0] + cos(pi*x[0]) - pi*x[0]*sin(pi*x[0]), -1],[x[1] + x[0]**(-2.), x[0] - exp(-x[1])]])
####		
####	expected = np.array([1, 0])
####	tol = 1e-4
####	def Newton_system():
####		x=np.array([2, -1])
####		eps=0.0001
####	
####	 return (F, J, x, eps)
####	 x, n = Newton_system()
####	print(n, x)
####	
####	error_norm = np.linalg.norm(expected - x, ord=2)
####	assert error_norm < tol, 'norm of error ={:g}'.format(error_norm)
####	print('norm of error ={:g}'.format(error_norm))
#def f(x):
#	f1=x[0]+2*x[1]
#	f2=1.5*x[0]-x[1]-0.5
#	return [f1,f2]
#x=fsolve(f,[1,1])
#print(x)

import numpy as np
from scipy.linalg import solve
#x=0.5, y=-1 
def myFcn(z):
	x, y = z
	return np.array([x**2+y**2-1, x-.5])
#def myJac(z):
#	x, y = z
#	return np.array([[2*x,2*y],[1,0]])
#zGuess = np.array([0.5,-1])
#zexact = np.array([.5,-np.sqrt(3)/2])
#print 'exact ', zexact
#print myJac(zGuess)
#print myFcn(zGuess)
#print 'Am coming'
#A= np.linalg.inv(myJac(zGuess))
#t=A.dot(myFcn(zGuess))
#p=zGuess-t
#print p
#print t
#print 'how are you'
#print A
#print ' '
#print 'Newton'
#z = zGuess
#dz = np.empty(2)
#print z
#n=6
#for k in range(n):
#    f = -myFcn(z)    
#    Df = myJac(z)    
#    dz = solve(Df, f)
#    z = z + dz
#    print z
#z[n+1]=z[n]-myFcn(z)/myJac(z)
#print (z)
import numpy as np
from scipy.linalg import solve
def myFcn(z):
	x, y = z
	return np.array([x**2+y**2-1, x-.5])
def myJac(z):
	x, y = z
	return np.array([[2*x,2*y],[1,0]])
zGuess = np.array([0.5,-1])
print myJac(zGuess)
print myFcn(zGuess)
print 'The inverse of the Jacobian matrix is'
A= np.linalg.inv(myJac(zGuess))
print A
print 'Note that the newton formular is  x[n+1]=x[n]-J(x,y)F(x,y)'
print 'J(x,y)F(x,y)=A.dot(myFcn(zGuess))'
t=A.dot(myFcn(zGuess))
p=zGuess-t
print 'The jacobia iteration is '
Q=list(zGuess)
mylist=[]
for k in range(6):
	p=zGuess-t
	zGuess=p
	t=A.dot(myFcn(zGuess))
	mylist.append(p)
	print p
	
#import numpy as np
#import matplotlib.pyplot as plt
#from scipy.optimize import fsolve
#def f(x):
#	return np.exp(x)-5*x
##x=np.linspace(-5,5,100)
#y=f(x)
#plt.plot(x,y)
#print (x)
#results=fsolve(f,5)
#print(results)
#plt.plot(x,y,"k")
#plt.plot(results[0], f(results[0]),'ko')
#plt.show()
#plt.plot(p, f(p))
#import numpy as np
#from scipy.linalg import solve
#print(mylist)
#def myFcn(z):
#   x, y = z
#   return np.array([x**2+y**2-1, x-.5])

#def myJac(z):
#   x, y = z
#   return np.array([[2*x,2*y],[1,0]])

#zGuess = np.array([0.5,-1])
#zexact = np.array([.5,-np.sqrt(3)/2])
#print 'exact ', zexact


#print ' '
#print 'Newton'
#z = zGuess
#dz = np.empty(2)
#print z
#for k in range(6):
#    f = -myFcn(z)    
#    Df = myJac(z)    
#    dz = solve(Df, f)
#    z = z + dz
#    print z
#	

