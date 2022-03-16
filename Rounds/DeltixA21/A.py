import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  m = 0
  for i in range(n):
    p = l
    for j in range(n):
      if i!=j:
        while p[j]&1==0:
          p[j] //= 2
          p[i] *= 2
    m = max(m, sum(p))
  print(m)