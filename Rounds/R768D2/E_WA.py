n = int(input())
arr = list(map(int, input().split()))
dic = {}
for i in range(n):
  v = arr[i]
  if dic.get(v)==None: dic[v] = [i, i]
  else: dic[v][1] = i

ans = 0
s, e = 0, 0

i = 0
while i<n:
  s, e = dic[arr[i]]
  flag = True
  if e-s<=1 or s!=i: 
    i += 1
    continue
  m = e
  for j in range(s+1, e):
    ns, ne = dic[arr[j]]
    if ns!=j: continue
    if m<ne: 
      flag = False
      e = ne
      m = e

  if flag:
    ans += e-s-1
    i = e+1
  else:
    ans += e-s-2
    i += 1
   
print(ans)

