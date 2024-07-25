import numpy as np
import matplotlib.pyplot as plt

data = np.array([[0,1],[3,15],[7,30],[12,22],[16,18],[19,12],[24,10]])
x=data[:,0]
y = data[:,1]
coefficients = np.polyfit(x,y, 2)

a,b,c =coefficients
y1 = a*x**2 + b*x+ c
plt.scatter(x,y,label='actual data')
plt.plot(x,y1,color='red',label='quadratic model')
plt.xlabel('Time in hours')
plt.ylabel('Temperature in celcius')

plt.legend()
plt.show()