a = int(input('Type the number which you wanna divide to simple numbers: '))

for b in range(2, a, 1):
    print('\n'+f'{b}: ')
    while b != 1:
        for c in range(2, b+1, 1):
            d = b % c
            e = 1
            while d == 0:
                print(c,end='')
                b //= c
                d = b % c
                e +=c   
           
