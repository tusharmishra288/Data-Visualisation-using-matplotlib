
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,10,2)
y=x
plt.plot(x,y,linewidth=2.0,linestyle=':',color='red',alpha=0.5,marker='o')
plt.plot(x,y+3,linewidth=2.0,linestyle='-',color='blue',alpha=0.5,marker='x')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend(['line1','line2'],loc='best')
plt.grid(True)
plt.savefig('output/linegraph.jpeg')
plt.show()