import numpy as np
import matplotlib.pyplot as plt
def f(x):
#	return np.exp(x)-5*x**2
	return 2*x**2-5*x+3
def g(x):
	return (np.exp(x)/5)**(0.5)
	return (2*x**2+3)/5
tol=0.0000001
i=0
x=1
x0=0
while(abs(x-x0)>tol):
	x0=x
	x=g(x)
	print(i,"   %10f:   %10f"% (x,abs(x-x0)))
	i=i+1

