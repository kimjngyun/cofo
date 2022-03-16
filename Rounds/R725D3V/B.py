import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  l.sort(reverse=True)
  s = sum(l)
  pref = [0] * (n+1)
  for i in range(n):
    pref[i+1] = pref[i]+l[i]
  t = 0
  mean = s//n
  for i in range(n):
    if (l[i]<mean): t += mean-l[i]
  if s%n!=0: print(-1)
  else:
    for i in range(n):
      if pref[i]-(i)*mean >= t : print(i); break
