import sys
input=sys.stdin.readline

def pr(x, n):
  while x>n:
    x//=2
  return x

for _ in range(int(input())):
  n = int(input())
  arr = list(map(int, input().split()))
  arr = list(map(lambda x: pr(x, n), arr))
  v = [0] * (n+1)
  for i in range(n):
    t = arr[i]
    while t:
      if v[t]==0: v[t]=1; break;
      else: t//=2
  if sum(v)==n: print("YES")
  else: print("NO")