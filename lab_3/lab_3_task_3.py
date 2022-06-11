import numpy as np 
from lab_3_task_1 import g

x0 = 1
y0 = 1 
v0 = 1 

for t in np.linspace(0, 5, 11):

  x = x0 + v0 * t 
  y = y0 + v0 * t - (g * (t**2)) / 2

  tb = [t, x, y]
  print(tb)
 
