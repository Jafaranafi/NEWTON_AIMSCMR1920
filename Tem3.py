import numpy as np
from scipy.linalg import solve
#from newton import newton


def f2(x,tau):
#	x[0],x[1],x[2],x[3],x[4],x[5]=x
	x[0]=0
	x[4]=0
	n = len(x)/2 - 1
	h2 = .5/n
	f = np.zeros(len(x))
	f[0] = x[0]
	f[1] = x[4]
	f[2] = x[2]-x[0] - h2*(x[0] + x[2])
	f[3] = x[3]-x[1] + h2*tau*(np.exp(x[0]) + np.exp(x[2]))
	f[4] = x[4]-x[3] - h2*(x[3] + x[4])
	f[5] = x[5]-x[4] + h2*tau*(np.exp(x[4]) + np.exp(x[5]))
	f[6] = x[6]-x[5] + h2*tau*(np.exp(x[5]) + np.exp(x[6]))
	f[7] = x[7]-x[6] + h2*tau*(np.exp(x[6]) + np.exp(x[7]))
	f[8] = x[8]-x[7] + h2*tau*(np.exp(x[7]) + np.exp(x[8]))
	f[9] = x[9]-x[8] + h2*tau*(np.exp(x[8]) + np.exp(x[9]))
	return f

def df2(x,tau):
#	x[0],x[1],x[2],x[3],x[4],x[5]=x
	x[0]=0
	x[4]=0
	n = len(x)
	h2 = .5/n
	df = np.zeros((n,n))
	n = len(x)/2 - 1
	df[0]=[1,0,0,0,0,0,0,0,0,0]
	df[1]=[0,0,0,0,1,0,0,0,0,0]
	df[2]=[-1,1,0,0,0,-0.5/2,-0.5/2,0,0,0]
	df[3]=[h2*tau*(np.exp(x[0])),h2*tau*(np.exp(x[2])),0,0,0,-1,1,0,0,0]
	df[4]=[0,-1,1,0,0,0,-0.5/2,-0.5/2,0,0]
	df[5]=[0,h2*tau*(np.exp(x[2])),h2*tau*(np.exp(x[3])),0,0,0,-1,1,0,0]
	df[6]=[0,0,-1,1,0,0,0,-0.5/2,-0.5/2,0]
	df[7]=[0,0,h2*tau*(np.exp(x[3])),h2*tau*(np.exp(x[4])),0,0,0,-1,1,0]
	df[8]=[0,0,0,-1,1,0,0,0,-0.5/2,-0.5/2]
	df[9]=[0,0,0,h2*tau*(np.exp(x[4])),h2*tau*(np.exp(x[5])),0,0,0,-1,1]



	return df
x0=np.array([0,0,0,0,0,0,0,0,0,0])
tau=1
print('To be implemented')
for i in range(20):
	s=solve(df2(x0,tau),-f2(x0,tau))
	x=x0+s
	x0=x
	print ("%10f:%10f:%10f:%10f:%10f:%10f:%10f:%10f:%10f:%10f:"%(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]))

    # df[i,j] =  ...


#if __name__ == "__main__":
#    from numpy.linalg import solve

#    tau = 3.0
#    x0 = np.zeros(6)

#    x = newton(f2, df2, x0)
