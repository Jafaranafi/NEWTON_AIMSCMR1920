import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return np.exp(x)-x**2+3*x-2
def Bisection(f,a,b,tol):
	while (np.abs(a-b)>tol):
		c=(a+b)/2
		print(c)
		p=f(a)*f(c)
		if p>tol:
			a=c
		else:
			if p<tol:
				b=c
#			print (c)
	return c
A=Bisection(f,-2,0,1e-8)
#print(A)
x=np.linspace(-2,2,100)
#plt.plot(x,f(x),"r.-")
#plt.show()
