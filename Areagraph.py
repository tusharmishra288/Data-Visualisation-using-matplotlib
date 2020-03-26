
import matplotlib.pyplot as plt
x=[1,2,3,4,7]
y=[1,4,5,6,5]
plt.stackplot(x,y,color='g',alpha=0.5)
plt.plot(x,y,color='m')
plt.title('Area plot')
plt.legend(['area1'],loc='best')
plt.grid(True)
plt.savefig('output/areagraph.png')
plt.show()
