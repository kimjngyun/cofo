# WA
import sys
input = lambda: sys.stdin.readline().rstrip()

n = 2**int(input())-1
s = input()
ret = [1]
MOD = 998244353
def solve(cur):
  if cur*2>=n: return s[cur-1]
  left = solve(cur*2)
  right = solve(cur*2+1)

  if left != right:
    ret[0] *= 2
    ret[0] %= MOD
    if left < right: return s[cur-1] + left + right
    else: s[cur-1] + right + left
  
  return s[cur-1] + left + right

solve(1)
print(ret[0])