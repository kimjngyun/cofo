import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
  n, k = map(int, input().split())  
  mice = list(map(int, input().split()))
  mice.sort()
  t = 0
  cnt = 0
  while t <= n:
    if(len(mice)==0): break
    cand = mice.pop()
    if(n-cand<n-t):
      cnt += 1
      t += n-cand
    else: break
  print(cnt)
