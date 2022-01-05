print('a * (x ** 2) + b * x + c = 0') # решение квадратных уравнений

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

d = (b ** 2) - 4 * a * c
t = d ** (1/2)

if d < 0:
    print('There is no solution')
elif d == 0:
    e = -b / (2 * a) 
    print(f'There is one solution:{e}')
else: 
    f = (-b + t) / (2 * a)
    g = (-b - t) / (2 * a)
    print(f'There is two solutions: {f} and {g}')