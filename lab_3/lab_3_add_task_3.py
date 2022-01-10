import numpy as np 

N = int(input('Type the amount of strings: ')) # кол-во строк и столбцов
M = int(input('Type the amount of columns: '))

a = np.ndarray((N, M)) # основной массив 
c = np.ndarray((M)) # маленький массивчик, для того чтобы максимальные значения писать в конце - после основного массива, а не сразу после введния данных одного столбца

for j in range(0, M, 1): # для ввода членов
  d = 0
  for i in range(0, N, 1):
    a[i, j] = b = int(input(f'Type the value of the member a[{i}, {j}]: '))
    
    if b >= d: # для определения максимального значения 
      c[j] = d = b  
    elif b < d:
      c[j] = d = d 
  
  #b = np.max(a[i, j])  - вместо тысячи слов...
  
print(a) 
print('Max members:')

for j in range(0, M, 1): 
  print(f'-Column number {j}:', c[j])

