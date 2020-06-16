import numpy as np
from scipy.linalg import solve,norm
import matplotlib.pyplot as plt
#This code the following system
#x+y+z=3
#x**2+y**2+z**2=5
#np.exp(x)+x*y-x*z=1
#Defined the function
def f(z1):
    x, y ,z=z1
    return np.array([x+y+z-3,x**2+y**2+z**2-5,np.exp(x)+x*y-x*z-1])
#Defined the Jacobian Matrix
def Df(z1):
    x, y , z=z1
    return np.array([[1,1,1],[2*x,2*y,2*z],[np.exp(x),x,-x]])
#execute Newton method for the  system
print ('Output of Newton approximation method')
print ('No.     x           y           z           f_norm')
z1=np.array([1,2,3.5])
i=0
while True:
    tol=1.e-7
    f_norm=norm(f(z1),1)
    Solvefunction = solve(Df(z1),-f(z1))
    znew = z1 + Solvefunction
    print (i,":%10f:%10f:%10f" %(z1[0],z1[1],z1[2]),":%10f"%(f_norm))
    i+=1
    if f_norm<tol:break
    else:
        z1=znew

