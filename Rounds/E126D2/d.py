from math import ceil
n, k = map(int,input().split())
b = list(map(int, input().split()))
a = [0] * n 
s = 0; total = 0
for i in range(n-1, -1, -1):
  b[i] -= total
  if b[i] > 0:
    t = min(k, i+1)
    a[i] = ceil(b[i]/t)
  s += a[i] - (a[i+k] if i + k < n else 0)
  total += a[i] * t - s
print(sum(a))