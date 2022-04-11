def solve():
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  for i in range(n):
    if a[i] < b[i]: a[i], b[i] = b[i], a[i]
  ret = 0
  for i in range(n-1):
    ret += abs(a[i+1]-a[i])
    ret += abs(b[i+1]-b[i])
  print(ret)
  
for _ in range(int(input())):
  solve()