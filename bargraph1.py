
import matplotlib.pyplot as plt
import pandas as pd
r=pd.read_csv('realEstate_trans.csv')
x=r['baths']
y=r['beds']
fig=plt.figure(figsize=(9,5))
plt.bar(x,y,color='red')
plt.title("Bar graph")
plt.xlabel('baths')
plt.ylabel('beds')
plt.legend(["line1"],loc='best')
plt.savefig('output/bargraph1.jpeg')
plt.show()
