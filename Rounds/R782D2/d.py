# @eepsilon
import sys
input = lambda: sys.stdin.readline().rstrip()
def solve():
  n = int(input())
  c = list(map(int, input().split()))
  zero = n - sum(c)//n
  ans = [1] * n
  i = 0
  while i<n and c[i]==0:
    ans[i]=0; i+=1
  if i==n: return ans 
  zero -= i
  while zero:
    a = c[i]
    if ans[i] == 0:
      a+= i
    ans[a] = 0
    zero -= 1
    i += 1
  return ans
for _ in range(int(input())):
  print(*solve())