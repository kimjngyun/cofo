for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  one = False
  cons = False
  l.sort()
  
  for i in range(n):
    if l[i]==1: one=True
    if i>0 and l[i]==l[i-1]+1: cons=True
  
  if not cons: print("YES")
  else:
    if one: print("NO")
    else: print("YES")