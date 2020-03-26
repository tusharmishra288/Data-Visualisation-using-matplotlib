
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[3,2,7,6,8]
z=[7,9,0,5,4]
data=list([x,y,z])
plt.boxplot(data,showmeans=True)
plt.title('Box plot')
plt.savefig('output/boxgrpah.jpeg')
plt.show()