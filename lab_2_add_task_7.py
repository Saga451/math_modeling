a = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # таблица уммножения 9 * 9

for b in range(1, 10,1):
    for i in a:
       print(i * b, end=' ')
    print('\n')