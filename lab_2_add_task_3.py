a = int(input('Type the number a: '))
print('b: ')
while a >= 0.1:
  b = a % 10
  print(b, end='')
  a = a // 10


''' (тоже работает)
a = int(input('type the volue: '))

b = a // 10
c = a % 10

while b != 0:
    print(f"{c}", end ='')
    c = b % 10
    b //= 10

print(f'{c}')
'''    