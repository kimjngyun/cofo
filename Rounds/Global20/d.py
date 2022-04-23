from collections import defaultdict
import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))
  ta = [[a[0], 1]]
  tb = [[b[0], 1]]
  for i in range(1, n):
    if a[i]==a[i-1]: ta[-1][1] += 1
    else: ta.append([a[i], 1])

    if b[i]==b[i-1]: tb[-1][1] += 1 
    else: tb.append([b[i], 1])

  flag = True
  d = defaultdict(int)
  while tb:
    bx, bc = tb.pop()
    ax, ac = -1, -1
    while True and ta:
      ax, ac = ta.pop()
      if ax == bx and bc+d[ax]>ac: break;
      if d[ax] >= ac: d[ax]-=ac
      else: ac -= d[ax]; d[ax] = 0; break
    if ax!=bx: flag = False; break;
    else:
      if ac > bc: 
        if d[ax]+bc<ac: flag = False; break;
        else: d[ax] += bc-ac
      else:
        d[ax] += bc-ac
  if flag: print("YES")
  else: print("NO")
