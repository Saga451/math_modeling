a = int(input()) #совершенные числа

for b in range (1, a+1, 1):
  e = 0
  for c in range(1, b+1, 1):
        
        if b % c == 0:
            e += c
            #print(f'{b} - {c}')
        else:
            continue
  #print(e)
  if b == e / 2:
      print(b)
  else: 
      continue  


''' 
без лишнего кода

a = int(input())

for b in range (1, a+1, 1):
  e = 0
  for c in range(1, b+1, 1):
        if b % c == 0:
            e += c
  if b == e / 2:
      print(b)

'''  
