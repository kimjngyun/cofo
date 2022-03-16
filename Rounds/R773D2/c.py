from collections import defaultdict

for _ in range(int(input())):
  n, x = map(int,input().split())
  l = list(map(int, input().split()))
  l.sort()
  d = defaultdict(int)
  ans = n
  for i in range(n):
    d[l[i]]+=1
    
  for i in range(n):
    if d[l[i]] > 0 and d[l[i]*x] > 0:
      ans-=2 
      d[l[i]] -= 1
      d[l[i]*x] -= 1
  
  print(ans)
  