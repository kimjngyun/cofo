for _ in range(int(input())):
  n, m = map(int,input().split())
  l = [list(map(int, input())) for _ in range(n)]
  if l[0][0]==1: print(-1); continue;
  SUM = sum(map(sum, l))
  if SUM==0: print(0); continue;
  print(SUM)
  for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
      if l[i][j]==1:
        if j==0: print(i, j+1, i+1, j+1)
        else: print(i+1, j, i+1, j+1)