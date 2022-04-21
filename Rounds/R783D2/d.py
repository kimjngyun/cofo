# WA
def solve(n, l):
  pp = []
  t = []
  for i in range(n):
    t.append(l[i])
    if l[i]>0: pp.append(t); t = []
  pp.append(t)
  ans = 0 
  for p in pp:
    p.reverse()
    s = 0
    idx = 0
    while idx<len(p):
      if s + p[idx] > 0: s+=p[idx]; idx +=1
      else: break;
    ans += idx
    for i in range(idx, len(p)):
      if p[idx]<0: ans -=1
  # if l[-1]<0: ans -= len(pp[-1])
  return ans

for _ in range(int(input())):
  n = int(input())
  l = list(map(int, input().split()))
  a = solve(n, l)
  l.reverse()
  b = solve(n, l)
  print(max(a,b))