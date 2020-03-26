
import matplotlib.pyplot as plt
x=['dog','cat','lion','tiger','deer']
y=[3,2,7,6,8]
plt.pie(y,labels=x,autopct='%.1f%%',shadow=True,startangle=90,explode=(0.1,0.1,0.1,0,0))
plt.title('Pie chart')
plt.savefig('output/piechart.png')
plt.show()
