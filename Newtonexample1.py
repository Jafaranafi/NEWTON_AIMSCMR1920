import numpy as np
from scipy.linalg import solve,norm
import matplotlib.pyplot as plt
#This Code Solve the following system 
#x**3+y=1,
#y**3-x=-1
#Defined the function
def f(z):
    x, y =z
    return np.array([x**3+y-1,-x+y**3+1])
#Defined the Jacobian Matrix
def Df(z):
    x, y =z
    return np.array([[3*x**2,1],[-1,3*y**2]])
#execute the newton method
print ('Output of Newton approximation method')
print ('No.     x           y        f_norm')
z=np.array([0,0])
i=0
#begin  the newton iteration
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
#plotting the graph of the system
x=np.linspace(-2,2)
y=1-x**3
f_2=-x+y**3+1
plt.plot(x,y,"b",label="f_1(x,y)=x**3+y-1")
plt.plot(x,f_2,"g",label="$f_2(x,y)=y**3-x+1$")
plt.plot(z[0],z[1],"r.-",label="Solution point")
plt.title("Continuation graph for two function")
plt.xlim(-2,2)
plt.ylim(-2,2)
plt.legend()
plt.grid()
plt.show()
