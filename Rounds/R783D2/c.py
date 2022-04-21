from math import floor
n = int(input())
l = list(map(int, input().split()))
MIN = 10**30
for i in range(n):
  t = 0
  m = 0
  for j in range(i-1, -1, -1):
    x = floor(t/l[j])+1
    m += x
    t = x*l[j]
  t = 0
  for j in range(i+1, n):
    x = floor(t/l[j])+1
    m += x
    t = x*l[j]
  MIN = min(m, MIN)
print(MIN)