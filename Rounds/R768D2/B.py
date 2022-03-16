from cmath import inf


for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  arr.reverse()
  t = 0
  ans = 0
  while True:
    while(t<n-1 and arr[t+1] == arr[0]):
      t+=1
    if t>=n-1: break
    t = (t+1)*2-1
    ans += 1
  print(ans)
