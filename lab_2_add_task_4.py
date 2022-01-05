a = int(input('Type the number which you wanna divide to simple numbers: '))

while a != 1:
    for b in range (2, a+1, 1):
      d = a % b  
      while d == 0:
        print (f'{b}')
        a = a / b
        d = a % b