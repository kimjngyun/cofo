import sys
input = sys.stdin.readline
t = int(input())  
for _ in range(t):
  n = int(input())
  l = list(map(int, input().rstrip().split()))
  l.sort()
  MIN = l[0]
  for i in range(1, n):
    MIN = max(MIN, l[i]-l[i-1])
  print(MIN)