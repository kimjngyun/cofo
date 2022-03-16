from math import inf
import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  s1 = input()
  s2 = input()
  cnt = 0
  for i in range(n):
    if s1[i]!=s2[i]: cnt+=1
  print(cnt)
  ans = -1
  t1, t2 = n+1, n+1
  if cnt%2==0:
    t1 = cnt
  if (n-1-cnt)%2==0:
    t2 = (n-cnt)
  if t1<n+1 or t2<n+1:
    print(min(t1, t2))
  else: print(-1)