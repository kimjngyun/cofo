from collections import defaultdict
from email.policy import default
import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  d = defaultdict(list)
  for i in range(n):
    d[l[i]].append(i)
  
  c = []
  for i, v in d.items():
    c.append([i, v])
  
  c.sort(key=lambda x: (len(x[1])))
  s = 0
  e = len(c)-1
  ans = l[:]
  most = c[e][1][:]
  flag = False
  for i in range(n-len(most)):
    if len(c[s][1])==0 or len(c[e][1])==0: break;
    lv = c[s][0]
    li = c[s][1].pop()
    if len(c[s][1])==0: s+=1
    rv = c[e][0]
    ri = c[e][1].pop()

    if len(c[e][1])==0: c[e][1] = most[:]; flag = True
    if flag == False:
      ans[li] = rv
      ans[ri] = lv
    else:
      ans[li], ans[ri] = ans[ri], ans[li]
  print(*ans)

