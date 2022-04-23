import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  t = []
  x = 0
  for i in range(n-1):
    if arr[i+1]==arr[i]: x+=1
    else: 
      if x!=0: t.append(x)
      x = 0
  if x!=0: t.append(x)
  t.sort()
  if len(t)==0: print(0)
  elif len(t)==1:
    if t[0]==1: print(0)
    elif t[0]==2: print(1)
    else: print(t[0]-2)
  else: 
    s = -1; e = -1
    for i in range(n-1):
      if arr[i+1]==arr[i]:
        if s==-1: s = i
        else: e = i
    print(e-s-1)