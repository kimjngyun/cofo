import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n, k = map(int,input().split())
  l = list(map(int, input().split()))
  b = [0] * 31
  for i in range(31):
    for j in range(n):
      if l[j] & (1<<i): b[i] += 1
  ans = 0

  for j in range(30, -1, -1):
    need = n - b[j]
    if k>=need: k-=need; ans += 1<<j
  print(ans)
