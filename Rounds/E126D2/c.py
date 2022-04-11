# UPSOLVED
def solve():
  n = int(input())
  a = list(map(int, input().split()))
  M = max(a)
  
  def f(a, M):
    l = list(map(lambda x: M-x, a))
    odd = []
    even = []
    for i in range(n):
      if l[i]>0 and l[i]%2==0: even.append(l[i])
      if l[i]%2: odd.append(l[i]-1)
    need = (sum(odd) + sum(even))//2
    use = len(odd)*2-1
    need -= len(odd)-1
    if need>0: 
      use += (need//3) * 4
      if need%3==1: use += 1
      elif need%3==2: use += 3
    return use

  print(min(f(a, M), f(a, M+1)))
  
for _ in range(int(input())):
  solve()