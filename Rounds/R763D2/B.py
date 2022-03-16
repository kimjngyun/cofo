import sys
input=sys.stdin.readline
for _ in range(int(input())):
  n = int(input())
  arr = [list(map(int, input().split())) for _ in range(n)]
  for i in range(n):
    l, r = arr[i]
    arr[i].append(r-l)
  arr.sort(key=lambda x: x[2])
  visited = [0] * (n+1)
  for i in range(n):
    l, r = arr[i][0], arr[i][1]
    d = 0
    for j in range(l, r+1):
      if visited[j]==0: d = j; visited[d]=1; break
    print(l, r, d)
    

