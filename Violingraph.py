
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[3,2,7,6,8]
z=[7,9,0,5,4]
data=list([x,y,z])
plt.violinplot(data,showmeans=True,showmedians=True)
plt.title('Violin plot')
plt.savefig('output/violingraph.jpeg')
plt.show()
#for PDF add an additional datatype having 0 and 1 only and notice the trend in the graph
