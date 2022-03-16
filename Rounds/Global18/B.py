import sys
from math import log2
input=sys.stdin.readline
def p(x): 
  arr = [0] * 20
  for i in range(20, -1, -1):
    if x & (1<<i):
      arr[i] += x-(1<<i)+1
      for j in range(i):
        arr[j] += 1<<(i-1)
      x -= 1<<i
  return arr

for _ in range(int(input())):
  l, r = map(int,input().split())
  hl = int(log2(l))
  hr = int(log2(r))
  if hl==hr: print(0)
  else:
    al = p(l-1)
    ar = p(r)
    ans = 0
    for i in range(20):
      ans = max(ans, ar[i]-al[i])
    print(r-l+1-ans)

  
