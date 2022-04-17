from math import ceil
for _ in range(int(input())):
  n, r, b = map(int,input().split())
  s = 'R' * (r//(b+1)) + 'R' + 'B'
  s *= r%(b+1)
  t = 'R' * (r//(b+1)) + 'B'
  t *= (b+1) - (r%(b+1))
  print(s+t[:-1])
