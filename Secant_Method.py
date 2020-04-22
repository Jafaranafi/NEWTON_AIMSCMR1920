import matplotlib.pyplot as plt
import numpy as np
def secant(f,x1,x2,tol,n):
	i=0
	for i in range(n):
		xnew=x2-(x2-x1)/(f(x2)-f(x1))*f(x2)
		if abs(xnew-x2)<tol:break
		else:
			x1=x2
			x2=xnew
		print(i,"   %10f:   %10f"% (xnew,abs(x2-x1)))
	return i, xnew
def f(x):
	return np.exp(x)-x**2+3*x-2
x1=-2
x2=0
tol=1.e-11
n=20
i,xnew, =secant(f,x1,x2,tol,n)

print(i,"%10f"%xnew)
#plt.plot(p,f(p),"r")
#plt.show()
