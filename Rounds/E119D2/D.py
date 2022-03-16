import sys
import math
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  l = list(map(int,input().split()))
  l.sort()
  MAX = l[-1]
  ans = MAX//3 + (MAX%3!=0)
  modset = list(set(list(map(lambda x: x%3, l))))

  if MAX%3==0:
    if len(modset)>1: ans+=1
 
  elif MAX%3==2:
    if 1 in modset: ans+=1
 
  else:
    if 2 in modset:
      if l[0]==1 or (n>=2 and MAX-1 in l): ans+=1

  print(ans)
