import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n, m, rb, cb, rd, cd = map(int,input().split())
  ans = 0
  dx, dy = 1, 1
  while rb != rd and cb != cd:
    if rb+dx==0 or rb+dx==n+1: dx = -dx
    if cb+dy==0 or cb+dy==m+1: dy = -dy
    rb += dx
    cb += dy
    ans+=1
  print(ans)
