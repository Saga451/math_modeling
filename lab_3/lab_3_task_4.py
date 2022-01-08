import numpy as np 

N = 7 #количество строк
M = 3 #кол-во столбцов

a = np.ndarray((N, M))
 
for i in range(0,N, 1):
  for j in range(0, M, 1):
   a[i, j] = np.sin(3 * i + 3 * j) 
   if a [i, j] < 0:
     a[i, j] = 0

print(a)