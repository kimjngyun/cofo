import sys
from collections import deque
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  l.reverse()
  d = deque(l)
  MAX = max(l)
  count = 0
  t = d[0]
  while True:
    if t==MAX: break
    d.popleft()
    if d[0]>t: count+=1; t=d[0]
    
  print(count)
