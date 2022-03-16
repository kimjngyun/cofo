from math import ceil
for _ in range(int(input())):
  n, h = map(int,input().split())
  l = list(map(int, input().split()))
  m = []
  for i in range(1, n):
    m.append(l[i]-l[i-1])
  m.sort()

  pref = [0] * (n)
  for i in range(1, n):
    pref[i] = pref[i-1]+m[i-1]

  flag = True
  for i in range(n-1):
    if ceil((h - pref[i]) / (n-i)) <= m[i]:
      print (ceil((h - pref[i]) / (n-i))); flag=False; break
  
  if flag:
    print( h - pref[n-1] )