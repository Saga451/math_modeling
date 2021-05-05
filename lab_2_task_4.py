a = int(input('Enter the number: '))

while a >= 0:
  b = (((1+5**(1/2))/2)**a - ((1-5**(1/2))/2)**a)/(5**(1/2))
  print('b(', a, '): ', b)
  a -= 1

