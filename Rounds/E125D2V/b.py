import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n, b, x, y = map(int,input().split())
  s = 0
  ans = 0
  for i in range(n):
    if s+x<=b: s+=x; ans += s
    else: s-=y; ans+=s
  print(ans)