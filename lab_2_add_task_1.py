print('y = a*x^2+b*x+c')

a = int(input('Type the value of a: '))
b = int(input('Type the value of b: '))
c = int(input('Type the value of c: '))

d=(b**2)-(4*a*c)

if d < 0:
  print('No roots')
elif d == 0:
  x = (-1*b)/(2*a)
  print('x = ', x)
else:
  k = ((-1*b)+((d)**(1/2)))/(2*a)
  p = ((-1*b)-((d)**(1/2)))/(2*a)
  print('x(1) = ', k, end = '\n')  
  print('x(2) = ', p)