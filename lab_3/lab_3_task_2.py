import numpy as np 
from lab_3_task_1 import *


h = 100 # m
a = np.pi / 3 
b = np.pi / 6

c = g * h * (np.tan(b))**2
d = 2 * (np.cos(a))**2
f = 1 - np.tan(b) * np.tan(a)

v = (c / (d * f)) ** (1/2)
print(v)

T = 200 #k
eps = 300 #Dj

a = 2 / (np.pi)**(1/2)
b = H / (k * T)**(3/2)
c = e ** (-e / (k * T))
d = e ** (T / 2)

N = a * b * c * d
print(N)