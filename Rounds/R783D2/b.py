import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n, m = map(int,input().split())
  l = list(map(int, input().split()))
  s = n + sum(l)- min(l) + max(l)
  if s<=m: print("YES")
  else: print("NO")
