import numpy as np
#import matlibplot.pyplot as plt
import matplotlib.pyplot as plt
def f(x):
	return np.exp(x)-x**2+3*x-2
u=np.linspace(0,1,20)
u[0]=0
u[1]=0.5
for i in range(18):
	u[i+2]=u[i-1]-(f(u[i-1])*(u[i-1]-u[i-2]))/(f(u[i-1])-f(u[i-2]))
print(u)
#t=np.linspace(0,5,20)
#plt.plot(t,u,"r.-")
#plt.show()
