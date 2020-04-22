import numpy as np
import matplotlib.pyplot as plt 
x=np.linspace(-2.0, 2.0, 15)
y=(x+1)*(x-0.5)
plt.plot(x,y ,'r.-')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
