from math import log2

def solve(a, b, ans):
  ans1 = a - b + 1
  la, lb = 0, 0
  if a>0: la = la = 2**int(log2(a))
  if b>0: lb = lb = 2**int(log2(b))
  if a==b: print(1)
  elif lb==0: print(min(ans, ans1))
  elif la==lb: return solve(a-la, b-lb, ans)
  elif lb>la: return solve(a, b-lb, ans)
  else: print(min(ans, ans1))
    

for _ in range(int(input())):
  a, b = map(int,input().split())
  solve(a,b, b-a)




