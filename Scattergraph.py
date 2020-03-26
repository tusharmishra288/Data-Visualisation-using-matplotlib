
import matplotlib.pyplot as plt
a=[1,2,3,4,5]
b=[6,4,7,11,10]
x=[1,6,5,3,2]
plt.scatter(a,b,s=200,c='yellow',edgecolors='black',marker='o',alpha=1)
plt.scatter(a,x,s=200,c='orange',edgecolors='black',marker='1',alpha=1)
plt.legend(['b','x'],loc='best')
plt.title('scatter graph')
plt.xlabel('Xaxis')
plt.ylabel('Yaxis')
plt.savefig('output/scattergraph.jpeg')
plt.show()
