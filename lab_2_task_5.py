a = int(input('Вводите делимое: '))
b = int(input('Вводите делитель: '))

c = a / b
print('Частное: ', c)

d = a % b 

if d==0:
  print('Делится без остатка')
else:
  print('Делится с остатком.')   

print('Остаток: ', d)