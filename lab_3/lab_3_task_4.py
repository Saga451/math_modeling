import numpy as np 

N = 3 #количество строк
M = 3 #кол-во столбцов

a = np.ndarray((N, M))
 
for i in range(0,N, 1):
  for j in range(0, M, 1):
   a[i, j] = np.sin(N * (i + 1) + M * (j + 1))

   if a[i, j] < 0:
     a[i, j] = 0
   
print(a)


