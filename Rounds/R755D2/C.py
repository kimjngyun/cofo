for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  a.sort()
  b.sort()
  flag = True
  for i in range(n):
    if b[i]-a[i] >1: print("NO"); flag = False; break
  if flag: print("YES")
  