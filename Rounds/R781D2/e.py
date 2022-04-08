# UPSOLVED, EDITORIAL
import sys
input = lambda: sys.stdin.readline().rstrip()

MAXK = 31
INF = 2**30

def min_pair(a, b):
  if a[0]>b[0]: return b
  elif a[0]<b[0]: return a
  else:
    if a[1]>b[1]: return b
    else: return a

def get(v, vl, vr, l, r):
  if (vl >= l and vr <= r): return t[v]
  if (r <= vl or l >= vr): return [INF, INF]
  vm = (vl+vr)//2
  return min_pair(get(2*v+1, vl, vm, l, r), get(2*v+2, vm, vr, l, r))

def update(v, vl, vr, idx, val):
  if (vr -vl == 1):
    t[v] = [val, idx]
    return
  vm = (vl+vr)//2
  if (idx < vm): update(2*v+1, vl, vm, idx, val)
  else: update(2*v+2, vm, vr, idx, val)
  t[v] = min_pair(t[2*v+1], t[2*v+2])

for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))

  t = [[0, 0] for _ in range(4*n)]
  for i in range(n):
    update(0, 0, n, i, arr[i])

  for _ in range(int(input())):
    l, r = map(int,input().split())
    l -= 1
    b = []
    for i in range(min(r-l, MAXK)):
      now = get(0, 0, n, l, r)
      b.append(now)
      update(0, 0, n, now[1], INF)
    ans = 2**31-1
    for i in range(len(b)):
      for j in range(i+1, len(b)):
        ans = min(ans, b[i][0] | b[j][0])
    for el in b:
      update(0, 0, n, el[1], el[0])
    print(ans)