MOD = 998244353
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  l.sort()
  if l[0] > 1: print(0)
  x = 0
  for i in range(n):
    if l[i] == x: x += 1
  print(x)
  t = [0] * (x+2)
  for i in range(n):
    p = l[i]
    if p > x+1: break
    t[p] += 1
  print(t)



