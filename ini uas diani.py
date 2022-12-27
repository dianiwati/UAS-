#Metode Reimann

import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return 3 * np.exp (3*x)

a = float(input('batas bawah(a) = '))
b = float(input('batas atas(b) = '))
n = int(10)
x = np.linspace (a,b,n) 
dx = (x[-1]-x[0])/(n-1)

hasil = 0

for i in range (n-1) :
  hasil += dx*func(x[i])
print (hasil)

xp = np.linspace (a, b)
plt.plot (xp, func(xp))
for i in range (n-1) :
  plt.bar(x[i],func(x[i]), align = 'edge', width=dx, color = 'gray', edgecolor = 'red')
plt.show()

