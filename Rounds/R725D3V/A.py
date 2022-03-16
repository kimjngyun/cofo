import sys
from collections import deque
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input()) 
  l = list(map(int, input().split()))
  MIN = min(l); MAX = max(l)
  ndx = l.index(MIN)
  xdx = l.index(MAX)
  if ndx>xdx: ndx, xdx = xdx, ndx
  print(min(ndx+1+n-xdx, xdx+1, n-ndx))