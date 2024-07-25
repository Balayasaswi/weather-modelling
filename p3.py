import numpy as np
import matplotlib.pyplot as plt

with open ('int.txt' ,'r') as f:
  a=float(f.readline())
  b=float(f.readline())
  c=float(f.readline())
  d=float(f.readline())
  e=float(f.readline())
  f=float(f.readline())


x = np.linspace(1, 10, 100)
y = a * x**2 + b * x + c


y1 = d * x**2 + e* x + f
plt.plot(x, y, c="red" ,label="set1:a=1,b=-7,c=12")


plt.plot(x, y1, c="blue", lw=1, marker="*",label="set2:d=1,e=-5,f=6")


plt.xlabel('Time in hrs')
plt.ylabel('Temperature in Celsius')
plt.title("Read from file")


plt.legend()




plt.show()
