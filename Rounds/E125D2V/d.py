import sys
input = lambda: sys.stdin.readline().rstrip()
MAX = 1000001
n, C = map(int,input().split())
md = [0] * MAX
for i in range(n):
  c, d, h = map(int,input().split())
  md[c] = max(md[c], d*h)

for i in range(1, MAX):
  cnt = 2
  for j in range(i*2, MAX, i): 
    md[j] = max(md[j], md[i] * cnt)
    cnt += 1

for i in range(1, MAX):
  md[i] = max(md[i], md[i-1])

m = int(input())
for i in range(m):
  d, h = map(int,input().split())
  cur = d*h
  l, r = 0, C+1
  while l+1 < r:
    mid = (l+r)//2
    if md[mid] > cur: r = mid
    else: l = mid
  if r==C+1: print(-1, end=' ')
  else: print(r, end=' ')
  
