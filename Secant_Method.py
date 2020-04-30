import matplotlib.pyplot as plt
import numpy as np
def secant(f,x1,x2,tol,n):
#	i=0
#	u=np.zeros(10)
#	u[0]=x1
#	u[1]=x2
	for i in range(n):
		xnew=x2-(x2-x1)/(f(x2)-f(x1))*f(x2)
#		u[i+1]=xnew
#		xnew=(f(x2)*x1-f(x1)*x2)/(f(x2)-f(x1))
		if abs(xnew-x2)<tol:break
		else:
			x1=x2
			x2=xnew
		print(i,"%10f:%10f"%(xnew,abs(xnew-x2)))
	return i, xnew
def f(x):
	return np.exp(x)-np.cos(x)
x1=-2
x2=2
tol=1.e-19
n=20
i,xnew =secant(f,x1,x2,tol,n)
x=np.linspace(-2,2,20)
y=(np.exp(xnew)+np.sin(xnew))*(x-xnew)
print()
print(i,"%10f"%xnew)
plt.plot(x,f(x),label="Equation")
plt.plot(x,y,label="Tangent Line")
plt.plot(xnew,f(xnew),"r.-",label="Solution point")
plt.title("Continuation Method using Secant Graph")
plt.legend()
plt.show()
