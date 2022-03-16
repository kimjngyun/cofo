import sys
from math import floor
input=sys.stdin.readline
for _ in range(int(input())):
  n, k = map(int,input().split())
  arr = list(map(int, input().split()))
  arr.sort()
  ans = 10**13
  key = arr[0]
  if n==1:
    if k>=key: print(0)
    else: print(key-k)
    continue

  if sum(arr)<=k:
    print(0)
    continue
  
  
  left = arr[1:]
  pref = [0] * n
  for i in range(1, n):
    pref[i] = pref[i-1] + left[i-1]

  for i in range(n):
    x = floor((k-pref[i])/(n-i))
    t = n-i-1
    
    if key-x>0: t += key-x
    ans = min(ans, t)
  
  print(ans)

