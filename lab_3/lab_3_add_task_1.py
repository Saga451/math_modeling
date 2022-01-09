import numpy as np 

N = int(input("Type the amount of strings: "))# количество строк и столбцов
M = int(input("Type the amount of columns: "))

a = np.ndarray((N, M)) #собственно массивы
c = np.ndarray((N, M))

for i in range(0, N, 1):  #первый массив 
 for j in range(0, M, 1):
   b = int(input(f"Type the value of a[{i}, {j}]: "))
   a[i, j] = b

print(a)

for i in range(0, N, 1): # второй массив
 for j in range(0, M, 1):
   b = int(input(f"Type the value of c[{i}, {j}]: "))
   c[i, j] = b

print(c)

d = np.ndarray((N, M))

for i in range(0, N, 1): # third array
  for j in range(0, M, 1):
    if a[i, j] > c[i, j]:
      d[i, j] = a[i, j]
    elif a[i, j] == c[i, j]:
      d[i, j] = 0
    else:
    #elif a[i, j] < c[i, j]:
      d[i, j] = c[i, j]

print('The third array is: ', '\n', d)
