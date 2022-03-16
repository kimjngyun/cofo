import sys
input=sys.stdin.readline
for _ in range(int(input())):
  l = list(input())
  cnt = 0
  for i in range(len(l)):
    if cnt>1: break
    if l[i]=='N': cnt+=1
  if cnt==1: print("NO")
  else: print("YES")