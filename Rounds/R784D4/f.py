from bisect import bisect_left
import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  r = list(reversed(l))
  pl = [0] * (n+1)
  pr = [0] * (n+1)
  for i in range(1, n+1):
    pl[i] = pl[i-1]+l[i-1]
    pr[i] = pr[i-1]+r[i-1]

  s = 0
  e = sum(l)//2
  ans = 0
  for i in range(n):
    ll = pl[i]
    idx = bisect_left(pr, ll)
    if pr[idx] != ll: continue
    else:
      if i+idx>n: break
      else: ans = i+idx
  print(ans)



