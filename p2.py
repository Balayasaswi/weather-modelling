import numpy as np
import matplotlib.pyplot as plt
a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=int(input("Enter the value of c: "))
x=np.linspace(1,10,100)

y = a*x**2 + b*x + c
plt.plot(x,y,c="red",lw=2)
plt.xlabel('Time in hrs')
plt.ylabel('Temperature as celsius')
plt.title("Key board input")

plt.show()