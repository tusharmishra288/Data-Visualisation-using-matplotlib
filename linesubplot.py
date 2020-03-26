
import numpy as np
import matplotlib.pyplot as plt
x=np.arange(1,10,2)
y=x
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title('graph1')
plt.subplot(1,2,2)
plt.plot(x,y+1)
plt.title('graph2')
plt.savefig('output/subplotline.jpeg')
plt.show()