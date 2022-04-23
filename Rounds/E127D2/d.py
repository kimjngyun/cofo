import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
  n, x = map(int,input().split())
  arr = list(map(int, input().split()))
  MAX = max(arr)
  MIN = min(arr)
  ans = 0
  
  if MIN > 1:
    nn = min(abs(arr[0]-1), abs(arr[-1]-1))
    idx = 0 if abs(arr[0]-1) < abs(arr[-1]-1) else len(arr)
    for i in range(len(arr)-1):
      t = abs(arr[i]-1) + abs(arr[i+1]-1) - abs(arr[i+1] - arr[i])
      if t<nn: idx = i+1
      nn = min(nn, t)
    arr = arr[:idx] + [1] + arr[idx:]

  if MAX < x: 
    xx = min(abs(arr[0]-x), abs(arr[-1]-x))
    idx = 0 if abs(arr[0]-x) < abs(arr[-1]-x) else len(arr)
    for i in range(len(arr)-1):
      t = abs(arr[i]-x) + abs(arr[i+1]-x) - abs(arr[i+1] - arr[i])
      if t<xx: idx = i+1
      xx = min(xx, t)
    arr = arr[:idx] + [x] + arr[idx:]

  for i in range(len(arr)-1):
    ans += abs(arr[i+1]- arr[i])
  # print(arr)
  print(ans)
  # print("ANS", ans)