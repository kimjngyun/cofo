t = int(input())
for _ in range(t):
  n = int(input())
  l = list(map(int, input().split()))
  v = [1]+[0]*100
  c = 0
  for i in range(n):
    t = abs(l[i])
    if v[t]>1: continue
    if v[t]==0: 
      v[t]+=1
      c+=1
    elif v[t]==1: 
      v[t]+=1
      c+=1
  print(c)