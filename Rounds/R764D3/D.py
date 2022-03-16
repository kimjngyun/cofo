import sys
from collections import Counter
input=sys.stdin.readline
for _ in range(int(input())):
  n, k = map(int,input().split())
  s = input().rstrip()
  c = Counter(s)
  kth = [0] * k
  pairs = 0
  left = 0
  for key, value in c.items():
    pairs += (value//2)
    left += value%2
  ans = (pairs//k)*2
  if left+(pairs%k)*2>=k: ans += 1
  print(ans)
