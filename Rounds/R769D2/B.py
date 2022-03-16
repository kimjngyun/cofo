
for _ in range(int(input())):
  n = int(input())
  t = 1
  while n>2*t:
    t*=2
  

  for i in range(t):
    print(t-1-i, end=' ')
  for i in range(n-t):
    print(t+i, end=' ')

  print()
  