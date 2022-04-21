from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  d = defaultdict(int)
  flag = True
  for i in range(n):
    d[str(l[i])]+=1
    if d[str(l[i])]>=3: print(l[i]); flag = False; break;
  if flag: print(-1)
  
