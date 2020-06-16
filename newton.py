import numpy as np
from scipy.linalg import solve, norm
import matplotlib.pyplot as plt
def newton(f2,df2,m,tol,tau,x0):
	"Implemented of Newton method "
	c=[]
	for i in range(m):
		f_norm=norm(f2(x0,tau),2)
		c.append(f_norm)
		if f_norm<tol:
			break
		else:
			s=solve(df2(x0,tau),-f2(x0,tau))
			x=x0+s
			x0=x
			if i == m-1:
				print('Newton method fails to converge')
	print('The function converge to %10f'%f_norm)
	return c,x

