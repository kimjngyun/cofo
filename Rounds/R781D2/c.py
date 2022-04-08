from collections import defaultdict
import math

for _ in range(int(input())):
  n = int(input())
  l = [0] + list(map(int, input().split()))
  d = defaultdict(int)
  
  for i in range(n):
    d[l[i]] += 1

  ans = 0
  MAX = 0
  c = []
  for i, v in d.items():
    ans+=1
    MAX = max(MAX, v)
    c.append(v)
  c.sort(reverse=True)
  for i in range(len(c)): 
    t = max(0, c[i]-len(c)+i)
    c[i] = t
  t = []
  for i in range(len(c)):
    if c[i]>0: t.append(c[i])
  while t:
    t.sort(reverse=True)
    t[0] -= 1
    for i in range(len(t)):
      t[i] -= 1
    while t and t[-1]<=0:
      t.pop()
    ans += 1
  print(ans)
  
  
