import numpy as np 

a = np.ndarray((5))

for d in range(0, 4, 1):
  a[d] = int(input('Type the volue: '))
  

print(a)

c = int(input("Pepe i: "))
a[c] = int(input('Type!!: '))

print(a)


for i in range(0, 5, 1):
  
  if c < i:
    a[i] = a [i-1]


print(a)
