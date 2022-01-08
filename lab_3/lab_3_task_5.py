import numpy as np 
from lab_3_task_4 import *

for i in range(0, N, 1):
  b = a[i, 1]
  for j in range(0, M, 1):
    if a[i, j] == a[i, 0]:
      a[i, 1] = a[i, 0]  
      a[i, j] = b
      
print(a)
  