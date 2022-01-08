import numpy as np 
from lab_3_task_1 import g

x0 = 1
y0 = 1
v0 = 2

t = np.arange(0, 5, 0.5)

x = x0 + v0 * t
y = y0 + v0 * t - (g * t**2) / 2

a = [t, x, y]
b = np.array(a)

for d in range(1, 10, 1):
 c = slice = b[::, d]
 print(c, '\n')