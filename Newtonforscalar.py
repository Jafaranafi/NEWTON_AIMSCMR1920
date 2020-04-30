import numpy as np
#This example is for example 1 of Newton method for one variable
import matplotlib.pyplot as plt
x=np.linspace(-2,2,100)
def newton(x0,f,g,n,tol):
	for i in range(n):
		x1=x0-f(x0)/g(x0)
		if abs(x1-x0)>tol:
			x0=x1
		print(i,":%10f:%10f:%10f" %(x1,f(x0),abs(x1-x0)))
	return x1,i
def f(x):
	return np.exp(x)-x**2+3*x-2
def g(x):
	return np.exp(x)-2*x+3
x1,i = newton(0,f,g,30,1.e-10)
x0=1
y=(np.exp(x1)-2*x1+3)*(x-x1)
print(x1,i)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("$x**2-1$")
plt.plot(x,y,"blue",label="Tangent line")
plt.plot(x,f(x),"green",label="Equation graph")
#plt.plot(x,p,"r.-")
plt.title("Continuation Graph using Newton method")
plt.plot(x1,f(x1),"r.-",label="Solution point")
#plt.plot(u,p,'r.-')
plt.legend()
plt.show()


