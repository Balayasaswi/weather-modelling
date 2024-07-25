import numpy as np
import matplotlib.pyplot as plt
a=1
b=-4
c=4
x=np.linspace(0,10,100)

y = a*x**2 + b*x + c
plt.plot(x,y,c="red",lw=2,label="hard coding")
plt.xlabel('Time in hrs')
plt.ylabel('Temperature as celsius')

plt.title("hard coding")
plt.show()