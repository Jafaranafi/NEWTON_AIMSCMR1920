import numpy as np
import matplotlib.pyplot as plt
def f(x):
	return np.exp(x)*np.cos(x)+np.sin(x)
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
plt.plot(x,f(x),"green")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Continuation Graph Using Bisection Method")
plt.plot(c,f(c),"r.-")
plt.show()
