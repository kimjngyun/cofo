import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n, x = map(int,input().split())
  arr = list(map(int, input().split()))
  arr.sort()
  p = [0] * (n+1)
  for i in range(1, n+1):
    p[i] = p[i-1] + arr[i-1]
  ans = 0
  for i in range(1, n+1):
    ans += max((x + i - p[i]) // i, 0)
  print(ans)