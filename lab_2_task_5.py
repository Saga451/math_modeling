a = int(input('Type a dividend: '))
b = int(input('Type a dvivsor: '))

d = a % b # the remainder

if b == 0: 
    print('There is not solution')
elif d == 0:
    c = a // b # the quotient
    print(f'The remainder:{c}')
elif a < b:
    e = a / b # the quotient
    print(f'The quotient:{e}')
else:
    c = a // b # the quotient
    print(f'The quotient:{c}',f'The remainder:{d}',sep='\n')