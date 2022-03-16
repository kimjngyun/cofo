from math import ceil
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  s = set(l)
  l.sort()
  c = n//2
  a = 0
  for i in range(n-1):
    for j in range(i+1, n):
      if a==c: break
      if l[j]%l[i]==0 or l[j]%l[i] not in s: print(l[j], l[i]); a+=1
    if a==c: break

