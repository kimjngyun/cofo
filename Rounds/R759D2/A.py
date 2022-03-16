import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  t = 1
  if l[0]==1: t+=1
  for i in range(1, n):
    if l[i-1]==0 and l[i]==1: t+=1
    if l[i-1]==1 and l[i]==1: t+=5
    if l[i-1]==0 and l[i]==0: t=-1; break
  print(t)
  