l = [list(map(int, input().split())) for _ in range(5)]
idx, idy = 0, 0
for i in range(5):
  for j in range(5):
    if l[i][j] == 1: idx=i; idy=j

print(abs(idx-2)+abs(idy-2))
