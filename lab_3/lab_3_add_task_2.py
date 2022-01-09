import numpy as np 

a = np.ndarray((5))

for d in range(0, 4, 1):
  a[d] = int(input('Type the volue: '))

c = int(input("Pepe i: "))

for i in range(4, -1, -1):
  d = i
  
  if c < i:
    a[i] = a [i-1]

a[c] = int(input('Type!!: '))

print(a)
