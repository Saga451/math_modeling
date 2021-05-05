a = int(input('Type the number a: '))
print('b: ')
while a >= 0.1:
  b = a % 10
  print(b, end='')
  a = a // 10