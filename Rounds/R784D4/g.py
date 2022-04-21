import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n, m = map(int,input().split())
  g = [list(input()) for _ in range(n)]
  for i in range(m):
    t = 0
    for j in range(n):
      if g[j][i]=="*": t += 1; g[j][i] = '.'
      if g[j][i]=='o':
        for k in range(t):
          g[j-k-1][i] = '*'
        t = 0
    if t>0:
      for k in range(t):
        g[n-k-1][i] = '*'
  for i in range(n):
    print(''.join(g[i]))

      
