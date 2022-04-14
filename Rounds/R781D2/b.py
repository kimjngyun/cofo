from collections import defaultdict
import time

def solve(n, l):
  d = defaultdict(int)
  for i in range(n):
    d[l[i]] += 1
  MAX = 0
  for i, v in d.items():
    MAX = max(MAX, v)
  t = n - MAX
  a = 0
  while MAX < n:
    MAX *= 2
    a += 1
  print(a+t)


mask = (1<<16)-1
N = 10**5
prefill = (1<<15) + 1
l = [mask+1]
x = 1
for i in range(1, prefill):
  l.append(x)
  x = x*5 + 1
  x &= mask
for i in range(prefill, N):
  l.append(0)

start = time.time()
solve(N, l)
print("time: ", time.time() - start)

# for _ in range(int(input())):
#   n = int(input())
#   l = list(map(int, input().split()))
#   solve(n ,l)

