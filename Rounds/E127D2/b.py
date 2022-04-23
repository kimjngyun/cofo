from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  flag = False
  for i in range(l[0]-1, l[0]+2):
    t = True
    for j in range(n):
      if not i-1+j<=l[j]<=i+1+j: t = False; break
    if t: flag = True

  if flag: print("YES")
  else: print("NO")