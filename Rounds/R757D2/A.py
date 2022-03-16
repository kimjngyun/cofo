for _ in range(int(input())):
  n, l, r, k = map(int,input().split())
  p = list(map(int, input().split()))
  p.sort()
  ans = 0
  for i in range(n):
    if p[i]>=l and p[i]<=r and k>=p[i]: k -= p[i]; ans+=1
    if p[i]>k: break
  print(ans)