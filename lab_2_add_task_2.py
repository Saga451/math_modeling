print('Hi, I can guess if there is a triangle with the sides you listed or not. Type the values of sides.')

a = int(input('First side of triangle: '))
b = int(input('Second side of triangle: '))
c = int(input('Third side of triangle: '))

if (a + b > c) and (b + c > a) and (a + c > b):
  print('Triangle exists')
  if a == c and a == b:
    print("Equilateral triangle") 
  elif a == c or a == b or b == c: 
    print('Isosceles triangle')
  else:
    print('Versatile triangle')
else:
  print("Triangle doesn't exist")