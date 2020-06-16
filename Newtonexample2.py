import numpy as np
from scipy.linalg import solve,norm
import matplotlib.pyplot as plt

def f(z):
    x1, x2 =z
    return np.array([x1-x2+1,x1**2+x2**2-4])

def Df(z):
    x1, x2 =z
    return np.array([[1,-1],[2*x1,2*x2]])
    #execute Newton method for the  system
print ('Output of Newton approximation method')
print ('No.     x           y        f_norm')
#def Solution(JacobianMatrix,Function):
z=np.array([0.8,1.8])
i=0
#while condition on iteration
while True:
    tol=1.e-7
    f_norm=norm(f(z),1)
    Solvefunction = solve(Df(z),-f(z))
    znew = z + Solvefunction
    print (i,":%10f:%10f" %(z[0],z[1]),":%10f"%(f_norm))
    i+=1
    if f_norm<tol:break
    else:
        z=znew

x1=np.linspace(-2,2)
x2=1+x1
f_2=-np.sqrt(4-x1**2)
f_3=np.sqrt(4-x1**2)

plt.plot(x1,x2,"b",label="$f_1(x1,x2)=x1-x2+1$")
plt.plot(x1,f_2,"g")
plt.plot(x1,f_3,"g",label="$f_2(x1,x2)=x1**2+x2**2-4$")
plt.plot(z[0],z[1],"r.-",label="Solution point")
plt.title("Continuation graph for two function")
plt.xlim(-2,2)
plt.ylim(-4,4)
plt.legend()
plt.grid()
plt.show()
