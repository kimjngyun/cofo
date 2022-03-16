
for _ in range(int(input())):
  n, m = map(int,input().split())
  l = [list(map(int, input())) for _ in range(n)]
  flag= False
  for i in range(1, n):
    for j in range(1, m):
      if l[i-1][j-1]==0 and l[i-1][j]==1 and l[i][j-1]==1 and l[i][j]==1: flag = True; break;
      if l[i-1][j-1]==1 and l[i-1][j]==0 and l[i][j-1]==1 and l[i][j]==1: flag = True; break;
      if l[i-1][j-1]==1 and l[i-1][j]==1 and l[i][j-1]==0 and l[i][j]==1: flag = True; break;
      if l[i-1][j-1]==1 and l[i-1][j]==1 and l[i][j-1]==1 and l[i][j]==0: flag = True; break;
  if flag: print("NO")
  else: print("YES")