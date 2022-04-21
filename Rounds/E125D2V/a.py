import sys
input = lambda: sys.stdin.readline().rstrip()
from math import ceil
for _ in range(int(input())):
  x, y = map(int,input().split())
  t = ceil((x**2+y**2)**0.5)
  if x==0 and y==0: print(0)
  elif t**2 == x**2 + y**2: print(1)
  else: print(2)