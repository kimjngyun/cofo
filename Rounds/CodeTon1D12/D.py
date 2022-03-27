for _ in range(int(input())):
  n = int(input())
  flag = False
  k = 1
  t = n*2
  while t%2==0:
    t//=2
    k*=2
  odd = 2*n//k
  k, odd = min(k, odd), max(k, odd)
  if k!=1: print(k); flag=True

  if not flag: print(-1)