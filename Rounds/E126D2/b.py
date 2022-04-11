import math
def solve(n):
  ans = 15
  for i in range(1, 16):
    t = math.ceil(n/(2**i)) * (2**i)
    m = (t-n) + 15-i
    ans = min(m, ans)
  return ans

n = int(input())
l = list(map(int, input().split()))
print(*list(map(lambda x: solve(x), l)))
