import numpy as np 

a = np.ndarray((5)) #массив

for d in range(0, 4, 1): # значения элементов
  a[d] = int(input('Type the volue: '))

c = int(input("Choose the column of the last member: ")) #столбец, в который должны вставить последний элемент 

for i in range(4, -1, -1): #сдвиг элементов
  d = i
  if c < i:
    a[i] = a [i-1]

a[c] = int(input('Type the value of the last member: ')) #последний элемент

print(a)
