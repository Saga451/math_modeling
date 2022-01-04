c = int(input('Type the amount of Fibonachi members: '))
a = -1 
b = 1 
e = 1

while e <= c:
    d = a + b 
    print(f'{e}:', d)
    a = b
    b = d
    e += 1
   