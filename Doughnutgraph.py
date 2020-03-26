
import matplotlib.pyplot as plt
x=['dog','cat','lion','tiger']
y=[3,2,7,6]
z=[4]
a,b,c,d=[plt.cm.Reds,plt.cm.Blues,plt.cm.Greens,plt.cm.Oranges]
pie1=plt.pie(y,labels=x,radius=1.0,colors=[a(0.5),b(0.7),c(1.0),d(1.5)])
pie2=plt.pie(z,radius=0.5,colors='y')
plt.title('Doughnut chart')
plt.savefig('output/doughnutchart.png')
plt.show()

