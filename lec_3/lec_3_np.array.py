import numpy as np 

a = [1, 2, 4]

b = np.array(a) #создание массива из списка 

print(type(a))
print(type(b))

print(a + a)
print(b + b)
print(b ** b)
print(b / b)
print(b - b)

print(b[-1])
print(a[-3])
