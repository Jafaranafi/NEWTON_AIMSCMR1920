import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return np.exp(x)*np.cos(x)+np.sin(x)/(1+np.cos(x))
#	return x
def Bisection(f,a,b,tol,n):
#	while (np.abs(a-b)>tol):
	for i in range(n):
#		if np.abs(a-b)>tol:
		if i<=n :

			c=(a+b)/2
#		print(c)
			p=f(a)*f(c)
			if p>0:
				a=c
			else:
				if p<0:
					b=c
		print (i,"   %10f:%10f"%(c,p))
	return i,c
i,c=Bisection(f,-2,2,1e-28,40)
#print(i,"   %10f"%c)

x=np.linspace(-2,2,100)
#t=-np.exp(c)*np.sin(c)+np.exp(c)*np.cos(c)
#T=(1+np.cos(c))*np.cos(c)-np.sin(c)*(-np.sin(c))
#y=((t+T)/(1+np.cos(c)**2))*(x-c)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Continuation Graph using Bisection")
plt.plot(c,f(c),"r.-",label="Soluion Point")
plt.plot(x,f(x),label="Equation Graph")
#plt.plot(x,y,label="Tangent Line")
plt.legend()
plt.show()
