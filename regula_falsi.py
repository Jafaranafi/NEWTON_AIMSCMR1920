import matplotlib.pyplot as plt
import numpy as np
def secant(f,a,b,tol,n):
#	i=0
#	u=np.zeros(10)
#	u[0]=x1
#	u[1]=x2
	for i in range(n):
		x1=(a*f(b)-b*f(a))/(f(b)-f(a))
#		u[i+1]=xnew
#		xnew=(f(x2)*x1
#-f(x1)*x2)/(f(x2)-f(x1))
		if f(x1)<0:
			b=x1
		else:
			a=x1
		print(i,"%10f"%x1)
	return i,x1
def f(x):
	return x**3-4*x+1
a=0
b=1
tol=1.e-19
n=20
x=np.linspace(-2,2,20)
y=1-4*x
i,x1 =secant(f,a,b,tol,n)
print()
print(i,"%10f"%x1)
plt.ylabel("f(x)")
plt.xlabel("x")
plt.plot(x,f(x),label="Equation graph")
plt.plot(x1,f(x1),"r.-",label="Point of Solution")
plt.plot(x,y,label="Tangent line")
plt.legend()
plt.title("Continuation Method using Regular Falsi method")
plt.show()
